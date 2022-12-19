'''
simulare un robto pulisci-pavimaneti che è impazzito 
5 px
siumular eil movimento del robot perm2 ore 
'''
import turtle
import random
import time

zoassa = turtle.Turtle()
zoassa.color("red")
for k in range(0,3600000):
    x = random.randint(0,100)
    zoassa.forward(x)
    x = random.randint(0,100)
    zoassa.right(x)
    x = random.randint(0,100)
    zoassa.forward(x)
    x = random.randint(0,100)
    zoassa.left(x)
    x = random.randint(0,100)
    zoassa.forward(x)

    time.sleep(10000)
    
turtle.done()

