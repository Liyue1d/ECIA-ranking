import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

import streamlit as st

st.set_page_config(page_title="Comparaison énergétique des langages de programmation", page_icon=":guardsman:", layout="wide")
st.image("talan.png", width=50, use_column_width=True)

st.title("Projet empreinte carbone de l'IA")

st.markdown("Dans le **premier lien**, nous présentons une comparaison énergétique des différents langages de programmation")
st.markdown("Dans le **2ème lien**, nous présentons, grâce à une IA, la consommation énergétique dépensée par votre"
            " modèle à chaque batch, pour des données tabulaires).")