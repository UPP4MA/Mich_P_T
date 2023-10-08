from tkinter import *

ventana = Tk()
ventana.title("Calculadora de Números Complejos")
ventana.configure (background='Thistle')
ventana.geometry('300x450')

i = 0

# Entrada
e_texto = Entry(ventana, font=("sans-serif 20"))
e_texto.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

# Funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def hacer_operacion():
    ecuacion = e_texto.get()
    
    # Reemplazar 'i' con 'k' para números complejos y evaluar
    ecuacion = ecuacion.replace('i', 'k')
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0
#Cambio de color de botones 

import random

def changeBG():
    ventana.config(backgrond = 'green')
    colors =["pink", "yellow", "black", "green", "purple", "red", "gray"]
    random_colors = random.choice(colors)
    ventana.config(background = random_colors)
   
def BACK():
    global i
    i = i-1
    e_texto.delete(i,END)
    
def switchButtonState(): 
   if (boton_ON['text'] == "OFF"):
       boton_ON['text'] = "ON"
   else:
       boton_ON['text'] = 'OFF'

   if  (boton1['state'] == NORMAL ):
       boton1['state'] = DISABLED
   else:
       boton1['state'] = NORMAL
    
   if  (boton2['state'] == NORMAL):
       boton2['state'] = DISABLED
   else:
       boton2['state'] = NORMAL
    
   if (boton3['state'] == NORMAL):
       boton3['state'] =  DISABLED
   else:
       boton3['state'] = NORMAL
    
   if (boton4['state'] == NORMAL):
       boton4['state']== DISABLED
   else:
       boton4['state'] = NORMAL

    
# Botones

boton_ON = Button(ventana, text = "ON", foreground='GREEN', activeforeground='RED',
                  width = 5, height = 2, command = lambda: switchButtonState())


boton1 = Button(ventana, text = "1", width = 5, height = 2, state= DISABLED, command = lambda: click_boton('1'),
                background='LightSalmon', activeforeground='RED') 
boton2 = Button(ventana, text = "2", width = 5, height = 2, state= DISABLED, command = lambda: click_boton('2'),
                background='LightSalmon', activeforeground='RED',)
boton3 = Button(ventana, text = "3", width = 5, height = 2, state= DISABLED,command = lambda: click_boton('3'), 
                background='LightSalmon',  activeforeground='RED')
boton4 = Button(ventana, text = "4", width = 5, height = 2, state= DISABLED, command = lambda: click_boton('4'),
                background='LightSalmon',  activeforeground='RED')
boton5 = Button(ventana, text="5", width=5, height=3, command=lambda: click_boton(5), background='LightSalmon', activeforeground='RED')
boton6 = Button(ventana, text="6", width=5, height=3, command=lambda: click_boton(6), background='LightSalmon', activeforeground='RED')
boton7 = Button(ventana, text="7", width=5, height=3, command=lambda: click_boton(7), background='LightSalmon',  activeforeground='RED')
boton8 = Button(ventana, text="8", width=5, height=3, command=lambda: click_boton(8), background='LightSalmon',  activeforeground='RED')
boton9 = Button(ventana, text="9", width=5, height=3, command=lambda: click_boton(9), background='LightSalmon', activeforeground='RED')
boton0 = Button(ventana, text="0", width=13, height=3, command=lambda: click_boton(0), background='LightSalmon',  activeforeground='RED')

boton_borrar = Button(ventana, text="AC", width=5, height=3, command=lambda: borrar(), background='LightGreen')
boton_parentesis1 = Button(ventana, text="(", width=5, height=3, command=lambda: click_boton("("), background='LightGreen')
boton_parentesis2 = Button(ventana, text=")", width=5, height=3, command=lambda: click_boton(")"), background='LightGreen')
boton_punto = Button(ventana, text=".", width=5, height=3, command=lambda: click_boton("."), background='LightSalmon')

boton_div = Button(ventana, text="/", width=5, height=3, command=lambda: click_boton("/"), background='LightGreen')
boton_mult = Button(ventana, text="x", width=5, height=3, command=lambda: click_boton("*"), background='LightGreen')
boton_sum = Button(ventana, text="+", width=5, height=3, command=lambda: click_boton("+"), background='LightGreen')
boton_rest = Button(ventana, text="-", width=5, height=3, command=lambda: click_boton("-"), background='LightGreen')
boton_igual = Button(ventana, text="=", width=5, height=3, command=lambda: hacer_operacion(), background='LightGreen')
boton_Back = Button(ventana, text = "<-", width = 5, height = 2,command = lambda: BACK(), background='LightGreen')


# Botón 'k' para la unidad imaginaria
boton_k = Button(ventana, text="k", width=5, height=3, command=lambda: click_boton("k"), background='LightGreen')

# Agregar botones en pantalla
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_sum.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_rest.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_k.grid(row=5, column=3, padx=5, pady=5)
boton_igual.grid(row=6, column=0, columnspan=2, padx=5, pady=5 )
boton_Back.grid(row = 6, column= 3, columnspan=2,padx= 5, pady = 5)
boton_ON.grid(row = 6, column=2, padx=5, pady=5)


ventana.mainloop()