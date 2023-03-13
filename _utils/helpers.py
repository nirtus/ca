from PIL import Image

def resize_image(image_path: str, resize_percentage: float):
    with Image.open(image_path) as img:
        width, height = img.size
        new_width = int(width * resize_percentage / 100)
        new_height = int(height * resize_percentage / 100)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(image_path)