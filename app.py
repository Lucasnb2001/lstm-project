from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# ========== CONFIGS ==========
MAX_SEQUENCE_LENGTH = 200
TOKENIZER_PATH = "tokenizer.pkl"
MODEL_PATH = "best_model.h5"

# ========== INICIALIZAÇÃO ==========
app = FastAPI(title="Text Classification API (LSTM)")

# Carrega modelo
model = load_model(MODEL_PATH)

# Carrega tokenizer
with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)

# ========== SCHEMAS ==========
class TextInput(BaseModel):
    text: Union[str, List[str]]

class PredictionResponse(BaseModel):
    input: List[str]
    prediction: List[int]

# ========== ENDPOINT ==========
@app.post("/predict", response_model=PredictionResponse)
def predict(input_data: TextInput):
    # Garante lista
    texts = input_data.text if isinstance(input_data.text, list) else [input_data.text]

    # Tokeniza e padroniza
    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH, padding="post", truncating="post")

    # Predição
    preds = (model.predict(padded) > 0.5).astype("int32").flatten().tolist()

    return {"input": texts, "prediction": preds}
