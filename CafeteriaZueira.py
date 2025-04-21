import tkinter as tk
from PIL import Image, ImageTk
import random

def mover_nao(e):
    botao_nao.place(x=random.randint(50, 1000), y=random.randint(50, 700))

def resposta_sim():
    label.config(text="Então vamos marcar o dia! ☕😊", font=("Arial", 28), fg="black", bg="pink")
    botao_sim.place_forget()
    botao_nao.place_forget()

janela = tk.Tk()
janela.title("Pergunta Importante")
janela.geometry("1280x720")

# Carregar a imagem de fundo
imagem_fundo = Image.open("brunch-0.jpg")  # Troque pelo nome da sua imagem
imagem_fundo = imagem_fundo.resize((1280, 720))  # Ajusta para o tamanho da janela
bg = ImageTk.PhotoImage(imagem_fundo)

# Criar um label com a imagem de fundo
fundo_label = tk.Label(janela, image=bg)
fundo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Texto da pergunta
pergunta = tk.Label(janela, text="Vamos marcar nossa próxima ida a uma cafeteria?",
                    font=("Arial", 30), fg="black", bg="pink")
pergunta.pack(pady=20)

# Label de resposta
label = tk.Label(janela, text="", bg="#000000", fg="white", font=("Arial", 24)) 
label.pack()

# Botões
botao_sim = tk.Button(janela, text="Claro que sim, nós merecemos!",
                      font=("Arial", 18), bg="pink", fg="black", command=resposta_sim)
botao_sim.place(x=200, y=150)

botao_nao = tk.Button(janela, text="Não, precisamos economizar",
                      font=("Arial", 18), bg="pink", fg="black")
botao_nao.place(x=800, y=150)
botao_nao.bind("<Enter>", mover_nao)

janela.mainloop()
