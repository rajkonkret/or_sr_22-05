import tkinter as tk


def on_click():
    print("Przycisk został naciśnięty")


app = tk.Tk()
app.title("Przykład 1")
# rozmiar okienka
app.geometry("800x600")
button = tk.Button(app, text="Kliknij mnie!", command=on_click)

button.pack()
app.mainloop()
