from tkinter import *
from tkinter import ttk
import reconhecedor_regex


def compilar(entry):
    global linguagem
    try: 
        linguagem = reconhecedor_regex.configurar_expressao(entry.get())
    except:
        print("linguagem inválida!")
        entry.configure(background="red")
    else:
        print("compilou")
        entry.configure(background="lightblue")

def validar(entry):
    try:
        if linguagem.fullmatch(entry.get()):
            entry.configure(background='lightgreen')
        else:
            entry.configure(background='red')
    except:
        print("linguagem não compilada!")
    else:
        print("validou")



def gui_setup():
    root = Tk()
    root.title("Validador de expressões regulares")
    main_frame = ttk.Frame(root, padding=10)
    main_frame.grid()

    #Labels:
    ttk.Label(main_frame, text="expressão regular:").grid(column=0, row=0)
    ttk.Label(main_frame, text="palavra:").grid(column=0, row=2)

    #Entrys:
    entry_linguagem = Entry(main_frame, width=40)
    entry_linguagem.grid(column=0, row=1)
    entry_palavra = Entry(main_frame, width=40)
    entry_palavra.grid(column=0, row=3)

    # Vincula a compilação e validação ao evento de soltar uma tecla
    entry_linguagem.bind("<KeyRelease>", lambda event: compilar(entry_linguagem))
    entry_palavra.bind("<KeyRelease>", lambda event: validar(entry_palavra))

    root.mainloop()


if __name__ == "__main__":
    gui_setup()