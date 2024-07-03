from atleta.schemas import AtletaIn
from contrib.dependencies import DatabaseDependency
from fastapi import APIRouter, Body, status

router = APIRouter()

@router.post(
    '/',
    summary='Criar um novo atleta',
    status_code= status.HTTP_201_CREATED,
)

async def post(
    db_session: DatabaseDependency, 
    atleta_in: AtletaIn = Body(...)
):
    pass