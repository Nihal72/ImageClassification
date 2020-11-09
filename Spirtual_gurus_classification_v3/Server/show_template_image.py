import streamlit as st
from PIL import Image
def show_template():

    st.title("Spirtual Being classification")
    st.header("Now even AI can find the name of Enlightened One, who have ever walked on earth.")
    st.subheader("**_Science_** exists to uncover these deepest **_spiritual_ truths**. On the other hand, those engaged in **_spirituality_** are trying to find the hidden cause behind what is **_scientific_ fact**.")
    st.image(r"./template_images/wp2048106-buddha-hd-wallpapers (1).jpg", width = 800)

    st.markdown("This model has been developed to classify images by face recognition using OpenCV. To check it out upload any image of the personalities listed below and hit the submit button.")
    st.markdown("* SN goenka \n* Sadhguru \n* Jiddu KrishnaMurthi \n* A. C. Bhaktivedanta Swami Prabhupada \n* Neem Karoli baba\
                \n* Dr. B.R. Ambedkar \n* Paramahansa Yogananda \n* Osho \n* Mahatma Gandhi")
    # 	sn_goenka = Image.open(r"./template_images/SN_goenka.png")
    # 	swami_prabhupada = Image.open(r"./template_images/prabhupada.jpg")
    # 	paramhansa_yogananda = Image.open(r"./template_images/paramhansa_yogananda.jpg")
    # 	Osho = Image.open(r"./template_images/Osho-Quotes.jpg")
    # 	neem_karoli_baba = Image.open(r"./template_images/neem_karoli_baba.jpg")
    # 	mahatma_gandhi = Image.open(r"./template_images/mahatma_gandhi.jpg")
    # 	jiddu_krishnamurthi = Image.open(r"./template_images/jiddu_krishnamurthi.jpg")
    # 	dr_br_ambedkar = Image.open(r"./template_images/dr-br-ambedkar.jpg")
    # 	sadhguru = Image.open(r"./template_images/sadhguru.jpg")


    # 	st.image([sn_goenka, sadhguru, jiddu_krishnamurthi, swami_prabhupada, neem_karoli_baba,dr_br_ambedkar, paramhansa_yogananda,Osho, mahatma_gandhi  ],
    # 			  caption = ["SN_goenka","Sadhguru", "Jiddu KrishnaMurthi", "A. C. Bhaktivedanta Swami Prabhupada","Neem Karoli baba",
    # 			  "Dr. B.R. Ambedkar", "Paramahansa Yogananda", "Osho", "Mahatma Gandhi" ],
    # 				width = 250)
