import joblib
import os
from app.utils.load_data import limpar_texto

# Carregar modelo e vetor
modelo = joblib.load("app/models/modelo_emocoes.joblib")
vectorizer = joblib.load("app/models/tfidf_vectorizer.joblib")

def prever_emocao(frase: str):
    texto_limpo = limpar_texto(frase)
    vetor = vectorizer.transform([texto_limpo])
    predicao = modelo.predict(vetor)[0]
    probabilidades = modelo.predict_proba(vetor)[0]

    dist_emocoes = {
        classe: round(prob * 100, 2)
        for classe, prob in zip(modelo.classes_, probabilidades)
    }

    return {
        "emoção_predominante": predicao,
        "probabilidades (%)": dist_emocoes
    }

def obter_relatorio():
    relatorio_path = "app/results/relatorio_classificacao.txt"
    if os.path.exists(relatorio_path):
        with open(relatorio_path, "r", encoding="utf-8") as f:
            relatorio = f.read()
        return {"relatorio_classificacao": relatorio}
    return {"erro": "Relatório não encontrado."}
