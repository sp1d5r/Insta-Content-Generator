import os

from firebase.firebase import get_tasks
from post_generator.background import Background
from post_generator.conventa.conventa_answer import ConventaAnswer, ConventaTextOptionsAnswer, \
    ConventaBuildSentenceAnswer
from post_generator.conventa.conventa_build_sentence import ConventaBuildSentence
from post_generator.conventa.conventa_call_to_action import ConventaCTA
from post_generator.conventa.conventa_match_cards import ConventaFlipAndSelect
from post_generator.conventa.conventa_question import ConventaQuestion
from post_generator.conventa.conventa_text_options import ConventaTextOptions

USERNAME = "@conventa"
PRODUCTION = False

if PRODUCTION:
    TASKS = get_tasks()
else :
    TASKS = [
        {
            "illustration": "https://firebasestorage.googleapis.com/v0/b/convento-453e6.appspot.com/o/course-images%2Fachievements%20_%20accomplishment%2C%20target%2C%20mountain%2C%20top%2C%20flag%2C%20man%2C%20people%2C%20achievement.png?alt=media&token=3b9bbb0f-6feb-41ba-9e9f-35d251aff192",
            "title": "Introduction to Emotional Intelligence",
            "sentence": "Welcome to our course it's shown here.",
            "type": "build_sentence"
        },
        # {
        #     "illustration": "https://firebasestorage.googleapis.com/v0/b/convento-453e6.appspot.com/o/course-images%2Fachievements%20_%20accomplishment%2C%20target%2C%20mountain%2C%20top%2C%20flag%2C%20man%2C%20people%2C%20achievement.png?alt=media&token=3b9bbb0f-6feb-41ba-9e9f-35d251aff192",
        #     "title": "Introduction to Emotional Intelligence",
        #     "question": "Welcome to our course it's shown here.",
        #     "options": ["Option 1 hehllo llooerv hefvkdfkj kejhkvjefjv", "Option 2", "Option 3", "Option 4"],
        #     "answer": 2,  # zero indexed
        #     "type": "selection_text"
        # },
        {
            "illustration": "https://firebasestorage.googleapis.com/v0/b/convento-453e6.appspot.com/o/course-images%2Fachievements%20_%20accomplishment%2C%20target%2C%20mountain%2C%20top%2C%20flag%2C%20man%2C%20people%2C%20achievement.png?alt=media&token=3b9bbb0f-6feb-41ba-9e9f-35d251aff192",
            "title": "Introduction to Emotional Intelligence",
            "question": "Welcome to our course it's shown here.",
            "mapping": {"Mapping 1 Mapping 1 Mapping 1 Mapping 1 Mapping 1 Mapping 1 Mapping 1": "Option 1 Option 1 Option 1 Option 1 Option 1 Option 1 Option 1", "Mapping 2": "Option 2", "Mapping 3": "Option 3", "Mapping 4": "Option 4"},
            "type": "flip_and_select"
        }
    ]


if __name__=="__main__":

    # Get the firebase records

    for index, task in enumerate(TASKS):
        bg = Background()
        print("Generating a new image set:", task)
        print("Type", task['type'])
        print(task)
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
        elif task["type"] == " flip_and_select":
            print("Flip and select ")
            question_post = ConventaQuestion(
                background=bg.get_background(),
                question="Can you match the words",
                title=task["title"],
                illustrationPath=task["illustration"]
            ).return_image()

            flip_and_select = ConventaFlipAndSelect(
                background=bg.get_background(),
                mapping=task["mapping"]
            ).return_image()

            output_path = f"output/{index}"
            if (not os.path.exists(output_path)):
                os.mkdir(output_path)

            question_post.save(f"{output_path}/question_post.jpeg")
            flip_and_select.save(f"{output_path}/text_option_post.jpeg")
        else:
            print("Flip and select ", task['type'])
            question_post = ConventaQuestion(
                background=bg.get_background(),
                question="Can you match the words",
                title=task["title"],
                illustrationPath=task["illustration"]
            ).return_image()

            flip_and_select = ConventaFlipAndSelect(
                background=bg.get_background(),
                mapping=task["mapping"]
            ).return_image()

            output_path = f"output/{index}"
            if (not os.path.exists(output_path)):
                os.mkdir(output_path)

            question_post.save(f"{output_path}/question_post.jpeg")
            flip_and_select.save(f"{output_path}/text_option_post.jpeg")

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