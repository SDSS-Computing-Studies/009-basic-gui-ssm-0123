import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("270x150")
window.configure(bg="white")

Dog = tk.PhotoImage(file="dog.png")
input1 = tk.Label(window, image=Dog, bg="white")
input2 = tk.Label(window, text="Pochacco!", bg="white")
input3 = tk.Label(window, bg="cyan",text="A cuddly little puppy! This is from the same\n creators who brought you Keropi and Kero Kero")

input1.place(x=60, y=10)
input2.place(x=130, y=0)
input3.place(x=0, y=110)



window.mainloop()