import cv2
import numpy as np
from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

st.set_option('deprecation.showfileUploaderEncoding', False)

img_file = st.file_uploader("Upload da imagem", type=["png", "jpg", "jpeg"])

img_file_background = st.file_uploader("Upload da imagem de fundo", type=["png", "jpg", "jpeg"])

if img_file is not None and img_file_background is not None:
    
    image = Image.open(img_file)
    img_array = np.array(image)
    
    image2 = Image.open(img_file_background)
    img_array2 = np.array(image2)
    
    shape = np.shape(img_array)    
    img_array2 = img_array2[:shape[0], :shape[1]]
    
    st.image(img_array, caption="Imagem original", use_column_width=True)
    
    st.image(img_array2, caption="Imagem de fundo", use_column_width=True)
    
    r = st.sidebar.slider("Red", 0, 255, (0, 255), 1)
    g = st.sidebar.slider("Green", 0, 255, (0, 255), 1)
    b = st.sidebar.slider("Blue", 0, 255, (0, 255), 1)
    
    lower_green = np.array([r[0], g[0], b[0]]) 
    upper_green = np.array([r[1], g[1], b[1]]) 

    mask = cv2.inRange(img_array, lower_green, upper_green)
    
    st.image(mask, caption="Mask", use_column_width=True)
    
    masked_image = np.copy(img_array)

    masked_image[mask != 255] = [0, 0, 0]

    img_array2[mask == 255] = [0, 0, 0]

    st.image(img_array2, caption="Mask", use_column_width=True)

    imgfinal = img_array2+masked_image
    
    st.image(imgfinal, caption="Resultado final", use_column_width=True)