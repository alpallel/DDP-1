import turtle as ttl

# background
ttl.bgcolor("cyan")
ttl.shape("turtle")
ttl.width(5)
ttl.speed(3)
ttl.penup()


ttl.goto(-400, 0)
ttl.pendown()

# tanah
ttl.fillcolor("green")
ttl.begin_fill()
ttl.right(0)
ttl.forward(800)
ttl.right(90)
ttl.forward(400)
ttl.right(90)
ttl.forward(800)
ttl.right(180)
ttl.end_fill()


ttl.penup()
ttl.goto(-100,100)


ttl.pendown()
ttl.color("black")
ttl.fillcolor("white")
ttl.begin_fill()

# rumah
ttl.right(90)
ttl.forward(200)
for i in range(2):
    ttl.left(90)
    ttl.forward(200)
ttl.left(90)
ttl.forward(240)
ttl.end_fill()

# atap
ttl.fillcolor("brown")
ttl.begin_fill()
ttl.right(135)
ttl.forward(200)
ttl.right(90)
ttl.forward(200)
ttl.right(135)
ttl.forward(280)
ttl.end_fill()


ttl.penup()
ttl.goto(-70, -100)

# pintu
ttl.fillcolor("brown")
ttl.begin_fill()
ttl.pendown()
ttl.right(90)
ttl.forward(100)
ttl.right(90)
ttl.forward(50)
ttl.right(90)
ttl.forward(100)
ttl.end_fill()


ttl.penup()
ttl.goto(20, 10)

#jendela
ttl.pendown()
ttl.fillcolor("cyan")
ttl.begin_fill()
ttl.forward(50)
for i in range(3):
    ttl.left(90)
    ttl.forward(50)
ttl.end_fill()
ttl.penup()
ttl.left(90)
ttl.forward(25)
ttl.pendown()
ttl.left(90)
ttl.forward(50)
ttl.penup()
ttl.goto(45, 10)
ttl.right(90)
ttl.pendown()
ttl.forward(50)
ttl.penup()

# matahari
ttl.goto(200,300)
ttl.fillcolor("yellow")
ttl.begin_fill()
ttl.pendown()
ttl.circle(100)
ttl.end_fill()
ttl.penup()

# selesai
ttl.hideturtle()
ttl.exitonclick()