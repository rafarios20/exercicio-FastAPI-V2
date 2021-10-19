from pydantic import BaseModel


class ProdutoBaseSchema(BaseModel):
    id: int
    produto: str
    valor: float
    quantidade: str


class CreateProdSchema(ProdutoBaseSchema):
    produto: str = ""
    valor: float = ""
    quantidade: str = ""


class UpdateProdSchema(ProdutoBaseSchema):
    produto: str = ""
    valor: float = ""
    quantidade: str = ""


class ProdSchema(ProdutoBaseSchema):
    id: int
