import streamlit as st
import leafmap.foliumap as leafmap
from streamlit_image_comparison import image_comparison
import base64

st.set_page_config(page_title="Landslides in Brazil", layout="centered")

st.title("Landslides in Brazil 2023")

# render image-comparison
image_comparison(
    img1="../data/images/2023-01-26-brazil-rainfall-before.jpg",
    img2="../data/images/2023-02-25--brazil-rainfall-after.jpg",
)
st.write("Barra do Sahy and Juquehy: Jan 26th and Feb 25th 2023")

st.image("../data/images/google_ee_brazil_precipitation_map_small.jpg", caption="JAXA/GPM_L3/GSMaP/v6/operational")

### gif from local file
file_ = open("../data/images/weather_viz_small.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="weather gif">',
    unsafe_allow_html=True,
)
st.write("Hourly precipitation: Feb 24th - Feb 25th 2023")