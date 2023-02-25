from PIL import Image
import random


def hsv_to_rgb(h, s, v):
    c = v * s
    x = c * (1 - abs((h/60) % 2 - 1))
    m = v - c
    if h >= 0 and h < 60:
        return round(c + m, 2), round(x + m, 2), round(m, 2)
    elif h >= 60 and h < 120:
        return round(x + m, 2), round(c + m, 2), round(m, 2)
    elif h >= 120 and h < 180:
        return round(m, 2), round(c + m, 2), round(x + m, 2)
    elif h >= 180 and h < 240:
        return round(m, 2), round(x + m, 2), round(c + m, 2)
    elif h >= 240 and h < 300:
        return round(x + m, 2), round(m, 2), round(c + m, 2)
    elif h >= 300 and h < 360:
        return round(c + m, 2), round(m, 2), round(x + m, 2)

def generate_gradient(
        colour1, colour2, width: int, height: int) -> Image:
    """Generate a vertical gradient."""
    # print(f"New gradient, {colour1}, {colour2}")
    base = Image.new('RGB', (width, height), colour1)
    top = Image.new('RGB', (width, height), colour2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base


def rgb_str_from_tuple(rgb):
    # color = f"rgb({int(rgb[0] * 255)}, {int(rgb[1] * 255)}, {int(rgb[2] * 255)})"
    return (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))


class Background():
    def __init__(self, hue_min=100, saturation=0.5, value=1, hue_variance=160, width=1465, height=1624):
        [min_rgb, max_rgb] = self.get_min_max_rgb_colors(hue_min, saturation, value, hue_variance)
        self.width = width
        self.height = height
        self.min_rgb = rgb_str_from_tuple(min_rgb)
        self.max_rgb = rgb_str_from_tuple(max_rgb)

    def get_min_max_rgb_colors(self, hue_min, saturation, value, variance):
        half_variance = int(variance / 2)
        min_hue = max(hue_min + random.randint(0, half_variance), 0)
        max_hue = min(359, min_hue + random.randint(half_variance, variance))
        return [hsv_to_rgb(min_hue, saturation, value), hsv_to_rgb(max_hue, saturation, value)]

    def get_background(self):
        return generate_gradient(self.min_rgb, self.max_rgb, self.width, self.height)

