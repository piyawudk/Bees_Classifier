<div align="center">
    <img src="./etc/Banner.png" alt="🐝 Bees Classifier" width="800px" />
</div>

## Introduction 📝
Do you know why bees are important to our planet? It’s because they take a major part in pollination so the plant can reproduce. If all the bees went extinct, it would destroy the balance of the Earth’s ecosystem and affect global food supplies. Currently, there are more than 20,000 species that need to be classified and deployed to the selected pollinators to help the failing ecosystem. It is a dangerous and tedious task for the scientist and researcher to do it manually.

Our main objective is to correctly predict the bee species using several AI techniques to find out the best model for this problem. In this project, we will be focusing on 2 common pollinators which are honey bees from the Apis genus and bumblebees from the Bombus genus.

## Dataset 📚
The dataset used comes from <a href="https://beespotter.org/">BeeSpotter</a>, an online repository of volunteer submitted images of bees in Illinois, Ohio, and Missouri. We have around 3,142 pictures of bumblebees (genus Bombus) and 827 of honey bees (genus Apis). Notice that this is an imbalanced problem so we decided to make 3 datasets and compare the performance.
1. Unbalanced dataset - directly use the given dataset to train the model
2. Balanced dataset - apply the random over-sampling technique to equalize the amount of data
3. Optimized dataset - manually delete the unmeaningful images or the one that doesn't contain the bees

## Model used 🤖
- fine-tuned Support Vector Machine (SVM) with Bagging Classifier to speed up the training time
- fine-tuned Logistic Regression (LR)
- Convolutional Neural Network (CNN) - built model on top of Inception V3

## Summary ✍
Upon 3 scenarios of the dataset, we found out that the optimized dataset is performing the best here with a faster training time yet higher accuracy when compared to the balanced data. Here, CNN is performing really well with 98.36% accuracy and a 0.987 AUC score.

## Deploy 🌐
We select the best model and deploy it on Streamlit. You can test it out here https://share.streamlit.io/piyawudk/bees_classifier

## Endnotes 📜
Originally, we run our code on Google Colab and the files in this repository undergo changes in the file path without any testing. So if there are any issues, feel free to contact us.

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

## Contributors ✨
1. **Piyawud Koonmanee - https://github.com/piyawudk**
2. **Nithiwat Pattrapong - https://github.com/nithiwatp**
3. **Tulatorn Prakitjanuruk - TBA**
4. **Chananyu Kamolsuntron - TBA**
