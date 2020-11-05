import numpy as np
import pywt
import cv2    
import streamlit as st




def cropped_image_v2(img):
    face_cascade = cv2.CascadeClassifier(r"..\Model\opencv\haarcascades\haarcascade_frontalface_default.xml")
    if isinstance(img , np.ndarray):
        gray = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(faces) >= 1:
            x, y, w, h = faces[0]
            roi = img[y:y+h, x:x+w]
            
            return roi
            
            

def w2d(img, mode='haar', level=1):
    imArray = img
    #Datatype conversions
    #convert to grayscale
    imArray = cv2.cvtColor( imArray,cv2.COLOR_RGB2GRAY )
    #convert to float
    imArray =  np.float32(imArray)   
    imArray /= 255;
    # compute coefficients 
    coeffs=pywt.wavedec2(imArray, mode, level=level)

    #Process Coefficients
    coeffs_H=list(coeffs)  
    coeffs_H[0] *= 0;  

    # reconstruction
    imArray_H=pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H =  np.uint8(imArray_H)

    return imArray_H

def test_img_prepration(image):
    roi = cropped_image_v2(image)
    scalled_raw_img = cv2.resize(roi, (32, 32))
    img_har = w2d(roi,'db1',5)
    scalled_img_har = cv2.resize(img_har, (32, 32))
    combined_img = np.vstack((scalled_raw_img.reshape(32*32*3,1),scalled_img_har.reshape(32*32,1)))
    
    return combined_img
    


def make_prediction(img , model):
	roi = test_img_prepration(img)
	
	return model.predict(roi.T)[0]
	
