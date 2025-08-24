import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="Handwriting Generator", page_icon="✍️")

st.title("✍️ Handwriting Generator Tool")
st.write("Convert your typed text into a handwriting-style image.")

# Text input
user_text = st.text_area("Enter your text:", "Hello, this is a handwriting test!")

# Font selection
font_option = st.selectbox("Choose handwriting style:", ["Dancing Script", "Caveat", "Patrick Hand"])

font_files = {
    "Dancing Script": "fonts/DancingScript-Regular.ttf",
    "Caveat": "fonts/Caveat-Regular.ttf",
    "Patrick Hand": "fonts/PatrickHand-Regular.ttf"
}

# Font size
font_size = st.slider("Font size", 20, 80, 40)

# Generate handwriting
if st.button("Generate"):
    try:
        font = ImageFont.truetype(font_files[font_option], font_size)
        img = Image.new("RGB", (800, 400), "white")
        draw = ImageDraw.Draw(img)
        draw.text((50, 100), user_text, fill="black", font=font)

        st.image(img, caption="Handwritten Output", use_container_width=True)

        # Download option
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        st.download_button(
            label="Download Image",
            data=buf.getvalue(),
            file_name="handwriting.png",
            mime="image/png"
        )

    except Exception as e:
        st.error(f"Error: {e}")
