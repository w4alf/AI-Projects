This project was to see how different AI Agents would handle a promptng request to create a daily cyber Security newsletter that would provide 5 recent cyber security news articles from the web. It would then format them in a style I provide along with an example of how the newsletter would look. I gave it some context on who I was and why I was asking for the information. I also detailed where to be able to source the infomation and also gave other criteria on how to rate each article with a risk level scale I provided.
I tested the same prompt across several AI agents including: Copilot, Gemini, Claude, ChatGPT
WINNER? I picked the results from ChatGPT!

The prompt detailed information required such as:

A date range for when the articles should have been published out on the internet
Various names of websites where they can source the news articles to search for
specific format including how long summaries should be and providing a 3 point bulleted list of key insights
I asked that it rate each article with a level of Risk based on Number of affected users or devices, monetary size of data loss, severity of risk/s identified. THe Risk rating scale is as follows: Informational,Low, Medium, High, Very High

Each AI Agent had its Strengths, Weaknesses and Nuances.

Some General observations of this experiment:
All the models seemed to struggle to find recent articles on the internet to use when I initially prompted them to go find articles on the internet that were posted in the last 24 hours. I tweaked my prompt to ask for articles published between say March 6th 2025 and March 10th,2025. This still had mixed results as all the engines would still return articles that were sometimes months old and in some cases years old. I further prompted some of the AI agents that their results were old postings and to search again, same mixed results were obtained. One agent responded that it was not capable of pulling very recent articles from the web (Claude 3.5).
Given these mixed results I resorted to providing the AI agents a very specific URL where recent articles are only posted. e.g.
https://www.bleepingcomputer.com/news/security
THis definetly for worked for ChatGPT and Gemini. The other agents I tested still would provided a mix of new and old articles.

I landed on using the output for ChatGPT with Gemini being a close second. While I preferred Gemini's formatting slightly over ChatGpt's. ChatGPT did an excellent job at providing a risk rating to each article vs Gemini that in one instance marked couple articles as High or very high when I would have marked them as informational. BUT, I believe the prompt for Gemini could be further engineered to provide a rating I was comfortable with. I have access to Google's Vertex AI studio, So I will run this prompt and play with it, in that environment.
Additionally, I asked each AI agent to provide the output requested in HTML format for export. Most had issues with the request being in the main prompt request. malformed html that had extraneous info, or the paste section for the html was missing info or part of html code was rendered in the response but out side of the "copy this" section provided in the prompting result it fed back to me.
The solution for most was to make a second prompt query asking for the result to now be exported to HTML.




Some General Observations with each AI agent/"ChatBot":

Claude:
Copilot:
Gemini:
CHatGPT:
QWEN: Not Tested Yet
Deepseek: Not Tested Yet






.
