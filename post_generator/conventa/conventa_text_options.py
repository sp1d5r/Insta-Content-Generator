from PIL import Image
from PIL import ImageFont
from post_generator.text_functions import add_logo, add_image_ontop, add_text_center

class ConventaTextOptions():
    def __init__(self, background, question, options):
        # Add options questions post template
        answer_template = Image.open("images/TextOptions4.png")
        answer_post = add_image_ontop(background, answer_template, top=0, left=0, width=1465, height=1624)
        answer_post = add_logo(answer_post)

        # Add answer post text
        currentDepth = 370
        for option in options:
            answer_font = ImageFont.truetype('assets/Inter-Bold.ttf', 40)
            answer_post = add_text_center(
                answer_post,
                text=option,
                line_length=806,
                line_height=50,
                center_x=732,
                top_y=currentDepth,
                font=answer_font
            )

            currentDepth += 270

        # Add linked research paper

        self.answer_post = answer_post

    def return_image(self):
        return self.answer_post
