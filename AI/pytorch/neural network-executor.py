import torch
from torch import nn

dataa=[]
import csv
with open('data.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    dataa.append(lines[5])
data=[]
for i in range(90):
  ind=len(dataa)-96+i
  data.append(float(dataa[ind])/1000)
truee=[]
for i in range(6):
  ind=len(dataa)-90+i
  truee.append(float(dataa[ind])/1000)
  

truee
device = (
  """ "cuda"
    if torch.cuda.is_available()
    else "mps" """
    if torch.backends.mps.is_available()
    else "cpu"
)
print(f"Using {device} device")

model = torch.jit.load('itc4.pt')
model.eval()

x=torch.tensor(data)
result=model(x)
for i in range(6):
    print(result[i].item())
