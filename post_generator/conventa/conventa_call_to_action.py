from post_generator.text_functions import add_logo, add_image_ontop, add_text_center
from PIL import Image
from PIL import ImageFont

class ConventaCTA():
    def __init__(self, background, tagline, handle):
        call_to_action_image = Image.open("images/CallToActionTemplate.png")
        call_to_action = add_image_ontop(background, call_to_action_image, top=130, left=0, width=1264,
                                         height=1485)

        call_to_action = add_logo(call_to_action)

        tag_line_font = ImageFont.truetype("assets/Lexend-Medium.ttf", 50)
        call_to_action = add_text_center(
            call_to_action,
            text=tagline,
            line_length=741,
            line_height=65,
            center_x=732,
            top_y=677,
            font=tag_line_font
        )

        handle_font = ImageFont.truetype("assets/Lexend-Bold.ttf", 60)
        call_to_action = add_text_center(
            call_to_action,
            text=handle,
            line_length=741,
            line_height=65,
            center_x=732,
            top_y=1160,
            font=handle_font,
            text_color=(40, 126, 255)
        )

        self.cta = call_to_action

    def return_image(self):
        return self.cta