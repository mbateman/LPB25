# pages/supplementary.py

import streamlit as st


st.title("📦 Supplementary Components")

# --- Latest Research and Trends ---
st.header("🔬 Latest Research and Trends")
st.markdown("🎯 **Objective:** Provide learners with insights into current breakthroughs, innovations, and future directions in generative AI.")

with st.expander("📘 Reading Material"):
    st.markdown("""
**1. [Introducing GPT-4.5](https://openai.com/index/introducing-gpt-4-5/)**  
A research preview of OpenAI's strongest GPT model, with enhanced context handling and hybrid reasoning.

**2. [Gemini 2.5: Our most intelligent AI model](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/)**  
Designed for hybrid reasoning, Gemini 2.5 can toggle between flash-fast and deeper thoughtful output.

**3. [Introducing Runway Gen-4](https://runwayml.com/research/introducing-runway-gen-4)**  
Generates consistent characters, locations, and objects across entire media scenes.
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**Introduction to GPT-4.5**")
    st.video("https://www.youtube.com/watch?v=cfRYp0nItZ8")

    st.markdown("**Gemini 2.5 Flash – Hybrid Reasoning on Demand**")
    st.video("https://www.youtube.com/watch?v=_WCszNgL2j0")

    st.markdown("**Introducing Runway Gen-4 | Runway**")
    st.video("https://www.youtube.com/watch?v=uRkfzKYFOxc")

st.subheader("🧠 Activity")
st.markdown("""
**Research a generative AI innovation**  
Create a short presentation with:
- Tool name and purpose  
- Use case in creative fields  
- Why it’s innovative  
- Include visuals or audio samples if possible
""")

with st.expander("📝 Quizzes (With Answers Clearly Marked)"):
    st.markdown("""
**1. What is the main feature of Gemini 2.5 that differentiates it from earlier models?**  
- A) It runs offline only  
- B) It only supports short prompts  
- ✅ C) Hybrid reasoning with toggleable depth of thought  
- D) It requires manual tuning by developers

**2. What can Runway's Gen-4 model generate?**  
- A) Only background images  
- B) Random text captions  
- ✅ C) Consistent characters, locations, and objects across scenes  
- D) Video subtitles only

**3. What limitation is acknowledged in GPT-4.5?**  
- ✅ A) Occasional hallucinations in niche topics  
- B) No multilingual support  
- C) Only works in dark mode  
- D) Doesn’t support code generation

**4. Which creative industries benefit most from generative video tools?**  
- ✅ A) Film, advertising, and gaming  
- B) Agriculture and logistics  
- C) Legal services and auditing  
- D) Translation services only

**5. Why is it important to track AI trends in creative fields?**  
- A) To avoid copyright laws  
- B) To replace all human creators  
- ✅ C) To stay informed, innovate, and prepare for disruption  
- D) To automate government policy
    """)

# --- Ethical, Legal, and Societal Implications ---
st.header("⚖️ Ethical, Legal, and Societal Implications")
st.markdown("🎯 **Objective:** Encourage critical thinking around the impact of AI in creative industries.")

with st.expander("📘 Reading Material"):
    st.markdown("""
**1. [WIPO: Copyright and Artificial Intelligence](https://www.wipo.int/about-ip/en/artificial_intelligence/)**  
Explores legal ownership of AI-generated content globally.

**2. [How Generative AI Could Disrupt Creative Work](https://hbr.org/2023/04/how-generative-ai-could-disrupt-creative-work)**  
Looks at the tension between creative originality and automation.

**3. [European Parliament Report on AI and IP](https://www.europarl.europa.eu/doceo/document/A-9-2020-0176_EN.html)**  
An EU-centered legal framework around authorship and regulation of AI content.
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**Who Owns AI-Generated Art?**")
    st.video("https://www.youtube.com/watch?v=7enbkPxq3_0")

    st.markdown("**The Ethics of AI │ Stuart Russell**")
    st.video("https://www.youtube.com/watch?v=KiT0T12Yyno")

st.subheader("🧠 Activity")
st.markdown("""
**Debate Prompt**  
"AI-generated creative works should be eligible for copyright protection under the same conditions as human-created works."  
- Team A: For  
- Team B: Against  
Support your argument with legal examples and real-world cases.
""")

with st.expander("📝 Quizzes (With Answers Clearly Marked)"):
    st.markdown("""
**1. Who currently holds copyright on AI-generated work in most countries?**  
- A) The AI model itself  
- ✅ B) The human who provided input  
- C) The AI developer  
- D) The hosting platform

**2. What is a common ethical concern with AI-generated content?**  
- A) Too much transparency  
- ✅ B) Lack of attribution or originality  
- C) Overuse of color  
- D) Too many fonts used

**3. How does bias enter AI-generated creative outputs?**  
- ✅ A) Through biased training data and human reinforcement  
- B) By using random number generators  
- C) Because of GPU overheating  
- D) Through user interface design

**4. What legal framework is actively exploring AI ownership rights?**  
- A) The World Bank  
- ✅ B) The European Union (EU)  
- C) The FDA  
- D) The Olympic Committee

**5. Why is transparency important in AI-assisted creation?**  
- ✅ A) It allows audiences to evaluate authenticity and accountability  
- B) It improves spelling accuracy  
- C) It reduces server load  
- D) It guarantees viral success
    """)

# --- Capstone Projects and Presentations ---
st.header("🏁 Capstone Projects and Presentations")
st.markdown("🎯 **Objective:** Allow learners to apply generative AI tools to a creative project and reflect on the process.")

with st.expander("📘 Reading Material"):
    st.markdown("""
**1. [Creative AI Projects](https://www.projectpro.io/article/generative-ai-projects/1004)**  
Curated examples of innovative generative AI use cases.

**2. [AI as a Co-Creator and Design Material](https://www.sciencedirect.com/science/article/pii/S0142694X25000158)**  
Discusses AI’s evolving role in ideation and evaluation across design disciplines.
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**Museum of Modern Art: AI-Generated Art 'Unsupervised'**")
    st.video("https://www.youtube.com/watch?v=MlxsSWqrnZs")

    st.markdown("**Creative AI**")
    st.video("https://www.youtube.com/@Creative_AI")

st.subheader("🧠 Capstone Assignment")
st.markdown("""
Develop a creative project using one or more generative AI tools:  
- Examples: story, comic, song, illustration, short film, animation  
- Submit with:  
- Process summary  
- AI-generated vs original elements  
- Reflection on creative collaboration with AI
""")

