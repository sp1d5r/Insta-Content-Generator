from PIL import Image
from PIL import ImageFont
import random
from post_generator.text_functions import add_logo, add_image_ontop, add_text_center, add_text_boxes, add_question


class ConventaBuildSentence():
    def __init__(self, background, sentence):
        # Add options questions post template
        scrambled = sentence.split(" ")
        random.shuffle(scrambled)
        scrambled = " ".join(scrambled)
        answer_post = background

        # Add swipe text
        swipe_text = Image.open("images/SwipeAnswer.png")
        answer_post = add_image_ontop(answer_post, swipe_text, top=1526, left=518, width=432, height=32)

        # Add Question
        answer_post = add_question(answer_post, "Can you unscramble the words.", y=500)

        # Specify the font
        fnt = ImageFont.truetype("assets/Inter-Bold.ttf", 40)

        answer_post = add_text_boxes(answer_post, scrambled, 200, 800, fnt)

        self.answer_post = answer_post

    def return_image(self):
        return self.answer_post
