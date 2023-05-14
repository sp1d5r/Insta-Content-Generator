import os

from firebase.firebase import get_tasks
from post_generator.background import Background
from post_generator.conventa.conventa_answer import ConventaAnswer, ConventaTextOptionsAnswer, \
    ConventaBuildSentenceAnswer
from post_generator.conventa.conventa_build_sentence import ConventaBuildSentence
from post_generator.conventa.conventa_call_to_action import ConventaCTA
from post_generator.conventa.conventa_question import ConventaQuestion
from post_generator.conventa.conventa_text_options import ConventaTextOptions

USERNAME = "@conventa"
TASKS = get_tasks()

if __name__=="__main__":

    # Get the firebase records

    for index, task in enumerate(TASKS):
        bg = Background()
        print("Generating a new image set:", task)
        if task["type"] == "selection_text":
            question_post = ConventaQuestion(
                background=bg.get_background(),
                question=task["question"],
                title=task["title"],
                illustrationPath=task["illustration"]
            ).return_image()

            text_options_post = ConventaTextOptions(
                background=bg.get_background(),
                question=task['question'],
                options=task["options"]
            ).return_image()

            answer_post = ConventaTextOptionsAnswer(
                background=bg.get_background(),
                answer=task['options'][task["answer"] - 1],
                question=task["question"]
            ).return_image()

            call_to_action = ConventaCTA(
                background=bg.get_background(),
                tagline="Accelerate your Career Growth",
                handle=USERNAME
            ).return_image()

            output_path = f"output/{index}"
            if (not os.path.exists(output_path)):
                os.mkdir(output_path)

            question_post.save(f"{output_path}/question_post.jpeg")
            text_options_post.save(f"{output_path}/text_option_post.jpeg")
            answer_post.save(f"{output_path}/answer_post.jpeg")
            call_to_action.save(f"{output_path}/call_to_action.jpeg")
        elif task["type"] == "build_sentence":
            question_post = ConventaQuestion(
                background=bg.get_background(),
                question="Can you unscramble the words?",
                title=task["title"],
                illustrationPath=task["illustration"]
            ).return_image()

            text_options_post = ConventaBuildSentence(
                background=bg.get_background(),
                sentence=task["sentence"]
            ).return_image()

            answer_post = ConventaBuildSentenceAnswer(
                background=bg.get_background(),
                sentence=task["sentence"]
            ).return_image()

            call_to_action = ConventaCTA(
                background=bg.get_background(),
                tagline="Accelerate your Career Growth",
                handle=USERNAME
            ).return_image()

            output_path = f"output/{index}"
            if (not os.path.exists(output_path)):
                os.mkdir(output_path)

            question_post.save(f"{output_path}/question_post.jpeg")
            text_options_post.save(f"{output_path}/text_option_post.jpeg")
            answer_post.save(f"{output_path}/answer_post.jpeg")
            call_to_action.save(f"{output_path}/call_to_action.jpeg")
        # else:
        #     question_post = ConventaQuestion(
        #         background=bg.get_background(),
        #         question=task["question"],
        #         title=task["title"],
        #         illustrationPath=task["illustration"]
        #     ).return_image()
        #
        #     answer_post = ConventaAnswer(
        #         background=bg.get_background(),
        #         answer=task["answer"],
        #         research_paper=task["paper"]
        #     ).return_image()
        #
        #     call_to_action = ConventaCTA(
        #         background=bg.get_background(),
        #         tagline="To improve your relationship with the people you love",
        #         handle=USERNAME
        #     ).return_image()
        #
        #
        #     output_path = f"output/{index}"
        #     if (not os.path.exists(output_path)):
        #         os.mkdir(output_path)
        #
        #     question_post.save(f"{output_path}/question_post.jpeg")
        #     answer_post.save(f"{output_path}/answer_post.jpeg")
        #     call_to_action.save(f"{output_path}/call_to_action.jpeg")