import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font





countdown_job = None

def countdown(count):
    global countdown_job
    label['text'] = f"{count // 60:02d}:{count % 60:02d}"

    if count > 0:
        # call countdown again after 1000ms (1s)
        countdown_job = painel.after(1000, countdown, count - 1)

def start_30min():
    global countdown_job
    # Cancelando a contagem regressiva atual, se houver
    if countdown_job is not None:
        painel.after_cancel(countdown_job)
    countdown(30 * 60)

def start_5min():
    global countdown_job
    # Cancelando a contagem regressiva atual, se houver
    if countdown_job is not None:
        painel.after_cancel(countdown_job)
    countdown(5 * 60)

painel = tk.Tk()
painel.geometry('550x350')
painel.title('Study Timer K0mth3')
painel.configure(background='#16141a')
painel.resizable(False, False)
painel.iconbitmap('C:/Users/PEDRO MORAES/Downloads/brand_hello_kitty_icon_158867.ico')

# fonts komth3countdown
fontecust = font.Font(family="Merriweather", size=22)
fontecust2 = font.Font(family="Merriweather", size=16)
fontecust3 = font.Font(family="Merriweather", size=26)





# images links komth3
path = 'C:/Users/PEDRO MORAES/Downloads/girljava.jpg'

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(painel, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

# Adicionando um texto na tela do painel
texto = tk.Label(painel, text="Study Timer", bg='#FED49A', fg='black', font=fontecust, highlightbackground='black',
                 highlightthickness=2)
texto.place(x=190, y=90)

label = tk.Label(painel, text="", bg='#B836FF', fg='black', font=fontecust3, borderwidth=5, highlightbackground='black', highlightthickness=2)
label.place(x=230, y=150)


botao_iniciar = tk.Button(painel, text='Study!', bg='#00BCD4', fg='black', font=fontecust2, borderwidth=5,
                          command=start_30min)
botao_iniciar.place(x=185, y=220)

botao_rest = tk.Button(painel, text='Rest', bg='#FFFF00', fg='black', font=fontecust2, borderwidth=5,
                       command=start_5min)
botao_rest.place(x=300, y=220)


komthe = tk.Label(painel, text='Coded by K0MTH3', font=fontecust2, bg='#569890', fg='black', highlightbackground='black', highlightthickness=2)
komthe.place(x=360, y=310)


painel.mainloop()
