from pathlib import Path
from PIL import Image

import streamlit as st
import torch

import settings
import helper

# Initialize model and path variables
model_path = Path(settings.DETECTION_MODEL)
model = helper.load_model(model_path)

# Page contents
st.set_page_config(page_icon='📡', 
                   page_title='Landslide Detector')
st.title("📡 Landslide Path Detector")

st.markdown(
    """
Explore the capabilities of YOLO custom models to identify and analyze landslides in 
satellite and aerial images. This web application  features two models for landslide 
detection: **Object detection** (bounding box) and **Instance segmentation** (object shape). 
The confidence threshold can be controlled with the slider, allowing you to fine-tune 
the results based on specific requirements. This application is a prototype that deliver 
fairly accurate results, providing both bounding boxes and pixel locations for each 
detected landslide as output.
    """
)

st.markdown(
    """
    This is an open-source project and you are very welcome to contribute your comments, 
    questions, and resources as [issues](https://github.com/Kestener/celerleve-sentinel/issues) 
    or [pull requests](https://github.com/Kestener/celerleve-sentinel/pulls) to the 
    [GitHub repository](https://github.com/Kestener/celerleve-sentinel).
    """
)

st.sidebar.image('images/celerleve_logo_small.jpg')
st.sidebar.header("Model Settings")

mlmodel_radio = st.sidebar.radio(
    "Select Task", ['Detection', 'Segmentation'])
conf = float(st.sidebar.slider("Select confidence", 25, 100, 40)) / 100
if mlmodel_radio == 'Detection':
    dirpath_locator = settings.DETECT_LOCATOR
    model_path = Path(settings.DETECTION_MODEL)
elif mlmodel_radio == 'Segmentation':
    dirpath_locator = settings.SEGMENT_LOCATOR
    model_path = Path(settings.SEGMENTATION_MODEL)
try:
    model = helper.load_model(model_path)
except Exception as ex:
    print(ex)
    st.write(f"Unable to load model. Check the specified path: {model_path}")

source_img = None
st.sidebar.header("Image configuration")
source_radio = st.sidebar.radio(
    "Select Source", settings.SOURCES_LIST)

# body
# If image is selected
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Choose an image...", type=["jpg", "jpeg", "png", 'bmp', 'webp'])
    #save_radio = st.sidebar.radio("Save image to download", ["Yes", "No"])
    #save = True if save_radio == 'Yes' else False
    save = False

    if source_img is None:
        col1, col2 = st.columns(2)

        with col1:
            default_image_path = str(settings.DEFAULT_IMAGE)
            image = Image.open(default_image_path)
            st.image(default_image_path, caption='Default Image')
        
        with col2:
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            image = Image.open(default_detected_image_path)
            st.image(default_detected_image_path, caption='Detected Image')

    else:
        with st.container():
        #if source_img is None:
        #    default_image_path = str(settings.DEFAULT_IMAGE)
        #    image = Image.open(default_image_path)
        #    st.image(default_image_path, caption='Default Image')
        #else:
            image = Image.open(source_img)
            st.image(source_img, caption='Uploaded Image')

    #with col2:
    with st.container():
        #if source_img is None:
        #    default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
        #    image = Image.open(default_detected_image_path)
        #    st.image(default_detected_image_path, caption='Detected Image')
        #else:
            if st.sidebar.button('Detect Objects'):
                with torch.no_grad():
                    res = model.predict(
                        image, save=save, save_txt=save, exist_ok=True, conf=conf)
                    boxes = res[0].boxes
                    res_plotted = res[0].plot(line_width=1, font_size=1)[:, :, ::-1]
                    st.image(res_plotted, caption='Detected Image')
                #    IMAGE_DOWNLOAD_PATH = f"runs/{dirpath_locator}/predict/image0.jpg"
                #    with open(IMAGE_DOWNLOAD_PATH, 'rb') as fl:
                #        st.download_button("Download object-detected image",
                #                           data=fl,
                #                           file_name="image0.jpg",
                #                           mime='image/jpg'
                #                           )
                try:
                    with st.expander("Detection Results"):
                        for box in boxes:
                            st.write(box.xywh)
                except Exception as ex:
                    # st.write(ex)
                    st.write("No image is uploaded yet!")
