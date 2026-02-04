#Tkinter
from tkinter import *
from tkinter import Tk,StringVar, ttk
#Pillow
from PIL import Image,ImageTk
#Organizar as pastas da imagem
import os
#tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# Cores (Estilo Profissional)
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # Branca
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#e06666"  # Vermelho
co6 = "#038cfc"  # Azul
co9 = "#e9edf5"  # Sky Blue

#-------------Criando a Janela----------------
janela = Tk()
janela.title('Controle de inventario')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)

#--------------------FRAMES-------------------------------
# Use 'Frame' (padrão) em vez de 'ttk.Frame' para conseguir usar o 'bg'
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=303, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

#--------------------ABRINDO IMG-----------------------------
diretorioAtual = os.path.dirname(os.path.abspath(__file__))
caminhoImagem = os.path.join(diretorioAtual,'assets', 'logo.png')

appImage = Image.open(caminhoImagem)
appImage = appImage.resize((55,55))
appImage = ImageTk.PhotoImage(appImage)
#-------------------------------------------------------------

#Customização frame cima
appLogo = Label(
    frameCima,
    image=appImage,
    text='Controle de Inventário',
    width=900,
    compound='left',
    padx=5,
    relief='raised',
    anchor='nw',
    font=('Verdana 20 bold'),
    bg= co1
)

appLogo.place(x=0,y=0)

#Customização frame meio
#criando entradas

labelNome = Label(frameMeio,text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1, fg=co4)
labelNome.place(x=10, y=10)
entryName = Entry(frameMeio, width=30, justify='left',relief='solid')
entryName.place(x=130, y=11)

#--------------------------------------------------------------------------------------

labelArea = Label(frameMeio,text='Sala/Área', height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1, fg=co4)
labelArea.place(x=10, y=40)
entryArea = Entry(frameMeio, width=30, justify='left',relief='solid')
entryArea.place(x=130, y=41)

#--------------------------------------------------------------------------------------

labelDescricao = Label(frameMeio,text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1, fg=co4)
labelDescricao.place(x=10, y=70)
entryDescricao = Entry(frameMeio, width=30, justify='left',relief='solid')
entryDescricao.place(x=130, y=71)

#--------------------------------------------------------------------------------------

labelModelo = Label(frameMeio,text='Modelo/Marca', height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1, fg=co4)
labelModelo.place(x=10, y=100)
entryModelo = Entry(frameMeio, width=30, justify='left',relief='solid')
entryModelo.place(x=130, y=101)

#--------------------------------------------------------------------------------------
labelData = Label(frameMeio,text='Data da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1, fg=co4)
labelData.place(x=10, y=130)
entryData = DateEntry(frameMeio, width=27, justify='left',relief='solid')
entryData.place(x=130, y=131)

#--------------------------------------------------------------------------------------

labelCompra = Label(frameMeio,text='Valor da Compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1, fg=co4)
labelCompra.place(x=10, y=160)
entryCompra = Entry(frameMeio, width=30, justify='left',relief='solid')
entryCompra.place(x=130, y=161)

#--------------------------------------------------------------------------------------

labelSerie = Label(frameMeio,text='Número de Série', height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1, fg=co4)
labelSerie.place(x=10, y=190)
entrySerie = Entry(frameMeio, width=30, justify='left',relief='solid')
entrySerie.place(x=130, y=191)

#--------------------------------------------------------------------------------------

labelImagem = Label(frameMeio,text='Imagem do Item', height=1, anchor=NW, font=('Ivy 10 bold'), bg= co1, fg=co4)
labelImagem.place(x=10, y=220)

#-----------------------------------Criando Botoes---------------------------------------------------

buttonCarregar = Button(frameMeio,width=22,overrelief=RIDGE,text='carregar',anchor=CENTER, font=('Ivy 10'), bg= co9, compound=CENTER)
buttonCarregar.place(x=130, y=221)


#---------------------------------------------------
style.theme_use('clam')

janela.mainloop()


