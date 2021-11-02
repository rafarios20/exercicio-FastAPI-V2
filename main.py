from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi_simple_security import api_key_security, api_key_router
from sqlalchemy.orm import Session
from crud import (
    create_prod,
    remove_product,
    retrieve_all_products,
    retrieve_product,
    update_product
)
from typing import Generator
from database import Base, SessionLocal, engine
from datatypes import ProdType
from schemas import (
    CreateProdSchema,
    UpdateProdSchema
)

Base.metadata.create_all(bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

app.include_router(api_key_router, prefix="/auth", tags=["_auth"])


@app.get("/secure", dependencies=[Depends(api_key_security)])
async def secure_endpoint():
    return {"message": "Chave está funcionando!!"}


@app.get("/", tags=["Home"])
async def root():
    response = RedirectResponse(url='/docs')
    return response


@app.get("/produtos/", status_code=status.HTTP_200_OK, tags=["Procurar todos os produtos"], dependencies=[Depends(api_key_security)])
def get_all_products(db: Session = Depends(get_db)) -> Generator:
    if result := retrieve_all_products(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem produtos cadastrados.",
    )


@app.get("/produtos/{id_produto}", status_code=status.HTTP_200_OK, tags=["Procurar por um produto"], dependencies=[Depends(api_key_security)])
def get_produto(id_produto: int, db: Session = Depends(get_db)) -> ProdType:
    if result := retrieve_product(db, id_produto):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Produto 'id={id_produto}' não encontrado.",
    )


@app.post("/produtos/", status_code=status.HTTP_201_CREATED, tags=["Inserir um produto"], dependencies=[Depends(api_key_security)])
def post_product(produto: CreateProdSchema, db: Session = Depends(get_db), ) -> ProdType:
    if result := create_prod(db, produto):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )


@app.put("/produtos/{id_produto}", status_code=status.HTTP_201_CREATED, tags=["Atualizar um produto"], dependencies=[Depends(api_key_security)])
def put_product(id_produto: int, produto: UpdateProdSchema, db: Session = Depends(get_db), ) -> ProdType:
    if result := update_product(
            db, id_produto, {key: value for key, value in produto if value}
    ):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Produto 'id={id_produto}' não encontrado.",
    )


@app.delete("/produtos/{id_produto}", status_code=status.HTTP_204_NO_CONTENT, tags=["Remover um produto"], dependencies=[Depends(api_key_security)])
def delete_produto(id_produto: int, db: Session = Depends(get_db)) -> None:
    if not remove_product(db, id_produto):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto 'id={id_produto}' não encontrado.",
        )
