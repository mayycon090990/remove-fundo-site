from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import shutil
from rembg import remove
from pathlib import Path

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    return Path("index.html").read_text()

@app.post("/remover-fundo")
async def remover_fundo(file: UploadFile = File(...)):
    input_path = "static/input.png"
    output_path = "static/output.png"

    with open(input_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    with open(input_path, "rb") as inp:
        result = remove(inp.read())

    with open(output_path, "wb") as out:
        out.write(result)

    return FileResponse(output_path, media_type="image/png")
