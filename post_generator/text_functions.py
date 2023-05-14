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

def add_text_boxes(image, sentence, start_x, start_y, font, padding=30, margin=50, text_color=(0,0,0), box_color=(242, 249, 255), border_color=(120, 120, 120)):
    draw = ImageDraw.Draw(image)
    x, y = start_x, start_y

    # Split sentence into words
    words = sentence.split(' ')

    for word in words:
        # Calculate text and box dimensions
        text_width, text_height = draw.textsize(word, font)
        box_width = text_width + 2 * padding
        box_height = text_height + 2 * padding

        # Check if the box fits on the current line
        if x + box_width + margin > image.width - 200:
            # Start a new line
            x = start_x
            y += box_height + margin

        # Draw the box
        box_coords = [(x, y), (x + box_width, y + box_height)]
        draw.rectangle(box_coords, fill=box_color, outline=border_color, width=3)

        # Draw the text
        text_x = x + padding
        text_y = y + padding
        draw.text((text_x, text_y), word, fill=text_color, font=font)

        # Move to the next position
        x += box_width + margin

    return image
def add_question(image, question, line_length=1173, line_height=70, y=1348):
    font = ImageFont.truetype('assets/Inter-Bold.ttf', 60)
    draw = ImageDraw.Draw(image)
    wraped_text = get_wrapped_text(question, font, line_length)
    for index, text in enumerate(wraped_text):
        draw.text((1465/2, y + line_height * index), text, (0, 0, 0), font=font, anchor="mm")
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
