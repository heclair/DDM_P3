
# API de Reconhecimento de Emoções em Frases (PLN)

Este projeto consiste em uma API desenvolvida com **FastAPI** que detecta a emoção predominante em frases curtas em português do Brasil, utilizando técnicas de Processamento de Linguagem Natural (PLN) e aprendizado de máquina.

## 🔍 Objetivo
Classificar emoções como: `alegria`, `tristeza`, `raiva`, `medo`, `nojo` e `surpresa` com base no texto enviado pelo usuário.

---

## 📁 Estrutura do Projeto

```
p3_lab_dev/
│
├── app/
│   ├── api/
│   │   └── main.py               # API principal com os endpoints
│   ├── models/                   # Modelos salvos (.joblib)
│   ├── results/                  # Relatórios e CSV de importância de palavras
│   ├── train/
│   │   └── train_model.py        # Treinamento do modelo
│   └── utils/
│       └── load_data.py          # Pré-processamento e carregamento de dados
│
├── data/
│   └── dataset_emocoes_sintetico.csv
│
└── README.md
```

---

## ⚙️ Setup do Projeto

1. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Treine o modelo:
```bash
python -m app.train.train_model
```

4. Inicie a API:
```bash
uvicorn app.main:app --reload
```

---

## 📌 Endpoints

### `POST /api/detectar-emocao`
Recebe uma frase e retorna a emoção predominante e as probabilidades.

**Request JSON:**
```json
{
  "frase": "estou me sentindo animado"
}
```

**Response JSON:**
```json
{
  "emoção_predominante": "alegria",
  "probabilidades (%)": {
    "alegria": 39.07,
    "medo": 12.64,
    "nojo": 11.84,
    "raiva": 11.98,
    "surpresa": 13.3,
    "tristeza": 11.16
  }
}
```

---

## 📊 Resultados

Os resultados da avaliação do modelo são salvos em `app/results/relatorio_classificacao.txt`. Exemplo:

```
              precision    recall  f1-score   support
     alegria       1.00      1.00      1.00       148
        medo       1.00      1.00      1.00       162
        nojo       1.00      1.00      1.00       166
       raiva       1.00      1.00      1.00       160
    surpresa       1.00      1.00      1.00       167
    tristeza       1.00      1.00      1.00       167
```

Também é salvo um arquivo com as palavras mais influentes: `app/results/top_palavras_por_emocao.csv`.

---
## 📄 Licença

Este projeto é de uso educacional e acadêmico. Para uso em produção, é importante aplicar filtros adicionais, controle de viés e validação contínua.

---

## 🙋‍♂️ Contato

Dúvidas ou sugestões? Contribuições são bem-vindas!
