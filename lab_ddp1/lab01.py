import turtle as tl


n = int(input("n = "))

# r1 = float(input("r1 = ")
# g1 = float(input("g1 = ")
# b1 = float(input("b1 = ")


tl.bgcolor("white")
tl.shape("turtle")
tl.width(1)
tl.speed("fastest")

tl.colormode(255)
tl.pendown()

a = 1
for i in range(50 * n):

  tl.forward(a)
  tl.left(360/n)
  a += 1

tl.hideturtle()
tl.exitonclick()