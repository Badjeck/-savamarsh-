from tkinter import *
import time

J1=0
J2=0
score_max=0
col_J1=''
col_J2=''
col_b=''
col_bg=''
vit_b=0



dx=10
dy=10
b0=485
b1=285
b2=515
b3=315

ra0=50
ra1=230
ra2=70
ra3=370

rb0=930
rb1=230
rb2=950
rb3=370



def jouer():
    global tk,dx,dy,ra0,ra1,ra2,ra3,rb0,rb1,rb2,rb3,J1,J2
    J1=0
    J2=0
    def deplacement():
        global dx,dy,ra0,ra1,ra2,ra3,rb0,rb1,rb2,rb3,J1,J2,score_max,col_J1,col_J2,col_b,col_bg,vit_b

        def fin_jeux():
            tk.destroy()
            print('oui')

        if J1>=score_max or J2>=score_max:
            fin_jeux()
            
        
        if fen.coords(balle)[1]<0:
            dy = -dy
        if fen.coords(balle)[3]>600:
            dy = -dy
        #rebond raquette2
        if fen.coords(balle)[2] > fen.coords(raquetteb)[0] and fen.coords(balle)[3] > fen.coords(raquetteb)[1] and fen.coords(balle)[1] < fen.coords(raquetteb)[3] and fen.coords(balle)[0] < fen.coords(raquetteb)[2]:
            dx = -dx
        #rebond raquette1
        if fen.coords(balle)[2] > fen.coords(raquettea)[0] and fen.coords(balle)[3] > fen.coords(raquettea)[1] and fen.coords(balle)[1] < fen.coords(raquettea)[3] and fen.coords(balle)[0] < fen.coords(raquettea)[2]:
            dx = -dx
        if fen.coords(balle)[0]<0:
            J2=+1
            fen.coords(raquettea,ra0,ra1,ra2,ra3)
            fen.coords(raquetteb,rb0,rb1,rb2,rb3)
            time.sleep(0.5)
            fen.coords(balle,b0,b1,b2,b3)
            
        if fen.coords(balle)[2]>1000:
            J1+=1
            fen.coords(raquettea,ra0,ra1,ra2,ra3)
            fen.coords(raquetteb,rb0,rb1,rb2,rb3)
            time.sleep(0.5)
            fen.coords(balle,b0,b1,b2,b3)

        tk.after(20,deplacement)
        fen.move(balle,dx,dy)
    def hauta(event):
        if fen.coords(raquettea)[1]>0:
            fen.move(raquettea,0,-10)
    def basa(event):
        if fen.coords(raquettea)[3]<600:
            fen.move(raquettea,0,10)
    def hautb(event):
        if fen.coords(raquetteb)[1]>0:
            fen.move(raquetteb,0,-10)
    def basb(event):
        if fen.coords(raquetteb)[3]<600:
            fen.move(raquetteb,0,10)

    tk = Tk()
    tk.title('PONG')
    fen = Canvas(tk,width = 1000, height = 600, bg="black")
    fen.pack()

    btn_quit=Button(tk, text ='Quitter', command = tk.destroy).pack()
    raquetteb = fen.create_rectangle(rb0,rb1,rb2,rb3,fill="red")
    raquettea = fen.create_rectangle(ra0,ra1,ra2,ra3,fill="red")
    balle = fen.create_oval(b0,b1,b2,b3,fill="grey")

    tk.focus_force()

    fen.bind_all('<z>', hauta)
    fen.bind_all('<s>', basa)
    fen.bind_all('<Up>', hautb)
    fen.bind_all('<Down>', basb)
    deplacement() 

jouer()