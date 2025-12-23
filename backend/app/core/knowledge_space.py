"""
WeaR AI Knowledge - Space, Astronomy & Space Exploration
Pengetahuan tentang luar angkasa dan eksplorasi.
Created by RidTheWann
"""

KNOWLEDGE_SPACE = {
    # ============================================
    # THE SOLAR SYSTEM
    # ============================================
    "solar_system": {
        "category": "Space",
        "definition": "Solar System adalah sistem tata surya kita.",
        "age": "~4.6 billion years",
        "components": ["Sun", "8 planets", "Dwarf planets", "Moons", "Asteroids", "Comets"],
        "location": "Orion Arm of Milky Way Galaxy"
    },
    "sun_star": {
        "category": "Space",
        "definition": "Matahari adalah bintang pusat tata surya.",
        "type": "Yellow dwarf (G-type main sequence)",
        "diameter": "1.4 million km (109 Earths)",
        "composition": "73% Hydrogen, 25% Helium",
        "temperature": "Core: 15 million°C, Surface: 5,500°C",
        "age": "~4.6 billion years (halfway through life)"
    },
    "mercury_planet": {
        "category": "Planet",
        "definition": "Mercury adalah planet terdekat dengan Matahari.",
        "order": 1,
        "moons": 0,
        "day_length": "59 Earth days",
        "year_length": "88 Earth days",
        "facts": "No atmosphere, extreme temperature swings (-180°C to 430°C)"
    },
    "venus_planet": {
        "category": "Planet",
        "definition": "Venus adalah planet terpanas karena greenhouse effect.",
        "order": 2,
        "moons": 0,
        "temperature": "465°C average (hotter than Mercury)",
        "atmosphere": "96% CO2, thick clouds of sulfuric acid",
        "rotation": "Retrograde (spins backwards), 243 Earth days"
    },
    "earth_planet": {
        "category": "Planet",
        "definition": "Bumi adalah satu-satunya planet yang diketahui memiliki kehidupan.",
        "order": 3,
        "moons": 1,
        "age": "~4.54 billion years",
        "atmosphere": "78% N2, 21% O2",
        "water": "71% surface covered in water",
        "distance_sun": "1 AU (~150 million km)"
    },
    "moon": {
        "category": "Space",
        "definition": "Bulan adalah satellite alami Bumi.",
        "diameter": "3,474 km (1/4 Earth)",
        "distance": "384,400 km average",
        "phases": ["New Moon", "Waxing Crescent", "First Quarter", "Full Moon", "Waning"],
        "tides": "Moon's gravity causes ocean tides",
        "humans": "12 people walked on it (Apollo missions)"
    },
    "mars_planet": {
        "category": "Planet",
        "definition": "Mars adalah 'Red Planet' karena iron oxide.",
        "order": 4,
        "moons": ["Phobos", "Deimos"],
        "day_length": "24h 37m (similar to Earth)",
        "year_length": "687 Earth days",
        "features": ["Olympus Mons (largest volcano)", "Valles Marineris (largest canyon)"],
        "exploration": "Multiple rovers (Curiosity, Perseverance)"
    },
    "jupiter_planet": {
        "category": "Planet",
        "definition": "Jupiter adalah planet terbesar di tata surya.",
        "order": 5,
        "type": "Gas giant",
        "moons": "95+ (Ganymede, Europa, Io, Callisto main ones)",
        "great_red_spot": "Storm larger than Earth, 400+ years old",
        "mass": "2.5x all other planets combined"
    },
    "saturn_planet": {
        "category": "Planet",
        "definition": "Saturn terkenal dengan cincin-cincin indahnya.",
        "order": 6,
        "type": "Gas giant",
        "rings": "Made of ice and rock particles",
        "moons": "146 known (Titan largest, has atmosphere)",
        "density": "Less dense than water (would float)"
    },
    "uranus_planet": {
        "category": "Planet",
        "definition": "Uranus adalah ice giant yang berputar sideways.",
        "order": 7,
        "type": "Ice giant",
        "axial_tilt": "98° (rotates on its side)",
        "moons": 27,
        "color": "Blue-green (methane atmosphere)"
    },
    "neptune_planet": {
        "category": "Planet",
        "definition": "Neptune adalah planet terjauh dari Matahari.",
        "order": 8,
        "type": "Ice giant",
        "moons": 16,
        "winds": "Strongest in solar system (2,100 km/h)",
        "discovery": "Found through math before observation (1846)"
    },
    "pluto": {
        "category": "Dwarf Planet",
        "definition": "Pluto adalah dwarf planet di Kuiper Belt.",
        "reclassified": "2006, IAU downgraded from planet",
        "reason": "Hasn't cleared its orbital neighborhood",
        "moons": ["Charon (largest)", "Nix", "Hydra", "Kerberos", "Styx"],
        "new_horizons": "First flyby 2015"
    },
    
    # ============================================
    # STARS & GALAXIES
    # ============================================
    "star_types": {
        "category": "Space",
        "definition": "Klasifikasi bintang berdasarkan spektrum.",
        "types": {
            "O": "Blue, hottest, massive, short-lived",
            "B": "Blue-white, hot",
            "A": "White, bright",
            "F": "Yellow-white",
            "G": "Yellow (like Sun)",
            "K": "Orange",
            "M": "Red, coolest, longest-lived"
        },
        "mnemonic": "Oh Be A Fine Guy/Girl, Kiss Me"
    },
    "star_lifecycle": {
        "category": "Space",
        "definition": "Siklus hidup bintang.",
        "stages": [
            "Nebula (gas cloud)",
            "Protostar",
            "Main sequence (like Sun now)",
            "Red giant/supergiant",
            "Planetary nebula (low mass) or Supernova (high mass)",
            "White dwarf / Neutron star / Black hole"
        ]
    },
    "black_hole": {
        "category": "Space",
        "definition": "Black hole adalah region dengan gravitasi sangat kuat.",
        "types": {
            "Stellar": "From collapsed massive stars",
            "Supermassive": "Center of galaxies (millions/billions of solar masses)",
            "Intermediate": "Medium-sized (rare)"
        },
        "event_horizon": "Point of no return, even light can't escape",
        "first_image": "M87* black hole, 2019 (Event Horizon Telescope)"
    },
    "neutron_star": {
        "category": "Space",
        "definition": "Neutron star adalah collapsed core bintang massif.",
        "density": "1 teaspoon = 6 billion tons",
        "size": "~20 km diameter",
        "pulsar": "Rapidly spinning neutron star emitting radiation beams"
    },
    "supernova": {
        "category": "Space",
        "definition": "Supernova adalah explosive death of massive star.",
        "brightness": "Can outshine entire galaxy briefly",
        "creates": "Heavy elements (gold, silver, uranium)",
        "remnant": "Neutron star or black hole"
    },
    "milky_way": {
        "category": "Space",
        "definition": "Milky Way adalah galaksi kita.",
        "type": "Barred spiral galaxy",
        "diameter": "100,000 light-years",
        "stars": "200-400 billion stars",
        "center": "Supermassive black hole (Sagittarius A*)",
        "our_location": "Orion Arm, ~26,000 ly from center"
    },
    "andromeda": {
        "category": "Space",
        "definition": "Andromeda adalah galaksi spiral terdekat.",
        "distance": "2.5 million light-years",
        "size": "Larger than Milky Way",
        "collision": "Will merge with Milky Way in ~4.5 billion years"
    },
    
    # ============================================
    # SPACE EXPLORATION
    # ============================================
    "nasa": {
        "category": "Space Agency",
        "definition": "NASA adalah space agency Amerika.",
        "founded": "1958",
        "achievements": ["Apollo Moon landings", "Space Shuttle", "ISS", "Mars rovers", "JWST"],
        "headquarters": "Washington D.C.",
        "centers": ["Kennedy (launches)", "JPL (robotics)", "Johnson (human spaceflight)"]
    },
    "spacex": {
        "category": "Space Company",
        "definition": "SpaceX adalah private space company Elon Musk.",
        "founded": "2002",
        "achievements": ["First private company to ISS", "Reusable rockets", "Starlink"],
        "rockets": ["Falcon 9", "Falcon Heavy", "Starship"],
        "goal": "Make humans multiplanetary (Mars)"
    },
    "mars_missions": {
        "category": "Space Exploration",
        "definition": "Misi eksplorasi Mars.",
        "rovers": {
            "Sojourner": "1997, first rover",
            "Spirit & Opportunity": "2004",
            "Curiosity": "2012, still operating",
            "Perseverance": "2021, sample collection"
        },
        "ingenuity": "First helicopter on another planet (2021)"
    },
    "apollo_program": {
        "category": "Space Exploration",
        "definition": "Apollo adalah program NASA yang mendaratkan manusia di Bulan.",
        "apollo_11": "First Moon landing, July 20, 1969",
        "astronauts": "Neil Armstrong (first), Buzz Aldrin (second)",
        "famous_quote": "That's one small step for man, one giant leap for mankind",
        "total_moonwalkers": 12
    },
    "iss": {
        "category": "Space Exploration",
        "definition": "ISS (International Space Station) adalah laboratorium di orbit.",
        "orbit": "408 km above Earth",
        "speed": "27,600 km/h (orbits every 90 minutes)",
        "crew": "Usually 6-7 astronauts",
        "partners": "USA, Russia, Japan, Canada, ESA",
        "construction": "1998-2011"
    },
    "hubble": {
        "category": "Space Exploration",
        "definition": "Hubble Space Telescope adalah iconic space telescope.",
        "launched": "1990",
        "orbit": "547 km above Earth",
        "discoveries": ["Age of universe", "Black holes", "Deep Field images"],
        "successor": "James Webb Space Telescope"
    },
    "jwst": {
        "category": "Space Exploration",
        "definition": "James Webb Space Telescope adalah telescope infrared terbesar.",
        "launched": "December 25, 2021",
        "location": "L2 Lagrange point (1.5 million km from Earth)",
        "mirror": "6.5 meters (vs Hubble's 2.4m)",
        "goal": "Early universe, exoplanets, infrared observation"
    },
    
    # ============================================
    # SPACE CONCEPTS
    # ============================================
    "light_year": {
        "category": "Space",
        "definition": "Light year adalah jarak yang ditempuh cahaya dalam 1 tahun.",
        "distance": "9.46 trillion km",
        "example": "Nearest star (Proxima Centauri) = 4.24 light-years"
    },
    "parsec": {
        "category": "Space",
        "definition": "Parsec adalah unit jarak astronomi.",
        "equals": "3.26 light-years",
        "pop_culture": "Kessel Run in less than 12 parsecs (Star Wars joke)"
    },
    "exoplanet": {
        "category": "Space",
        "definition": "Exoplanet adalah planet di luar tata surya kita.",
        "discovered": "5,500+ confirmed exoplanets",
        "habitable_zone": "Distance where liquid water possible",
        "methods": ["Transit method", "Radial velocity", "Direct imaging"]
    },
    "asteroid": {
        "category": "Space",
        "definition": "Asteroid adalah rocky object yang mengorbit Matahari.",
        "location": "Mostly between Mars and Jupiter (asteroid belt)",
        "largest": "Ceres (now classified as dwarf planet)"
    },
    "comet": {
        "category": "Space",
        "definition": "Comet adalah icy body yang develops tail near Sun.",
        "origin": "Kuiper Belt, Oort Cloud",
        "famous": "Halley's Comet (every 75-79 years)",
        "tail": "Gas and dust pushed by solar wind"
    },
    "rocket_science": {
        "category": "Space",
        "definition": "Dasar-dasar roket.",
        "principle": "Newton's Third Law (action-reaction)",
        "fuel_types": ["Liquid (LOX/LH2)", "Solid", "Hybrid"],
        "stages": "Multiple stages for efficiency"
    },
    "orbital_mechanics": {
        "category": "Space",
        "definition": "Mekanika orbit satelit dan spacecraft.",
        "concepts": {
            "LEO": "Low Earth Orbit (160-2,000 km)",
            "GEO": "Geostationary (35,786 km, stays over same spot)",
            "Escape velocity": "11.2 km/s from Earth",
            "Delta-v": "Change in velocity needed for maneuvers"
        }
    },
    "space_suit": {
        "category": "Space",
        "definition": "Space suit melindungi astronaut di luar spacecraft.",
        "functions": "Oxygen, temperature, pressure, radiation protection",
        "cost": "~$12 million each",
        "weight": "~140 kg on Earth (weightless in space)"
    },
    
    # ============================================
    # EXTRATERRESTRIAL
    # ============================================
    "seti": {
        "category": "Space",
        "definition": "SETI adalah Search for Extraterrestrial Intelligence.",
        "methods": "Radio signals, optical signals",
        "drake_equation": "Estimates number of civilizations",
        "fermi_paradox": "If life is common, where is everybody?"
    },
    "fermi_paradox": {
        "category": "Space",
        "definition": "Fermi Paradox: Contradiction between probability of ET life and lack of evidence.",
        "explanations": [
            "Great Filter (civilizations destroy themselves)",
            "Too far apart",
            "We're not listening correctly",
            "They're avoiding us",
            "We're first/alone"
        ]
    },
    "habitable_zone": {
        "category": "Space",
        "definition": "Habitable zone adalah area di mana air cair mungkin ada.",
        "goldilocks": "Not too hot, not too cold",
        "solar_system": "Venus (edge), Earth (in), Mars (edge)"
    }
}
