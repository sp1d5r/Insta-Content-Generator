class QuestionPage():
    def __init__(self, post_maker):
        image = post_maker.get_background()
        image = add_logo(image)
