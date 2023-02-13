class PostMaker():
    def __init__(self, username, question, answer, background, research_paper, illustration, pages):
        self.username = username
        self.question = question
        self.illustration = illustration
        self.answer = answer
        self.background = background
        self.research_paper = research_paper
        self.pages = pages
        self.final = []

        for page in pages:
            self.final.append(page.generate(self))

    def get_images(self):
        return self.final