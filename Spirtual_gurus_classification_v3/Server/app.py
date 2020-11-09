import streamlit as st
from classifier import make_prediction
from PIL import Image , ImageOps
import joblib
import numpy as np
import json
import cv2
import pandas as pd
import matplotlib.pyplot as plt 
from show_template_image import show_template
from Uploader import file_uploader

f = open(r"./class_info/class_dict_pred.json", "r")
class_info_pre = json.load(f)
show_template()
st.header("Upload the image to classify.")

option = None
image = None

[option , image] = file_uploader()

if option is not None:    
    if image is not None:
        st.image(image, caption = "uploaded file", use_columns_width = True, width = 400)
        #if st.button("Press me to move forward."):
        with st.spinner("uploading ongoing"):
            st.balloons()
        #st.write("Classifying...")
        model = joblib.load('./SaveModel/saved_model_v2.pkl')
        (prediction, prediction_proba )= make_prediction(image, model)
        if prediction>0:
            st.write("This is ",class_info_pre[str(prediction)])
        else:
            st.write(class_info_pre[str(prediction)])
        if prediction_proba is not None:
            prediction_proba = pd.DataFrame(prediction_proba)
            prediction_proba.rename({0: "Dr. B.R. Ambedkar", 1: "Jiddu Krishnamurthi", 2: "Mahatma Gandhi", 3: "Neem Karoli baba", 4: "Osho", 5: "Param hansa yogananda",
            6: "Sadhguru", 7: "SN Goenka", 8: "A. C. Bhaktivedanta Swami Prabhupada"}, axis = 1, inplace= True)
            st.write(prediction_proba.T)