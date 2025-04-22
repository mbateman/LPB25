# pages/module7.py

import streamlit as st
from utils import global_chat

st.title("🎨 Module 7: Experimentation with New Styles and Techniques")

global_chat()

# --- 7.1 Style Transfer ---
st.header("7.1 Style Transfer")
st.markdown("🎯 **Objective:** Explore AI-driven style transformation to apply different artistic styles to images.")

with st.expander("📘 Reading Material & Summaries"):
    st.markdown("""
**1. [Understanding Neural Style Transfer]**  
- Summary: This tutorial by TensorFlow introduces neural style transfer, a technique that blends the content of one image with the style of another using deep learning.
🔗 [Read article](https://ai.picsagon.com/advanced-techniques/the-impact-of-ai-on-concept-art-and-storyboarding/)

**2. [Magnific AI: Advanced Style Transfer](#)**  
- Summary: This tutorial by TensorFlow introduces neural style transfer, a technique that blends the content of one image with the style of another using deep learning.
🔗 [Read article](https://magnific.ai)

**3. [Adobe Firefly: Style Reference Feature](#)**  
- Summary: Adobe Firefly enables users to match the style of generated images to a reference image, facilitating consistent visual aesthetics across projects.
🔗 [Read article](https://www.adobe.com/learn/firefly/web/generate-image-using-reference-image)
    """)

with st.expander("🎥 Featured Videos"):
    st.markdown("**Magnific Style Transfer Tutorial: Turn Any Storyboard Into A Film Still**")
    st.video("https://www.youtube.com/watch?v=0PIMWxvfJrM")

    st.markdown("**Adobe Firefly: Match Composition and Style of Any Image**")
    st.video("https://www.youtube.com/watch?v=avNIE_dEQmI")

    st.markdown("**Neural Style Transfer Tutorial with TensorFlow and Python in 10 Minutes**")
    st.video("https://www.youtube.com/watch?v=bFeltWvzZpQ")

st.subheader("🧩 Exercises")
st.markdown("""
**Exercise 1: Applying Style Transfer with Magnific AI**  
- Visit Magnific AI  
- Upload a personal photograph  
- Choose an artistic style (e.g., watercolor, oil painting)  
- Apply the style and download the transformed image

**Exercise 2: Utilizing Adobe Firefly's Style Reference**  
- Access Adobe Firefly  
- Upload a reference image  
- Enter a text prompt  
- Generate the image and observe the style transfer

**Exercise 3: Exploring Neural Style Transfer with TensorFlow**  
- Follow TensorFlow tutorial  
- Use sample or custom images  
- Run the code to stylize  
- Experiment with combinations of style + content
""")

with st.expander("❓ Quizzes (With Answers Clearly Marked)"):
    st.markdown("""
**1. What is the primary goal of neural style transfer?**  
- A) To detect image objects  
- ✅ B) To blend the content of one image with the style of another using deep learning techniques  
- C) To generate high-resolution images  
- D) To segment backgrounds from portraits

**2. Which neural network architecture is commonly used for style transfer?**  
- A) Recurrent Neural Networks (RNNs)  
- ✅ B) Convolutional Neural Networks (CNNs)  
- C) Transformers  
- D) GANs

**3. In neural style transfer, what does the 'content image' represent?**  
- ✅ A) The image whose structural elements are to be preserved in the final output  
- B) The brushstroke reference  
- C) The target texture  
- D) The style definition

**4. What role does the 'style image' play in neural style transfer?**  
- A) It defines object boundaries  
- B) It controls file compression  
- ✅ C) It provides the artistic style (e.g., brushstrokes, color palette) to be applied to the content image  
- D) It limits the resolution

**5. Which loss functions are typically used in neural style transfer?**  
- A) Classification and entropy loss  
- ✅ B) Content loss and style loss, often combined into a total loss function  
- C) Reconstruction loss only  
- D) Time series loss
    """)
