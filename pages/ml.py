import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Charger le modèle pré-entraîné
loaded_model = pickle.load(open("best_model_2.pkl", "rb"))

# Charger le scaler
with open('scaler_2.pkl', 'rb') as f:
    scaler, column_names = pickle.load(f)


# Titre en gras et italique
st.set_page_config(page_title="Consommation énergétique Modèle de ML", page_icon=":guardsman:", layout="wide")
st.title("Consommation énergétique")

# Inputs de l'utilisateur
input1 = st.number_input("Taille Dataset")
input2 = st.number_input("Nombre de Batch")
input3 = st.number_input("Nombre de parametres")

input1 = float(input1)
input2 = float(input2)
input3 = float(input3)

# Normaliser les inputs de l'utilisateur avec le scaler
new_data = pd.DataFrame([[input1, input2, input3]], columns=column_names)
inputs_scaled = scaler.transform(new_data)

# Stocker les inputs de l'utilisateur pour optimiser les performances
@st.cache
def get_prediction(inputs_scaled):
    return loaded_model.predict(inputs_scaled)

# Bouton pour calculer la prédiction
if st.button("Calculer"):
    prediction = get_prediction(inputs_scaled)
    st.write("La consommation énergétique sera de", prediction[0])

