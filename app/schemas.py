from pydantic import BaseModel
from typing import List

class ImageRequest(BaseModel):
    name: str
    image: bytes

class SimilarImagesRequest(BaseModel):
    embedding: List[float]
    limit: int = 5