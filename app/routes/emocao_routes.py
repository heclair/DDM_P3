from fastapi import APIRouter
from pydantic import BaseModel
from app.services.emocao_service import prever_emocao, obter_relatorio

router = APIRouter()

class EntradaTexto(BaseModel):
    frase: str

@router.post("/api/detectar-emocao")
def detectar_emocao(entrada: EntradaTexto):
    return prever_emocao(entrada.frase)

@router.get("/api/resultados")
def resultados_avaliacao():
    return obter_relatorio()
