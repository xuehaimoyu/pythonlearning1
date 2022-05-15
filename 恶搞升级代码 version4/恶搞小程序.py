import time
import tkinter as tk 
import random 
import threading
print("Created BY ZSR")
scale =10
print("--------SUPER MONI LEARNING LOADING -----------")
for i in range(scale+1):
    a,b = '**' * i,'..' * (scale - i)
    c = (i/scale)*100
    print("%{:^3.0f}[{}-{}]" .format (c,a,b))
    time.sleep(0.2)
print("--------------Loading successfully-----------------")
print(' ')
print(' ')
print("--------PYTHON3.9 LOADING -----------")
for i in range(scale+1):
    a,b = '**' * i,'..' * (scale - i)
    c = (i/scale)*100
    print("%{:^3.0f}[{}-{}]" .format (c,a,b))
    time.sleep(0.1)
print("--------------Loading successfully-----------------")
print("--------IQ INCREASING  MACHINE LOADING -----------")
print(' ')
print(' ')
for i in range(scale+1):
    a,b = '**' * i,'..' * (scale - i)
    c = (i/scale)*100
    print("%{:^3.0f}[{}-{}]" .format (c,a,b))
    time.sleep(0.3)
print("--------------Loading successfully-----------------")
print(' ')
print('WELCOME')
import turtle
SIZE_TREE = 10
def draw_tree(size):
    if size > SIZE_TREE:
        turtle.forward(size)
        turtle.right(20)
        draw_tree(size / 1.5)
        turtle.left(40)
        draw_tree(size / 1.5)
        turtle.right(20)
        if size / 2 <= SIZE_TREE:
            turtle.color('green')
        else:
            turtle.color('brown')
        turtle.backward(size)
def main():
    turtle.speed(1)
    turtle.hideturtle()
    turtle.penup()
    turtle.left(90)
    turtle.backward(100)
    turtle.showturtle()
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('brown')
    draw_tree(50)
    turtle.penup()
    turtle.backward(30)
    turtle.pendown()
    turtle.write('WELCOME',align='center',font=('arial',20,'normal'))
    time.sleep(3)
if __name__ == '__main__':
    main()
def boom(): 
        window = tk.Tk() 
        width = window.winfo_screenwidth() 
        height = window.winfo_screenheight() 
        a = random.randrange(0, width) 
        b = random.randrange(0, height) 
        window.title('Closing Me') 
        window.geometry("300x100" + "+" + str(a) + "+" + str(b)) 
        tk.Label(window, text='FOOL', bg='green', font=('宋体', 20), width=20, height=4).pack() 
        window.mainloop()
        threads = [] 
        for i in range(0,9):
            t = threading.Thread(target=boom) 
            threads.append(t) 
            time.sleep(0.1)
            threads[i].start()
turtle.bye()   
print('LET US BEGIN OUR JOURNEY')
print('WARNING MISTAKE WILL HAVE PUNISHMENT')
x=input('please input your nickname:   ')
time.sleep(0.5)
print("LOADING>>>>>>>>>>")
boom()
time.sleep(0.5)
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print('THE AUTHOR HAS NOT PROGRAMED THE FOLLOWING THINGS YET')
print('BYE')
print('IF YOU WANT TO CLOSE,JUST CLOSE THE PROGRAM ')
print(' ')
print('PRESS ENTER TO EXIT')

input()

