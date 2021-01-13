from fastapi import File
import pandas as pd
import io
from fastapi.responses import StreamingResponse


def readXLS(data: File):
    fileData = pd.read_excel(data, header=None)
    return fileData.values.tolist()


def extractTxtFile(data: list, fileName: str):
    df = pd.DataFrame(data)
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(
        iter([stream.getvalue()]), media_type="text/plain")
    response.headers["Content-Disposition"] = "attachment; filename=preProcessed_"+fileName+".txt"
    return response
