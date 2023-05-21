from PIL import Image
from PIL import ImageFont
from post_generator.text_functions import add_logo, add_image_ontop, add_text_center, add_text_boxes


class ConventaAnswer():
    def __init__(self, background, answer, research_paper):
        # Add answer post template
        answer_template = Image.open("images/AnswerPostTemplate.png")
        answer_post = add_image_ontop(background, answer_template, top=285, left=230, width=1006, height=1236)
        answer_post = add_logo(answer_post)

        # Add answer post text
        answer_font = ImageFont.truetype('assets/Inter-Bold.ttf', 50)
        answer_post = add_text_center(
            answer_post,
            text=answer,
            line_length=806,
            line_height=80,
            center_x=732,
            top_y=408,
            font=answer_font
        )

        # Add linked research paper
        if (research_paper):
            research_paper_font = ImageFont.truetype('assets/Inter-Regular.ttf', 30)
            referenced_paper_font = ImageFont.truetype('assets/Inter-Bold.ttf', 30)
            answer_post = add_text_center(
                answer_post,
                text="Research Paper:",
                line_length=946,
                line_height=40,
                center_x=732,
                top_y=1103,
                font=research_paper_font
            )

            answer_post = add_text_center(
                answer_post,
                text=research_paper,
                line_length=946,
                line_height=40,
                center_x=732,
                top_y=175,
                font=referenced_paper_font
            )

        self.answer_post = answer_post

    def return_image(self):
        return self.answer_post

class ConventaTextOptionsAnswer():
    def __init__(self, background, question, answer):
        # Add answer post template
        answer_template = Image.open("images/AnswerPostTextOptions.png")
        answer_post = add_image_ontop(background, answer_template, top=0, left=0, width=1465, height=1624)
        answer_post = add_logo(answer_post)

        # Add answer post text
        question_font = ImageFont.truetype('assets/Inter-Bold.ttf', 50)
        answer_post = add_text_center(
            answer_post,
            text=question,
            line_length=806,
            line_height=80,
            center_x=732,
            top_y=540,
            font=question_font
        )

        answer_font = ImageFont.truetype('assets/Inter-Bold.ttf', 30)
        answer_post = add_text_center(
            answer_post,
            text=answer,
            line_length=806,
            line_height=80,
            center_x=732,
            top_y=933,
            font=answer_font
        )

        self.answer_post = answer_post

    def return_image(self):
        return self.answer_post

class ConventaBuildSentenceAnswer():
    def __init__(self, background, sentence):
        # Add answer post template
        answer_post = add_logo(background)

        # Add answer post text
        question_font = ImageFont.truetype('assets/Inter-Bold.ttf', 50)
        answer_post = add_text_center(
            answer_post,
            text="Did you get it right?",
            line_length=806,
            line_height=80,
            center_x=732,
            top_y=540,
            font=question_font
        )

        answer_font = ImageFont.truetype('assets/Inter-Bold.ttf', 30)
        answer_post = add_text_boxes(answer_post, sentence, 200, 800, answer_font, box_color=(227, 255, 234))

        self.answer_post = answer_post

    def return_image(self):
        return self.answer_post