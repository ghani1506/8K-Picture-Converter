import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import io

st.set_page_config(page_title="AI HD & 8K Upscaler", layout="wide")

st.title("AI HD & 8K Image Enhancer")

st.markdown("""
This app improves:
- Sharpness
- Clarity
- Color
- HD Quality
- 8K Resolution
""")

uploaded = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png", "webp"]
)

TARGET_8K = (7680, 4320)

def enhance_image(img):
    # Increase sharpness
    sharp = ImageEnhance.Sharpness(img).enhance(2.5)

    # Increase contrast
    contrast = ImageEnhance.Contrast(sharp).enhance(1.2)

    # Increase color richness
    color = ImageEnhance.Color(contrast).enhance(1.15)

    # Smooth tiny artifacts
    final = color.filter(ImageFilter.DETAIL)

    return final

if uploaded:
    image = Image.open(uploaded).convert("RGB")

    st.subheader("Original")
    st.image(image, use_container_width=True)

    upscale_factor = st.selectbox(
        "Choose Output Quality",
        ["2K", "4K", "8K"]
    )

    if upscale_factor == "2K":
        target_size = (2560, 1440)
    elif upscale_factor == "4K":
        target_size = (3840, 2160)
    else:
        target_size = TARGET_8K

    if st.button("Enhance & Upscale"):
        with st.spinner("Processing high-definition image..."):

            enhanced = enhance_image(image)

            upscaled = enhanced.resize(
                target_size,
                Image.Resampling.LANCZOS
            )

            st.subheader("Enhanced HD Output")
            st.image(upscaled, use_container_width=True)

            buffer = io.BytesIO()
            upscaled.save(buffer, format="PNG", optimize=True)
            buffer.seek(0)

            st.download_button(
                "Download Enhanced Image",
                data=buffer,
                file_name="enhanced_hd_image.png",
                mime="image/png"
            )
