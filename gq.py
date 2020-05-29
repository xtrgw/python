from turtle import *
hideturtle()
#长方形
pu()
goto(-350,-200)
pd()
begin_fill()
color("red")
for i in range(2):
    pencolor("red")
    fd(600)
    left(90)
    fd(400)
    left(90)
end_fill()

#大五角星
pu()
goto(-280,120)
pd()
pencolor("yellow")
begin_fill()
color("yellow")
for i in range(5):
    fd(80)
    left(-144)
end_fill()

#小五角星
def xwjx(x,y):
    pu()
    goto(x,y)
    left(-10)
    pd()
    for i in range(4):
        pencolor("yellow")
        begin_fill()
        color("yellow")
        for i in range(5):
            fd(25)
            left(144)
        end_fill()
        pu()
        circle(-60,50)
        pd()

def main():
    speed(0)
    setup(800,500)
    xwjx(-180,160)
    done()

if __name__ == '__main__':
    main()
    
