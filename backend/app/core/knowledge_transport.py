"""
WeaR AI Knowledge - Cars, Transportation & Vehicles
Pengetahuan tentang mobil, motor, dan transportasi.
Created by RidTheWann
"""

KNOWLEDGE_TRANSPORT = {
    # ============================================
    # CAR BRANDS
    # ============================================
    "toyota": {
        "category": "Car Brand",
        "definition": "Toyota adalah manufacturer mobil terbesar di dunia.",
        "country": "Japan",
        "founded": "1937",
        "models": ["Camry", "Corolla", "RAV4", "Land Cruiser", "Supra", "Prius"],
        "sub_brands": ["Lexus (luxury)", "Daihatsu", "Hino"]
    },
    "honda": {
        "category": "Car Brand",
        "definition": "Honda adalah manufacturer mobil dan motor dari Jepang.",
        "country": "Japan",
        "founded": "1948",
        "cars": ["Civic", "Accord", "CR-V", "HR-V", "Jazz/Fit"],
        "motorcycles": ["CBR", "CRF", "Beat", "Vario", "PCX"],
        "sub_brand": "Acura (luxury)"
    },
    "bmw": {
        "category": "Car Brand",
        "definition": "BMW (Bayerische Motoren Werke) adalah luxury car manufacturer dari Jerman.",
        "country": "Germany",
        "founded": "1916",
        "series": ["3 Series", "5 Series", "7 Series", "X Series (SUV)", "M Series (performance)"],
        "meaning": "Bayerische Motoren Werke"
    },
    "mercedes_benz": {
        "category": "Car Brand",
        "definition": "Mercedes-Benz adalah luxury car brand legendaris.",
        "country": "Germany",
        "founded": "1926",
        "classes": ["A/B Class", "C Class", "E Class", "S Class (flagship)", "G Class (SUV)", "AMG (performance)"],
        "innovation": "Invented the automobile (Karl Benz, 1886)"
    },
    "ferrari": {
        "category": "Car Brand",
        "definition": "Ferrari adalah supercar manufacturer Italia yang ikonik.",
        "country": "Italy",
        "founded": "1939 by Enzo Ferrari",
        "models": ["488", "SF90", "F8 Tributo", "Roma", "Purosangue (SUV)"],
        "f1": "Most successful F1 constructor"
    },
    "lamborghini": {
        "category": "Car Brand",
        "definition": "Lamborghini adalah supercar manufacturer Italia.",
        "country": "Italy",
        "founded": "1963 by Ferruccio Lamborghini",
        "models": ["Huracán", "Aventador", "Urus (SUV)", "Revuelto"],
        "owner": "Volkswagen Group"
    },
    "porsche": {
        "category": "Car Brand",
        "definition": "Porsche adalah sports car manufacturer Jerman.",
        "country": "Germany",
        "founded": "1931",
        "models": ["911 (iconic)", "Cayenne", "Macan", "Taycan (electric)", "Panamera"],
        "911": "Legendary rear-engine sports car since 1963"
    },
    "tesla_company": {
        "category": "Car Brand",
        "definition": "Tesla adalah pioneer electric vehicle.",
        "country": "USA",
        "founded": "2003",
        "ceo": "Elon Musk",
        "models": ["Model S", "Model 3", "Model X", "Model Y", "Cybertruck"],
        "features": ["Autopilot", "Supercharger network", "OTA updates"]
    },
    "mitsubishi": {
        "category": "Car Brand",
        "definition": "Mitsubishi adalah manufacturer mobil Jepang.",
        "country": "Japan",
        "popular_indonesia": ["Pajero Sport", "Xpander", "Triton", "Outlander"],
        "rally": "Rally legend dengan Lancer Evolution"
    },
    "suzuki": {
        "category": "Car Brand",
        "definition": "Suzuki membuat mobil dan motor.",
        "country": "Japan",
        "cars": ["Swift", "Jimny", "Ertiga", "XL7", "Ignis"],
        "motorcycles": ["GSX", "Satria", "Hayabusa"]
    },
    "hyundai": {
        "category": "Car Brand",
        "definition": "Hyundai adalah manufacturer mobil Korea Selatan terbesar.",
        "country": "South Korea",
        "models": ["Tucson", "Santa Fe", "Creta", "Ioniq (electric)", "Kona"],
        "sub_brand": "Genesis (luxury)"
    },
    "kia": {
        "category": "Car Brand",
        "definition": "Kia adalah manufacturer Korea yang sekarang populer.",
        "country": "South Korea",
        "models": ["Seltos", "Sportage", "Sorento", "EV6"],
        "related": "Part of Hyundai Motor Group"
    },
    
    # ============================================
    # MOTORCYCLES
    # ============================================
    "motorcycle_types": {
        "category": "Motorcycle",
        "definition": "Berbagai jenis motor.",
        "types": {
            "Sport": "Aerodynamic, high performance (CBR, YZF-R)",
            "Cruiser": "Relaxed riding position (Harley)",
            "Naked/Standard": "No fairing (MT, Z series)",
            "Adventure": "On/off road capable (ADV, GS)",
            "Scooter": "Automatic, practical (Vario, PCX)",
            "Trail/Enduro": "Off-road focused (CRF, KLX)"
        }
    },
    "harley_davidson": {
        "category": "Motorcycle",
        "definition": "Harley-Davidson adalah iconic American motorcycle brand.",
        "country": "USA",
        "founded": "1903",
        "style": "Cruiser motorcycles",
        "culture": "Biker culture, HOG (Harley Owners Group)"
    },
    "kawasaki": {
        "category": "Motorcycle",
        "definition": "Kawasaki membuat motor high-performance.",
        "country": "Japan",
        "series": ["Ninja (sport)", "Z (naked)", "Versys (ADV)", "W (retro)"],
        "famous": "Ninja H2 - supercharged motorcycle"
    },
    "yamaha": {
        "category": "Motorcycle",
        "definition": "Yamaha adalah manufacturer motor populer.",
        "country": "Japan",
        "models": ["R1/R6/R15 (sport)", "MT series (naked)", "NMAX/Aerox (scooter)", "WR (trail)"],
        "also_makes": "Musical instruments, audio equipment"
    },
    "ducati": {
        "category": "Motorcycle",
        "definition": "Ducati adalah premium Italian motorcycle brand.",
        "country": "Italy",
        "models": ["Panigale", "Monster", "Multistrada", "Scrambler"],
        "signature": "Desmodromic valve system, L-twin engine"
    },
    
    # ============================================
    # CAR TERMINOLOGY
    # ============================================
    "car_engine_types": {
        "category": "Car Tech",
        "definition": "Berbagai jenis mesin mobil.",
        "types": {
            "Inline-4 (I4)": "4 cylinders in line, common and efficient",
            "V6": "6 cylinders in V shape, balance power/efficiency",
            "V8": "8 cylinders, powerful, American muscle",
            "Boxer/Flat": "Horizontally opposed (Subaru, Porsche)",
            "Electric": "Battery powered, zero emissions",
            "Hybrid": "Combination ICE + electric"
        }
    },
    "transmission_types": {
        "category": "Car Tech",
        "definition": "Jenis transmisi mobil.",
        "types": {
            "Manual": "Driver controls gear with clutch",
            "Automatic": "Gears shift automatically",
            "CVT": "Continuous Variable Transmission, smooth",
            "DCT": "Dual Clutch, fast shifting",
            "AMT": "Automated Manual, affordable auto"
        }
    },
    "drivetrain": {
        "category": "Car Tech",
        "definition": "Sistem penggerak roda mobil.",
        "types": {
            "FWD": "Front Wheel Drive - most common, efficient",
            "RWD": "Rear Wheel Drive - sporty, drifting",
            "AWD": "All Wheel Drive - power to all wheels",
            "4WD": "Four Wheel Drive - off-road focused"
        }
    },
    "forced_induction": {
        "category": "Car Tech",
        "definition": "Cara menambah tenaga mesin.",
        "types": {
            "Turbocharger": "Exhaust-driven compressor, turbo lag",
            "Supercharger": "Belt-driven, instant response",
            "Twin-turbo": "Two turbochargers for more power"
        }
    },
    "suspension": {
        "category": "Car Tech",
        "definition": "Sistem suspensi mobil.",
        "types": {
            "MacPherson strut": "Common, space efficient",
            "Double wishbone": "Better handling, sportier",
            "Multi-link": "Comfort + handling balance",
            "Air suspension": "Adjustable height, luxury"
        }
    },
    
    # ============================================
    # AVIATION
    # ============================================
    "airplane_types": {
        "category": "Aviation",
        "definition": "Jenis-jenis pesawat.",
        "types": {
            "Narrow-body": "Single aisle (Boeing 737, A320)",
            "Wide-body": "Twin aisle (Boeing 777, A380)",
            "Regional jet": "Smaller (Embraer, CRJ)",
            "Private jet": "Business/personal (Gulfstream, Citation)",
            "Cargo": "Freight (747F, MD-11F)"
        }
    },
    "boeing": {
        "category": "Aviation",
        "definition": "Boeing adalah manufacturer pesawat Amerika.",
        "country": "USA",
        "models": ["737 (best seller)", "747 (Jumbo Jet)", "777", "787 Dreamliner"],
        "also": "Defense, space (Starliner)"
    },
    "airbus": {
        "category": "Aviation",
        "definition": "Airbus adalah manufacturer pesawat Eropa.",
        "country": "Europe (multinational)",
        "models": ["A320 (best seller)", "A350", "A380 (largest passenger)"],
        "rivalry": "Main competitor to Boeing"
    },
    "airline_classes": {
        "category": "Aviation",
        "definition": "Kelas penerbangan.",
        "classes": {
            "Economy": "Standard seating, most affordable",
            "Premium Economy": "Extra legroom, better service",
            "Business": "Lie-flat beds, lounge access",
            "First Class": "Suite-like, ultra luxury"
        }
    },
    
    # ============================================
    # SHIPS & MARITIME
    # ============================================
    "ship_types": {
        "category": "Maritime",
        "definition": "Jenis-jenis kapal.",
        "types": {
            "Container ship": "Carries shipping containers",
            "Tanker": "Carries oil, gas, chemicals",
            "Cruise ship": "Passenger vacation vessel",
            "Ferry": "Short-distance passenger/vehicle",
            "Yacht": "Luxury private vessel"
        }
    },
    
    # ============================================
    # TRAINS
    # ============================================
    "train_types": {
        "category": "Rail",
        "definition": "Jenis-jenis kereta.",
        "types": {
            "Commuter": "Short distance, urban/suburban",
            "Intercity": "City to city, medium distance",
            "High-speed rail": "300+ km/h (Shinkansen, TGV)",
            "Freight": "Cargo transport",
            "MRT/LRT": "Urban mass transit"
        }
    },
    "famous_trains": {
        "category": "Rail",
        "definition": "Kereta-kereta terkenal di dunia.",
        "trains": {
            "Shinkansen": "Japan's bullet train, 320 km/h",
            "TGV": "French high-speed, 574.8 km/h record",
            "Orient Express": "Luxury historic train",
            "Trans-Siberian": "Longest railway (Moscow-Vladivostok)"
        }
    },
    "indonesia_rail": {
        "category": "Rail",
        "definition": "Transportasi kereta di Indonesia.",
        "jakarta": ["MRT Jakarta", "LRT Jakarta", "KRL Commuter Line"],
        "intercity": ["Argo Bromo Anggrek", "Taksaka", "Gajayana"],
        "operator": "PT KAI, PT MRT Jakarta, PT LRT Jakarta"
    },
    
    # ============================================
    # TRAFFIC & DRIVING
    # ============================================
    "traffic_lights": {
        "category": "Traffic",
        "definition": "Arti lampu lalu lintas.",
        "colors": {
            "Red": "Stop/Berhenti",
            "Yellow": "Prepare to stop/Hati-hati",
            "Green": "Go/Jalan"
        }
    },
    "road_signs": {
        "category": "Traffic",
        "definition": "Jenis rambu lalu lintas.",
        "types": {
            "Regulatory": "Commands (speed limit, stop, no entry)",
            "Warning": "Cautions (curve, pedestrian, animal)",
            "Guide": "Information (direction, distance, services)"
        }
    },
    "indonesia_license": {
        "category": "Traffic",
        "definition": "Jenis SIM di Indonesia.",
        "types": {
            "SIM A": "Mobil penumpang, jeep, pickup",
            "SIM B1": "Bus, truk (>3500kg)",
            "SIM B2": "Kendaraan trailer",
            "SIM C": "Sepeda motor",
            "SIM D": "Khusus disabilitas"
        }
    },
    
    # ============================================
    # F1 & MOTORSPORT
    # ============================================
    "formula_1": {
        "category": "Motorsport",
        "definition": "Formula 1 adalah puncak motorsport.",
        "teams": ["Red Bull", "Ferrari", "Mercedes", "McLaren", "Aston Martin"],
        "champions": ["Max Verstappen", "Lewis Hamilton", "Sebastian Vettel", "Michael Schumacher"],
        "races": "20+ grand prix per season"
    },
    "motogp": {
        "category": "Motorsport",
        "definition": "MotoGP adalah puncak balap motor.",
        "classes": ["MotoGP (1000cc)", "Moto2 (765cc)", "Moto3 (250cc)"],
        "manufacturers": ["Ducati", "Yamaha", "Honda", "Aprilia", "KTM"],
        "champions": ["Francesco Bagnaia", "Marc Marquez", "Valentino Rossi"]
    },
    "nascar": {
        "category": "Motorsport",
        "definition": "NASCAR adalah stock car racing populer di Amerika.",
        "country": "USA",
        "format": "Oval track racing",
        "famous_race": "Daytona 500"
    },
    "rally": {
        "category": "Motorsport",
        "definition": "Rally adalah balap point-to-point di berbagai terrain.",
        "wrc": "World Rally Championship",
        "legendary": ["Subaru Impreza", "Mitsubishi Lancer Evolution", "Ford Focus RS"]
    },
    
    # ============================================
    # FUTURE TRANSPORT
    # ============================================
    "electric_vehicles": {
        "category": "Future",
        "definition": "Kendaraan listrik semakin populer.",
        "advantages": ["Zero emissions", "Lower running cost", "Quiet", "Instant torque"],
        "challenges": ["Charging infrastructure", "Range anxiety", "Battery cost"],
        "brands": ["Tesla", "BYD", "Rivian", "Lucid", "NIO"]
    },
    "autonomous_vehicles": {
        "category": "Future",
        "definition": "Kendaraan otonom/self-driving.",
        "levels": {
            "Level 0": "No automation",
            "Level 1": "Driver assistance (cruise control)",
            "Level 2": "Partial automation (Tesla Autopilot)",
            "Level 3": "Conditional automation",
            "Level 4": "High automation (limited area)",
            "Level 5": "Full automation (no driver needed)"
        }
    },
    "hyperloop": {
        "category": "Future",
        "definition": "Hyperloop adalah konsep transportasi ultra-cepat.",
        "concept": "Pods in near-vacuum tubes, 1000+ km/h",
        "proposed_by": "Elon Musk (2013)",
        "status": "Still in development/testing"
    }
}
