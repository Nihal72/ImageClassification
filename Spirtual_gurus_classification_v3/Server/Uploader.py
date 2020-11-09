import streamlit as st
import requests, io
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

CHOICES = {1: "Upload an image.", 2: "Enter a Image url"}

def format_func(option):
    return CHOICES[option]

def file_uploader():
    

    st.markdown("**How do you want to upload the image ?**")

    upload_image = None
    url = None
    image = None
    option = st.selectbox("Select option", options=list(CHOICES.keys()), format_func=format_func)
    #st.write(f"You selected option {option} called {format_func(option)}")
    if option == 1:
        #if st.button("Upload the image."):
        upload_image = st.file_uploader("Upload the image from above mentioned gurus.", type = "jpg")

        if upload_image is not None:
            image = Image.open(upload_image)
            image = np.asarray(image)
            
    if option == 2:
        url_1= st.text_input("Enter the Image address.", "")
        if st.button("Submit!"):
            url = url_1 
        if st.button("Reset"):
            url_1 = ""
        if url is not None:
            try:
                response = requests.get(url).content
                image = plt.imread(io.BytesIO(response), format='JPG')
            #    return (option, image)
            except:
                st.write("Link is invalid, Please try again with valide image address.")
            
    return [option, image]