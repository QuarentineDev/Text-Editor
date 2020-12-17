import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
import os
import tkinter as tk
from tkinter import ttk
import time
from pypresence import Presence
from tkinter import messagebox as mbox

# > Imports terminal actions
init(strip=not sys.stdout.isatty())
cprint(figlet_format("Unix", font="doh"), "white")
time.sleep(1)

"""Notas:
si ingreso informacion mediante un input, no me sirve, ya que estaria funcionando por terminal y no por
ventana.

Sugerencias pronoob: confirmar las dos informaciones a la vez ya que haria el programa mas eficientes:
implementacion:
	crear dos ventanas insert apartes y luego almacenarlas en una variable, luego llamarla en la funcion
	que hace registros de pruebas en la terminal"""


# > Initial options windows
starttime = time.time()
InitWindows = tk.Tk()
InitWindows.title("Unix Logs Register")                            #Window Title
InitWindows.geometry("720x660")                                    #Window Geometry
InitWindows.configure(bg="LightYellow4")                           #Window background color
# > Config information Entry
descriptionLog = ttk.Entry(InitWindows)                            #Requesting information about the description
descriptionLog.place(x=100, y=94)                                  #Geometry of the description request menu (no funciona, aunque por alguna razon necesita de esto para mostrarse en ventana)
titleLog = ttk.Entry(InitWindows)                                  #Requesting information abot the title
titleLog.place(x=50, y=30)                                         #Geometry of the title requesting menu  (no funciona, aunque por alguna razon necesita de esto para mostrarse en ventana)
information = titleLog, descriptionLog                             #storing the information base in a variable
# > Information test 
infoConfirm= ttk.Button(InitWindows, 
	text="Confirmar", command=lambda:print(information.get()))
infoConfirm.place(x=60, y=80)

#pypresence
client = "788978768965271562"
def rpc():
	richpresence = Presence(client)
	richpresence.connect()
	mbox.showinfo("Discord RPC iniciado", "El discord rich presence se inicio de manera correcta")
	while True:
		richpresence.update(start=int(starttime), details="QuarentineDev Test Project", state="Unix log v2")
		time.sleep(1)
		InitWindows.update()
initRPC = tk.Button(text="Iniciar RPC",font=("",30),width=3,height=1,command=rpc)
initRPC.pack()


"""print(richpresence.update(state="Unix Log v2", details="QuarentineDev Test project"))
while True:
	time.sleep(15)"""



InitWindows.mainloop()
