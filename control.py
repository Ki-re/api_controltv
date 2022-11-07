from tkinter import *

window=Tk()

encender_btn=Button(window, text="Encender", fg='green')
encender_btn.place(x=80, y=100)

apagar_btn=Button(window, text="Apagar", fg='green')
apagar_btn.place(x=80, y=100)

txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=150)

window.title('Hello Python')
window.geometry("300x200+10+20")

window.mainloop()