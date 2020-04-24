'''
Created on 9 may. 2019

@author: Roman Mussi
'''

import turtle
bob = turtle.Turtle()
#print(bob)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

#square(bob, 50)
polygon(bob, 100, 9)

turtle.mainloop()


