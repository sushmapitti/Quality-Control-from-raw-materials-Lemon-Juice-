import streamlit as st
import pandas as pd
import numpy as np 
from model import knnmodel
from detect import inputs
from PIL import Image
import os
st.header("""
Lemon Juice Quality control
""")
st.sidebar.header('Input Parameters')

def user_input_features():
    classt=0
    Lemons = st.sidebar.slider('No. of lemons', 0, 15,4)
    image_file = st.sidebar.file_uploader("Upload Lemons image",type=['png','jpeg','jpg'])
    if image_file is not None:
       img =Image.open(image_file)
       with open(os.path.join(r"C:\Users\sushma\AppData\Local\Programs\Python\Python38\Scripts\Inframind\static",image_file.name),"wb") as f: 
          f.write(image_file.getbuffer())         
       classt=inputs(r"C:\Users\sushma\AppData\Local\Programs\Python\Python38\Scripts\Inframind\static\\"+image_file.name)
    Sugar = st.sidebar.slider('Sugar in Table spoon', 0, 20,8)
    Salt = st.sidebar.slider('Salt in Table Spoon', 0, 15, 4)
    Plastic= st.sidebar.slider('plastic required in centimetres', 20, 400, 120)
    data = {'Lemons': Lemons,
            'Sugar': Sugar,
            'Salt': Salt,
            'Plastic': Plastic}
    features = pd.DataFrame(data, index=[0])
    return [features,classt]
feat = user_input_features()
st.header("""Input""")
st.write(feat[0])
if feat[1]=="Damaged":
    st.write("Lemons are damaged fully so quality product can not be produced")
elif feat[1]=="No Damage":
    resultant=knnmodel(feat[0])
    st.header("""Quality Product Result""")
    if resultant[0]=='Reject':
        st.write("It can't produce quality product")
    else:
        st.write("It can produce Quality product")
else:
    st.write("Check Input")





