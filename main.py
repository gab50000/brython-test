from browser import document, html
import math

canvas = document["zone"]
ctx = canvas.getContext("2d")


def parse_text(text):
    for line in text.splitlines():
        print(line)


document["button"].bind("click", lambda event: parse_text(document["text"].value))

text = document["text"]

print(text.textContent)
