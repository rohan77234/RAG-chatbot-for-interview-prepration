import gradio as gr
import random


def collect_info(name, skills, experience, projects, allowed_topics, sass_level):
    content = f"""
ABOUT {name.upper()}:
- Skills: {skills}
- Experience: {experience}
- Projects: {projects}

INTERVIEW RULES:
- Allowed Topics: {allowed_topics}
- Sass Intensity: {sass_level}/10
"""
    with open("my_data.txt", "w") as f:
        f.write(content)
    return "✅ Profile saved! Now run the main chatbot."


with gr.Blocks() as setup_app:
    gr.Markdown("## 🧑‍💻 Enter Your Professional Details")
    name = gr.Textbox(label="Your Full Name")
    skills = gr.Textbox(label="Key Skills (comma separated)", placeholder="Python, ML, Public Speaking")
    experience = gr.TextArea(label="Work Experience", placeholder="Job 1: 2020-2022\nJob 2: 2022-present")
    projects = gr.TextArea(label="Notable Projects")
    allowed_topics = gr.Textbox(label="Allowed Interview Topics", value="my skills, my projects, work experience")
    sass_level = gr.Slider(1, 10, label="Sass Intensity Level")
    save_btn = gr.Button("Create My Interview Bot")
    output = gr.Textbox()

    save_btn.click(collect_info, [name, skills, experience, projects, allowed_topics, sass_level], output)

setup_app.launch()