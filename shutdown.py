import os
import time
import tkinter as tk
from tkinter import messagebox

def schedule_shutdown(hours):
    time_to_wait = hours * 3600  # Converte horas para segundos
    messagebox.showinfo("Agendado", f"Computador será desligado em {hours} horas.")
    root.destroy()
    time.sleep(time_to_wait)
    os.system('shutdown /s /f /t 0')


root = tk.Tk()
root.title("Agendar Desligamento")

tk.Label(root, text="Escolha o tempo para desligar:").pack(pady=10)
tk.Button(root, text="1 Hora", command=lambda: schedule_shutdown(1)).pack(pady=5)
tk.Button(root, text="2 Horas", command=lambda: schedule_shutdown(2)).pack(pady=5)
tk.Button(root, text="3 Horas", command=lambda: schedule_shutdown(3)).pack(pady=5)

root.mainloop()