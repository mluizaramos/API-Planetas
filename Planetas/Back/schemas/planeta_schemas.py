from typing import Optional
from pydantic import BaseModel as SCBaseModel

class PlanetaSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    temperatura_media: int
    ano: str
    rotacao: str
    translacao: str
    
    class Config:
        orm_mode = True