import tkinter as tk

def on_button_click():
    print("Botão clicado!")

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo Tkinter")

# Criação de um rótulo
label = tk.Label(root, text="Olá, Tkinter!")
label.pack()

# Criação de um botão
button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack()

# Início do loop principal
root.mainloop()
