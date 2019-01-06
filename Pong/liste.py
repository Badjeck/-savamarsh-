from tkinter import *
import Pmw


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

    choix_vit_balle = Pmw.ComboBox(par, labelpos = NW,label_text = 'vitesse balle',scrolledlist_items = vitesse, listheight = 110, selectioncommand = changeVit)
    choix_vit_balle.place(relx=0.2,rely=0.5)

    choix_col_fond = Pmw.ComboBox(par, labelpos = NW,label_text = 'couleur fond',scrolledlist_items = color, listheight = 150, selectioncommand = changeCol_bg)
    choix_col_fond.place(relx=0.6,rely=0.5)

    btn_play = Button(par, text =" PLAAAAAAAAAY ", command = cbon).place(relx=0.4,rely=0.7)

    fpar.mainloop()

parametre()

