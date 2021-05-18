from fastapi import FastAPI, File, UploadFile
from starlette.responses import FileResponse
import os,time

app = FastAPI()


@app.get("/")
async def home():
    return "ESP32Cam FastAPI"


@app.post("/upload/")
async def create_upload_file(imageFile: UploadFile = File(...)):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = f'{dir_path}/uploads/{time.time()}-{imageFile.filename}'
    f = open(f'{filename}', 'wb')
    content = await imageFile.read()
    f.write(content)
    return {"filename": imageFile.filename}

@app.get("/getFile")
async def getFile():
    return os.listdir(os.path.dirname(os.path.realpath(__file__) + "/uploads")

@app.get("/getFile/{fileName}")
async def downloadFile(fileName: str):
    return FileResponse(os.path.dirname(os.path.realpath(__file__) + "/uploads/" + fileName)