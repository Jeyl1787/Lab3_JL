import tkinter as tk


root = tk.Tk()
HEIGHT = 800
WIDTH = 800

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame =tk.Frame(root, bg='gray', bd=2)
frame.place()

entry = tk.Entry(frame, bg='gray')
entry.place(relx= 0.15, rely=0, relwidth =1, relheight=0.15)

button = tk.Button(root, text=">>", bg="black", fg="white")
button.pack(side ='right')
button = tk.Button(root, text="P", bg="black", fg="white")
button.pack(side ='right')
button = tk.Button(root, text="OpenFile", bg="black", fg="white")
button.pack()

root.mainloop()
