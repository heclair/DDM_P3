import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from app.utils.load_data import carregar_dados

df = carregar_dados("data/dataset_emocoes_sintetico.csv")
print(df.head())
