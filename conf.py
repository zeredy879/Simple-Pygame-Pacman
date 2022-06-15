CAPTION_NAME = "Pygame_PACMAN"
WIDTH = 606
HEIGHT = 606

## 定义颜色
COLOR_SET = {
    "RED": (255, 0, 0),
    "DARKRED": (139, 0, 0),
    "GOLD": (255, 215, 0),
    "ORANGE": (255, 165, 0),
    "ORANGE": (255, 165, 0),
    "DARKORANGE": (255, 140, 0),
    "LIGHTYELLOW": (255, 255, 224),
    "YELLOW": (255, 255, 0),
    "LIMEGREEN ": (50, 205, 50),
    "GREEN ": (0, 255, 0),
    "SPRINGGREEN": (0, 255, 127),
    "SEAGREEN": (46, 139, 87),
    "OLIVE": (128, 128, 0),
    "CYAN": (0, 255, 255),
    "DARKCYAN": (0, 139, 139),
    "LIGHTSKYBLUE": (135, 206, 250),
    "SKYBLUE": (135, 206, 235),
    "DEEPSKYBLUE": (0, 191, 255),
    "LIGHTSTEELBLUE": (176, 196, 222),
    "BLUE": (0, 0, 255),
    "MEDIUMBLUE": (0, 0, 205),
    "DARKBLUE": (0, 0, 139),
    "VIOLET": (238, 130, 238),
    "FUCHSIA": (255, 0, 255),
    "PURPLE": (128, 0, 128),
    "INDIGO": (75, 0, 130),
    "PINK": (255, 192, 203),
    "LIGHTPINK": (255, 182, 193),
    "DEEPPINK": (255, 20, 147),
    "WHITE": (255, 255, 255),
    "SNOW": (255, 250, 250),
    "AZURE": (240, 255, 255),
    "LIGHTGRAY": (211, 211, 211),
    "SILVER": (192, 192, 192),
    "DARKGRAY": (169, 169, 169),
    "GRAY": (128, 128, 128),
    "WHEAT": (245, 222, 179),
    "CHOCOLATE": (210, 105, 30),
    "BROWN": (165, 42, 42),
}

WALL_MAP = [
    [0, 0, 6, 600],
    [0, 0, 600, 6],
    [0, 600, 606, 6],
    [600, 0, 6, 606],
    [300, 0, 6, 66],
    [60, 60, 186, 6],
    [360, 60, 186, 6],
    [60, 120, 66, 6],
    [60, 120, 6, 126],
    [180, 120, 246, 6],
    [300, 120, 6, 66],
    [480, 120, 66, 6],
    [540, 120, 6, 126],
    [120, 180, 126, 6],
    [120, 180, 6, 126],
    [360, 180, 126, 6],
    [480, 180, 6, 126],
    [180, 240, 6, 126],
    [180, 360, 246, 6],
    [420, 240, 6, 126],
    [240, 240, 42, 6],
    [324, 240, 42, 6],
    [240, 240, 6, 66],
    [240, 300, 126, 6],
    [360, 240, 6, 66],
    [0, 300, 66, 6],
    [540, 300, 66, 6],
    [60, 360, 66, 6],
    [60, 360, 6, 186],
    [480, 360, 66, 6],
    [540, 360, 6, 186],
    [120, 420, 366, 6],
    [120, 420, 6, 66],
    [480, 420, 6, 66],
    [180, 480, 246, 6],
    [300, 480, 6, 66],
    [120, 540, 126, 6],
    [360, 540, 126, 6],
]