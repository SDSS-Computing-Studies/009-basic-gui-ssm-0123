import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("400x30")

input1 = tk.Entry(window, width = 20)
x = tk.Label(window, text=" x ")
input2 = tk.Entry(window, width = 20)
equal = tk.Label(window, text="=", relief= "groove")
output = tk.Label(window, text = "", width = 20, relief="groove",borderwidth=1, background="white")


input1.grid(row = 1, column = 1)
x.grid(row = 1, column = 2)
input2.grid(row = 1, column = 3)
equal.grid(row = 1, column = 4)
output.grid(row = 1, column= 5)

window.mainloop()