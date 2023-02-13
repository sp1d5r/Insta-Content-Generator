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

def add_question(image, question, line_length=1173, line_height=70):
    font = ImageFont.truetype('assets/Inter-Bold.ttf', 60)
    draw = ImageDraw.Draw(image)
    wraped_text = get_wrapped_text(question, font, line_length)
    for index, text in enumerate(wraped_text):
        draw.text((1465/2, 1348 + line_height * index), text, (0, 0, 0), font=font, anchor="mm")
    return image

