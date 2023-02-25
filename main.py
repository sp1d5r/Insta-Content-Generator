import os

from post_generator.background import Background
from post_generator.conventa.conventa_answer import ConventaAnswer
from post_generator.conventa.conventa_call_to_action import ConventaCTA
from post_generator.conventa.conventa_question import ConventaQuestion
from post_generator.text_functions import add_logo, add_question, add_image_ontop, add_title, add_text_center
from PIL import Image
from PIL import ImageFont


USERNAME = "@cleo.conventa"
TASKS = [
    {
        "illustration": "images/ExampleImage.png",
        "title": "Child Psychology",
        "question": "What is the most effective way to teach someone something?",
        "answer": "(1) Understand their current mental model of what you are trying to teach.\n \n(2) Experience is the most effective way to teach, slowly expose them to new ideas.",
        "paper": "Mental models of the earth, Vosniadou and Brewer (1991)",
    }
]

if __name__=="__main__":

    for index, task in enumerate(TASKS):
        bg = Background()

        question_post = ConventaQuestion(
            background=bg.get_background(),
            question=task["question"],
            title=task["title"],
            illustrationPath=task["illustration"]
        ).return_image()

        answer_post = ConventaAnswer(
            background=bg.get_background(),
            answer=task["answer"],
            research_paper=task["paper"]
        ).return_image()

        call_to_action = ConventaCTA(
            background=bg.get_background(),
            tagline="To improve your relationship with the people you love",
            handle=USERNAME
        ).return_image()


        output_path = f"output/{index}"
        if (not os.path.exists(output_path)):
            os.mkdir(output_path)

        question_post.save(f"{output_path}/question_post.jpeg")
        answer_post.save(f"{output_path}/answer_post.jpeg")
        call_to_action.save(f"{output_path}/call_to_action.jpeg")
