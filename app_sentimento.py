import streamlit as st
import tensorflow as tf
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

@st.cache_resource
def load_model_and_tokenizer():
    model = tf.keras.models.load_model("best_model.h5")
    with open("tokenizer.pkl", "rb") as handle:
        tokenizer = pickle.load(handle)
    return model, tokenizer

model, tokenizer = load_model_and_tokenizer()
MAX_SEQUENCE_LENGTH = 200

def prever_sentimento(texto):
    sequencia = tokenizer.texts_to_sequences([texto])
    entrada = pad_sequences(sequencia, maxlen=MAX_SEQUENCE_LENGTH, padding='post', truncating='post')
    previsao = model.predict(entrada)[0][0]
    return "Positiva 😀" if previsao >= 0.5 else "Negativa 😞"

st.title("Análise de Sentimentos 🎬")
st.write("Digite uma review de filme (em inglês) e veja se o sentimento é positivo ou negativo.")

input_text = st.text_area("Digite aqui:")

if st.button("Analisar"):
    if not input_text.strip():
        st.warning("Digite algum texto primeiro!")
    else:
        resultado = prever_sentimento(input_text)
        st.success(f"Sentimento previsto: **{resultado}**")
