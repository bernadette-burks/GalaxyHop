# calculator.py (logic layer)
# Bernadette Burks
# May 17, 2026

# “How do we calculate things?”

EARTH_GRAVITY = 9.81


def calculate_weight(earth_weight, target_gravity):

    converted_weight = (
        earth_weight / EARTH_GRAVITY
    ) * target_gravity

    return round(converted_weight, 2)


def calculate_jump_height(earth_jump_height, gravity):
    EARTH_GRAVITY = 9.81
    return round((earth_jump_height / EARTH_GRAVITY) * gravity, 2)

def calculate_fall_speed(earth_fall_speed, gravity):
    EARTH_GRAVITY = 9.81
    return round((earth_fall_speed / EARTH_GRAVITY) * gravity, 2)

def calculate_survivability(earth_survivability, gravity):
    EARTH_GRAVITY = 9.81
    return round((earth_survivability / EARTH_GRAVITY) * gravity, 2)

def convert_temperature(earth_temperature, planet):
    if planet == "Mercury":
        return round((earth_temperature - 32) * 5/9 + 100, 2)
    elif planet == "Venus":
        return round((earth_temperature - 32) * 5/9 + 462, 2)
    elif planet == "Mars":
        return round((earth_temperature - 32) * 5/9 - 63, 2)
    elif planet == "Jupiter":
        return round((earth_temperature - 32) * 5/9 - 145, 2)
    elif planet == "Saturn":
        return round((earth_temperature - 32) * 5/9 - 178, 2)
    elif planet == "Uranus":
        return round((earth_temperature - 32) * 5/9 - 224, 2)
    elif planet == "Neptune":
        return round((earth_temperature - 32) * 5/9 - 214, 2)
    elif planet == "Pluto":
        return round((earth_temperature - 32) * 5/9 - 387, 2)
    else:
        return earth_temperature

def calculate_distance_from_sun(earth_distance, planet):
    if planet == "Mercury":
        return round(earth_distance * 0.39, 2)
    elif planet == "Venus":
        return round(earth_distance * 0.72, 2)
    elif planet == "Mars":
        return round(earth_distance * 1.52, 2)
    elif planet == "Jupiter":
        return round(earth_distance * 5.20, 2)
    elif planet == "Saturn":
        return round(earth_distance * 9.58, 2)
    elif planet == "Uranus":
        return round(earth_distance * 19.22, 2)
    elif planet == "Neptune":
        return round(earth_distance * 30.05, 2)
    elif planet == "Pluto":
        return round(earth_distance * 39.48, 2)
    else:
        return earth_distance