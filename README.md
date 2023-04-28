# Celerleve - Landslides detection with satellite imagery
An accessible framework for object detection

This repository provides the code required to replicate the figures and functionalities presented at Spiced Data Science bootcamp final project presentation.

It also provides examples of the generalizability of this approach, enabling users with limited computing resources and basic knowledge in machine learning or satellite imagery processing to train and utilize the application for custom objects.

![interface_example](../celerleve-sentinel/interface/inference_app/images/interface_example.png)

## Structure of the repository

### 1. Installation

The easiest way to replicate the environment is by pip installing the requirements.txt or activating the conda yml. This project is coded in Python 3.9.

### 2. Code

- [eda/](eda/): This folder contains scripts and notebooks used for exploratory data analysis, Google Earth Engine script for the precipitation figures using JAXA, and a simple function to generate the gif time lapse images used in the presentation.
- [interface/](interface/): This folder contains two subfolders including the application interface using Streamlit. The backup folder refers to the first version attempt, while the [inference_app/](interface/inference_app/) contains the working application.
- [preprocessing/](preprocessing/): Here you find the notebooks and scripts used to collect satellite data and preprocess them before image annotation and model training.
- [training/](training/): This folder includes the Google Colab notebooks used to train the model.

### 3. Data
Data collected from Copernicus Open Access Hub using the sentinelsat and sentinelhub libraries, plus additional images manually collected from multiple media sources.

### 4. Results
This application demonstrates the potential of a computer vision workflow using platforms like [Roboflow](https://roboflow.com/) with [YOLOv8](https://github.com/ultralytics/ultralytics) for satellite imagery with limited hardware and storage capability. The first iteration of the project is a prototype with basic functionality.

## Use of code and data
Further details are available in the [code license](LICENSE).

## Acknowledgments
The streamlit application is based on [CodingMantras](https://github.com/CodingMantras/yolov8-streamlit-detection-tracking) repository.