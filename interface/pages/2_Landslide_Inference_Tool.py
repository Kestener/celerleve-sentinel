import io
from PIL import Image
import streamlit as st
from ultralytics import YOLO
import time


MODEL_PATH = '../../data/models/YOLOv8_Landslide_WorkingV1_best.pt'
LABELS_PATH = '../../data/models/model_classes.txt'


def load_image():
    uploaded_file = st.file_uploader(label='Pick an image to test')
    if uploaded_file is not None:
        st.write(uploaded_file)
        img = Image.open(uploaded_file)
        #image_data = uploaded_file.getvalue()
        st.image(img)
        #return Image.open(io.BytesIO(image_data))
        return img
    else:
        return None


def load_model(model_path):
    model = YOLO(model_path)
    return model


def load_labels(labels_file):
    with open(labels_file, "r") as f:
        categories = [s.strip() for s in f.readlines()]
        return categories


def mod_predict(model, input_image):
    result = model.predict(input_image)
    return result

def mod_predict2(model, input_image):
    im1 = input_image
    results = model.predict(source=im1, save=True)  # save plotted images
    return results



def main():
    st.title('Custom model demo')
    model = load_model(MODEL_PATH)
    #categories = load_labels(LABELS_PATH)
    image = load_image()
    result = st.button('Run on image')
    if result:
        st.write('Calculating results...')
        #mod_predict2(model, image)
        im1 = Image.open('../../data/satellite_images_train_v1/satellite_predict_test_y.jpg')
        results = model.predict(source=im1, save=True)
        st.image('runs/detect/predict/satellite_predict_test_y.jpg')

#        import glob
#        import os

#        list_of_files = glob.glob('/path/to/folder/*') # * means all if need specific format then *.csv
#        latest_file = max(list_of_files, key=os.path.getctime)
#        print(latest_file)
        


if __name__ == '__main__':
    main()