import turtle
s = turtle.getscreen()
t = turtle.Turtle()
for _ in range(100):
    t.circle(100)
    t.right(50)
    t.width(3)
    t.speed(0)
    t.color('green')
    t.screen.mainloop()