bounus = None
couleur_bonus_list = ["green","yellow","red"]
last_hit = 0

def bonus():
            global bounus,couleur_bonus,j1,j2,b
            if bounus == None:
                x_bul = randrange(50,largeur-90)
                y_bul = randrange(5,hauteur-5)
                couleur_bonus = couleur_bonus_list[randrange(0,3,1)]
                bul_bonus = canvas.create_oval(x_bul,y_bul,x_bul+40,y_bul+40,fill=couleur_bonus)
            if (canvas.coords(ball)[1]<=canvas.coords(bul_bonus)[3]) and (canvas.coords(ball)[3]>=canvas.coords(bul_bonus)[1]) and (canvas.coords(ball)[2]>=canvas.coords(bul_bonus)[0]) and (canvas.coords(ball)[0]<=canvas.coords(bul_bonus)[2]):
                if couleur_bonus == "green":
                    if last_hit == True:
                        canvas.delete(j1)
                        j1 = canvas.create_rectangle((15,y1_j1-20),(30,y2_j1+20),fill=couleurs[coul_j1%5])
                    if last_hit == False:
                        canvas.delete(j2)
                        j2 = canvas.create_rectangle((1050,y1_j2+20),(1065,y2_j2-20),fill=couleurs[coul_j2%5])
                if couleur_bonus == "yellow":
                    b += b
                if couleur_bonus == 'red':
                    if last_hit == True:
                        canvas.delete(j2)
                        j2 = canvas.create_rectangle(450,y1_j2+20,425,y2_j2-20,fill=couleurs[coul_j2%5])
                    if last_hit == False:
                        canvas.delete(j1)
                        j1 = canvas.create_rectangle(50,y1_j1+20,75,y2_j1-20,fill=couleurs[coul_j1%5])
                canvas.delete(bul_bonus)
                bounus = None
            canvas.after(1000,bonus)

        scores(score_j1,score_j2)
        
        if ((canvas.coords(ball)[1]<=canvas.coords(j1)[3]) and (canvas.coords(ball)[1]>=canvas.coords(j1)[1]) and (canvas.coords(ball)[0]<=canvas.coords(j1)[2]) and (canvas.coords(ball)[0]>=canvas.coords(j1)[0])):
            b = -int(b)
            dy += randrange(-100,100)/100
            last_hit = True
        if ((canvas.coords(ball)[2]>=canvas.coords(j2)[0]) and (canvas.coords(ball)[2]<=canvas.coords(j2)[2]) and (canvas.coords(ball)[3]>=canvas.coords(j2)[1]) and (canvas.coords(ball)[1]<=canvas.coords(j2)[3])):
            b = -int(b)
            dy += randrange(-100,100)/100
            last_hit = False
        if (canvas.coords(ball)[3]>=hauteur) or (canvas.coords(ball)[1]<=0):
            dy = -dy
        
        if (canvas.coords(ball)[0] <= 0):
            dy = 0
            score_j2 += 1
            scores(score_j1,score_j2)
            fenetre_jeu.destroy()
            le_jeu()

        elif (canvas.coords(ball)[2] >= largeur):
            dy = 0
            score_j1 += 1
            scores(score_j1,score_j2)
            fenetre_jeu.destroy()
            le_jeu()

        global temps_fin
        if score_j1==int(a):
            temps_fin = time()
            fenetre_jeu.destroy()
            victoire_j1()
        elif score_j2==int(a):
            temps_fin = time()
            fenetre_jeu.destroy()
            victoire_j2()

        canvas.move(ball,b,dy)
        fenetre_jeu.after(10,gametick)