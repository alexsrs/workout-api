from typing import Annotated
from contrib.schemas import BaseSchema
from pydantic import Field

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome do categoria', example='Scale', max-length=10)]
