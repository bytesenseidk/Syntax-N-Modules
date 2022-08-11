import turtle

turtle.pensize(5)
turtle.pencolor("red")
turtle.color("red")
turtle.speed(2)

def drawing():
    for line in range(5):
        turtle.left(144)
        turtle.forward(200)

    turtle.penup()
    turtle.goto(-270, -120)
    turtle.write("python_genius", font=('Arial', 40, 'normal'))

if __name__ == "__main__":
    drawing()
    turtle.mainloop()
    
