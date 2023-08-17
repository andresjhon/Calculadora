from tkinter import*

interfaz = Tk()
interfaz.title ("Calculadora")

i=0

#Entrada de interfaz
texto=Entry(interfaz, font=("Calibri 16"))
texto.grid(row=0, column=0,columnspan=4,padx=5, pady=5)

#Funcion de botones
def click_boton (valor):
    global i
    texto.insert(1, valor)
    i+=1
def borrar ():
    texto.delete(0, END)
    i=0
def operaciones():
    ecuacion=texto.get()
    resultado=eval(ecuacion)
    texto.delete(0,END)
    texto.insert(0, resultado)
    i=0

#Configuracion de botones 

boton1=Button(interfaz, text="1", width=5, height=2, command=lambda:click_boton(1))
boton2=Button(interfaz, text="2", width=5, height=2, command=lambda:click_boton(2))
boton3=Button(interfaz, text="3", width=5, height=2, command=lambda:click_boton(3))
boton4=Button(interfaz, text="4", width=5, height=2, command=lambda:click_boton(4))
boton5=Button(interfaz, text="5", width=5, height=2, command=lambda:click_boton(5))
boton6=Button(interfaz, text="6", width=5, height=2, command=lambda:click_boton(6))
boton7=Button(interfaz, text="7", width=5, height=2, command=lambda:click_boton(7))
boton8=Button(interfaz, text="8", width=5, height=2, command=lambda:click_boton(8))
boton9=Button(interfaz, text="9", width=5, height=2, command=lambda:click_boton(9))
boton0=Button(interfaz, text="0", width=13, height=2, command=lambda:click_boton(0))

boton_borrar=Button(interfaz, text="AC", width=5, height=2, command=lambda:borrar())
boton_parentesis1=Button(interfaz, text="(", width=5, height=2, command=lambda:click_boton("("))
boton_parentesis2=Button(interfaz, text=")", width=5, height=2, command=lambda:click_boton(")"))
boton_punto=Button(interfaz, text=".", width=5, height=2, command=lambda:click_boton("."))

boton_division=Button(interfaz, text="/", width=5, height=2, command=lambda:click_boton("/"))
boton_multiplicacion=Button(interfaz, text="x", width=5, height=2, command=lambda:click_boton("*"))
boton_suma=Button(interfaz, text="+", width=5, height=2, command=lambda:click_boton("+"))
boton_resta=Button(interfaz, text="-", width=5, height=2, command=lambda:click_boton("-"))
boton_igual=Button(interfaz, text="=", width=5, height=2, command=lambda:operaciones())

#Mostrar botones en pantalla 

boton_borrar.grid(row= 1, column= 0, padx= 5, pady=5)
boton_parentesis1.grid(row= 1, column= 1, padx= 5, pady=5)
boton_parentesis2.grid(row= 1, column= 2, padx= 5, pady=5)
boton_division.grid(row= 1, column= 3, padx= 5, pady=5)

boton1.grid(row= 2, column= 0, padx= 5, pady=5)
boton2.grid(row= 2, column= 1, padx= 5, pady=5)
boton3.grid(row= 2, column= 2, padx= 5, pady=5)
boton_multiplicacion.grid(row= 2, column= 3, padx= 5, pady=5)

boton4.grid(row= 3, column= 0, padx= 5, pady=5)
boton5.grid(row= 3, column= 1, padx= 5, pady=5)
boton6.grid(row= 3, column= 2, padx= 5, pady=5)
boton_suma.grid(row= 3, column= 3, padx= 5, pady=5)

boton7.grid(row= 4, column= 0, padx= 5, pady=5)
boton8.grid(row= 4, column= 1, padx= 5, pady=5)
boton9.grid(row= 4, column= 2, padx= 5, pady=5)
boton_resta.grid(row= 4, column= 3, padx= 5, pady=5)

boton0.grid(row= 5, column= 0, columnspan=2, padx= 5, pady=5)
boton_punto.grid(row= 5, column= 2, padx= 5, pady=5)
boton_igual.grid(row= 5, column= 3, padx= 5, pady=5)


interfaz.mainloop()