import random
import tkinter as tk

def roll_dice():
    """Roll the dice and update the label."""
    result = random.choice([1, 2, 3, 4, 5, 6])
    dice_label.config(text=str(result))

root = tk.Tk()
root.title("Dice")
root.configure(bg="white")

dice_label = tk.Label(root, text="", width=4, height=2, font=("Helvetica", 48), bg="red", fg="white")
dice_label.pack(pady=20)

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Helvetica", 16), bg="blue", fg="white")
roll_button.pack()

root.mainloop()