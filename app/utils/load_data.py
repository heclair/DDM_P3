import pandas as pd
import nltk
import re
import unicodedata
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("portuguese"))

def limpar_texto(texto):
    # Converter para string e lowercase
    texto = str(texto).lower()
    
    # Remover acentuação
    texto = unicodedata.normalize("NFKD", texto).encode("ASCII", "ignore").decode("utf-8")
    
    # Remover pontuação e números
    texto = re.sub(r"[^\w\s]", "", texto)  # pontuação
    texto = re.sub(r"\d+", "", texto)      # números

    # Tokenizar e remover stopwords
    tokens = texto.split()
    tokens = [palavra for palavra in tokens if palavra not in stop_words]

    return " ".join(tokens)

def carregar_dados(caminho_csv):
    try:
        df = pd.read_csv(
            caminho_csv,
            sep=",",
            engine="python",
            on_bad_lines="skip",  # <- substitui error_bad_lines
            quoting=0
        )

        df.dropna(inplace=True)
        df = df.iloc[:, :2]  # Garante que só teremos as duas primeiras colunas
        df.columns = ["texto", "emocao"]
        df["texto_limpo"] = df["texto"].apply(limpar_texto)
        return df
    except Exception as e:
        print(f"[ERRO] Falha ao carregar CSV: {e}")
        raise
