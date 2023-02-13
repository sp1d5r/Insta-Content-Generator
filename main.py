from post_generator.background import Background
from post_generator.text_functions import add_logo, add_question

USERNAME = "cleo.conventa"
TASKS = [
    {
        "question": "What is the most effective way to teach someone something?",
        "answer": "(1) Understand their current mental model of what you are trying to teach.\n \n(2) Experience is the most effective way to teach, slowly expose them to new ideas.",
        "paper": "Mental models of the earth, Vosniadou and Brewer (1991)",
    }
]

if __name__=="__main__":

    # for task in TASKS:
    #     posts = PostMaker(
    #         username=task["username"],
    #         question=task["question"],
    #         answer=task["answer"],
    #         background=None,
    #         research_paper=task["paper"],
    #         illustration=None,
    #         pages=[
    #             # QuestionPage(),
    #             # SidePage(),
    #             # FinalPage()
    #         ]
    #     )

    bg = Background()
    image = add_logo(bg.background)
    image = add_question(image, "What is the most effective way to teach someone something?")
    image.save("image.jpeg")
