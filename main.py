import tkinter as tk
import math

RED = '#ff0000'
BLACK = '#000000'
BLUE = '#0000ff'
YELLOW = '#ffff00'
WIDTH = 500
HEIGHT = 500
root = tk.Tk()
root.title('Рулетка')
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
diameter = 450
x = WIDTH / 2
y = HEIGHT / 2
canvas.create_oval(x - diameter/2, y - diameter/2, x + diameter/2, y + diameter/2)

sd = 400
num_of_segments = 38
angle_per_segment = 360/num_of_segments
start_angle = 0
for i in range(num_of_segments):
    if i % 2 == 0:
        fill_color = BLACK
    else:
        fill_color = RED
    angle_to_draw = angle_per_segment
    canvas.create_arc(x - sd/2, y - sd/2, x + sd /2, y + sd/2,
                      start=start_angle, extent=angle_to_draw, fill=fill_color)

    angle = start_angle + angle_to_draw / 2
    text_x = x + diameter / 2.1 * math.cos(math.radians(angle))
    text_y = y - diameter / 2.1 * math.sin(math.radians(angle))
    canvas.create_text(text_x, text_y, text=str(i), fill=BLUE, font=('Ariel', 16))
    start_angle = start_angle + angle_to_draw

radius = 10
dist = WIDTH/2.7
ball_x = x + dist * math.cos(math.radians(angle))
ball_y = y - dist * math.sin(math.radians(angle))
ball = canvas.create_oval(ball_x-radius,ball_y-radius,ball_x+radius,ball_y+radius, fill=YELLOW)
angle = 0
delta = 1

def rotate_ball():
    global angle, delta, ball_x, ball_y
    angle = (angle + delta) % 360
    ball_x = x + dist * math.cos(math.radians(angle))
    ball_y = y - dist * math.sin(math.radians(angle))
    canvas.coords(ball,ball_x - radius, ball_y - radius, ball_x+radius, ball_y+radius)
    root.after(10, rotate_ball)
rotate_ball()
root.mainloop()
