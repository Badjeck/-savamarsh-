from tkinter import *

attaques={'1080':3,'533':2,'22':1}
taille_cube=100
hauteur=taille_cube*5
largeur=taille_cube*8

def change_coo():
    x1=taille_cube*(x+1)
    y1=hauteur-taille_cube*(y+1)
    return x1,y1

def init_canevas():
    canevas.create_line(0,hauteur-taille_cube, largeur, hauteur-taille_cube, fill="green",dash=(2,2,4,2), width=2)
    # #dessiner l'histogramme du port 1080
    # canevas.create_rectangle(coord(0,0),coord(1,3),fill='red')
    # #l'histo port 533
    # canevas.create_rectangle(coord(2,0),coord(3,2),fill='red')
    # #port 22
    # canevas.create_rectangle(coord(4,0),coord(5,1),fill='red')
    # # i=0
    # # for cle,valeur in attaques.items():

def raz():
    pass

#fenetre graphique
fenetre = Tk()
canevas=Canvas(fenetre, width= largeur, height= hauteur, bg='black')
btn_raz=Button(fenetre, text='Raz',command=raz)
btn_quit=Button(fenetre,text='Quitter',command=fenetre.destroy)

#placement des widgets
canevas.grid(row=0,column=0,columnspan=3)
btn_raz.grid(row=1,column=1)
btn_quit.grid(row=1,column=2)

init_canevas()

#boucle infini
fenetre.mainloop()