# Home.py (or main.py in root directory)

import streamlit as st
from utils import global_chat

st.set_page_config(page_title="Generative AI for Creative People", layout="wide")

st.title("🎨 Generative AI for Creative People")
global_chat()
st.markdown("Welcome to your interactive course on creative exploration using Generative AI tools! 👋")

st.subheader("🚀 What You'll Learn")
st.markdown("""
This course is designed to help creative professionals and aspiring artists harness the power of AI in storytelling, visual design, music, and interactive media.

You'll explore:
- Idea generation with AI collaborators
- Text, image, audio, and video content creation
- Automation and customization in workflows
- Prototyping, storyboarding, and experimentation
- Ethical and legal considerations in AI-powered creativity
- Capstone project showcasing your creative + AI journey
""")

st.subheader("📚 Course Modules")
st.markdown("""
Each module is listed in the sidebar on the left. You can start from Module 1 or jump to any topic that interests you:

1. 💡 Idea Generation and Brainstorming  
2. 📝 Content Creation  
3. ⚙️ Automation of Repetitive Tasks  
4. 🧑‍🎨 Customisation & Personalisation  
5. 🤝 Collaboration and Co-Creation  
6. 🛠️ Prototyping & Conceptualisation  
7. 🧪 Experimentation with New Styles and Techniques  
8. ✨ Creative Discovery Through AI Outputs  
9. 🧠 Supplementary: Research, Ethics & Capstone  
""")

st.subheader("📌 How to Use This App")
st.markdown("""
- Use the **sidebar navigation** to browse modules  
- Interact with **videos, exercises, and quizzes**  
- Work on the final **Capstone Project** to apply your skills  
""")

st.info("💬 Tip: This app is best viewed on desktop or large screens for full interactivity.")
