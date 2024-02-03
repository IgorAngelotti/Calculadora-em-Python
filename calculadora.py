import tkinter as tk
from tkinter import ttk

#Função de inserir elemento no comando de entrada
def press(key):
    entry.insert(tk.END, key)

#Para calcular expressão que está na entrada usando o eval(), usando o .delete para apagar o texto anterior
def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))

#Limpar area de entrada
def clear():
    entry.delete(0, tk.END)

#Cria a janela principal utilizando a classe Tk() e define o título
root = tk.Tk()
root.title("calculadora")
#É possível utilizar o .configure() para customizar a tela

#Define o campo de entrada Entry() na janela principal (root)
entry = tk.Entry(root, width=16, font=('Arial', 16))

#Ajuste de posição com o .grid para ocupar 4 colunas
entry.grid(row=0, column=0, columnspan=4)

#Botões da calculadora
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

#Para indicar a posição ao criar os botões
row_val = 1
col_val = 0

#Laço de repetição para criar os botões, adicionando comando lambda em cada um para chamar determinada função de acordo com o valor do botão ao clicar sobre ele, além de  posicionar com .grid
for button in buttons:
    tk.Button(root, text=button, padx= 20, pady=20, command=lambda b=button: clear() if b == 'C' else press(b) if b != '=' else calculate() if b == '=' else None).grid(row= row_val, column= col_val)

    #Verificação das posições
    col_val += 1
    if col_val > 3: 
        col_val = 0
        row_val += 1

root.mainloop()
