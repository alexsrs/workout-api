from typing import Annotated
from contrib.schemas import BaseSchema
from pydantic import Field, PositiveFloat

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max-length=50)]
    cpf: Annotated[str, Field(description='Cpf do atleta', example='12345678900', max-length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example='25')]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example='75.0')]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example='1.83')]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max-length=1)]

