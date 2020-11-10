from requests import get
from io import BytesIO
from PIL import Image

# @see https://stackoverflow.com/questions/51116907/beatifulsoup-how-to-get-image-size-by-url

def get_image_size(image_url):
	image_raw = get(image_url)
	image = Image.open(BytesIO(image_raw.content))
	return image.size

print(get_image_size("https://apod.nasa.gov/apod/image/2011/IC1848_Guenzel_1080.jpg"))
