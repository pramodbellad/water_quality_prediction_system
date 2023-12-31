import requests
import pickle
from PIL import Image
import streamlit as st
from io import BytesIO

# URLs of the pickle and image files
pickle_url = "https://github.com/pramodbellad/water_quality_prediction_system/raw/master/pramod.pkl"
image_url = "https://github.com/pramodbellad/water_quality_prediction_system/raw/master/bbb.png"

# Download the pickle file
response = requests.get(pickle_url)
if response.status_code == 200:
    pickle_content = response.content
else:
    st.error("Error downloading pickle file. Status code:", response.status_code)

# Download the image file
response = requests.get(image_url)
if response.status_code == 200:
    image_content = BytesIO(response.content)
else:
    st.error("Error downloading image file. Status code:", response.status_code)

try:
    # Load the pickle content directly
    model = pickle.loads(pickle_content)
    st.success("Pickle file loaded successfully.")
except Exception as e:
    st.error("Error loading pickle file:", e)

try:
    # Open the image using PIL
    image = Image.open(image_content)
    st.success("Image opened successfully.")
except Exception as e:
    st.error("Error opening image:", e)

# Define the function to make a prediction
def prediction(aluminium, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper,flouride,bacteria, viruses, lead, nitrates, nitrites, perchlorate, radium,silver, uranium):
    # Use the model to predict based on the input parameters
    prediction = model.predict([[aluminium, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper,flouride,
                                 bacteria, viruses, lead, nitrates, nitrites, perchlorate, radium, silver, uranium]])
    if prediction == 0:
        result = "Safe"
    else:
        result = "Unsafe"
    return result

# Define the Streamlit app interface
def main():
    st.title('Automated Water Quality Prediction System')

    st.image(image, "Water Quality sample prediction")

    # Enter all the parameters of water
    st.header('Enter the characteristics of the water:')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        aluminium = st.number_input('aluminium:', min_value=0.000, max_value=5.050, value=0.500)
        ammonia = st.number_input('ammonia:', min_value=0.0, max_value=30.0, value=0.5)
        arsenic = st.number_input('arsenic:', min_value=0.0, max_value=1.05, value=0.5)
        lead = st.number_input('lead:', min_value=0.0, max_value=0.8, value=0.5)
        nitrates = st.number_input('nitrates:', min_value=0.0, max_value=20.0, value=0.5)
    
    with col2:
        barium = st.number_input('barium:', min_value=0.0, max_value=5.0, value=0.5)
        cadmium = st.number_input('cadmium:', min_value=0.0, max_value=0.9, value=0.5)
        chloramine = st.number_input('chloramine:', min_value=0.0, max_value=9.0, value=0.5)
        nitrites = st.number_input('nitrites:', min_value=0.0, max_value=3.0, value=0.5)
        perchlorate = st.number_input('perchlorate:', min_value=0.1, max_value=60.0, value=0.5)

    with col3:
        chromium = st.number_input('chromium:', min_value=0.0, max_value=1.0, value=0.5)
        copper = st.number_input('copper:', min_value=0.0, max_value=2.0, value=0.5)
        flouride = st.number_input('flouride:', min_value=0.0, max_value=3.0, value=0.5)
        bacteria = st.number_input('bacteria:', min_value=0.0, max_value=1.0, value=0.5)
        radium = st.number_input('radium:', min_value=0.0, max_value=8.0, value=0.5)

    with col4:
        silver = st.number_input('silver:', min_value=0.0, max_value=0.5, value=0.5)
        viruses = st.number_input('viruses:', min_value=0.0, max_value=1.0, value=0.5)
        uranium = st.number_input('uranium:', min_value=0.0, max_value=1.0, value=0.5)

    result = " "
    if st.button("Predict Quality of water"):
        result = prediction(aluminium, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper,flouride,
               bacteria, viruses, lead, nitrates, nitrites, perchlorate, radium, silver, uranium)
        st.success("Status of new water sample is: {}".format(result))

if __name__=='__main__':
    main()
