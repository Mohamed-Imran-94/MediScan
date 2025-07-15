import os
import uuid
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.extractor import extract

app = FastAPI()

# ✅ Enable CORS for frontend (change origin as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "MediScan API is running"}

@app.post("/extract_from_doc")
async def extract_from_doc(
    file: UploadFile = File(...),
    file_format: str = Form(...)
):
    try:
        # ✅ Ensure uploads folder exists
        upload_dir = "backend/uploads"
        os.makedirs(upload_dir, exist_ok=True)

        # ✅ Save uploaded file with a unique filename
        file_ext = file.filename.split('.')[-1]
        file_id = str(uuid.uuid4())
        file_name = f"{file_id}.{file_ext}"
        file_path = os.path.join(upload_dir, file_name)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        # ✅ Call the document extractor
        result = extract(file_path, file_format)
        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to process document: {str(e)}"},
            status_code=500
        )
