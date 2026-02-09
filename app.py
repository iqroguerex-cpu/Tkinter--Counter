import tkinter as tk

x = tk.Tk()
x.title("Roggy's Counter!")
x.geometry("400x300")

c = 0

def increase():
    global c
    c += 1
    counter.config(text=f"Counter: {c}")

def decrease():
    global c
    c -= 1
    counter.config(text=f"Counter: {c}")

counter = tk.Label(x, text="Counter: 0", font=("Arial", 20))
counter.pack(pady=60)

frame = tk.Frame(x)
frame.pack()

button1 = tk.Button(frame, text="Increase", command=increase, font=("Arial", 15))
button1.grid(row=0, column=0, padx=20)

button2 = tk.Button(frame, text="Decrease", command=decrease, font=("Arial", 15))
button2.grid(row=0, column=1, padx=20)

x.mainloop()
