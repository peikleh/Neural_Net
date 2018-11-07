from tkinter import Tk, Label, Button
import os, binascii
class MyFirstGUI:
	def __init__(self, master):
		self.rand = binascii.b2a_hex(os.urandom(3))
		rand_col = "#" + self.rand.decode()
		
		self.f = open("training.txt", "a")
		self.master = master
		master.title("A simple GUI")

		self.label = Label(master, text="Creating training data")
		self.label.pack()

		self.dark_button = Button(master, text="Dark is a mysterious thing", command=self.dark_text, height = 20, width = 60, background = rand_col)
		self.dark_button.pack()

		self.light_button = Button(master, text="Light is a mysterious thing", fg = 'white', command=self.light_text, height = 20, width = 60, background = rand_col)
		self.light_button.pack()

	def dark_text(self):
		raw_col = int(self.rand.decode(),16)
		print(self.rand)
		self.f.write(str(raw_col) + ',' + 'd\n')
		
		self.rand = binascii.b2a_hex(os.urandom(3))
		rand_col = "#" + self.rand.decode()
		
		self.dark_button.configure(background = rand_col)
		self.light_button.configure(background = rand_col)
	
		
	def light_text(self):
		raw_col = int(self.rand.decode(),16)
		print(self.rand)
		self.f.write(str(raw_col) + ',' + 'l\n')
		
		self.rand = binascii.b2a_hex(os.urandom(3))
		rand_col = "#" + self.rand.decode()
		
		self.dark_button.configure(background = rand_col)
		self.light_button.configure(background = rand_col)
		
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()