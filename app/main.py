from fastapi import FastAPI
from app.routes.emocao_routes import router as emocao_router

app = FastAPI(title="API de Reconhecimento de Emoções", version="1.0")

# Incluir rotas
app.include_router(emocao_router)
