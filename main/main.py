from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkcalendar import DateEntry
from tkinter import messagebox

# Importando as funções que criamos no view.py
from view import * # --- CORES ---
co0 = "#f0f3f5"  # Cinza claro
co1 = "#feffff"  # Branco
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Azul escuro
co4 = "#403d3d"  # Grafite
co6 = "#038cfc"  # Azul vivo

janela = Tk()
janela.title('Controle de Inventário')
janela.geometry('900x600')
janela.configure(background=co0)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use('clam')

# --- FUNÇÕES ---

def adicionar():
    nome = entries['Nome'].get()
    local = entries['Sala/Área'].get()
    descricao = entries['Descrição'].get()
    modelo = entries['Modelo/Marca'].get()
    data = entries['Data Compra'].get()
    valor = entries['Valor Compra'].get()
    serie = entries['Nº de Série'].get()

    lista = [nome, local, descricao, modelo, data, valor, serie]

    if nome == '':
        messagebox.showerror('Erro', 'O nome do item é obrigatório')
    else:
        inserirItem(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        for entrada in entries.values():
            if hasattr(entrada, 'delete'):
                entrada.delete(0, END)
    mostrar()

def deletar():
    try:
        itemSelecionado = tree.selection()
        valores = tree.item(itemSelecionado)['values']
        idItem = valores[0]
        confirmar = messagebox.askyesno('Confirmação', 'Tem certeza que deseja deletar?')
        if confirmar:
            excluirItem(idItem)
            messagebox.showinfo('Sucesso', 'O item foi removido com sucesso')
            mostrar()
    except IndexError:
        messagebox.showerror('Erro', 'Por favor, selecione um item na tabela primeiro')

def carregarDados(event):
    # 1. Verifica se existe alguma seleção na tree
    selecao = tree.selection()
    
    if not selecao:
        return # Se a lista de seleção estiver vazia, sai da função e não faz nada
        
    try:
        # 2. Agora que sabemos que existe algo, pegamos o primeiro item [0]
        itemSelecionado = selecao[0]
        valores = tree.item(itemSelecionado)['values']
        
        # 3. Limpa os campos atuais
        for entrada in entries.values():
            if hasattr(entrada, 'delete'):
                entrada.delete(0, END)
                
        # 4. Preenche os campos com os valores da tabela
        # Importante: Verifique se a ordem dos valores[x] bate com seus campos
        entries['Nome'].insert(0, valores[1])
        entries['Sala/Área'].insert(0, valores[2])
        entries['Descrição'].insert(0, valores[3])
        entries['Modelo/Marca'].insert(0, valores[4])
        # Para DateEntry usamos set_date
        entries['Data Compra'].set_date(valores[5])
        entries['Valor Compra'].insert(0, valores[6])
        entries['Nº de Série'].insert(0, valores[7])

    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

def atualizar():
    try:
        # Precisamos do ID para saber QUAL item atualizar
        itemSelecionado = tree.selection()[0]
        valoresAntigos = tree.item(itemSelecionado)['values']
        idItem = valoresAntigos[0]

        # Coleta os NOVOS dados dos campos
        listaNova = [
            entries['Nome'].get(),
                entries['Sala/Área'].get(),
                entries['Descrição'].get(),
                entries['Modelo/Marca'].get(),
                entries['Data Compra'].get(),
                entries['Valor Compra'].get(),
                entries['Nº de Série'].get(),
                idItem  # O ID deve ser o ÚLTIMO para bater com a query SQL
        ]

        if entries['Nome'].get() == '':
            messagebox.showerror('Erro', 'O nome não pode Estar Vazio')
        else:
            atualizarItem(listaNova)# Função do meu view.py
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados!')
                
            # Limpa e atualiza
            for entrada in entries.values():
                if hasattr(entrada, 'delete'): entrada.delete(0, END)
            mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item na tabela para atualizar')

# --- CONFIGURAÇÃO DE LAYOUT (GRID) ---
janela.grid_columnconfigure(0, weight=1)

# --- FRAMES ---
frameCima = Frame(janela, width=900, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0, sticky=NSEW)

frameMeio = Frame(janela, width=900, height=250, bg=co1, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, sticky=NSEW)

frameBaixo = Frame(janela, width=900, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

# IMPORTANTE: Faz a tabela expandir dentro do frameBaixo
frameBaixo.grid_columnconfigure(0, weight=1)
frameBaixo.grid_rowconfigure(0, weight=1)

# --- LOGO ---
diretorioAtual = os.path.dirname(os.path.abspath(__file__))
try:
    caminhoImagem = os.path.join(diretorioAtual, 'assets', 'logo.png')
    appImage = Image.open(caminhoImagem).resize((40, 40))
    appImage = ImageTk.PhotoImage(appImage)
    appLogo = Label(frameCima, image=appImage, text=' Controle de Inventário', compound='left', 
                    padx=10, anchor='nw', font=('Verdana 15 bold'), bg=co1, fg=co4)
    appLogo.place(x=5, y=5)
except:
    appLogo = Label(frameCima, text=' Controle de Inventário', anchor='nw', font=('Verdana 15 bold'), bg=co1, fg=co4)
    appLogo.place(x=5, y=5)

# --- FORMULÁRIO (Frame Meio) ---
campos = [
    ("Nome", 10), ("Sala/Área", 40), ("Descrição", 70), 
    ("Modelo/Marca", 100), ("Data Compra", 130), 
    ("Valor Compra", 160), ("Nº de Série", 190)
]

entries = {} 

for texto, pos_y in campos:
    Label(frameMeio, text=texto, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4).place(x=10, y=pos_y)
    if texto == "Data Compra":
        entry = DateEntry(frameMeio, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024)
    else:
        entry = Entry(frameMeio, width=30, justify='left', relief='solid')
    entry.place(x=130, y=pos_y)
    entries[texto] = entry

# --- BOTÕES ---
btn_inserir = Button(frameMeio, command=adicionar, text='INSERIR', width=10, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
btn_inserir.place(x=330, y=10)

btn_atualizar = Button(frameMeio, text='ATUALIZAR', width=10, font=('Ivy 8 bold'), bg=co6, fg=co1, relief=RAISED, overrelief=RIDGE)
btn_atualizar = Button(frameMeio, command=atualizar, text='ATUALIZAR', width=10, font=('Ivy 8 bold'), bg=co6, fg=co1, relief=RAISED, overrelief=RIDGE)
btn_atualizar.place(x=330, y=45)

btn_deletar = Button(frameMeio, command=deletar, text='DELETAR', width=10, font=('Ivy 8 bold'), bg="#e06666", fg=co1, relief=RAISED, overrelief=RIDGE)
btn_deletar.place(x=330, y=80)

# --- CARTÕES DE RESUMO ---
Label(frameMeio, text='VALOR TOTAL ITENS', width=25, height=1, anchor=CENTER, font=('Ivy 10 bold'), bg=co3, fg=co1).place(x=550, y=10)
label_total = Label(frameMeio, text='R$ 0,00', width=15, height=1, anchor=CENTER, font=('Ivy 18 bold'), bg=co3, fg=co1)
label_total.place(x=550, y=35)

Label(frameMeio, text='QUANTIDADE TOTAL', width=25, height=1, anchor=CENTER, font=('Ivy 10 bold'), bg=co3, fg=co1).place(x=550, y=90)
label_qtd = Label(frameMeio, text='0', width=15, height=1, anchor=CENTER, font=('Ivy 18 bold'), bg=co3, fg=co1)
label_qtd.place(x=550, y=115)

# --- TABELA (Frame Baixo) ---
def mostrar():
    for item in tree.get_children():
        tree.delete(item)
    
    lista_itens = verItens() 
    total_valor = 0
    for item in lista_itens:
        tree.insert('', 'end', values=item)
        try:
            total_valor += float(item[6]) 
        except: pass
        
    label_total['text'] = f"R$ {total_valor:,.2f}"
    label_qtd['text'] = len(lista_itens)

tabela_head = ['ID', 'Nome', 'Área', 'Descrição', 'Marca', 'Data', 'Valor', 'Série']

# Treeview com sticky='nsew' para ocupar todo o espaço do frameBaixo
tree = ttk.Treeview(frameBaixo, columns=tabela_head, show='headings')
# '<<TreeviewSelect>>' é o evento de clique na linha
tree.bind('<<TreeviewSelect>>', carregarDados)

# Scrollbars posicionadas corretamente no grid
vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)
hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

# Ajustando larguras das colunas para preencher melhor os 900px
# [ID, Nome, Área, Descrição, Marca, Data, Valor, Série]
larguras = [40, 150, 110, 170, 120, 90, 90, 90]
for i, col in enumerate(tabela_head):
    tree.heading(col, text=col, anchor=CENTER)
    tree.column(col, width=larguras[i], anchor=CENTER)

mostrar() 

janela.mainloop()