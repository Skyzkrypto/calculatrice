from tkinter import *
import webbrowser
import os
# Boucle principale

running = bool(True)

if running == True :

    def calcul():

         # fonction

        def quitter():
 
            calculator.destroy()
        def git():
            webbrowser.open_new(url="https://github.com/Wishrito/calculatrice")
            
        # fenetre
        calculator = Tk()
        
        # frame
        bg = PhotoImage(file="src/img/1140270591828570112 (1).png")
        label1 = Label(calculator, image = bg)
        label1.place(x = 0, y = 0)
        
        frame_calcul = Frame(calculator)
        frame_calcul.pack()

        # Configuration de la fenetre

        calculator.minsize(250, 350)
        calculator.maxsize(650, 750)
        calculator.title("Calculatrice")
        calculator.iconbitmap(bitmap="src/img/1140270591828570112.ico")
        # boutons
        github = Button(calculator, text="voir sur Github", font=("arial", 25), command=git)
        github.pack(side="top")
        
        plus = Button(frame_calcul, text="+", font=("arial", 25))
        plus.place()
        plus.pack(side="right")

        moins = Button(frame_calcul, text="-", font=("arial", 25))
        moins.pack(side="left")

        quiT = Button(calculator, text="quitter", font=("arial", 25), command=quitter)
        quiT.place(x=-10, y=-10)


        # mainloop fen

        calculator.mainloop()

    calcul()        
