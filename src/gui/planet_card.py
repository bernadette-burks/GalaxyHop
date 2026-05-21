# planet_card.py (GUI component layer)
# Bernadette Burks
# May 17, 2026

# Reusable GUI component

import tkinter as tk

from numpy.char import title

def create_planet_card(parent, body_data):
        frame = tk.Frame(
        parent,
        bg="white",
        borderwidth=1,
        relief="solid"
    )

        title = tk.Label(
        frame,
        text=body_data["display_name"]
    )

        title.pack()

        frame.pack(pady=10)