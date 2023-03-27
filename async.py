from Generator import *
from imports import *


def generate_blog_sections(blog_plan, keywords, topic, file_name):
    sections = blog_plan
    blog_sections = []

    for section in sections:
        messages = [{'role': 'user', 'content': f"You are a professional writer with appropriate domain knowledge of {topic}. I want you to write a blog section about {section}. This section should be fairly verbose and under no circumstances less than two thousand words long. This section should be between 2000 and 3000 words long. This section should be written in a way that is engaging, fun, and easy to read. You should not number your sections or their subheadings. You should also emphasize utilization of {keywords} where appropriate without overstuffing the section with the keywords. This section should also be optimized for SEO discovery on the internet through the use of keywords and other SEO techniques. Also, this section will be part of a larger work that follows this outline: {blog_plan}. You should stick specifically to the assigned section within that outline. Do not write about another section. Also, try to transition to and from the previous and following sections in a natural way."}]
        essay = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=0.7)
        output = essay.choices[0].message.content
        blog_sections.append(output)

    blog_to_string = '\n'.join(blog_sections)

    return blog_sections

