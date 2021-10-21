from pydantic import BaseModel


class ProdutoBaseSchema(BaseModel):
    produto: str
    valor: float
    quantidade: int


class CreateProdSchema(ProdutoBaseSchema):
    produto: str = ""
    valor: float = ""
    quantidade: int = ""


class UpdateProdSchema(ProdutoBaseSchema):
    produto: str = ""
    valor: float = ""
    quantidade: int = ""


class ProdSchema(ProdutoBaseSchema):
    id: int
