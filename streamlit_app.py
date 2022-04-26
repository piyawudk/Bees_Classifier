import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# setup page
CURRENT_THEME = "dark"
IS_DARK_THEME = True
st.set_page_config(page_title='Bees Classifier', page_icon="🐝")
st.set_option('deprecation.showfileUploaderEncoding', False) # disable deprecation error
with open("streamlit_app.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# picture banner
image = Image.open('etc/Banner.png')
st.image(image)

st.header("AI that classifies Honey bees and Bumble bees.")
st.caption("by Piyawud Koonmanee, Nithiwat Pattrapong, Tulatorn Prakitjanuruk, Chananyu Kamolsuntron")

# load CNN model
@st.cache(allow_output_mutation = True)     # enable cache to improve the loading time
def get_model():
    model = load_model('model/balaced_op_cnn.h5')
    return model

with st.spinner('Loading Model...'):
    model = get_model()

# file uploader
img = st.file_uploader("Please upload the file", type=["jpg","jpeg","png"])

# perform prediction
if img is not None:
    img = Image.open(img)
    img = img.convert('RGB')
    
    # display centered picture
    col1, col2, col3 = st.columns([1,4,1])
    with col1:
        st.write('')
    with col2:
        st.image(img, caption="Predicting image")
    with col3:
        st.write('')

    with st.spinner('Predicting...'):
        # resize the image to 100x100 pixels
        img = img.resize((100,100))

        # scale down the data
        data = np.asarray(img) / 255.0

        # expan dimension for CNN layers
        data = np.expand_dims(data, axis=0)

        # predict
        prediction = model.predict(data)

        # get maximum value
        classes = np.argmax(prediction, axis = 1)

        if classes == 1.0:
            result = "I'm " + str(np.round(np.max(prediction)*100,2)) +"% sure that this is a Bumble bee (genus Bombus)."
            st.subheader(result)
        else:
            result = "I'm " + str(np.round(np.max(prediction)*100,2)) +"% sure that this is a Honey bee (genus Apis)."
            st.subheader(result)