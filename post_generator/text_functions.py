from PIL import ImageFont, ImageDraw


def add_logo(image):
    draw = ImageDraw.Draw(image)
    logo_text = ImageFont.truetype("assets/Lexend-Bold.ttf", 50)
    draw.text((1150, 63), "conventa", (255, 255, 255), font=logo_text)
    return image

def get_wrapped_text(text: str, font,
                     line_length: int):
    lines = ['']
    for word in text.split():
        line = f'{lines[-1]} {word}'.strip()
        if font.getlength(line) <= line_length:
            lines[-1] = line
        else:
            lines.append(word)
    return lines

def add_text_center(image, text, line_length, line_height, center_x, top_y, font, text_color=(0,0,0)):
    draw = ImageDraw.Draw(image)
    split_text = text.split("\n")
    split_text = [get_wrapped_text(i, font, line_length) for i in split_text]
    wraped_text = []
    for i in split_text:
        for t in i:
            wraped_text.append(t)

    for index, text in enumerate(wraped_text):
        draw.text((center_x, top_y + line_height * index), text, text_color, font=font, anchor="mm")
    return image

def add_question(image, question, line_length=1173, line_height=70):
    font = ImageFont.truetype('assets/Inter-Bold.ttf', 60)
    draw = ImageDraw.Draw(image)
    wraped_text = get_wrapped_text(question, font, line_length)
    for index, text in enumerate(wraped_text):
        draw.text((1465/2, 1348 + line_height * index), text, (0, 0, 0), font=font, anchor="mm")
    return image

def add_image_ontop(background_image, front_image, top=312, left=232, width=1000, height=1000):
    front_image = front_image.resize((width, height))
    background_image.paste(front_image, (left, top), mask=front_image)
    return background_image

def add_title(image, title, line_length=1173, line_height=70):
    font = ImageFont.truetype('assets/Inter-Bold.ttf', 100)
    draw = ImageDraw.Draw(image)
    wraped_text = get_wrapped_text(title, font, line_length)
    for index, text in enumerate(wraped_text):
        draw.text((110, 164 + line_height * index), text, (255, 255, 255), font=font)
    return image
