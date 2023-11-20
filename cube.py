from tkinter import *
from math import *


# черный треугольный фон
def treugol(canvas, x: int, y: int, length: int) -> None:


    canvas.create_polygon(
        [x, y,
        x + length, y,
        x + length, y + length,
        x, y + length,
        x, y],
        fill='black')




def salfetka(canvas, x: int, y: int, length: int, n: int) -> None:
    if n > 0:
        delta = length / 3
        canvas.create_rectangle(
            [x + delta, y + delta, x + 2 * delta, y + 2 * delta],
            fill='white')
        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1):
                    salfetka(canvas, x + i * delta, y + j * delta, length / 3, n - 1)

        # salfetka(canvas, x, y, length/2, n-1)
        # salfetka(canvas, x - dx, y + dy, length / 2, n - 1)
        # salfetka(canvas, x + dx, y + dy, length / 2, n - 1)




root = Tk()
root.title("Фрактал – треугольник Серпинского")
w = 900
h = 900
c = Canvas(root, width=w, height=h, bg='white')
c.pack()
length = w - 500
# черный треугольный фон
treugol(c, 200, 200, length)


# белые треугольники внутри
salfetka(c, 200, 200, length, 6)
root.mainloop()