from fastapi import FastAPI, UploadFile, HTTPException
from app.models import insert_image, search_similar_images
from app.schemas import ImageRequest, SimilarImagesRequest
from app.utils import image_to_vector

app = FastAPI()

@app.post("/upload/")
async def upload_image(file: UploadFile):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    # Convert image to vector
    content = await file.read()
    embedding = image_to_vector(content)

    # Save to database
    insert_image(file.filename, embedding)
    return {"message": "Image uploaded and vector stored successfully"}

@app.post("/search/")
async def search_images(request: SimilarImagesRequest):
    results = search_similar_images(request.embedding, request.limit)
    return {"results": results}