import streamlit as st
import pickle
import numpy as np
import pandas as pd
from PIL import Image

# Load the pre-trained model
#loaded_model = pickle.load(open("best_model_2.pkl", "rb"))

# Load the scaler
with open('scaler_2.pkl', 'rb') as f:
    scaler, column_names = pickle.load(f)

# Bold and italic title

st.set_page_config(page_title="Consommation énergétique Modèle de ML", page_icon=":guardsman:", layout="wide")

st.markdown(
    """
    <style>
        body {
            background-color: #2b2d42;
        }
        h1 {
            text-align: center;
            color: #2b2d42;

            border-color: #f2f2f2;
        }
        .number-input-container {
            width: 50%;
            color: #f2f2f2;
        }
        input[type='number'] {
            color: #f2f2f2;
            background-color: #5e5e5e;
            border-color: #5e5e5e;
        }
        .stButton {
            background-color: #f2f2f2;
            color: #2b2d42;
            border-color: #f2f2f2;
        }
    </style>


    """,
    unsafe_allow_html=True,
)

st.title("Consommation énergétique")

input1 = st.number_input("Taille Dataset", value=0, step=10000)
input2 = st.number_input("Taille du Batch", value=0, step=16)
input3 = st.number_input("Nombre de parametres", value=0, step=100000)

input1 = float(input1)
input2 = float(input2)
input3 = float(input3)

#new_data = pd.DataFrame([[input1, input2, input3]], columns=column_names)
#inputs_scaled = scaler.transform(new_data)


@st.cache
def get_prediction(inputs):
    #return loaded_model.predict(inputs_scaled)
    w0 = 0.0036
    w1 = - 0.084
    w2 = 7.4e-05

    return w0 * inputs[0] + w1 * inputs[1] + w2 * inputs[2]


if st.button("Calculer"):
    prediction = get_prediction([input1, input2, input3])
    #prediction = get_prediction(inputs_scaled)
    st.write("La consommation énergétique sera de ", prediction[0], " mwh")
