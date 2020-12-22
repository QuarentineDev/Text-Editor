from tkinter import *
import tkinter as tk
from pypresence import Presence
import time
from tkinter import messagebox as mbox
from tkinter import ttk
from tkinter.filedialog import asksaveasfile

# > Functions
def SaveFileAs():
	files = [('All Files', '*.*'),
			 ('Text Files', '*.txt')]
	file = asksaveasfile(filetypes = files, defaultextension = files)
	if file is None:
		return
	textsave = str(text.get(1.0,END))
	file.write(textsave)

def DiscordRPC():
	client_id = "790768262883442698"
	rpc = Presence(client_id)
	rpc.connect()
	mbox.showinfo("QuarentineDev Text Editor | Beta", "Discord Rich Presence fue activado")
	while True:
		rpc.update(start=int(starttime), details="Working", state="Testing a new project | Unix")
		time.sleep(1)
		window.update()
		print("Discord RPC Funcionando")

# > Windows Properties
starttime = time.time()
window = tk.Tk()
window.title("QuarentineDev Text Editor | Beta")
window.geometry("642x590")
text = Text(window)
text.pack()
window.resizable(width=False, height=False)
menubar = Menu(window)

# > Windows Properties > Option Menu Bar
OptionMenu = Menu(menubar, tearoff=0)
OptionMenu.add_command(label="Discord RPC",command=DiscordRPC)
OptionMenu.add_separator()
OptionMenu.add_command(label="Exit",command=window.quit)
menubar.add_cascade(label="Options", menu=OptionMenu)

# > Windows Properties > File Menu Bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save File As", command=lambda: SaveFileAs())
menubar.add_cascade(label="File", menu=filemenu)
window.config(menu=menubar)

window.mainloop()
