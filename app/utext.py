from tkinter import *
import tkinter as tk
from pypresence import Presence
import time
from tkinter import messagebox as mbox
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename
import os

# > Functions
def SaveFileAs():
	files = [('All Files', '*.*'),
			 ('Text Files', '*.txt')]
	file = asksaveasfile(filetypes = files, defaultextension = files)
	if file is None:
		return
	textsave = str(text.get(1.0,END))
	file.write(textsave)
	window.title(f"U-Text | v0.1 | {file_name}")
	rpc.update(start=int(starttime), details="Working", state=f"Editing {file_name} File") #Editing {file_name} File

def writeToFile(file_name):
	try:
		content = text.get(1.0, 'end')
		with open(file_name, 'w') as fileFin:
			fileFin.write(content)
	except IOError:
		pass
	
def SaveFile():
	global file_name
	if not file_name:
		SaveFileAs()
	else:
		writeToFile(file_name)
		return "break"
		rpc.update(start=int(starttime), details="Working", state=f"Editing {file_name} File") #Editing {file_name} File

def OpenFile():
	files = [('All Files', '*.*'),
			 ('Text Files', '*.txt')]
	selectOpenFile = askopenfilename(defaultextension=files, filetypes=files)
	if selectOpenFile:
		global file_name
		file_name = selectOpenFile
		text.delete(1.0, END)
		with open(selectOpenFile) as namefile:
			text.insert(1.0, namefile.read())
		window.title(f"U-Text | v0.1 | {file_name}")
		rpc.update(start=int(starttime), details="Working", state=f"Editing {file_name} File") #Editing {file_name} File
		print(f"mostrando {file_name}")

def DiscordRPC():
	rpc.connect()
	mbox.showinfo("U-Text | v0.1", "Discord Rich Presence fue activado")
	while True:
		rpc.update(start=int(starttime), details="Working", state=f"Waiting to open or create file") #Editing {file_name} File
		time.sleep(0.1)
		window.update()

def trasparentMode():
	window.wm_attributes("-alpha",0.9)

def transparentModeOff():
	window.wm_attributes("-alpha",1.0)

def spacesTab(arg):
	text.insert(tk.INSERT, " "*4)
	return 'break'

def Help():
	winhelp = Toplevel()
	winhelp.title("U-Text | v0.1 | Find Strings")
	help = """ Tab - Print 4 spaces in text widget.
	"""
	winhelp.wm_attributes("-alpha", 0.9)
	winhelp.resizable(False, False)
	Label(winhelp, text=help, width=50, height=5, bg='gray12', fg='White').pack()
	Button(winhelp, text="Ok",bg='gray12', fg='White', command=winhelp.destroy).pack()
	#winhelp.iconbitmap(r"C:\Users\outby\Desktop\qdtext NF beta\app\img\logo.ico")
	
# > Windows Properties
starttime = time.time()
window = tk.Tk()
window.title("U-Text | v0.1")
window.geometry("642x379")
text = Text(window, wrap=tk.WORD, foreground="White")
text.configure(bg="gray12")
text.config(insertbackground="White")

# > RPC Properties
client_id = "790768262883442698"
rpc = Presence(client_id)

#window.resizable(width=False, height=False)
menubar = Menu(window)

# > Windows Properties > Scrollbar Options
scrollY = tk.Scrollbar(window, orient=tk.VERTICAL)
scrollY.config(command=text.yview)
text.configure(yscrollcommand=scrollY.set)
scrollY.pack(side=tk.RIGHT, fill=tk.Y)

# > Windows Properties > Option Menu Bar
OptionMenu = Menu(menubar, tearoff=0)
OptionMenu.add_command(label="Discord RPC",command=DiscordRPC)
OptionMenu.add_command(label="Enable Transparency", command=trasparentMode)
OptionMenu.add_command(label="Disable Transparency", command=transparentModeOff)
OptionMenu.add_separator()
OptionMenu.add_command(label="Exit",command=window.destroy)
menubar.add_cascade(label="Options", menu=OptionMenu)

# > Windows Properties > File Menu Bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save File As", command=lambda: SaveFileAs())
filemenu.add_command(label="Save File", command=lambda: SaveFile())
filemenu.add_command(label="Open File", command=lambda: OpenFile())
filemenu.add_separator()
filemenu.add_command(label="Help", command=Help)
#filemenu.add_command(label="Find String", command=find)
menubar.add_cascade(label="File", menu=filemenu)
window.config(menu=menubar)

text.pack(expand=YES, fill=BOTH)
window.mainloop()
