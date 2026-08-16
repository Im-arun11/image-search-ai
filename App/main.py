import streamlit as st
st.title("Image Search Model")

upload_image = st.file_uploader(
    "Insert the Image", accept_multiple_files="false",type=["jpg","png","WebP","AVIF"] 
)
if upload_image is not None:
    st.image(upload_image,width=300,caption="Uploaded image")