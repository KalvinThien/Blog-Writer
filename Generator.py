import openai
# import asyncio
# import aiohttp
from prompts import *
from imports import *

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")
generations = "Generations/"


def generate_outline(topic, keywords, file_name):
    messages = [{'role': 'user', 'content': outline_prompt}]
    prompt = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=0.7)
    output = prompt.choices[0].message.content
    write_file(generations, f"outline_{file_name}", output)
    return file_name


def generate_blog_plan(outline):
    read_file(generations, outline)
    messages = [{'role': 'user', 'content': blog_plan_prompt}]
    blog_plan = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=0.7, max_tokens=3750)
    write_file(generations, f"blog_plan_{topic}", blog_plan)
    return blog_plan


def generate_blog_sections(blog_plan, keywords, topic, file_name):
    sections = blog_plan
    blog_sections = []

    for section in sections:
        messages = [{'role': 'user', 'content': section_prompt}]
        essay = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=0.7, max_tokens=3500)
        output = essay.choices[0].message.content
        blog_sections.append(output)

    blog_to_string = '\n'.join(blog_sections)
    write_file(generations, f"finished_blog_{file_name}", blog_to_string)
    return blog_sections





