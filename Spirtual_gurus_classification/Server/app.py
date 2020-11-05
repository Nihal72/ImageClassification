import streamlit as st
from classifier import make_prediction
from PIL import Image , ImageOps
import joblib
import numpy as np
import json

f = open(r"../Model/class_dict_pred.json", "r")
class_info_pre = json.load(f)

st.title("Spirtual person classification")
st.header("model can classify 9 gurus mentioned above.")
st.text("Upload the image to classify.")

upload_image = st.file_uploader("Choose the image for classify", type = "jpg")
#st.write("upload image ->",upload_image)

if upload_image is not None:
    #image = cv2.imread
    image = Image.open(upload_image)
    
    image = np.asarray(image)
    st.image(image, caption = "uploaded file", use_columns_width = True)
    st.write("")
    st.write("Classifying...")
    model = joblib.load('../Model/SaveModel/saved_model.pkl')
    prediction = make_prediction(image, model)
    st.write(class_info_pre[str(prediction)])