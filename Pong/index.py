from tkinter import *
import time

J1=0
J2=0
score_max=2

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

def menu():
    def menudestroy():
        menu.destroy()
        jouer()

    menu = Tk()
    menu.title("C UN POOOOOOOOOOOOOOOONG")
    fenmen = Canvas(menu, width=300, height=150,bg='blue').pack()
    menu.focus_force()

    btn_play = Button(fenmen, text =" JOUEEEEEEEEEEEER ", command = menudestroy).place(relx=0.3,rely=0.3)
    btn_quitm=Button(menu, text ='Quitter', command = menu.destroy).place(relx=0.4,rely=0.6)
    menu.mainloop()

def parametre():
    def cbon():
        fpar.destroy()
        jouer()
    
    def changeCol_J1(col1):
        col_J1 = col1 
        return col_J1

    def changeCol_J2(col2):
        col_J2 = col2
        return col_J2

    def changeCol_b(colb):
        col_b = colb
        return col_b

    def changeCol_bg(colbg):
        col_bg = colbg
        par.configure(background = colbg)
        return col_bg

    def changeVit(vit):
        vit_b = vit
        return vit_b


    color=('white', 'black', 'grey', 'red', 'dark red', 'blue', 'royal blue', 'vert', 'yellow')
    vitesse=(5,6,7,8,9,10)

    fpar = Tk()
    fpar.title('PONG')
    par = Canvas(fpar,width = 750, height = 400, bg="black")
    par.pack()

    choix_col_J1 = Pmw.ComboBox(par, labelpos = NW,label_text = 'couleur J1',scrolledlist_items = color, listheight = 150, selectioncommand = changeCol_J1)
    choix_col_J1.place(relx=0.1,rely=0.3)

    choix_col_J2 = Pmw.ComboBox(par, labelpos = NW,label_text = 'couleur J2',scrolledlist_items = color, listheight = 150, selectioncommand = changeCol_J2)
    choix_col_J2.place(relx=0.4,rely=0.3)

    choix_col_balle = Pmw.ComboBox(par, labelpos = NW,label_text = 'couleur balle',scrolledlist_items = color, listheight = 150, selectioncommand = changeCol_b)
    choix_col_balle.place(relx=0.7,rely=0.3)

    choix_vit_balle = Pmw.ComboBox(par, labelpos = NW,label_text = 'vitesse balle',scrolledlist_items = vitesse, listheight = 150, selectioncommand = changeVit)
    choix_vit_balle.place(relx=0.2,rely=0.5)

    choix_col_fond = Pmw.ComboBox(par, labelpos = NW,label_text = 'couleur fond',scrolledlist_items = color, listheight = 150, selectioncommand = changeCol_bg)
    choix_col_fond.place(relx=0.6,rely=0.5)

    btn_play = Button(par, text =" PLAAAAAAAAAY ", command = cbon).place(relx=0.4,rely=0.7)

    fpar.mainloop()    

def jouer():
    global tk,dx,dy,ra0,ra1,ra2,ra3,rb0,rb1,rb2,rb3,J1,J2
    J1=0
    J2=0
    def deplacement():
        global dx,dy,ra0,ra1,ra2,ra3,rb0,rb1,rb2,rb3,J1,J2,score_max

        def fin_jeux():
            tk.destroy()
            ecran_fin_party()

        if J1>=score_max or J2>=score_max:
            t_fin_jeux = time.time()
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
            time.sleep(1)
            fen.coords(balle,b0,b1,b2,b3)
            
        if fen.coords(balle)[2]>1000:
            J1+=1
            fen.coords(raquettea,ra0,ra1,ra2,ra3)
            fen.coords(raquetteb,rb0,rb1,rb2,rb3)
            time.sleep(1)
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
    raquetteb = fen.create_rectangle(rb0,rb1,rb2,rb3,fill='red')
    raquettea = fen.create_rectangle(ra0,ra1,ra2,ra3,fill='red')
    balle = fen.create_oval(b0,b1,b2,b3,fill='white')

    tk.focus_force()

    fen.bind_all('<z>', hauta)
    fen.bind_all('<s>', basa)
    fen.bind_all('<Up>', hautb)
    fen.bind_all('<Down>', basb)
    deplacement() 


def ecran_fin_party():
    global J1, J2, score, t_debut_jeux, t_fin_jeux

    ecran_fin = Tk()
    ecran_fin.title('mangez 7 frite et poulet par jour')
    oui = Canvas(ecran_fin, width=300, height=150,bg='green')
    oui.pack()
    ecran_fin.focus_force()
    
    
    if J1<J2:
        kikigagne = Label(oui,text="J1 WIN SUPER \(-.-)/").place(relx=0.3,rely=0.1)
    else:
        kikigagne = Label(oui,text="J2 WIN SUPER \(-.-)/").place(relx=0.3,rely=0.1)
    
    btn_quitm = Button(oui, text ='Quitter', command = ecran_fin.destroy).place(relx=0.4,rely=0.7)
    btn_play = Button(oui, text =" (re)JOUEEEEEEEER ", command = lambda:replay()).place(relx=0.3,rely=0.4)
    
    def replay():
        ecran_fin.destroy()
        jouer()

    ecran_fin.mainloop()




menu()