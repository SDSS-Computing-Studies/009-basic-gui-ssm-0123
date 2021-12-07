import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("270x150")
window.configure(bg="white")

Dog = tk.PhotoImage(file="dog.png")
input1 = tk.Label(window, image=Dog, bg="white")
input2 = tk.Label(window, text="Pochacco!", bg="white")
input3 = tk.Label(window, bg="cyan",text="A cuddly little puppy! This is from the same\n creators who brought you Keropi and Kero Kero")

input1.grid(row = 1, column = 2, rowspan=3)
input2.grid(row = 2, column = 3)
input3.grid(row = 5, column = 1, columnspan=4)



window.mainloop() 