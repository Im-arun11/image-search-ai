from model import analyse_image
import streamlit as st
st.title("Image Search Model")
upload_image = st.file_uploader(
    "Insert the Image", accept_multiple_files="false",type=["jpg","png","WebP","AVIF"] 
)
if upload_image is not None:
    st.image(upload_image,width=300,caption="Uploaded image")
    with st.spinner("Analyzing image..."):
        description = analyse_image(upload_image)
        st.subheader("AI Description")
        st.write(description)