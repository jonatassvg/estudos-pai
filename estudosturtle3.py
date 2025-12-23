import turtle
import time

t = turtle.Turtle()

for _ in range(9):
    print("passou")
    time.sleep(1)
    t.backward(100)
    t.left(40)

turtle.done()