import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="8K Image Upscaler", layout="centered")

st.title("AI Image to 8K Upscaler")

uploaded = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png", "webp"]
)

TARGET_8K = (7680, 4320)

if uploaded:
    img = Image.open(uploaded).convert("RGB")

    st.image(img, caption="Original Image", use_container_width=True)

    if st.button("Upscale to 8K"):
        upscaled = img.resize(TARGET_8K, Image.Resampling.LANCZOS)

        st.image(
            upscaled,
            caption="8K Upscaled Image",
            use_container_width=True
        )

        buffer = io.BytesIO()
        upscaled.save(buffer, format="PNG")
        buffer.seek(0)

        st.download_button(
            label="Download 8K Image",
            data=buffer,
            file_name="upscaled_8k.png",
            mime="image/png"
        )
