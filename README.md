# Blog-Writer
This project is generates blog posts based on a few simple keywords and a topic. It leverages GPT 3.5 in order to create the post. The length of the post generated is generally between 8 and 12 thousand words long. The code takes a few minutes to run as it queries gpt-3.5-turbo and is synchronous. Asynchronous API calls to that occasionally run into a Rate Limit Error and can be unreliable. This could be fixed by using a different, faster, and more expensive model such as text-davinci-003. This is because the application will make around (The exact number is dependant on the first output of the initial prompt/API call) 7 API calls in short succession while asynchronously written with async.io.

At current the blog generated often reuses some subheading names and restates some facts due to the fact that getting around the token limit within the chat memory requires starting a new chat and feeding in an outline before asking GPT 3.5 to write that section whilst it has no memory of the rest of the blog. The intent is to tweak the prompts in the future in order to prevent the repetition in restating facts and rewriting the titles. There are also techniques to make AI detection systems less reliable when used against the generated output which will also be added.

Initially looking at this might make one wonder why not just use GPT-4 as it has a memory buffer that would make GPT-4 comparable to this application out of the box. The answer is two fold, first this was written prior to the release of GPT-4 and not everyone has access to that model yet even as this is being uploaded to github. Secondly this technique, and indeed application, can be used with GPT-4 by simply modifying the model in the code and possibly some reworking of the format that the prompt is presented. With GPT-4's expanded token limit this may be able to handle short stories with some additional work.

# Overview of how the application works:

1. Ask GPT to generate an oultine for a blog.

2. Take that outline and feed it back into GPT and ask it to break up the outline into various strings and output as a Python list.

3. For each section in the outline, ask GPT to write that section and append it to another list.

4. Use Python to join the strings within the list to create a unified file which is saved in a folder named Generations.

NOTE: Review of outputs indicates a clear need to update the prompts to make the blog more cohesive and reword it to avoid being easily detected as AI generated.

# Future Updates:

1. Update code to query a different GPT model and thereby allow for more succesful asynchronous requests

2. Update code to make generate_blog_sections more reusable for reworking outputs OR make generate_blog_sections function take care of that before appending to string

3. Remove hard coded Prompt Engineering from functions and place prompts in a seperate file

4. Rework Prompt Engineering to more closely align with intended goal of having a cohesive blog and more appropriate subheading names

5. Add prompts to reword initial GPT outputs in a manner that appears more natural and less AI generated
