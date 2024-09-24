from lambda_dive_photo_corrector.handler import color_correct_image
from base64 import b64encode, b64decode
from PIL import Image
from io import BytesIO


def test_color_correct_image():
    with open("tests/resources/test.jpg", "rb") as file:
        # red channel is 0 here
        original_image = Image.open(file)
        assert original_image.getpixel(xy=(0, 0))[0] == 0
        # reset file pointer so we can use it
        file.seek(0)
        encoded_image = b64encode(file.read()).decode("utf-8")
        image_string = color_correct_image(encoded_image)
        assert type(image_string) == str
        # red channel should be greater than 0 here
        image_bytes = BytesIO(b64decode(image_string))
        image = Image.open(image_bytes)
        assert image.getpixel(xy=(0, 0))[0] > 0
