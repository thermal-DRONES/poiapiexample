from pydantic import BaseModel

class ExampleModel(BaseModel):
    a: float
    b: float

def calculate(params: dict) -> dict:
    result = params["a"] + params["b"]
    return {"result": result}