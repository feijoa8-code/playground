
from fastapi import FastAPI, File, UploadFile, HTTPException
import preProcessData
import fileOperations
import pandas as pd

tags_metadata = [
    {
        "name": "preprocess",
        "description": "these apis will be used for preprocessing of data for model",
    }
]

app = FastAPI(title="Feijoa8",
              description="This is a python project which is used to feijoa8 ML models",
              version="1.0",
              openapi_tags=tags_metadata)


@app.post("/theming/preprocess", tags=["preprocess"])
async def preprocessThemingData(data: list):
    return preProcessData.preprocessData(data)


@app.post("/theming/preprocess/file", tags=["preprocess"])
async def preprocessFileData(file: UploadFile = File(...)):
    fileName = file.filename.split(".")[0]
    if(file.filename.split(".")[-1] not in ['xls', 'xlsx']):
        raise HTTPException(
            status_code=400, detail="only xls and xlsx is supported")
    fileData = await file.read()
    fileDataFrame = fileOperations.readXLS(fileData)
    data = preProcessData.preprocessData(fileDataFrame)
    return fileOperations.extractTxtFile(data, fileName)
