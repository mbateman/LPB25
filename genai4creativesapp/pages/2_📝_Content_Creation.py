# pages/module2.py

import streamlit as st
from utils import global_chat

st.title("🖋️ Module 2: Content Creation")

global_chat()

# --- 2.1 Text Generation ---
st.header("2.1 Text Generation")
st.markdown("🎯 **Objective:** Utilize AI for writing and content generation.")

with st.expander("📚 Reading Material"):
    st.markdown("""
**1. [How GPT-4 Generates and Refines Text](https://mljourney.com/how-does-openais-gpt-4-work/)**  
- Summary: Understand the underlying architecture of GPT-4, how it generates coherent text, and how it can be prompted to refine or expand content.

**2. [QuillBot AI - Best AI Writing Assistant](https://quillbot.com/guides/ai-writing-assistant)**  
- Summary: Learn how tools like Quillbot can paraphrase content, adjust tone (formal/informal), and reframe writing for different audiences.
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**ChatGPT 4 Writes Like a Human**")
    st.video("https://www.youtube.com/watch?v=S0GJnHj69L4")
    st.caption("Summary: Demonstrates how ChatGPT-4 can generate content that passes AI Detection tests without paraphrasing.")

    st.markdown("**Paraphrase Like a Pro with QuillBot (Easy Tutorial)**")
    st.video("https://www.youtube.com/watch?v=Vb5_8_coHLs")
    st.caption("Summary: A practical guide to using QuillBot for enhancing writing by improving sentence structure and clarity.")

st.subheader("📝 Exercises")
st.markdown("""
1. Write a short blog post on “The Future of AI in Creative Work” using GPT-4.  
2. Use Quillbot to paraphrase the GPT-4 post in a more informal tone.  
3. Refine a paragraph from a past project using GPT-4 for conciseness and professionalism.
""")

with st.expander("❓ Quizzes (With Answers)"):
    st.markdown("""
**1. What is the main function of GPT-4 in creative writing?**  
- A) Data analysis  
- B) Visual design  
- ✅ C) Natural language generation  
- D) Audio synthesis

**2. Which tool is primarily used to adjust tone and rephrase sentences?**  
- A) Midjourney  
- ✅ B) Quillbot  
- C) AIVA  
- D) Udio

**3. True or False: GPT-4 can be fine-tuned by users directly on their own data.**  
- ❌ False

**4. Quillbot allows users to modify tone. Which of the following is NOT a tone Quillbot offers?**  
- A) Formal  
- ✅ B) Sarcastic  
- C) Simple  
- D) Academic

**5. Which concept describes GPT-4’s ability to generate contextually relevant follow-ups?**  
- A) Style transfer  
- B) Zero-shot learning  
- C) Context window  
- ✅ D) Prompt chaining
    """)

# --- 2.2 Visual Creation ---
st.header("2.2 Visual Creation")
st.markdown("🎯 **Objective:** Use AI to create visual assets.")

with st.expander("📚 Reading Material"):
    st.markdown("""
**1. [Intro to Generative Art with Midjourney](https://docs.midjourney.com/docs/prompts)**  
- Summary: Dive into how prompts influence art generation in Midjourney and explore community-generated examples.

**2. Comparing Leonardo and Stable Diffusion for Artists**  
- [Leonardo Learn](https://leonardo.ai/learn/)  
- [Stable Diffusion Learning Hub](https://stability.ai/blog/stable-diffusion-public-release)  
- Summary: Learn the key differences between Leonardo’s fine-tuned models and the flexibility of Stable Diffusion.
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**Free Leonardo AI Course for Beginners (AI Art Generation Tutorial)**")
    st.video("https://www.youtube.com/watch?v=gtzNUq7OnFQ")
    st.caption("Summary: Comprehensive tutorial for beginners to create images using Leonardo AI.")

    st.markdown("**NEW Stable Diffusion 2.1 Tutorial – Easy Setup + What You Need to Know**")
    st.video("https://www.youtube.com/watch?v=e3vcYVwEkW0")
    st.caption("Summary: Step-by-step tutorial on Stable Diffusion 2.1 and its image generation features.")

st.subheader("📝 Exercises")
st.markdown("""
1. Create a poster for a fictional event using Midjourney or Leonardo.  
2. Use Stable Diffusion to generate three fantasy landscape variations.  
3. Compare results between Midjourney and Stable Diffusion using the same prompt.
""")

with st.expander("❓ Quizzes (With Answers)"):
    st.markdown("""
**1. Which tool operates primarily through Discord?**  
- A) Leonardo  
- ✅ B) Midjourney  
- C) AIVA  
- D) Quillbot

**2. Stable Diffusion uses which kind of learning technique?**  
- A) Supervised Learning  
- B) Reinforcement Learning  
- ✅ C) Latent Diffusion  
- D) Neural Translation

**3. True or False: Leonardo is only usable via desktop apps.**  
- ❌ False

**4. Which of these is known for higher prompt responsiveness?**  
- A) Leonardo  
- ✅ B) Midjourney v5  
- C) GPT-4  
- D) AIVA

**5. What does the term “prompt engineering” refer to in visual creation tools?**  
- A) Coding AI models  
- B) Compressing images  
- ✅ C) Crafting effective input phrases  
- D) Enhancing resolution
    """)

# --- 2.3 Music Composition ---
st.header("2.3 Music Composition")
st.markdown("🎯 **Objective:** Understand AI-assisted music composition.")

with st.expander("📚 Reading Material"):
    st.markdown("""
**1. [Composing with AIVA](https://www.aiva.ai/)**  
- Summary: Explore how AIVA helps musicians generate classical or cinematic scores and adapt to genres.

**2. Suno and Udio for Contemporary Music Creation**  
- [Suno AI Overview](https://suno.com/)  
- [Udio | AI Music Generator – Official Website](https://www.udio.com/)  
- Summary: Learn how Suno and Udio generate beats, lyrics, and melodies based on simple prompts.
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**AIVA - Create Emotional Soundtracks (YouTube)**")
    st.video("https://www.youtube.com/shorts/LNBPC3pGBbI")
    st.caption("Demonstrates how AIVA can be used to create emotional soundtracks for various media.")

    st.markdown("**Using Suno AI to Create Sounds & Make Beats: A Producer’s Guide**")
    st.video("https://www.youtube.com/watch?v=jPxeeslmcWs")
    st.caption("A producer's walkthrough on beat-making using Suno AI.")

    st.markdown("**Udio Walkthrough (YouTube)**")
    st.video("https://www.youtube.com/watch?v=ZsCJnjpjlzY&rco=1")
    st.caption("A tutorial on Udio's tools for AI music generation.")

st.subheader("📝 Exercises")
st.markdown("""
1. Compose a 30-second piano piece using AIVA.  
2. Generate a hip-hop loop using Suno and write a few lyrics for it.  
3. Use Udio to create a musical intro for a podcast.
""")

with st.expander("❓ Quizzes (With Answers)"):
    st.markdown("""
**1. Which AI is designed to mimic emotional classical scores?**  
- A) Suno  
- B) Udio  
- ✅ C) AIVA  
- D) Quillbot

**2. True or False: Suno can generate lyrics and beats.**  
- ✅ True

**3. Udio’s primary strength is in:**  
- A) Movie editing  
- B) Podcasting  
- C) Audio mastering  
- ✅ D) Contemporary music generation

**4. Which platform focuses more on structured composition like sonatas?**  
- ✅ A) AIVA  
- B) Suno  
- C) Midjourney  
- D) GPT-4

**5. A key differentiator of Udio is:**  
- A) It uses images as input  
- ✅ B) It focuses on full-song production  
- C) It only works offline  
- D) It requires a DAW
    """)

# --- 2.4 Multimedia Content Generation ---
st.header("2.4 Multimedia Content Generation")
st.markdown("🎯 **Objective:** Combine AI-generated text, images, and sound.")

with st.expander("📚 Reading Material"):
    st.markdown("""
**1. Creating Videos with Runway ML**  
- [Runway ML's Gen-2 Guide](https://research.runwayml.com/gen2)  
- [Getting Started with Generative Video](https://help.runwayml.com/hc/en-us/articles/37425232841875-Getting-Started-with-Generative-Video)  
- Summary: Learn how Runway ML enables creators to combine video, audio, and text with AI models like Gen-2.
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**Introducing Gen-2: Text to Video | Runway**")
    st.video("https://www.youtube.com/watch?v=trXPfpV5iRQ")
    st.caption("An introduction to Runway Gen-2 and its text-to-video capabilities.")

    st.markdown("**Creating Cinematic Short Films with AI & Runway Gen-2**")
    st.video("https://www.youtube.com/watch?v=fkIEMn5e2Q4")
    st.caption("A practical example of cinematic storytelling using Runway's AI tools.")

st.subheader("📝 Exercises")
st.markdown("""
1. Script and storyboard a 30-second AI video using GPT-4 and Midjourney.  
2. Use Runway ML to animate a short scene using generated images.  
3. Add AI-generated voice-over or background music to your video using Udio or Suno.
""")

with st.expander("❓ Quizzes (With Answers)"):
    st.markdown("""
**1. Runway ML’s Gen-2 allows:**  
- A) Image editing only  
- B) Music mastering  
- ✅ C) Text-to-video generation  
- D) Script writing

**2. What’s essential for a good AI-generated video?**  
- A) Coding experience  
- ✅ B) Prompt engineering and assets  
- C) DSLR cameras  
- D) Paid actors

**3. True or False: Runway ML only supports still image generation.**  
- ❌ False

**4. Which AI tool is best paired with Runway for voiceovers?**  
- A) Quillbot  
- B) GPT-4  
- ✅ C) Udio  
- D) Leonardo

**5. Which of the following combinations represents a full multimedia project stack?**  
- A) GPT-4 + Midjourney + AIVA  
- B) GPT-4 + Leonardo + Quillbot  
- ✅ C) GPT-4 + Midjourney + Udio + Runway ML  
- D) GPT-4 + Stable Diffusion + Quillbot
    """)

