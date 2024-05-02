from typing import Optional
from pydantic import BaseModel as SCBaseModel

class LuaSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    
    
    class Config:
        orm_mode = True
