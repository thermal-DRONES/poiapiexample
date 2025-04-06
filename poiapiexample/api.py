from fastapi import FastAPI, APIRouter, UploadFile, File, Query
from fastapi.responses import FileResponse, StreamingResponse
import logging
import io

API_VERSION = "/v0.1.0"

from . import model

try:
    from .. import *
    router = APIRouter(prefix=API_VERSION[0:3])
    logging.info("Using APIRouter class")
except:
    router = FastAPI(prefix=API_VERSION[0:3])
    logging.info("Using FastAPI class")

logger = logging.getLogger("uvicorn.error")

@router.get("/")
def helloworld():
    logger.info("Hallo!!!")
    return {"message": "Hello World"}

# GET-Endpunkt mit Beispielberechnung via Query-Parametern
@router.get("/calculate")
def calculate_get(a: float = Query(...), b: float = Query(...)):
    result = model.calculate({"a": a, "b": b})
    return result

# POST-Endpunkt für JSON mit pydantic-Modell
@router.post("/create")
async def create(data: model.ExampleModel):
    params = data.dict()
    return model.calculate(params)

# Dateiexport (klassisch, z. B. generierte Datei)
@router.get("/download")
def download_file():
    path = "/tmp/example.txt"
    with open(path, "w") as f:
        f.write("Dies ist eine exportierte Datei.")
    return FileResponse(path, filename="example.txt")

# Streaming-Export (z. B. große Datenmengen, DEM-Datei etc.)
@router.get("/stream")
def stream_file():
    def file_generator():
        for i in range(10):
            yield f"Zeile {i}\n".encode("utf-8")
    return StreamingResponse(file_generator(), media_type="text/plain")

# Datei-Upload
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    logger.info(f"Dateiinhalt (gekürzt): {content[:50]}")
    return {"filename": file.filename, "size": len(content)}

# FastAPI-Entrypoint
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("your_service.api:router", host="0.0.0.0", port=8000, reload=True)
