import openai
# import asyncio
# import aiohttp

from imports import *

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")
generations = "Generations/"


def generate_outline(topic, keywords, file_name):
    messages = [{'role': 'user', 'content': f"Write an outline for a blog post about {topic} that is optimized for search engines. The outline should consider including the following keywords: {keywords}. The outline should have a clear and engaging title suitable for discussing {topic} that includes the main keyword phrase. Each section of the outline should have at least 5 subheadings on which to write an essay for that section. The outline should have a catchy title at the top of the page and be clearly marked as such. For example, Title: The greatest essay on writing essays. The 'T' in Title should always be the first character on the page"}]
    prompt = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=0.7)
    output = prompt.choices[0].message.content
    write_file(generations, file_name, output)
    return file_name


def generate_blog_plan(outline):
    read_file(generations, outline)
    messages = [{'role': 'user', 'content': f"I want you to go through this {outline} and convert it into a python list. It should look like this when it is done: ['section 1 title: contents', 'section 2 title: contents', 'section 3 title: contents', 'etc..']. In addition I would like you to rename the title for the Introduction and Conclusion to be something fitting with the theme of the outline and the contents of that section."}]
    return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=0.7, max_tokens=3500)


def generate_blog_sections(blog_plan, keywords, topic, file_name):
    sections = blog_plan
    blog_sections = []

    for section in sections:
        messages = [{'role': 'user', 'content': f"You are a professional writer with appropriate domain knowledge of {topic}. I want you to write a blog section about {section}. This section should be fairly verbose and under no circumstances less than two thousand words long. This section should be between 2000 and 3000 words long. This section should be written in a way that is engaging, fun, and easy to read. You should not number your sections or their subheadings. You should also emphasize utilization of {keywords} where appropriate without overstuffing the section with the keywords. This section should also be optimized for SEO discovery on the internet through the use of keywords and other SEO techniques. Also, this section will be part of a larger work that follows this outline: {blog_plan}. You should stick specifically to the assigned section within that outline. Do not write about another section. Also, try to transition to and from the previous and following sections in a natural way."}]
        essay = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=0.7, max_tokens=3500)
        output = essay.choices[0].message.content
        blog_sections.append(output)

    blog_to_string = '\n'.join(blog_sections)
    write_file(generations, file_name, blog_to_string)
    return blog_sections





