import streamlit as st
import leafmap.foliumap as leafmap
from streamlit_image_comparison import image_comparison

st.set_page_config(page_title="Landslides in Brazil", layout="centered")

st.title("Landslides in Brazil 2023")

# render image-comparison
image_comparison(
    img1="../data/images/2023-01-26-brazil-rainfall-before.jpg",
    img2="../data/images/2023-02-25--brazil-rainfall-after.jpg",
)
st.write("Barra do Sahy and Juquehy: Jan 26th and Feb 25th 2023")

st.image("../data/images/google_ee_brazil_precipitation_map_small.jpg", caption="JAXA/GPM_L3/GSMaP/v6/operational")