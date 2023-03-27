import Generator
from imports import *


from flask import Request
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        keywords = request.form["keywords"]
        file_name = topic + '_' + datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        outline = Generator.generate_outline(topic, keywords, file_name)
        blog_plan = Generator.generate_blog_plan(outline)
        blog_sections = Generator.generate_blog_sections(blog_plan, keywords, topic, file_name)
        # blog_ai_avoidance = Generator.generate_ai_avoidance(blog_sections)
        return redirect(url_for("index", result=blog_sections))

    result = request.args.get("result") 
    return render_template("index.html", result=result)


