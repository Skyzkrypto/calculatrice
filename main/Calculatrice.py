from tkinter import *

# Boucle principale

running = True

while running == True :

    def calcul():

         # fonction

        def quitter():
 
            calculator.destroy()
            running = False
        
        # fenetre

        calculator = Tk()

        # frame

        frame_calcul = Frame(calculator)
        frame_calcul.pack()

        # Configuration de la fenetre

        calculator.minsize(250, 350)
        calculator.maxsize(650, 750)
        calculator.title("Calculatrice")
        calculator.config(bg="#EACDC7")
        # boutton   

        plus = Button(frame_calcul, text="+", font=("arial", 25))
        plus.pack(side="right")

        moins = Button(frame_calcul, text="-", font=("arial", 25))
        moins.pack(side="left")

        quiT = Button(calculator, text="quitter", font=("arial", 25), command=quitter)
        quiT.pack(anchor="sw")

        # mainloop fen

        calculator.mainloop()

    calcul()        
