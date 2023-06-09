import base64
from io import BytesIO
from ultralytics import YOLO


def load_model(model_path):
    model = YOLO(model_path)
    return model

def get_image_download_link(img,filename,text):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href