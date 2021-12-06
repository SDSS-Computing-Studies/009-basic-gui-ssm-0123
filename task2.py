import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("750x200")
window.configure(bg="white")

Dog = tk.PhotoImage(file="dog.png")

inputName = tk.Entry(window, width = 20)
inputType = tk.Entry(window, width = 20)
inputBreed = tk.Entry(window, width = 20)
inputOwner = tk.Entry(window, width = 20)
inputBirth = tk.Entry(window, width = 20)
inputSearchname = tk.Entry(window, width = 20)

LabelName = tk.Label(window, width=20, text="Name", background="white")
LabelType = tk.Label(window, width=20, text="Type", background="white")
LabelBreed = tk.Label(window, width=20, text="Breed", background="white")
LabelOwner = tk.Label(window, width=20, text="Owner", background="white")
LabelBirth = tk.Label(window, width=20, text="Birthdate", background="white")
LabelClient = tk.Label(window, width=20, text="Client Database", background="white")
LabelDog = tk.Label(window, image=Dog, background="white")

Prebutton = tk.Button(window, text="< Previous")
Nexbutton = tk.Button(window, text="Next >")
Savebutton = tk.Button(window, text="Save Entry")
LabelSearchname = tk.Button(window, text="Search by Name")



#grid
LabelDog.grid(row=1, column=1, rowspan=3)
LabelSearchname.grid(row=1, column=4)
inputSearchname.grid(row=1, column=5)



LabelClient.grid(row=2, column=3)



LabelName.grid(row=4, column=1)
LabelType.grid(row=4, column=2)
LabelBreed.grid(row=4, column=3)
LabelOwner.grid(row=4, column=4)
LabelBirth.grid(row=4, column=5)


inputName.grid(row=5, column=1)
inputType.grid(row=5, column=2)
inputBreed.grid(row=5, column=3)
inputOwner.grid(row=5, column=4)
inputBirth.grid(row=5, column=5)

Prebutton.grid(row=6, column=1)
Savebutton.grid(row=6, column=3)
Nexbutton.grid(row=6, column=5)



window.mainloop()