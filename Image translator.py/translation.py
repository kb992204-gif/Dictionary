import requests
from PIL import Image
from io import BytesIO

url = "https://dummyimage.com/600x400/ffffff/000000.png?text=Hello+World"

response = requests.get(url)

image = Image.open(BytesIO(response.content))

print(image)