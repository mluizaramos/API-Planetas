from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.planeta_lua_models import LuaModel
from schemas.lua_schemas import LuaSchema
from core.deps import get_session

router = APIRouter()

# POST
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=LuaSchema)
async def post_lua(lua: LuaSchema, db: AsyncSession = Depends(get_session)):
    novo_id_planeta = lua.planeta_id  # Supondo que o ID do planeta é fornecido no objeto LuaSchema
    nova_lua = LuaModel(nome=lua.nome, planeta_id=novo_id_planeta)  # Atribua o ID do planeta à nova instância de LuaModel
    db.add(nova_lua)
    await db.commit()
    return nova_lua


# GET ALL
@router.get("/", response_model=List[LuaSchema])
async def get_luas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(LuaModel)
        result = await session.execute(query)
        luas: List[LuaModel] = result.scalars().all()
    return luas


# GET ID
@router.get("/{lua_id}", status_code=status.HTTP_200_OK, response_model=LuaSchema)
async def get_lua(lua_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(LuaModel).filter(LuaModel.id == lua_id)
        result = await session.execute(query)
        lua = result.scalar_one_or_none()

        if lua:
            return lua
        else: 
            raise HTTPException(detail="Lua não encontrada", status_code=status.HTTP_404_NOT_FOUND)
        
# PUT
@router.put("/{lua_id}", status_code=status.HTTP_202_ACCEPTED, response_model=LuaSchema)
async def put_lua(lua_id: int, lua: LuaSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(LuaModel).filter(LuaModel.id == lua_id)
        result = await session.execute(query)
        lua_up = result.scalar_one_or_none()
    
        if lua_up:
            lua_up.nome = lua.nome
            await session.commit()
            return lua_up
        else: 
            raise HTTPException(detail="Lua não encontrada", status_code=status.HTTP_404_NOT_FOUND)
        
# DELETE
@router.delete("/{lua_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lua(lua_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(LuaModel).filter(LuaModel.id == lua_id)
        result = await session.execute(query)
        lua_del = result.scalar_one_or_none()

        if lua_del:
            await session.delete(lua_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else: 
            raise HTTPException(detail="Lua não encontrada", status_code=status.HTTP_404_NOT_FOUND)
