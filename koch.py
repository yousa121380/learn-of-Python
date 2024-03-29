import turtle
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(600,600,0,0)
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(-210,100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.hideturtle()
    turtle.getscreen().tracer(0)
    level=5
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
main()
