import io
from torchvision import models, transforms
from PIL import Image
import torch

# Load model ResNet pretrained
model = models.resnet50(pretrained=True)
model.eval()

# Transformasi gambar
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def image_to_vector(image: bytes):
    img = Image.open(io.BytesIO(image)).convert("RGB")
    img = transform(img).unsqueeze(0)
    with torch.no_grad():
        embedding = model(img).squeeze().tolist()
    return embedding