# pages/module4.py

import streamlit as st
from utils import global_chat

st.title("🎯 Module 4: Customisation & Personalisation")

global_chat()

# --- 4.1 Tailored Content for Audiences ---
st.header("4.1 Tailored Content for Audiences")
st.markdown("🎯 **Objective:** Leverage AI to craft personalized messaging, campaigns, and creative outputs tailored to individual user profiles, behavior, and preferences.")

with st.expander("📘 Reading Material & Summaries"):
    st.markdown("""
**1. The Rise of AI in Hyper-Personalized Marketing – LinkedIn**  
- Summary: Analyzes how leading brands use AI to create customized content in real-time based on user behavior and interests.  
- 🔗 [Read article](https://www.linkedin.com/pulse/rise-ai-hyper-personalized-marketing-nicholas-melillo/)

**2. AI-driven personalization: Unraveling consumer perceptions in social media engagement – ScienceDirect**  
- Summary: Practical guide on using tools like Einstein GPT to personalize email, website, and ad experiences.  
- 🔗 [Read article](https://www.sciencedirect.com/science/article/abs/pii/S0747563224004175)

**3. How To Use AI In Your Content Strategy: A Guide – RivalFlow**  
- Summary: Focuses on how creatives and marketers can use AI tools for audience segmentation and targeted storytelling.  
- 🔗 [Read article](https://www.rivalflow.com/blog/how-to-use-ai-in-your-content-strategy)
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**How to Use AI for Personalization in Marketing**")
    st.video("https://www.youtube.com/watch?v=Dr3plx3qhbQ")

    st.markdown("**Write personalized emails with ChatGPT in Google Sheets**")
    st.video("https://www.youtube.com/watch?v=XDHug_doqZU")

st.subheader("🧩 Exercises")
st.markdown("""
1. Use GPT-4 to draft three personalized product descriptions based on different customer personas.  
2. Design an AI-driven email campaign targeting two audience segments (e.g., gamers vs artists).  
3. Analyze an existing campaign and rewrite it with AI personalization for tone, offer, and call-to-action.
""")

with st.expander("❓ Quizzes (With Answers)"):
    st.markdown("""
**1. What is a key benefit of AI in marketing?**  
- A) Reducing image quality  
- ✅ B) Personalized content delivery  
- C) Randomized messaging  
- D) One-size-fits-all approach

**2. Salesforce Einstein is used for:**  
- A) Designing logos  
- B) Creating music  
- ✅ C) AI-powered personalization  
- D) Video editing

**3. What data helps AI personalize content?**  
- ✅ A) User behavior  
- B) Stock market trends  
- C) DNS records  
- D) IP routing

**4. AI can tailor messages based on:**  
- A) Horoscope signs only  
- B) Birthday and height  
- ✅ C) Demographics and interaction history  
- D) Shoe size

**5. GPT-4 can personalize emails by:**  
- A) Adding emojis randomly  
- B) Copying and pasting templates  
- ✅ C) Adjusting tone and content for specific users  
- D) Using only generic greetings
    """)

# --- 4.2 Interactive and Immersive Experiences ---
st.header("4.2 Interactive and Immersive Experiences")
st.markdown("🎯 **Objective:** Explore how AI is transforming games, experiences, and immersive environments through real-time adaptation and intelligent behavior.")

with st.expander("📘 Reading Material & Summaries"):
    st.markdown("""
**1. Adaptive Worlds: Generative AI in Game Design – Lindenwood**  
- Summary: Explores the implications of generative AI for the future of edutainment, gaming, and beyond.  
- 🔗 [Read article](https://digitalcommons.lindenwood.edu/faculty-research-papers/686/)

**2. Immersive storytelling: empowering XR entrepreneurs – UnrealEngine**  
- Summary: Explores AI-driven simulations, virtual humans, and procedural scene building in Unreal Engine.  
- 🔗 [Read article](https://www.unrealengine.com/en-US/spotlights/immersive-storytelling-empowering-the-next-generation-of-xr-entrepreneurs)

**3. How AI is Making Immersive Experiences More Powerful – RockPaperReality**  
- Summary: Reviews current uses of generative AI in AR/VR, interactive worlds, and adaptive gameplay.  
- 🔗 [Read article](https://rockpaperreality.com/insights/extended-reality/how-ai-is-making-immersive-experiences-more-powerful/)
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**Unity ML Agents Tutorial - Penguins**")
    st.video("https://www.youtube.com/watch?v=axF_nHHchFQ")

    st.markdown("**Easily Set Up Conversation for AI Characters in Unreal Engine**")
    st.video("https://www.youtube.com/watch?v=iGn_WMjfU-A")

st.subheader("🧩 Exercises")
st.markdown("""
1. Use Unity with ML-Agents to create a basic AI character that responds to user movement.  
2. Design a branching conversation scene in Unreal Engine using AI prompts or NPC tools.  
3. Storyboard an interactive AR experience that changes based on user choices and uses generative text/image.
""")

with st.expander("❓ Quizzes (With Answers)"):
    st.markdown("""
**1. Unity's ML-Agents allow you to:**  
- A) Bake lighting  
- ✅ B) Train AI characters  
- C) Create audio effects  
- D) Compress builds

**2. AI in immersive experiences enhances:**  
- A) Loading screens  
- ✅ B) Creative control over NPCs  
- C) Credit rolls  
- D) GPU overheating

**3. Unreal Engine integrates AI for:**  
- A) Hair simulation only  
- ✅ B) Procedural storytelling and smart scenes  
- C) Keyboard layouts  
- D) Excel plugins

**4. Generative AI is useful in AR/VR for:**  
- A) Making headsets heavier  
- ✅ B) Dynamic content personalization  
- C) Upload speeds  
- D) Fixing Wi-Fi

**5. One advantage of AI in game dev:**  
- A) Higher production costs  
- B) Static gameplay  
- ✅ C) Real-time player response and adaptation  
- D) Fewer creative options
    """)

# --- 4.3 Adaptive Storytelling ---
st.header("4.3 Adaptive Storytelling")
st.markdown("🎯 **Objective:** Use AI-powered tools to build dynamic, branching, and responsive story experiences in games, virtual productions, or interactive media.")

with st.expander("📘 Reading Material & Summaries"):
    st.markdown("""
**1. Conversational experiences: testing free-text entry with Charisma.ai – BBC**  
- Summary: How Charisma uses natural language and emotion-aware AI to drive story progression.  
- 🔗 [Read article](https://www.bbc.com/makerbox/case-studies/conversational-experiences:-testing-free-text-entry-with-charisma.ai)

**2. Interactive storytelling: Story Branching – FasterCapital**  
- Summary: Discusses the rise of interactive narratives driven by user choices and AI-generated plot shifts.  
- 🔗 [Read article](https://fastercapital.com/content/Interactive-storytelling--Story-Branching--The-Many-Paths-of-Story-Branching.html)

**3. How AI Story Writers Are Changing the Future of Fiction – AI Story Writer Engine**  
- Summary: Covers AI tools for co-writing, character generation, and emotional tone adaptation.  
- 🔗 [Read article](https://www.aibookgenerator.org/blog/ai-story-writers-future-fiction)
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**Charisma.ai: Getting Started**")
    st.video("https://www.youtube.com/watch?v=xycsY45rTrw")

    st.markdown("**Branching Scenarios Using AI**")
    st.video("https://www.youtube.com/watch?v=hq0xDqyNm2o")

st.subheader("🧩 Exercises")
st.markdown("""
1. Create a simple AI-driven story in Charisma.ai with at least 3 branching paths.  
2. Write a scene with multiple emotional responses and use GPT-4 to rewrite each with different tones.  
3. Design a story map that evolves based on player input and use AI to generate outcomes.
""")

with st.expander("❓ Quizzes (With Answers)"):
    st.markdown("""
**1. Charisma.ai helps you:**  
- A) Make 3D models  
- ✅ B) Build adaptive dialogue and narratives  
- C) Animate skeletons  
- D) Play music

**2. Adaptive storytelling responds to:**  
- A) Screen resolution  
- ✅ B) User interaction  
- C) Refresh rate  
- D) Social media trends

**3. GPT-4 can assist in storytelling by:**  
- ✅ A) Creating interactive content  
- B) Rendering backgrounds  
- C) Importing sprites  
- D) Setting up payments

**4. A branching story provides:**  
- A) One linear plot  
- B) Non-stop tutorials  
- ✅ C) Multiple user-determined outcomes  
- D) Only exposition

**5. AI helps creative writers by:**  
- A) Removing creativity  
- B) Writing clichés  
- ✅ C) Generating options and variations  
- D) Reducing vocabulary
    """)
