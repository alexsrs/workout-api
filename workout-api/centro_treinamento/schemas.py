from typing import Annotated
from contrib.schemas import BaseSchema
from pydantic import Field

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de treinamento', example='CT Magrelo', max-length=20)]
    endereco: Annotated[str, Field(description='Endereço do Centro de treinamento', example='Rua do arroz - 34', max-length=60)]
    proprietario: Annotated[str, Field(description='Nome do Proprietario do Centro de treinamento', example='CT Magrelo', max-length=30)]