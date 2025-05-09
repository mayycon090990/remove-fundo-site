
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
import io

app = FastAPI()

# Liberar CORS para o frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/remove-background")
async def remove_background(image: UploadFile = File(...)):
    input_image = await image.read()
    output_image = remove(input_image)
    return StreamingResponse(io.BytesIO(output_image), media_type="image/png")
