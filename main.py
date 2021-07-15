from dataclasses import dataclass
import math
from typing import Tuple

from browser import document, html

canvas = document["canvas"]
ctx = canvas.getContext("2d")


@dataclass
class Field:
    x: int
    y: int
    width: int = 80
    height: int = 20
    color: str = "white"

    def draw(self):
        ctx.fillStyle = self.color
        ctx.fillRect(self.x, self.y, self.width, self.height)


def parse_text(text):
    for line in text.splitlines():
        print(line)


field = Field(20, 20, color="red")

document["button"].bind("click", lambda event: field.draw())

text = document["text"]

print(text.textContent)
