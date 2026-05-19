# planets.py (database layer)
# Bernadette Burks
# May 17, 2026

CELESTIAL_BODIES = {
    "mars": {
        "category": "planet",

        "physics": {
            "gravity": 3.71
        },

        "environment": {
            "temperature": -63,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/mars.jpg",
            "3d_model_path": "assets/3d/mars.glb"
        },

        "fun_fact": "Mars has the largest volcano in the solar system.",
        "display_name": "Mars",
    },

        "venus": {
            "category": "planet",

            "physics": {
                "gravity": 8.87
            },

        "environment": {
            "temperature": 464,
            "atmosphere": "Thick",
            "survivability_score": 0
            },

        "media": {
            "image_path": "assets/images/venus.jpg",
            "3d_model_path": "assets/3d/venus.glb"
            },

        "fun_fact": "Venus is the hottest planet in the solar system.",
        "display_name": "Venus",
    },

    "jupiter": {
        "category": "planet",
        
        "physics": {
            "gravity": 24.79
        },

        "environment": {
            "temperature": -108,
            "atmosphere": "Thick",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/jupiter.jpg",
            "3d_model_path": "assets/3d/jupiter.glb"
        },

        "fun_fact": "Jupiter is the largest planet in the solar system.",
        "display_name": "Jupiter",
    },

    "saturn": {
        "category": "planet",
        
        "physics": {
            "gravity": 10.44
        },

        "environment": {
            "temperature": -139,
            "atmosphere": "Thick",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/saturn.jpg",
            "3d_model_path": "assets/3d/saturn.glb"
        },

        "fun_fact": "Saturn is known for its prominent ring system.",
        "display_name": "Saturn",
    },

    "uranus": {
        "category": "planet",
    
        "physics": {
            "gravity": 8.69
        },

    "environment": {
        "temperature": -197,
        "atmosphere": "Thick",
        "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/uranus.jpg",
            "3d_model_path": "assets/3d/uranus.glb"
        },

        "fun_fact": "Uranus rotates on its side.",
        "display_name": "Uranus",
    },

    "neptune": {
        "category": "planet",
        
        "physics": {
            "gravity": 11.15
        },

        "environment": {
            "temperature": -201,
            "atmosphere": "Thick",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/neptune.jpg",
            "3d_model_path": "assets/3d/neptune.glb"
        },

        "fun_fact": "Neptune has the strongest winds in the solar system.",
        "display_name": "Neptune",
    },

    "pluto": {
        "category": "dwarf planet",
        
        "physics": {
            "gravity": 0.62
        },

        "environment": {
            "temperature": -229,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/pluto.jpg",
            "3d_model_path": "assets/3d/pluto.glb"
        },

        "fun_fact": "Pluto is classified as a dwarf planet.",
        "display_name": "Pluto",
    },

    "mercury": {
        "category": "planet",
    
        "physics": {
            "gravity": 3.7
        },

        "environment": {
            "temperature": 167,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/mercury.jpg",
            "3d_model_path": "assets/3d/mercury.glb"
        },

        "fun_fact": "Mercury is the closest planet to the Sun.",
        "display_name": "Mercury",
    },

    "earth": {
        "category": "planet",
    
        "physics": {
            "gravity": 9.81
        },

        "environment": {
            "temperature": 15,
            "atmosphere": "Breathable",
            "survivability_score": 100
        },

        "media": {
            "image_path": "assets/images/earth.jpg",
            "3d_model_path": "assets/3d/earth.glb"
        },

        "fun_fact": "Earth is the only planet known to support life.",
        "display_name": "Earth",
    },

    "moon": {
        "category": "moon",
    
        "physics": {
            "gravity": 1.62
        },

        "environment": {
            "temperature": -53,
            "atmosphere": "None",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/moon.jpg",
            "3d_model_path": "assets/3d/moon.glb"
        },

        "fun_fact": "The Moon is Earth's only natural satellite.",
        "display_name": "Moon",
    },

    "phobos": {
        "category": "moon",
    
        "physics": {
            "gravity": 0.0057
        },

        "environment": {
            "temperature": -40,
            "atmosphere": "None",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/phobos.jpg",
            "3d_model_path": "assets/3d/phobos.glb"
        },

        "fun_fact": "Phobos is one of Mars' moons.",
        "display_name": "Phobos",
    },

    "deimos": {
        "category": "moon",
    
        "physics": {
            "gravity": 0.003
        },

        "environment": {
            "temperature": -40,
            "atmosphere": "None",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/deimos.jpg",
            "3d_model_path": "assets/3d/deimos.glb"
        },

        "fun_fact": "Deimos is one of Mars' moons.",
        "display_name": "Deimos",
    },

    "europa": {
        "category": "moon",
    
        "physics": {
            "gravity": 1.315
        },

        "environment": {
            "temperature": -160,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/europa.jpg",
            "3d_model_path": "assets/3d/europa.glb"
        },

        "fun_fact": "Europa is one of Jupiter's moons.",
        "display_name": "Europa",
    },

    "ganymede": {
        "category": "moon",
    
        "physics": {
            "gravity": 1.428
        },

        "environment": {
            "temperature": -160,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/ganymede.jpg",
            "3d_model_path": "assets/3d/ganymede.glb"
        },

        "fun_fact": "Ganymede is the largest moon of Jupiter.",
        "display_name": "Ganymede",
    },

    "callisto": {
        "category": "moon",
    
        "physics": {
            "gravity": 1.235
        },

        "environment": {
            "temperature": -139,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/callisto.jpg",
            "3d_model_path": "assets/3d/callisto.glb"
        },

        "fun_fact": "Callisto is one of Jupiter's moons.",
        "display_name": "Callisto",
    },

    "titan": {
        "category": "moon",
    
        "physics": {
            "gravity": 1.352
        },

        "environment": {
            "temperature": -179,
            "atmosphere": "Thick",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/titan.jpg",
            "3d_model_path": "assets/3d/titan.glb"
        },

        "fun_fact": "Titan is the largest moon of Saturn.",
        "display_name": "Titan",
    },

    "enceladus": {
        "category": "moon",
    
        "physics": {
            "gravity": 0.113
        },

        "environment": {
            "temperature": -198,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/enceladus.jpg",
            "3d_model_path": "assets/3d/enceladus.glb"
        },

        "fun_fact": "Enceladus is one of Saturn's moons.",
        "display_name": "Enceladus",
    },

    "mimas": {
        "category": "moon",
    
        "physics": {
            "gravity": 0.064
        },

        "environment": {
            "temperature": -201,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/mimas.jpg",
            "3d_model_path": "assets/3d/mimas.glb"
        },

        "fun_fact": "Mimas is one of Saturn's moons.",
        "display_name": "Mimas",
    },

    "iapetus": {
        "category": "moon",
    
        "physics": {
            "gravity": 0.223
        },

        "environment": {
            "temperature": -201,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/iapetus.jpg",
            "3d_model_path": "assets/3d/iapetus.glb"
        },

        "fun_fact": "Iapetus is one of Saturn's moons.",
        "display_name": "Iapetus",
    },

    "rhea": {
        "category": "moon",
    
        "physics": {
            "gravity": 0.264
        },

        "environment": {
            "temperature": -174,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/rhea.jpg",
            "3d_model_path": "assets/3d/rhea.glb"
        },

        "fun_fact": "Rhea is one of Saturn's moons.",
        "display_name": "Rhea",
    },

    "dione": {
        "category": "moon",
    
        "physics": {
            "gravity": 0.232
        },

        "environment": {
            "temperature": -188,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/dione.jpg",
            "3d_model_path": "assets/3d/dione.glb"
        },

        "fun_fact": "Dione is one of Saturn's moons.",
        "display_name": "Dione",
    },

    "tethys": {
        "category": "moon",
    
        "physics": {
            "gravity": 0.146
        },

        "environment": {
            "temperature": -187,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/tethys.jpg",
            "3d_model_path": "assets/3d/tethys.glb"
        },

        "fun_fact": "Tethys is one of Saturn's moons.",
        "display_name": "Tethys",
    },

    "hyperion": {
        "category": "moon",
    
        "physics": {
            "gravity": 0.077
        },

        "environment": {
            "temperature": -183,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/hyperion.jpg",
            "3d_model_path": "assets/3d/hyperion.glb"
        },

        "fun_fact": "Hyperion is one of Saturn's moons.",
        "display_name": "Hyperion",
    },

    "phoebe": {
        "category": "moon",
        
        "physics": {
            "gravity": 0.059
        },

        "environment": {
            "temperature": -220,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/phoebe.jpg",
            "3d_model_path": "assets/3d/phoebe.glb"
        },

        "fun_fact": "Phoebe is one of Saturn's moons.",
        "display_name": "Phoebe",
    },

    "charon": {
        "category": "moon",
        
        "physics": {
            "gravity": 0.288
        },

        "environment": {
            "temperature": -220,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/charon.jpg",
            "3d_model_path": "assets/3d/charon.glb"
        },

        "fun_fact": "Charon is the largest moon of Pluto.",
        "display_name": "Charon",
    },

    "ceres": {
        "category": "asteroid",
        
        "physics": {
            "gravity": 0.27
        },

        "environment": {
            "temperature": -105,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/ceres.jpg",
            "3d_model_path": "assets/3d/ceres.glb"
        },

        "fun_fact": "Ceres is the largest object in the asteroid belt.",
        "display_name": "Ceres",
    },

    "vesta": {
        "category": "asteroid",
        
        "physics": {
            "gravity": 0.25
        },

        "environment": {
            "temperature": -20,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/vesta.jpg",
            "3d_model_path": "assets/3d/vesta.glb"
        },

        "fun_fact": "Vesta is one of the largest objects in the asteroid belt.",
        "display_name": "Vesta",
    },

    "pallas": {
        "category": "asteroid",
        
        "physics": {
            "gravity": 0.22
        },

        "environment": {
            "temperature": -40,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/pallas.jpg",
            "3d_model_path": "assets/3d/pallas.glb"
        },

        "fun_fact": "Pallas is one of the largest objects in the asteroid belt.",
        "display_name": "Pallas",
    },

    "hygiea": {
        "category": "asteroid",
        
        "physics": {
            "gravity": 0.14
        },

        "environment": {
            "temperature": -40,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/hygiea.jpg",
            "3d_model_path": "assets/3d/hygiea.glb"
        },

        "fun_fact": "Hygiea is one of the largest objects in the asteroid belt.",
        "display_name": "Hygiea",
    },

    "eris": {
        "category": "dwarf planet",
        
        "physics": {
            "gravity": 0.082
        },

        "environment": {
            "temperature": -231,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/eris.jpg",
            "3d_model_path": "assets/3d/eris.glb"
        },

        "fun_fact": "Eris is one of the largest dwarf planets in the Solar System.",
        "display_name": "Eris",
    },

    "makemake": {
        "category": "dwarf planet",
        
        "physics": {
            "gravity": 0.103
        },

        "environment": {
            "temperature": -239,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/makemake.jpg",
            "3d_model_path": "assets/3d/makemake.glb"
        },

        "fun_fact": "Makemake is one of the largest dwarf planets in the Solar System.",
        "display_name": "Makemake",
    },

    "haumea": {
        "category": "dwarf planet",
        
        "physics": {
            "gravity": 0.44
        },

        "environment": {
            "temperature": -241,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/haumea.jpg",
            "3d_model_path": "assets/3d/haumea.glb"
        },

        "fun_fact": "Haumea is one of the largest dwarf planets in the Solar System.",
        "display_name": "Haumea",
    },

    "gonggong": {
        "category": "dwarf planet",
        
        "physics": {
            "gravity": 0.11
        },

        "environment": {
            "temperature": -220,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/gonggong.jpg",
            "3d_model_path": "assets/3d/gonggong.glb"
        },

        "fun_fact": "Gonggong is one of the largest dwarf planets in the Solar System.",
        "display_name": "Gonggong",
    },

    "quaoar": {
        "category": "dwarf planet",
        
        "physics": {
            "gravity": 0.12
        },

        "environment": {
            "temperature": -210,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/quaoar.jpg",
            "3d_model_path": "assets/3d/quaoar.glb"
        },

        "fun_fact": "Quaoar is one of the largest dwarf planets in the Solar System.",
        "display_name": "Quaoar",
    },

    "sedna": {
        "category": "dwarf planet",
        
        "physics": {
            "gravity": 0.14
        },

        "environment": {
            "temperature": -240,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/sedna.jpg",
            "3d_model_path": "assets/3d/sedna.glb"
        },

        "fun_fact": "Sedna is one of the largest dwarf planets in the Solar System.",
        "display_name": "Sedna",
    },

    "orcus": {
        "category": "dwarf planet",
        
        "physics": {
            "gravity": 0.23
        },

        "environment": {
            "temperature": -220,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/orcus.jpg",
            "3d_model_path": "assets/3d/orcus.glb"
        },

        "fun_fact": "Orcus is one of the largest dwarf planets in the Solar System.",
        "display_name": "Orcus",
    },

    "salacia": {
        "category": "dwarf planet",
        
        "physics": {
            "gravity": 0.29
        },

        "environment": {
            "temperature": -220,
            "atmosphere": "Thin",
            "survivability_score": 0
        },

        "media": {
            "image_path": "assets/images/salacia.jpg",
            "3d_model_path": "assets/3d/salacia.glb"
        },

        "fun_fact": "Salacia is one of the largest dwarf planets in the Solar System.",
        "display_name": "Salacia",
    }
}

print(f"There are currently {len("planets")} planets, {len("moons")} moons, {len("asteroids")} asteroids, and {len("dwarf_planets")} dwarf planets in the database.")

# Data Resources:
# https://nssdc.gsfc.nasa.gov/planetary/factsheet/
# https://en.wikipedia.org/wiki/List_of_gravitational_accelerations_on_planets
# https://en.wikipedia.org/wiki/Surface_gravity
# https://en.wikipedia.org/wiki/Temperature_of_planets_in_the_Solar_System
# https://en.wikipedia.org/wiki/Atmosphere_of_planets
# https://en.wikipedia.org/wiki/Survivability_of_planets