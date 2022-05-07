<div align="center">
    <img src="./etc/Banner.png" alt="🐝 Bees Classifier" width="800px" />
</div>

## Introduction 📝
Do you know why bees are important to our planet? It’s because they take a major part in pollination so the plant can reproduce. If all the bees went extinct, it would destroy the balance of the Earth’s ecosystem and affect global food supplies. Currently, there are more than 20,000 species that need to be classified and deployed to the selected pollinators to help the failing ecosystem. It is a dangerous and tedious task for the scientist and researcher to do it manually.

Our main objective is to correctly predict the bee species using several AI techniques to find out the best model for this problem. In this project, we will be focusing on 2 common pollinators which are honey bees from the Apis genus and bumblebees from the Bombus genus.
<br><br>

## Dataset 📚
The dataset used comes from <a href="https://beespotter.org/">BeeSpotter</a>, an online repository of volunteer submitted images of bees in Illinois, Ohio, and Missouri. We have around 3,142 pictures of bumblebees (genus Bombus) and 827 of honey bees (genus Apis). Notice that this is an imbalanced problem so we decided to make 3 datasets and compare the performance.
1. Unbalanced dataset - directly use the given dataset to train the model
2. Balanced dataset - apply the random over-sampling technique to equalize the amount of data
3. Optimized dataset - manually delete the unmeaningful images or the one that doesn't contain the bees
<br><br>

## Model used 🤖
- fine-tuned Support Vector Machine (SVM) with Bagging Classifier to speed up the training time
- fine-tuned Logistic Regression (LR)
- Convolutional Neural Network (CNN) - built model on top of Inception V3
<br><br>

## Summary ✍
Upon 3 scenarios of the dataset, we found out that the optimized dataset is performing the best here with a faster training time yet higher accuracy when compared to the balanced data. Here, CNN is performing really well with 98.36% accuracy and a 0.987 AUC score.
<br><br>

## Deploy 🌐
We select the best model and deploy it on Streamlit. You can test it out here https://share.streamlit.io/piyawudk/bees_classifier
<br><br>

## Repository Contents 📁
**datasets/**
- **Images/** - original dataset
- **resized_image/** - resize original dataset images
- **resized_image_balanced/** - resize original dataset images with random-oversampling technique
- **Optimized_Images/** - dataset that only contain meaningful images (clear view of bees)
- **resized_optimized_image_balanced/** - dataset that only contain meaningful images with random-oversampling technique
- **verify_images/** - cropeed images use for finding the confidence level (image from Google)
- **labels.csv** - original data labels
- **labels_balanced.csv** - data labels after random-oversampling technique
- **labels_optimized_balanced.csv** - data labels after optimizing images and random-oversampling technique
<br><br>

**etc/**
- **Bees Testing Image/** - images used to test on Streamlit (similar to **datasets/verify_images/**, can be found on Google)
- **Banner.png** - banner image for Streamlit and GitHub
<br><br>

**model/** - saved model from training
- key words:
    - svm - Support Vector Machine
    - lr - Logistic Regression
    - cnn - Convolutional Neural Network
    - op - optimized dataset
    - unbalanced - raw data
    - balanced - raw data with random-oversampling
<br><br>
 
**main.ipynb** - main python code
<br><br>

**Streamlit files:**
- **requirements.txt** - necessary dependencies for Streamlit (equivalent or higher)
- **streamlit_app.css** - CSS file for styling the website
- **streamlit_app.py** - python code to build a Streamlit website
<br><br>

## Dependencies 🦾
Tested on 2 May 2022
- Python - 3.7
- Tensorflow - 2.8.0
- Numpy - 1.21.6
- Pandas - 1.4.2
- Matplotlib - 3.5.1
- Pillow - 7.1.2
- OpenCV - 4.5.5.64
- Scikit-learn - 1.0.2
- Joblib - 1.1.0
- Streamlit - 1.8.1
<br><br>

## Endnotes 📜
Originally, we run our code on Google Colab and the files in this repository undergo changes in the file path without any testing. So if there are any issues, feel free to contact us.
<br><br>

## Contributors ✨
1. **Piyawud Koonmanee - https://github.com/piyawudk**
2. **Nithiwat Pattrapong - https://github.com/nithiwatp**
3. **Tulatorn Prakitjanuruk - TBA**
4. **Chananyu Kamolsuntron - TBA**
