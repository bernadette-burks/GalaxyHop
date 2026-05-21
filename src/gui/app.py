# app.py (GUI controller layer)
# Bernadette Burks
# May 17, 2026

import tkinter as tk
from src.data.planets import CELESTIAL_BODIES
from src.gui.planet_card import create_planet_card
from src.gui.styles import get_theme

def run_app():
    root = tk.Tk()
    
    root.title("GalaxyHop")
    
    styles = get_theme()
    
    # Configure root window background
    root.configure(background=styles["window"]["background"])
    
    # Pack a welcome label
    label = tk.Label(
        root, 
        text="Welcome to GalaxyHop!", 
        background=styles["window"]["background"], 
        foreground=styles["colors"]["text"], 
        font=styles["fonts"]["title"]
    )
    label.pack()
    
    subtitle = tk.Label(
        root, 
        text="The developer is still building the app, but feel free to explore in-progress features while you wait...⏳", 
        background=styles["window"]["background"], 
        foreground=styles["colors"]["text"], 
        font=styles["fonts"]["primary"]
    )
    subtitle.pack(pady=10)
    
    # Generate planet cards from CELESTIAL_BODIES dictionary
    for body_name, body_data in CELESTIAL_BODIES.items():
        create_planet_card(root, body_data)
        
    root.geometry("800x600")

    print("App is launching in a new window...")

    root.mainloop()
