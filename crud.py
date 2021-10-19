from typing import Generator
from sqlalchemy.orm import Session
from models import Prod
from schemas import CreateProdSchema
from datatypes import UpdateProdValuesType

Produto = Prod


def create_prod(db: Session, produto: CreateProdSchema):
    new_prod = Produto(**produto.dict())
    db.add(new_prod)
    db.commit()
    db.refresh(new_prod)
    return new_prod


def retrieve_all_products(db: Session) -> Generator:
    return db.query(Produto).all()


def retrieve_product(db: Session, product_id: int):
    return db.query(Produto).filter(
        Produto.id == product_id
    ).first()


def update_product(db: Session, product_id: int, values: UpdateProdValuesType):
    if Prod := retrieve_product(db, product_id):
        db.query(Produto).filter(
            product_id == product_id
        ).update(values)
        db.commit()
        db.refresh(Prod)
        return Prod


def remove_product(db: Session, product_id: int) -> bool:
    if Prod := retrieve_product(db, product_id):
        db.delete(Prod)
        db.commit()
        return True
    return False
