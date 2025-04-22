# pages/module3.py

import streamlit as st
from utils import global_chat

st.title("🤖 Module 3: Automation of Repetitive Tasks")

global_chat()

# --- 3.1 Image & Video Editing ---
st.header("3.1 Image & Video Editing")
st.markdown("🎯 **Objective:** Use AI tools to streamline and enhance editing processes, from applying filters to batch-processing visual content.")

st.markdown("🧠 **Tools:** ComfyUI – A powerful, node-based UI for automating image editing pipelines using Stable Diffusion models and AI filters.")

with st.expander("📘 Reading Material & Summaries"):
    st.markdown("""
**1. A Beginner's Guide with Hands-On Practice**  
- Summary: Walk through the basics of ComfyUI and explore its features.  
- 🔗 [Read article](https://www.runcomfy.com/tutorials/comfyui-beginners-guide)

**2. AI workflow automation**  
- Summary: AI workflow automation refers to the use of AI to streamline, optimize, and automate tasks or processes within a workflow.  
- 🔗 [Read article](https://www.pega.com/ai-workflow-automation)
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**Getting Started with ComfyUI: Beginners Tutorial**")
    st.video("https://www.youtube.com/watch?v=HHrOfUlu464")  # Replace with actual link

    st.markdown("**AI Image Enhancement Demo (Before & After)**")
    st.video("https://www.youtube.com/watch?v=OG0U_DSii5w")  # Replace with actual link

st.subheader("🧩 Exercises")
st.markdown("""
1. Install and set up ComfyUI, then run a pre-built workflow to apply a vintage filter to a portrait.  
2. Batch edit 5 images by changing lighting and contrast with AI nodes in ComfyUI.  
3. Compare a manually edited image vs AI-enhanced version and reflect on efficiency and quality.
""")

with st.expander("❓ Quizzes (With Answers)"):
    st.markdown("""
**1. What is ComfyUI primarily used for?**  
- A) Video game development  
- B) Audio mastering  
- ✅ C) Image editing automation  
- D) Code debugging

**2. AI filters in ComfyUI work through:**  
- A) Sliders  
- ✅ B) Node-based workflows  
- C) HTML coding  
- D) Cloud rendering

**3. One benefit of AI-powered image editing is:**  
- A) Random file renaming  
- B) Pixel destruction  
- ✅ C) Faster repetitive task completion  
- D) Larger file sizes

**4. What feature does ComfyUI offer for editing?**  
- A) Real-time multiplayer collaboration  
- B) Procedural 3D modeling  
- ✅ C) Drag-and-drop image nodes  
- D) Manual layer masking

**5. AI-enhanced editing is especially helpful when:**  
- A) You're working with one image only  
- ✅ B) Batch editing a collection  
- C) You need to encode video  
- D) Writing dialogue
    """)

# --- 3.2 Data Organisation & Analysis ---
st.header("3.2 Data Organisation & Analysis")
st.markdown("🎯 **Objective:** Leverage AI to automate data-heavy creative tasks like tagging, cataloging, and content classification—freeing you to focus on creative decision-making.")

st.markdown("🧠 **Tools:** Azure Computer Vision (via Microsoft Azure AI) – For tagging images, extracting text, and categorizing visual content at scale.")

with st.expander("📘 Reading Material & Summaries"):
    st.markdown("""
**1. [What is Azure AI Vision? – Microsoft Docs](https://learn.microsoft.com/en-us/azure/cognitive-services/computer-vision/overview)**  
- Summary: Describes how the tool automates metadata creation, OCR, and image description for large content libraries.

**2. [Organize Raw and Edited Creative Assets – Uplifted](https://www.uplifted.ai/use-cases/organize-raw-and-edited-creative-assets)**  
- Summary: Practical use cases for tagging photos, categorizing assets, and managing media archives.

**3. [Azure AI Vision – Microsoft Docs](https://azure.microsoft.com/en-us/products/ai-services/ai-vision)**  
- Summary: Covers using Azure’s object detection and OCR to make creative content searchable and navigable.
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**What is Azure AI Vision? | Quick Explainer**")
    st.video("https://youtu.be/X03oUbISp3I")  # Replace with actual link

    st.markdown("**Automatically Tag Azure Resources using Azure Policy**")
    st.video("https://www.youtube.com/watch?v=PUJe8Od7B9Q")  # Replace with actual link

st.subheader("🧩 Exercises")
st.markdown("""
1. Upload a batch of 10 images to Azure Computer Vision and extract tags for each.  
2. Use OCR in Azure to pull text from scanned posters or design mockups.  
3. Organize a folder of assets (e.g., photos, illustrations) into themes or categories using AI-generated tags.
""")

with st.expander("❓ Quizzes (With Answers)"):
    st.markdown("""
**1. What does Azure Computer Vision do?**  
- A) Compose songs  
- B) Translate websites  
- ✅ C) Analyze and tag images  
- D) Animate characters

**2. Which feature extracts text from images in Azure?**  
- A) Tagging Engine  
- B) Object Detection  
- ✅ C) OCR (Optical Character Recognition)  
- D) Style Transfer

**3. What’s a key benefit of AI for creative asset management?**  
- A) Reducing image quality  
- B) Faster uploads  
- ✅ C) Automatic tagging and classification  
- D) Secure hosting

**4. You can use Azure AI to:**  
- A) Compress audio files  
- ✅ B) Identify content in photos  
- C) Animate vector shapes  
- D) Mix soundtracks

**5. AI helps creatives by:**  
- A) Replacing creativity  
- B) Eliminating idea generation  
- ✅ C) Reducing manual repetitive tasks  
- D) Writing legal contracts
    """)
