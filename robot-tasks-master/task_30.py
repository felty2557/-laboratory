#!/usr/bin/python3

from pyrob.api import *


@task
def task_9_3():
    move = move_right
    size = 1

    while not wall_is_on_the_right():
        size += 1
        move()

    for i in range(size):
        move = move_right if move == move_left else move_left

        for j in range(size):
            if i != j and i + j != size - 1:
                fill_cell()
            if j != size - 1:
                move()

        if not wall_is_beneath():
            move_down()

if __name__ == '__main__':
    run_tasks()
