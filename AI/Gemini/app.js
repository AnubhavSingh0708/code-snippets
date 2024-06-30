/*
 * Install the Generative AI SDK
 *
 * $ npm install @google/generative-ai
 *
 * See the getting started guide for more information
 * https://ai.google.dev/gemini-api/docs/get-started/node
 */

const {
    GoogleGenerativeAI,
    HarmCategory,
    HarmBlockThreshold,
  } = require("@google/generative-ai");
  
  const apiKey = process.env.GEMINI_API_KEY;
  const genAI = new GoogleGenerativeAI(apiKey);
  
  const model = genAI.getGenerativeModel({
    model: "gemini-1.5-flash",
  });
  
  const generationConfig = {
    temperature: 1,
    topP: 0.95,
    topK: 64,
    maxOutputTokens: 8192,
    responseMimeType: "text/plain",
  };
  
  async function run() {
    const chatSession = model.startChat({
      generationConfig,
   // safetySettings: Adjust safety settings
   // See https://ai.google.dev/gemini-api/docs/safety-settings
      history: [
        {
          role: "user",
          parts: [
            {text: "make a project on role of APJ abdul kalam as the president of india"},
          ],
        },
        {
          role: "model",
          parts: [
            {text: "## Project: The People's President: A Look at APJ Abdul Kalam's Presidency\n\n**Introduction:**\n\nAvul Pakir Jainulabdeen Abdul Kalam, fondly known as the \"Missile Man of India,\" served as the 11th President of India from 2002 to 2007. His presidency was marked by a unique blend of scientific brilliance, humility, and a deep love for his country. This project aims to explore the multifaceted role of APJ Abdul Kalam as President of India, focusing on his contributions, vision, and lasting impact.\n\n**I. Background:**\n\n* **Early Life and Career:** Briefly discuss Kalam's humble beginnings, his passion for science and technology, and his significant contributions to India's space and missile programs.\n* **Election as President:** Highlight the circumstances surrounding his election, emphasizing the bipartisan support he received and the hopes pinned on him by the nation.\n\n**II. Key Contributions and Initiatives:**\n\n* **Vision for India:** Analyze Kalam's vision for India as a developed nation, focusing on his emphasis on education, technology, and self-reliance.\n* **Focus on Youth:** Discuss Kalam's unwavering belief in the power of youth and his numerous initiatives aimed at inspiring and empowering young Indians.\n* **Promoting Science and Technology:** Explore Kalam's efforts to promote scientific research and development, including his support for indigenous technology and innovation.\n* **Diplomacy and International Relations:** Examine Kalam's role in strengthening India's international relations, highlighting his visits to various countries and his emphasis on peace and cooperation.\n\n**III. Impact and Legacy:**\n\n* **\"People's President\":** Analyze Kalam's approachable and down-to-earth personality, which earned him the title of \"People's President.\" Discuss his interactions with ordinary citizens and his efforts to bridge the gap between the government and the people.\n* **Inspiration and Role Model:** Discuss Kalam's lasting impact as a source of inspiration for millions of Indians, particularly young people. Highlight his message of hard work, perseverance, and national pride.\n* **Continuing Relevance:** Analyze the relevance of Kalam's vision and ideas in contemporary India, particularly in the context of challenges such as poverty, inequality, and technological advancement.\n\n**IV. Conclusion:**\n\nSummarize the key findings of the project, emphasizing the significance of APJ Abdul Kalam's presidency and his enduring legacy as a visionary leader, scientist, and inspiration for generations to come.\n\n**Project Format:**\n\nThis project can be presented in various formats, including:\n\n* **Research Paper:** A detailed written analysis of Kalam's presidency, supported by evidence and citations.\n* **Presentation:** A multimedia presentation incorporating images, videos, and quotes to engage the audience.\n* **Documentary:** A short film exploring Kalam's life, presidency, and impact through interviews, archival footage, and narration.\n* **Website:** An interactive website dedicated to Kalam's legacy, featuring biographical information, speeches, writings, and multimedia content.\n\n**Resources:**\n\n* **Books:**\n\n    * \"Wings of Fire\" by APJ Abdul Kalam\n    * \"India 2020: A Vision for the New Millennium\" by APJ Abdul Kalam\n* **Websites:**\n\n    * The official website of the President of India\n    * The Abdul Kalam Foundation website\n* **Documentaries and Films:**\n\n    * \"Ignited Minds\" (documentary)\n    * \"Mission Mangal\" (film inspired by Kalam's work)\n\n**Note:** This project outline provides a framework for exploring the role of APJ Abdul Kalam as President of India. You can tailor it to your specific interests and the available resources. Remember to cite your sources properly and present your findings in a clear and engaging manner."},
          ],
        },
      ],
    });
  
    const result = await chatSession.sendMessage("INSERT_INPUT_HERE");
    console.log(result.response.text());
  }
  
  run();