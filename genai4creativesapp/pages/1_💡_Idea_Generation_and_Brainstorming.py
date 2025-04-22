# pages/module1.py

import streamlit as st
from utils import global_chat

st.title("🎨 Module 1: Idea Generation and Brainstorming")

global_chat()

# --- 1.1 ---
st.header("1.1 Inspiration & Concept Creation")
st.markdown("""
🔍 **Overview:**  
Explore how generative AI can spark ideas across disciplines—from visual art and scriptwriting to product design—by transforming minimal prompts into elaborate creative seeds.

🧠 **Tools:**  
- ChatGPT (GPT-4) – for idea generation and creative brainstorming  
- Text-to-Image Turbo Models (e.g., DALL·E 3 with Turbo)  
- Storyboarding with Text-to-Image
""")

with st.expander("📘 Reading Material & Summaries"):
    st.markdown("""
- [Don't Ask If AI Can Make Art – Ask How AI Can Be Art (The Verge)](https://www.theverge.com/23741524/ai-artificial-intelligence-creativity-authorship)  
*Summary:* Explores AI as an interactive medium that redefines authorship and creativity.  
- [How Generative AI Is Unlocking Creativity (Adobe Blog)](https://blog.adobe.com/en/publish/2023/03/21/how-generative-ai-is-unlocking-creativity)  
*Summary:* Shows how generative AI enables experimentation and innovation in creative workflows.  
- [Using AI for Storyboarding: A Comprehensive Guide for 2024 (Medium)](https://medium.com/@freelancefilmtools/using-ai-for-storyboarding-a-comprehensive-guide-for-2024-5020370222d6)  
*Summary:* From MidJourney v6 and DALL·E to animatics with generative video.
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**Adobe Firefly: Family of New Creative Generative AI Models**")
    st.video("https://www.youtube.com/watch?v=DvBRj--sUMU")
    st.markdown("**Midjourney AI Tutorial 2025 – Beginner to Advanced Course**")
    st.video("https://www.youtube.com/watch?v=877HAXmKwwM")  # Replace with actual if placeholder

st.subheader("🧩 Exercises")
st.markdown("""
- Brainstorm 10 character ideas using ChatGPT for a fantasy graphic novel.  
- Generate 3 visual prompts for a futuristic product design using a Text-to-Image tool.  
- Storyboard a short scene (3 panels) using AI-generated images and a caption for each.
""")

with st.expander("❓ Quizzes (Answers Hidden)"):
    st.markdown("""
**What’s one way AI like ChatGPT supports concept ideation?**  
- A) Adds visual effects  
- **B) Suggests narrative directions** ✅  
- C) Edits audio  
- D) Writes code

**Which AI tool is best for generating real-time concept images?**  
- A) Grammarly  
- B) GPT-4  
- **C) DALL·E 3 Turbo** ✅  
- D) Audacity

**What can text-to-image models help create in storyboarding?**  
- A) Audio tracks  
- B) Code snippets  
- **C) Image sequences** ✅  
- D) Slide decks

**Which creative field uses AI for sequential scene visualization?**  
- A) Fashion  
- B) Scriptwriting  
- C) Cinematography  
- **D) Storyboarding** ✅

**AI tools like ChatGPT can generate:**  
- A) Website hosting  
- **B) Story prompts** ✅  
- C) Video compression  
- D) Hardware specs
    """)

# --- 1.2 ---
st.header("1.2 Exploration of Variations")
st.markdown("""
🔍 **Overview:**  
Discover how AI tools generate variations of a single idea—expanding creative options in design, layout, characters, and visual storytelling.

🧠 **Tools:**  
- Freepik AI Image Generator – for graphic design and layout options  
- Magnific AI – for upscale and image variation
""")

with st.expander("📘 Reading Material & Summaries"):
    st.markdown("""
- [16 Best AI Tools for Web Designers (Designmodo)](https://designmodo.com/ai-tools-web-designers/)  
- [The Rise of AI Image Generators (The Verge)](https://www.theverge.com/2023/07/11/23789367/midjourney-ai-art-generator-creative-expression)  
- [Character Iteration With AI (Keywords Studios)](https://www.keywordsstudios.com/news/character-iteration-with-ai/)
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**Runway AI – Tutorial for Beginners in 13 Minutes**")
    st.video("https://www.youtube.com/watch?v=c38vtLw1nSk")
    st.markdown("**Mastering AI Image Generation with Leonardo AI**")
    st.video("https://www.youtube.com/watch?v=IRi0gJU2tqo")

st.subheader("🧩 Exercises")
st.markdown("""
- Create 5 variations of a digital poster using Freepik AI Generator.  
- Enhance and upscale a simple drawing or sketch using Magnific.  
- Compare two AI-generated versions of the same prompt and reflect on how they communicate different moods.
""")

with st.expander("❓ Quizzes (Answers Hidden)"):
    st.markdown("""
**What is the core function of Freepik's AI image tool?**  
- A) Composes music  
- **B) Generates multiple visual designs** ✅  
- C) Writes blog posts  
- D) Animates video

**Magnific is known for:**  
- A) Creating animations  
- B) Composing dialogue  
- **C) High-detail image upscaling** ✅  
- D) Translating languages

**What aspect of design does AI often vary?**  
- A) Grammar  
- B) Resolution  
- **C) Style and layout** ✅  
- D) File type

**AI visual variation can support:**  
- **A) Brainstorming new design directions** ✅  
- B) Data encryption  
- C) Sound editing  
- D) Color calibration only

**Exploring variations helps creators:**  
- A) Lock in a final product immediately  
- B) Avoid collaboration  
- **C) Refine or pivot design intent** ✅  
- D) Convert formats
    """)

# --- 1.3 ---
st.header("1.3 Prompt Engineering")
st.markdown("""
🔍 **Overview:**  
Understand the power of crafting thoughtful, clear, and specific prompts to influence generative AI outcomes.

🧠 **Tools:**  
- OpenAI GPT-4  
- Midjourney Prompting
""")

with st.expander("📘 Reading Material & Summaries"):
    st.markdown("""
- [Production Best Practices (OpenAI)](https://platform.openai.com/docs/guides/gpt-best-practices)  
- [Midjourney Prompting Handbook (GitHub)](https://github.com/willwulfken/MidJourney-Styles-and-Keywords-Reference)  
- [Unlocking the Art of Prompting (Professional Developer)](https://professionaldeveloper.ai/articles/unlocking-the-art-of-prompting/)
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**Building a Stylized Long-Form Narrative Workflow in Unreal Engine 5**")
    st.video("https://www.youtube.com/watch?v=UVRlNFFBa1o")
    st.markdown("**The Ultimate MidJourney Prompting Guide**")
    st.video("https://www.youtube.com/watch?v=NBT7hJEZw4k")

st.subheader("🧩 Exercises")
st.markdown("""
- Create 5 text prompts in GPT-4 to write the same story in different tones (e.g., humorous, dark, romantic).  
- Generate an image in Midjourney using a cinematic scene prompt with a defined art style (e.g., “neo-noir cyberpunk”).  
- Refine a prompt 3 times and document how each tweak changes the result (text or image).
""")

with st.expander("❓ Quizzes (Answers Hidden)"):
    st.markdown("""
**What is “prompt engineering”?**
- A) Coding for design tools  
- B) Editing AI-generated images  
- **C) Crafting inputs to guide AI outputs** ✅   
- D) Marketing strategies for AI tools     

**A good prompt is usually:**
- A) Random and vague  
- **B) Clear and specific** ✅   
- C) Long and unrelated  
- D) Non-verbal     

**Midjourney responds well to:**
- A) Paragraphs of dialogue  
- **B) Descriptive keywords (e.g., lighting, style)** ✅  
- C) Hashtags only  
- D) Video links    

**GPT-4 can adjust tone if:**
- A) You change the device  
- **B) You add a tone directive in the prompt** ✅   
- C) You reload the app  
- D) You delete cookies  

**Prompt iterations help you:**
- A) Confuse the AI  
- B) Shorten your work  
- **C) Get closer to desired output** ✅  
- D) Break the tool  

    """)
