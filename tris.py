import turtle
from turtle import *

class Casella():
    def __init__(self, stato):
        self.status = stato  # 0, 1, 2

    def setStatus(self, status):
        if status >= 0 & status <= 2:
            self.status = status,

    def getStatus(self):
        return self.status

def inserire(tris, pos, player):
        
     if tris[pos].getStatus() == 0:
            tris[pos].setStatus(player)
            return True
     else:
        return False

def disegnaGriglia(pen):
    pen.pendown()
    pen.color("black")
    pen.speed(10)
    for i in range(0,4):
        if i == 0:
            pen.right(180)
        else:
            pen.right(90)
        pen.forward(50)
        if i == 0:
            pen.left(90)
            pen.forward(50)
            pen.backward(50)
            pen.right(90)
            pen.forward(50)
        pen.left(90)
        pen.forward(50)
        pen.backward(50)
        pen.right(90)
        pen.forward(50)
        pen.backward(50)

    pen.right(180)

def disegnaCerchio(pos, t):    
    t.penup()
    t.goto(pos)
    
    t.forward(25)
    t.left(90)
    t.forward(5)
    t.left(-90)
    t.pendown()
    t.color("red")
    t.circle(20)

def disegnaCroce(pos, t):
    t.penup()
    t.goto(pos)
    t.pendown()
    t.left(45)
    t.penup()
    t.forward(15)
    t.pendown()
    t.color("blue")
    t.forward(40)
    t.backward(20)
    t.left(90)
    t.backward(20)
    t.forward(40)
    t.backward(20)
    t.right(90+90-45)
  
def controllaGioco(tris):
    #tris = [Casella(0) ,Casella(0) ,Casella(0) ,Casella(0) ,Casella(0) ,Casella(0) ,Casella(0) ,Casella(0) ,Casella(0)]
    tro = False
    k = 0

    while not tro and k <= 6:
        uno = tris[k].status
        due = tris[k+1].status
        tre = tris[k+2].status

        if uno != 0:
            if uno == due:
                if due == tre:
                    tro = not tro
                    giocatore = tre 

        k = k+3 
   
    if tro:
        return giocatore

    k = 0
    while not tro and k < 3:
        uno = tris[k].status
        due = tris[k+3].status
        tre = tris[k+6].status

        if uno != 0:
            if uno == due:
                if due == tre:
                    tro = not tro
                    giocatore = tre 

        k = k+1
   
    if tro:
        return giocatore

    if(tris[0].status == tris[4].status and tris[0].status != 0 and tris[0].status == tris[8].status):
        return tris[0].status
    elif tris[2].status == tris[4].status and tris[2].status != 0 and tris[4].status == tris[6].status:
        return tris[6].status
    else: 
        return -1 

def main():
    pos = [(-100,-50), (-50,-50), (0,-50),(-100,0), (-50,0), (0,0),(-100,50), (-50,50), (0,50)]
    tris = [Casella(0) ,Casella(0) ,Casella(0) ,Casella(0) ,Casella(0) ,Casella(0) ,Casella(0) ,Casella(0) ,Casella(0)]
    pos1 = 0
    tro = True
    t = turtle.Pen()
    t.hideturtle()
    disegnaGriglia(t)
    k=0
    while(True and k<9):
        while(True):
            print("cerchio")
            pos1 = int(input())
            if pos1 > 0 and pos1 <= 9 and inserire(tris, pos1-1, 1) :
                break
        disegnaCerchio(pos[pos1-1], t)
        print(pos[pos1-1])  

        if controllaGioco(tris) == -1:
            pass
        else:
            print(F"vince il giocatore: {controllaGioco(tris)}")
            break
        k = k +1 

        if(k >= 9): break
              
        while(True):
            print("croce")
            pos1 = int(input())
            if  pos1 > 0 and pos1 <= 9 and inserire(tris, pos1-1, 2):
                break
        
        disegnaCroce(pos[pos1-1], t)
        print(pos[pos1-1])   

        if controllaGioco(tris) == -1:
            pass
        else:
            print(F"vince il giocatore: {controllaGioco(tris)}")
            break
        k = k +1 

    if k >= 9:
        print("pareggio")     

    turtle.done()

if __name__ == "__main__":
    main()