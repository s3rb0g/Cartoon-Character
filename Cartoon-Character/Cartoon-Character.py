import turtle
t = turtle.Turtle()
t.speed(5) 

t.color('brown')
t.begin_fill()
t.circle(100)

t.lt(90)
t.penup()
t.fd(100)
t.lt(90)
t.fd(100)
t.rt(180)
t.pendown()
t.end_fill()

t.color('brown')
t.begin_fill()
for i in range(4):
  t.fd(200)
  t.rt(90) 
t.end_fill()

t.fd(60)

for j in range(2):
  t.color('black')
  t.begin_fill()
  t.circle(20)
  t.end_fill()

  t.penup()
  t.lt(90)
  t.fd(15)
  t.pendown()

  t.rt(90)
  t.color('white')
  t.begin_fill()
  t.circle(5)
  t.end_fill()

  t.penup()
  t.rt(90)
  t.fd(15)
  t.lt(90)
  t.pendown()

  t.penup()
  t.fd(80)
  t.pendown()

t.penup()
t.home()
t.fd(25)
t.pendown()
for k in range(2):
  t.color('orange')
  t.begin_fill()
  t.circle(25)
  t.end_fill()
	
  t.penup()
  t.rt(180)
  t.fd(50)
  t.rt(180)
  t.pendown()

t.penup()
t.fd(50)
t.pendown()

t.begin_fill()
for l in range(4):
  t.fd(50)
  t.lt(90)
t.end_fill()

t.penup()
t.home()
t.rt(90)
t.fd(100)
t.lt(90)
t.pendown()

t.color('black')
t.fd(150)
t.bk(300)
