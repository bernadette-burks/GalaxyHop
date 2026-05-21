# styles.py (design layer)
# Bernadette Burks
# May 17, 2026
# Centralized design system for the entire application

def get_theme():
    colors = {
        "background": "#f0f0f0",  # light gray
        "accent": "#5503a1",      # purple
        "text": "#333333"         # dark gray
    }
    
    fonts = {
        "primary": ("Helvetica", 12),
        "title": ("Helvetica", 16, "bold")
    }
    
    sizes = {
        "button": (100, 40),
        "spacing": 10
    }
    
    return {
        "window": {
            "background": colors["background"],
            "title": "GalaxyHop",
            "size": (400, 600)
        },
        "colors": colors,
        "fonts": fonts,
        "sizes": sizes,
        "button": {
            "background": colors["accent"],
            "foreground": "white",
            "font": fonts["primary"],
            "width": sizes["button"][0],
            "height": sizes["button"][1]
        },
        "label": {
            "background": colors["background"],
            "foreground": colors["text"],
            "font": fonts["primary"]
        },
        "title": {
            "background": colors["background"],
            "foreground": colors["text"],
            "font": fonts["title"]
        },
        "entry": {
            "background": "white",
            "foreground": colors["text"],
            "font": fonts["primary"]
        },
        "frame": {
            "background": colors["background"]
        },
        "planet_card": {
            "background": "white",
            "foreground": colors["text"],
            "font": fonts["primary"],
            "borderwidth": 1,
            "relief": "solid"
        }
    }


