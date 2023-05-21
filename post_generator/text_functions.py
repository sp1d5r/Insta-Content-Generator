from PIL import ImageFont, ImageDraw
from textwrap import wrap
import numpy as np

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


def add_single_text_box(image, sentence, start_x, start_y, font, padding=30, box_color=(242, 249, 255), border_color=(120, 120, 120), text_color=(0,0,0)):
    draw = ImageDraw.Draw(image)

    # Calculate text and box dimensions
    text_width, text_height = draw.textsize(sentence, font)
    box_width = text_width + 2 * padding
    box_height = text_height + 2 * padding

    # Draw the box
    box_coords = [(start_x, start_y), (start_x + box_width, start_y + box_height)]
    draw.rectangle(box_coords, fill=box_color, outline=border_color, width=3)

    # Draw the text
    text_x = start_x + padding
    text_y = start_y + padding
    draw.text((text_x, text_y), sentence, fill=text_color, font=font)

    return image

def rounded_rectangle(draw, position, corner_radius, fill=None, outline=None):
    # Unpack rectangle corners
    x1, y1, x2, y2 = position

    # Draw rectangle with rounded corners
    draw.rectangle(((x1, y1 + corner_radius), (x2, y2 - corner_radius)), fill=fill)  # Top and bottom straight edges
    draw.rectangle(((x1 + corner_radius, y1), (x2 - corner_radius, y2)), fill=fill)  # Left and right straight edges
    draw.pieslice((x1, y1, x1 + corner_radius * 2, y1 + corner_radius * 2), 180, 270, fill=fill)  # Top-left corner
    draw.pieslice((x2 - corner_radius * 2, y1, x2, y1 + corner_radius * 2), 270, 360, fill=fill)  # Top-right corner
    draw.pieslice((x2 - corner_radius * 2, y2 - corner_radius * 2, x2, y2), 0, 90, fill=fill)  # Bottom-right corner
    draw.pieslice((x1, y2 - corner_radius * 2, x1 + corner_radius * 2, y2), 90, 180, fill=fill)  # Bottom-left corner

    # Draw outline on arcs only if an outline color is provided
    if outline:
        draw.arc((x1, y1, x1 + corner_radius * 2, y1 + corner_radius * 2), 180, 270, fill=outline)  # Top-left corner
        draw.arc((x2 - corner_radius * 2, y1, x2, y1 + corner_radius * 2), 270, 360, fill=outline)  # Top-right corner
        draw.arc((x2 - corner_radius * 2, y2 - corner_radius * 2, x2, y2), 0, 90, fill=outline)  # Bottom-right corner
        draw.arc((x1, y2 - corner_radius * 2, x1 + corner_radius * 2, y2), 90, 180, fill=outline)  # Bottom-left corner


def add_text_box_centered(image, text, center_x, center_y, font, box_width, padding=50, max_chars=30, box_color=(242, 249, 255), border_color=(120, 120, 120), text_color=(0,0,0)):
    draw = ImageDraw.Draw(image)

    # Wrap the text if it exceeds the maximum number of characters
    lines = wrap(text, width=max_chars)
    line_height = draw.textsize('A', font)[1]  # Assume 'A' character represents average line height
    text_height = line_height * len(lines)

    # Calculate box height based on text
    box_height = text_height + 2 * padding

    # Calculate box start coordinates based on center
    start_x = center_x - box_width / 2
    start_y = center_y - box_height / 2

    # Draw the box
    box_coords = (start_x, start_y, start_x + box_width, start_y + box_height)
    rounded_rectangle(draw, box_coords, 20, fill=box_color,
                      outline=None)  # Adjust 20 to your desired corner radius

    # Draw each line of text
    for i, line in enumerate(lines):
        # Calculate the width of the line and start the text so it's centered within the box
        line_width = draw.textsize(line, font)[0]
        text_x = start_x + (box_width - line_width) / 2
        text_y = start_y + padding + i * line_height
        draw.text((text_x, text_y), line, fill=text_color, font=font)

    return image

def drawMappedValues(image, keys, values, font, padding=30, max_chars=30, box_color=(242, 249, 255), border_color=(120, 120, 120), text_color=(0,0,0)):
    # Calculate box positions
    center_x1 = image.width * 1 / 4
    center_x2 = image.width * 3 / 4

    # Start the boxes some distance away from the top and bottom edges
    top_padding = image.height * 0.10  # 10% of the image height
    bottom_padding = image.height * 0.10  # 10% of the image height

    center_y_values = np.linspace(top_padding, image.height - bottom_padding, len(keys) + 2)[1:-1]  # +2 and [1:-1] to exclude the first and last values

    # Draw boxes
    for i in range(len(keys)):
        current_y = center_y_values[i]
        image = add_text_box_centered(image, keys[i], center_x1, current_y, font, 500, padding, max_chars, box_color, border_color, text_color)
        image = add_text_box_centered(image, values[i], center_x2, current_y, font, 500, padding, max_chars, box_color, border_color, text_color)

    return image


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
        # Draw the box
        box_coords = (x, y, x + box_width, y + box_height)
        rounded_rectangle(draw, box_coords, 20, fill=box_color,
                          outline=None)

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

def add_title(image, title, line_length=1173, line_height=100):
    font = ImageFont.truetype('assets/Inter-Bold.ttf', 100)
    draw = ImageDraw.Draw(image)
    wraped_text = get_wrapped_text(title, font, line_length)
    for index, text in enumerate(wraped_text):
        draw.text((110, 100 + line_height * index), text, (255, 255, 255), font=font)
    return image
