from PIL import ImageFont, ImageDraw


def add_logo(image):
    draw = ImageDraw.Draw(image)
    logo_text = ImageFont.truetype("assets/Lexend-Bold.ttf", 50)
    draw.text((1150, 63), "conventa", (255, 255, 255), font=logo_text)
    return image

