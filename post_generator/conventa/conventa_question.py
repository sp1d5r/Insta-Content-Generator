from post_generator.text_functions import add_logo, add_question, add_image_ontop, add_title
from PIL import Image
from io import BytesIO
import requests

class ConventaQuestion():
    def __init__(self, background, question, title, illustrationPath):
        # Add brush stroke
        top_banner_image = Image.open("images/TopBanner.png")

        # Add top banner
        image = add_image_ontop(background, top_banner_image, top=0, left=0, width=1465, height=339)

        # Add Logo
        image = add_logo(image)

        # Add Question
        image = add_question(image, question)

        # Add illustration from URL
        # Send a HTTP request to the URL of the image
        # Send a HTTP request to the URL of the image
        response = requests.get(illustrationPath)

        # Read the content of the server’s response
        data = response.content

        # Create a BytesIO object and read the response data into it
        byte_io = BytesIO(data)

        front_image = Image.open(byte_io)
        image = add_image_ontop(image, front_image)

        # Add swipe text
        swipe_text = Image.open("images/SwipeAnswer.png")
        image = add_image_ontop(image, swipe_text, top=1526, left=518, width=432, height=32)

        self.image = add_title(image, title)

    def return_image(self):
        return self.image