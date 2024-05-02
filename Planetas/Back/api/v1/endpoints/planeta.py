from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.planeta_lua_models import PlanetaModel
from schemas.planeta_schemas import PlanetaSchema
from core.deps import get_session

router = APIRouter()

# POST
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PlanetaSchema)
async def post_planeta(planeta: PlanetaSchema, db: AsyncSession = Depends(get_session)):

    novo_planeta = PlanetaModel(nome=planeta.nome, temperatura_media=planeta.temperatura_media, ano=planeta.ano , rotacao=planeta.rotacao, translacao=planeta.translacao)
    db.add(novo_planeta)
    await db.commit()
    return novo_planeta

# GET ALL
@router.get("/", response_model=List[PlanetaSchema])
async def get_planetas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PlanetaModel)
        result = await session.execute(query)
        planetas: List[PlanetaModel] = result.unique().scalars().all() 
    return planetas

# GET ID
@router.get("/{planeta_id}", status_code=status.HTTP_200_OK, response_model=PlanetaSchema)
async def get_planeta(planeta_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PlanetaModel).filter(PlanetaModel.id == planeta_id)
        result = await session.execute(query)
        planeta = result.scalar()

        if planeta:
            return planeta
        else: 
            raise HTTPException(detail="Planeta não encontrado", status_code=status.HTTP_404_NOT_FOUND)

 
# PUT
@router.put("/{planeta_id}", status_code=status.HTTP_202_ACCEPTED, response_model=PlanetaSchema)
async def put_planeta(planeta_id: int, planeta: PlanetaSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        # Consulta apenas o PlanetaModel pelo ID
        query = select(PlanetaModel).filter(PlanetaModel.id == planeta_id)
        result = await session.execute(query)
        planeta_up = result.scalar()

        if planeta_up:
            planeta_up.nome = planeta.nome
            planeta_up.temperatura_media = planeta.temperatura_media
            planeta_up.ano = planeta.ano
            planeta_up.rotacao = planeta.rotacao
            planeta_up.translacao = planeta.translacao
           
            await session.commit()
            return planeta_up
        else:
            raise HTTPException(detail="Planeta não encontrado", status_code=status.HTTP_404_NOT_FOUND)

        
# DELETE
@router.delete("/{planeta_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_planeta(planeta_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PlanetaModel).filter(PlanetaModel.id == planeta_id)
        result = await session.execute(query)
        planeta_del = result.scalar()

        if planeta_del:
            await session.delete(planeta_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else: 
            raise HTTPException(detail="Planeta não encontrado", status_code=status.HTTP_404_NOT_FOUND)