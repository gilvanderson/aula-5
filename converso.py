import tkinter as tk
from moeda import apidolar

def dolar():
    cotacao = apidolar();
    reais =  float(valor.get())
    conta = f'com R$ {reais:.2f}reais compra-se $ {conta} dólares'
    

janela = tk.Tk()
janela.geometry('300x600')
janela.title('aulan 04 - tkinter')
janela.configure(bg='#005C53')

titulo = tk.Label(janela, text='converso de reais para dolar', font=('verdana',16), fg='#D6D58E', bg='#005C53')
titulo.pack(pady=10)

rotulo = tk.Label(janela, text='digite valor em reais para comverte', font=('verdana',12),fg='#A5A692')
rotulo.pack(pady=10)

valor = tk.Entry(janela, bg='#011F26')
valor.pack(pady=10)

botão = tk.Button(janela, text='converte',command='bg=#011F26')
botão.pack(pady=10)

responda = tk.Label(janela, text='', font=('verdana',12), fg='#A5A692')
responda.pack(pady=10)









janela.mainloop()