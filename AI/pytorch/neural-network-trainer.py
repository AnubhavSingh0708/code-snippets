import torch
from torch import nn

device = (
  """ "cuda"
    if torch.cuda.is_available()
    else "mps" """
    if torch.backends.mps.is_available()
    else "cpu"
)
print(f"Using {device} device")

data=[]
odata=[]
cp=0
for d in range(61):
    darr=[]
    odarr=[]
    cp=(len(price)-(90*d))
    for ed2 in range(90):
        darr.append(float(price[(cp-ed2-1)])/1000)
    data.append(darr)
    darr=[]
    for ed1 in range(90):
        darr.append(float(price[(cp-46)-ed1])/1000)

    data.append(darr)

    for edo1 in range(6):
        odarr.append(float(price[(cp-91)-edo1])/1000)
    odata.append(odarr)
    odarr=[]
    for edo in range(6):
        odarr.append(float(price[(cp-136)-edo])/1000)

    odata.append(odarr)


X=torch.tensor(data,requires_grad=True)
y=torch.tensor(odata)

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        #self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(90, 2048),
            nn.Linear(2048, 2048),
            nn.Linear(2048, 2048),
            nn.Linear(2048, 2048),
            
            nn.Linear(2048, 2048),
            nn.Linear(2048, 2048),
            
            nn.Linear(2048, 2048),
            nn.Linear(2048, 2048),
            nn.Linear(2048, 2048),
            nn.Linear(2048, 2048),
            nn.Linear(2048, 2048),
            nn.Linear(2048, 2048),
            
            nn.Linear(2048, 2048),
            nn.ReLU(),
            nn.Linear(2048, 6),
        )
    def forward(self, x):
        #x = self.flatten(x)28643816133300736700966764544 
        logits = self.linear_relu_stack(x)
        return logits
model = NeuralNetwork().to(device)

loss_fn = nn.L1Loss()

optimizer = torch.optim.Adagrad(model.parameters(), lr=0.00005)


def train( model, loss_fn, optimizer):
    size = len(X)
    model.train()
    for ep in range(122):
        X[ep].to(device), y[ep].to(device)

        # Compute prediction error
        pred = model(X[ep])
        loss = loss_fn(pred, y[ep])

        # Backpropagation
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        
        loss  = loss.item()
        if ep==121:
            print(loss*1000)


def test( model, loss_fn):
    size = len(X[1])
    num_batches = len(X)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for ept in range(122):
            X[ept].to(device), y[ept].to(device)
            pred = model(X[ept])
            test_loss = loss_fn(pred, y[ept]).item()

epochs = 100
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train( model, loss_fn, optimizer)
    #test( model, loss_fn)


model_scripted = torch.jit.script(model) # Export to TorchScript
model_scripted.save('itc.pt') 
print("Done!")