from tkinter import *
import keyboard
import pyautogui
import time

is_on = True
texto = "desativado"

janela = Tk()
janela.title("AutoPress")
janela.iconbitmap('taiga.ico')

texto_orientacao = Label(janela, text="Aperte F8 para segurar o botão esquerdo e clique para parar")
texto_orientacao.grid(column=0, row=0)


def autopress():
    global is_on
    global texto
    if is_on:
        texto = "Ativado"
        is_on = False
        textoatides["text"] = texto
    else:
        pyautogui.mouseDown()
    textoatides["text"] = texto


keyboard.add_hotkey('f8', lambda: autopress())

textoatides = Label(janela, text="", fg="black")
textoatides.grid(column=0, row=1)

janela.mainloop()
