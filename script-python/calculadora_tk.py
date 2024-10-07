import tkinter as tk

janela = tk.Tk()
janela.resizable(False, False)

fonte = ('Arial', 32)

valor_1 = tk.StringVar()
valor_2 = tk.StringVar()
operador = tk.StringVar()

def confere():
    print(f'{operador.get() = }')
    print(f'{valor_1.get() = }')
    print(f'{valor_2.get() = }')

def joga_na_tela(num):
    ent_tela.insert('end', str(num))

def define_operacao(op):
    operador.set(op)
    valor_1.set(ent_tela.get())
    ent_tela.delete(0, 'end')
    btn_div.config(state='disabled')
    btn_mul.config(state='disabled')
    btn_sub.config(state='disabled')
    btn_som.config(state='disabled')
    btn_enter.config(state='active')
    confere()

def mata_todo_mundo():
    operador.set('')
    valor_1.set('')
    valor_2.set('')
    btn_div.config(state='active')
    btn_mul.config(state='active')
    btn_sub.config(state='active')
    btn_som.config(state='active')
    btn_enter.config(state='disabled')
    ent_tela.delete(0, 'end')
    confere()

def calcula():
    valor_2.set(ent_tela.get())
    ent_tela.delete(0, 'end')

    if operador.get() == '+':
        resultado = float(valor_1.get()) + float(valor_2.get())
        texto = f'{valor_1.get()} {operador.get()} {valor_2.get()} = '
        texto += f'{str(resultado)}'
        lbl_resultado.config(text=texto)
    elif operador.get() == '-':
        resultado = float(valor_1.get()) - float(valor_2.get())
        texto = f'{valor_1.get()} {operador.get()} {valor_2.get()} = '
        texto += f'{str(resultado)}'
        lbl_resultado.config(text=texto)
    elif operador.get() == '*':
        resultado = float(valor_1.get()) * float(valor_2.get())
        texto = f'{valor_1.get()} {operador.get()} {valor_2.get()} = '
        texto += f'{str(resultado)}'
        lbl_resultado.config(text=texto)
    elif operador.get() == '/':
        resultado = float(valor_1.get()) / float(valor_2.get())
        texto = f'{valor_1.get()} {operador.get()} {valor_2.get()} = '
        texto += f'{str(resultado)}'
        lbl_resultado.config(text=texto)
    mata_todo_mundo()


# linha 1
lbl_resultado = tk.Label(janela, font=fonte, text='resultado')
lbl_resultado.grid(row=0,column=0, columnspan=5)

# linha 2
ent_tela = tk.Entry(janela, font=fonte)
ent_tela.grid(row=1,column=0, columnspan=5)

# linha 3
btn_7 = tk.Button(janela, font=fonte, text='7')
btn_7.config(command=lambda: joga_na_tela(7))
btn_7.grid(row=2, column=0)
btn_8 = tk.Button(janela, font=fonte, text='8')
btn_8.config(command=lambda: joga_na_tela(8))
btn_8.grid(row=2, column=1)
btn_9 = tk.Button(janela, font=fonte, text='9')
btn_9.config(command=lambda: joga_na_tela(9))
btn_9.grid(row=2, column=2)
btn_div = tk.Button(janela, font=fonte, text='/')
btn_div.config(command=lambda: define_operacao('/'))
btn_div.grid(row=2, column=3)

# linha 4
btn_4 = tk.Button(janela, font=fonte, text='4')
btn_4.config(command=lambda: joga_na_tela(4))
btn_4.grid(row=3, column=0)
btn_5 = tk.Button(janela, font=fonte, text='5')
btn_5.config(command=lambda: joga_na_tela(5))
btn_5.grid(row=3, column=1)
btn_6 = tk.Button(janela, font=fonte, text='6')
btn_6.config(command=lambda: joga_na_tela(6))
btn_6.grid(row=3, column=2)
btn_mul = tk.Button(janela, font=fonte, text='*')
btn_mul.config(command=lambda: define_operacao('*'))
btn_mul.grid(row=3, column=3)

# linha 5
btn_1 = tk.Button(janela, font=fonte, text='1')
btn_1.config(command=lambda: joga_na_tela(1))
btn_1.grid(row=4, column=0)
btn_2 = tk.Button(janela, font=fonte, text='2')
btn_2.config(command=lambda: joga_na_tela(2))
btn_2.grid(row=4, column=1)
btn_3 = tk.Button(janela, font=fonte, text='3')
btn_3.config(command=lambda: joga_na_tela(3))
btn_3.grid(row=4, column=2)
btn_sub = tk.Button(janela, font=fonte, text='-')
btn_sub.config(command=lambda: define_operacao('-'))
btn_sub.grid(row=4, column=3)
btn_enter = tk.Button(janela, font=fonte, text='=')
btn_enter.config(state='disabled')
btn_enter.config(command=calcula)
btn_enter.grid(row=4, column=4, rowspan=2)

# linha 6
btn_0 = tk.Button(janela, font=fonte, text='0')
btn_0.config(command=lambda: joga_na_tela(0))
btn_0.grid(row=5, column=0)
btn_ponto = tk.Button(janela, font=fonte, text='.')
btn_ponto.config(command=lambda: joga_na_tela('.'))
btn_ponto.grid(row=5, column=1)
btn_limpa = tk.Button(janela, font=fonte, text='C')
btn_limpa.config(command=mata_todo_mundo)
btn_limpa.grid(row=5, column=2)
btn_som = tk.Button(janela, font=fonte, text='+')
btn_som.config(command=lambda: define_operacao('+'))
btn_som.grid(row=5, column=3)

janela.mainloop()
