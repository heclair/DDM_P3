import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from app.utils.load_data import carregar_dados


# 1. Carregar os dados
df = carregar_dados("data/dataset_emocoes_sintetico.csv")

# 2. Separar dados
X = df["texto_limpo"]
y = df["emocao"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# 3. Vetorização TF-IDF
vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=2)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 4. Treinamento
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# 5. Avaliação
y_pred = model.predict(X_test_tfidf)
relatorio = classification_report(y_test, y_pred)

os.makedirs("app/models", exist_ok=True)
os.makedirs("app/results", exist_ok=True)

with open("app/results/relatorio_classificacao.txt", "w", encoding="utf-8") as f:
    f.write(relatorio)

print("[OK] Relatório salvo em app/results/relatorio_classificacao.txt")
print(relatorio)

# 6. Explicabilidade aprimorada: palavras mais relevantes por emoção
feature_names = vectorizer.get_feature_names_out()
coef = model.coef_
classes = model.classes_

top_n = 10
explicacoes = {}

for i, classe in enumerate(classes):
    top_indices = np.argsort(np.abs(coef[i]))[::-1][:top_n]
    top_palavras = [(feature_names[j], coef[i][j]) for j in top_indices]
    explicacoes[classe] = top_palavras

with open("app/results/explicacao_por_emocao.csv", "w", encoding="utf-8") as f:
    f.write("emocao,palavra,peso\n")
    for emocao, palavras in explicacoes.items():
        for palavra, peso in palavras:
            f.write(f"{emocao},{palavra},{peso:.5f}\n")

print("[OK] Interpretação por emoção salva em app/results/explicacao_por_emocao.csv")

# 7. Salvar modelo e vetorizer
joblib.dump(model, "app/models/modelo_emocoes.joblib")
joblib.dump(vectorizer, "app/models/tfidf_vectorizer.joblib")
print("[OK] Modelo e vectorizer salvos.")
