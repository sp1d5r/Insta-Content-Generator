from PIL import Image
from PIL import ImageFont
from post_generator.text_functions import add_logo, add_image_ontop, add_text_center, drawMappedValues
import random

class ConventaFlipAndSelect():
    def __init__(self, background, mapping):
        # Add flip and select post template
        flip_select_post = background
        flip_select_post = add_logo(flip_select_post)

        # Add flip and select post text
        question_font = ImageFont.truetype('assets/Inter-Bold.ttf', 30)

        keys = list(mapping.keys())
        values = list(mapping.values())
        random.shuffle(keys)
        random.shuffle(values)

        flip_select_post = drawMappedValues(flip_select_post, keys, values, question_font)

        self.flip_select_post = flip_select_post

    def return_image(self):
        return self.flip_select_post
