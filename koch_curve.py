# !/usr/bin/python
# coch curve generator
# it is a taste of GUI and turtle
# for the task of drawing a fractal curve

import turtle
from tkinter import *

def koch_curve(t, iterations, length, shortening_factor, angle):
    if iterations == 0:
        t.forward(length)
    else:
        iterations = iterations - 1
        length = length / shortening_factor
        koch_curve(t, iterations, length, shortening_factor, angle)
        t.left(angle)
        koch_curve(t, iterations, length, shortening_factor, angle)
        t.right(angle * 2)
        koch_curve(t, iterations, length, shortening_factor, angle)
        t.left(angle)
        koch_curve(t, iterations, length, shortening_factor, angle)

def make_window():
    root = Tk()
    root.geometry("300x280")
    frame = Frame(root)
    frame.pack()
     
    leftframe = Frame(root)
    leftframe.pack(side=LEFT)
     
    rightframe = Frame(root)
    rightframe.pack(side=RIGHT)
     
    label = Label(frame, text = "Please input arguments")
    label.pack()

    iteration_prompt = Label(leftframe, text="Iteration number")
    iteration_prompt.pack(padx = 3, pady = 3)
    iteration_in = Entry(rightframe, bd = 1)
    iteration_in.insert(0,4)
    iteration_in.pack(padx = 3, pady = 3)

    length_prompt = Label(leftframe, text="Side length")
    length_prompt.pack(padx = 3, pady = 3)
    length_in = Entry(rightframe, bd = 1)
    length_in.insert(0,200)
    length_in.pack(padx = 3, pady = 3)

    sht_factor_prompt = Label(leftframe, text="Shortening factor")
    sht_factor_prompt.pack(padx = 3, pady = 3)
    sht_factor_in = Entry(rightframe, bd = 1)
    sht_factor_in.insert(0,3)
    sht_factor_in.pack(padx = 3, pady = 3)

    angle_prompt = Label(leftframe, text="Angle (0-90 degrees)")
    angle_prompt.pack(padx = 3, pady = 3)
    angle_in = Entry(rightframe, bd = 1)
    angle_in.insert(0,60)
    angle_in.pack(padx = 3, pady = 3)

    line_color_prompt = Label(leftframe, text="line color")
    line_color_prompt.pack(padx = 3, pady = 3)
    line_color_in = Entry(rightframe, bd = 1)
    line_color_in.insert(0,'black')
    line_color_in.pack(padx = 3, pady = 3)


    # A check button for filling shade
    global filled
    filled = 0
    def input_fill_color():
        global filled
        global fill_color_in
        global fill_color_prompt
        if filled == 0:
            fill_color_prompt = Label(leftframe, text="shade color")
            fill_color_prompt.pack(padx = 3, pady = 3)
            fill_color_in = Entry(rightframe, bd = 1)
            fill_color_in.pack(padx = 3, pady = 3)
            filled = 1
        else:
            filled = 0
            fill_color_prompt.destroy()
            fill_color_in.destroy()

    fill_shade = IntVar()
    chk_button = Checkbutton(frame, text = "fill shade", width = 15, variable = fill_shade, command = input_fill_color)
    chk_button.pack(padx = 3, pady = 3)

    iterations = 4
    length = 200
    shortening_factor = 3
    angle = 60
    line_color = 5
    def quit():
        root.destroy()
    def exe():
        global iterations
        global length
        global shortening_factor
        global angle
        global line_color
        global filled
        
        iterations = iteration_in.get()
        length = length_in.get()
        shortening_factor = sht_factor_in.get()
        angle = angle_in.get()
        line_color = line_color_in.get()
        if filled:
            fill_color = fill_color_in.get()
        print(iterations)
        print(length)
        print(shortening_factor)
        print(angle)
        print(line_color)
        print(filled)
        root.destroy()
        for i in range(3):
            koch_curve(t, int(iterations), int(length), int(shortening_factor), int(angle))
            t.right(120)
        #screen.onclick(draw_curve(t), btn = 1)
        
    cancel_button = Button(leftframe, text = "cancel", command = quit)
    cancel_button.pack(padx = 3, pady = 3)
    submit_button = Button(rightframe, text = "submit", command = exe)
    submit_button.pack(padx = 3, pady = 3)
    root.mainloop()

def draw_curve(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    make_window()
    

t = turtle.Turtle()
t.speed(200)
#t.hideturtle()
screen = turtle.Screen()

screen.listen()
screen.onclick(draw_curve, btn = 1)
screen.mainloop()
