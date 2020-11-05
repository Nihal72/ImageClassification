import streamlit as st
from classifier import make_prediction
from PIL import Image , ImageOps
import joblib
import numpy as np
import json
import cv2
import pandas as pd

f = open(r"./class_info/class_dict_pred.json", "r")
class_info_pre = json.load(f)

st.title("Spirtual person classification")
st.header("model can classify 9 gurus mentioned below.")


#sn_goenka = cv2.imread(r"./template_images/SN_goenka.png")
#sn_goenka = cv2.resize(sn_goenka, (32, 32 , 3))
sn_goenka = Image.open(r"./template_images/SN_goenka.png")
swami_prabhupada = Image.open(r"./template_images/prabhupada.jpg")
paramhansa_yogananda = Image.open(r"./template_images/paramhansa_yogananda.jpg")
Osho = Image.open(r"./template_images/Osho-Quotes.jpg")
neem_karoli_baba = Image.open(r"./template_images/neem_karoli_baba.jpg")
mahatma_gandhi = Image.open(r"./template_images/mahatma_gandhi.jpg")
jiddu_krishnamurthi = Image.open(r"./template_images/jiddu_krishnamurthi.jpg")
dr_br_ambedkar = Image.open(r"./template_images/dr-br-ambedkar.jpg")
sadhguru = Image.open(r"./template_images/sadhguru.jpg")


st.image([sn_goenka, sadhguru, jiddu_krishnamurthi, swami_prabhupada, neem_karoli_baba,dr_br_ambedkar, paramhansa_yogananda,Osho, mahatma_gandhi  ],
          caption = ["SN_goenka","Sadhguru", "Jiddu KrishnaMurthi", "A. C. Bhaktivedanta Swami Prabhupada","Neem Karoli baba",
          "Dr. B.R. Ambedkar", "Paramahansa Yogananda", "Osho", "Mahatma Gandhi" ],
            width = 250)

st.header("Upload the image to classify.")
upload_image = st.file_uploader("Upload the image from above mentioned gurus.", type = "jpg")
#st.write("upload image ->",upload_image)

if upload_image is not None:
    #image = cv2.imread
    image = Image.open(upload_image)
    
    image = np.asarray(image)
    st.image(image, caption = "uploaded file", use_columns_width = True, width = 400)
    if st.button("Press me to move forward."):
        st.write("")
        st.write("Classifying...")
        model = joblib.load('./SaveModel/saved_model.pkl')
        (prediction, prediction_proba )= make_prediction(image, model)
        st.write(class_info_pre[str(prediction)])
        if prediction_proba is not None:
            prediction_proba = pd.DataFrame(prediction_proba)
            prediction_proba.rename({0: "Dr. B.R. Ambedkar", 1: "Jiddu Krishnamurthi", 2: "Mahatma Gandhi", 3: "Neem Karoli baba", 4: "Osho", 5: "Param hansa yogananda",
            6: "Sadhguru", 7: "SN Goenka", 8: "A. C. Bhaktivedanta Swami Prabhupada"}, axis = 1, inplace= True)
            st.write(prediction_proba.T)