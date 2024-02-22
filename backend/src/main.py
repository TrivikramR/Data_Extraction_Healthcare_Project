from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extract
import uuid
import os

app = FastAPI()


@app.post("/extract_from_doc")
def extract_from_doc(
        file_format: str = Form(...),
        file: UploadFile = File(...)
):
    content = file.file.read()  # this is used to read the input file.

    file_path = "../uploads/" + str(uuid.uuid4()) + ".pdf"  # defining the file path and create a unique file.

    with open(file_path, "wb") as f:  # open the file in write bytes
        f.write(content)
    try:
        data = extract(file_path, file_format)
    except Exception as e:
        data = {
            'error': str(e)
        }

    if os.path.exists(file_path):  # condition to remove the temporary file.
        os.remove(file_path)

    return data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
