from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import model.model as det_models
import model.utilities
import shutil
from fastapi.staticfiles import StaticFiles
import json


app = FastAPI()

if not os.path.exists('static'):
    os.makedirs('static')
    
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("start_page.html", {"request": request})


@app.post("/uploadfile/")
async def create_upload_file(request: Request, file: UploadFile = File(...),
                             ):
    # Save the uploaded file temporarily
    file_path = os.getcwd() + f"\\static\\{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    det_model = det_models.model()
    det_model.inference_with_show(file_path, os.getcwd())

    path = os.getcwd() + os.path.sep + \
    "vis" + os.path.sep + file.filename

    json_path = os.getcwd() + os.path.sep + \
    "preds" + os.path.sep + os.path.splitext(file.filename)[0] + '.json'

    with open(json_path, 'r') as json_file:
        preds = json.load(json_file)

    score, box = model.utilities.find_best_box(preds)

    if score < 0.15:
        return templates.TemplateResponse("start_page.html", {"request": request, "text": "There is no APPLE! At least I don't see it..."})
    
    model.utilities.crop_apple(file_path, path, box)
    shutil.copy(path, "static" + os.path.sep + file.filename)
    result_image_url = request.url_for("static", path=file.filename)

    return templates.TemplateResponse("start_page.html", {"request": request, "image_url": result_image_url})
