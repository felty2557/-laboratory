from tkinter import *
from math import *


# черный треугольный фон
def treugol(canvas, x: int, y: int, length: int) -> None:
    dy = sqrt(length ** 2 - (length / 2) ** 2)
    dx = length / 2


    canvas.create_polygon(
        [x, y,
        x + dx, y + dy,
        x - dx, y + dy,
        x, y],
        fill='black')




def salfetka(canvas, x: int, y: int, length: int, n: int) -> None:
    if n > 0:
        dy = sqrt(length ** 2 - (length / 2) ** 2)
        dx = length / 2
        canvas.create_polygon(
            [x + dx, y + dy,
            x, y + 2 * dy,
            x - dx, y + dy,
            x + dx, y + dy],
            fill='white')
        salfetka(canvas, x, y, length/2, n-1)
        salfetka(canvas, x - dx, y + dy, length / 2, n - 1)
        salfetka(canvas, x + dx, y + dy, length / 2, n - 1)




root = Tk()
root.title("Фрактал – треугольник Серпинского")
w = 900
h = 900
c = Canvas(root, width=w, height=h, bg='white')
c.pack()
length = w - 100
# черный треугольный фон
treugol(c, w/2, 0, length)


# белые треугольники внутри
salfetka(c, w/2, 0, length/2, 6)
root.mainloop()