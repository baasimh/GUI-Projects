import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("tkinter Form")
root.geometry("500x300")
lblFrPerson = tk.LabelFrame(root, text="Personal Information", padx=10, pady=10)
lblFrPerson.pack(padx=10, pady=10, fill="x")
lblFirst = tk.Label(
    lblFrPerson,
    text="First Name:",
    bg="blue",
    fg="white"
)
lblFirst.grid(column=0, row=0, sticky="e", padx=5, pady=5)
entFirst = tk.Entry(lblFrPerson)
entFirst.grid(column=1, row=0, padx=5, pady=5)
lblLast = tk.Label(lblFrPerson, text="Last Name:", bg="blue", fg="white")
lblLast.grid(column=0, row=1, sticky="e", padx=5, pady=5)

entLast = tk.Entry(lblFrPerson)
entLast.grid(column=1, row=1, padx=5, pady=5)
lblEmail = tk.Label(lblFrPerson, text="Email:")
lblEmail.grid(column=0, row=2, sticky="e", padx=5, pady=5)

entEmail = tk.Entry(lblFrPerson)
entEmail.grid(column=1, row=2, padx=5, pady=5)
lblPhone = tk.Label(lblFrPerson, text="Phone:")
lblPhone.grid(column=0, row=3, sticky="e", padx=5, pady=5)

entPhone = tk.Entry(lblFrPerson)
entPhone.grid(column=1, row=3, padx=5, pady=5)
fraButtons = tk.Frame(root)
fraButtons.pack(pady=10)
def displayData():
    first = entFirst.get()
    last = entLast.get()
    email = entEmail.get()
    phone = entPhone.get()

    output = (
        f"First Name: {first}\n"
        f"Last Name: {last}\n"
        f"Email: {email}\n"
        f"Phone: {phone}"
    )

    messagebox.showinfo("Submitted Information", output)
btnS = tk.Button(
    fraButtons,
    text="Submit",
    width=5,
    command=displayData
)
btnS.pack(side=tk.LEFT, padx=5)
def clear():
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)
btnR = tk.Button(
    fraButtons,
    text="Reset",
    width=5,
    command=clear
)
btnR.pack(side=tk.LEFT, padx=5)
btnQ = tk.Button(
    fraButtons,
    text="Quit",
    width=5,
    command=root.destroy
)
btnQ.pack(side=tk.LEFT, padx=5)
root.mainloop()
