"""
WeaR AI Knowledge - Food, Cooking, Recipes & Culinary Arts
Pengetahuan tentang makanan, masak-memasak, dan kuliner.
Created by RidTheWann
"""

KNOWLEDGE_CULINARY = {
    # ============================================
    # INDONESIAN FOOD
    # ============================================
    "nasi_goreng": {
        "category": "Indonesian Food",
        "definition": "Nasi goreng adalah fried rice ala Indonesia.",
        "ingredients": ["Nasi", "Kecap manis", "Bawang putih", "Bawang merah", "Cabai", "Telur"],
        "variations": ["Nasi goreng kampung", "Nasi goreng seafood", "Nasi goreng petai"],
        "tip": "Nasi dingin (overnight) lebih baik untuk nasi goreng"
    },
    "mie_goreng": {
        "category": "Indonesian Food",
        "definition": "Mie goreng adalah stir-fried noodles.",
        "ingredients": ["Mie", "Sayuran", "Telur", "Kecap", "Bumbu"],
        "types": ["Mie goreng Jawa", "Mie Aceh", "Mie tektek"]
    },
    "sate": {
        "category": "Indonesian Food",
        "definition": "Sate adalah grilled skewered meat dengan sambal kacang.",
        "types": ["Sate ayam", "Sate kambing", "Sate Madura", "Sate Padang", "Sate lilit (Bali)"],
        "served_with": "Lontong, bumbu kacang, kecap manis"
    },
    "rendang": {
        "category": "Indonesian Food",
        "definition": "Rendang adalah slow-cooked beef dari Padang.",
        "origin": "Minangkabau, Sumatra Barat",
        "recognition": "CNN World's Best Food (multiple times)",
        "cooking_time": "4-8 hours slow cooking",
        "ingredients": ["Daging sapi", "Santan", "Bumbu lengkap"]
    },
    "gado_gado": {
        "category": "Indonesian Food",
        "definition": "Gado-gado adalah vegetable salad dengan bumbu kacang.",
        "vegetables": ["Tahu", "Tempe", "Kangkung", "Tauge", "Kol", "Kentang"],
        "sauce": "Bumbu kacang",
        "type": "Indonesian salad"
    },
    "soto": {
        "category": "Indonesian Food",
        "definition": "Soto adalah traditional Indonesian soup.",
        "types": {
            "Soto Ayam": "Chicken soup, yellow broth",
            "Soto Betawi": "Beef with coconut milk, Jakarta",
            "Soto Madura": "Beef, clear broth, Madura style",
            "Coto Makassar": "Beef innards, Makassar"
        }
    },
    "bakso": {
        "category": "Indonesian Food",
        "definition": "Bakso adalah meatball soup khas Indonesia.",
        "components": ["Bakso (meatball)", "Mie", "Tahu", "Kuah kaldu"],
        "types": ["Bakso urat", "Bakso isi telur", "Bakso gepeng"]
    },
    "rawon": {
        "category": "Indonesian Food",
        "definition": "Rawon adalah black beef soup dari Jawa Timur.",
        "color": "Black from kluwek nut",
        "origin": "Surabaya, East Java",
        "served_with": "Tauge, telur asin, sambal"
    },
    "nasi_padang": {
        "category": "Indonesian Food",
        "definition": "Nasi Padang adalah rice dengan berbagai lauk Minang.",
        "characteristics": "All dishes served at once",
        "common_dishes": ["Rendang", "Gulai", "Dendeng", "Daun singkong", "Sambal"],
        "restaurant_style": "Rumah Makan Padang"
    },
    "indomie": {
        "category": "Indonesian Food",
        "definition": "Indomie adalah mie instan legendaris Indonesia.",
        "manufacturer": "Indofood",
        "popular_flavor": "Mi Goreng, Soto Mie, Ayam Bawang",
        "global": "Exported to 80+ countries",
        "cult_status": "Beloved cultural icon"
    },
    
    # ============================================
    # WORLD CUISINES
    # ============================================
    "japanese_food": {
        "category": "World Cuisine",
        "definition": "Masakan Jepang terkenal dengan umami dan presentation.",
        "dishes": ["Sushi", "Ramen", "Tempura", "Udon", "Sashimi", "Donburi"],
        "concepts": ["Umami", "Seasonality", "Presentation"],
        "unesco": "Washoku is UNESCO Intangible Cultural Heritage"
    },
    "sushi": {
        "category": "Japanese Food",
        "definition": "Sushi adalah nasi cuka dengan seafood/bahan lain.",
        "types": {
            "Nigiri": "Rice topped with fish",
            "Maki": "Rolled in seaweed",
            "Sashimi": "Just raw fish (technically not sushi)",
            "Temaki": "Hand roll cone shape"
        },
        "etiquette": "Don't mix wasabi into soy sauce (traditionally)"
    },
    "ramen": {
        "category": "Japanese Food",
        "definition": "Ramen adalah mie kuah Jepang dengan berbagai topping.",
        "broth_types": {
            "Shoyu": "Soy sauce based",
            "Shio": "Salt based, clear",
            "Miso": "Miso paste based",
            "Tonkotsu": "Pork bone, creamy white"
        },
        "toppings": ["Chashu", "Ajitama (egg)", "Nori", "Green onion", "Menma"]
    },
    "korean_food": {
        "category": "World Cuisine",
        "definition": "Masakan Korea dengan fermentasi dan gochujang.",
        "dishes": ["Kimchi", "Bibimbap", "Korean BBQ", "Tteokbokki", "Jjigae"],
        "banchan": "Side dishes served with every meal",
        "hallyu_boost": "K-wave made Korean food globally popular"
    },
    "kimchi": {
        "category": "Korean Food",
        "definition": "Kimchi adalah fermented vegetables, usually napa cabbage.",
        "fermentation": "Lactobacillus bacteria",
        "health": "Probiotics, vitamin C, fiber",
        "unesco": "Kimjang culture is UNESCO heritage"
    },
    "korean_bbq": {
        "category": "Korean Food",
        "definition": "Korean BBQ adalah grilled meat di meja.",
        "meats": ["Samgyeopsal (pork belly)", "Bulgogi (marinated beef)", "Galbi (ribs)"],
        "served_with": "Lettuce wraps, ssamjang, garlic, kimchi"
    },
    "chinese_food": {
        "category": "World Cuisine",
        "definition": "Masakan Cina sangat beragam berdasarkan regional.",
        "regional": {
            "Cantonese": "Dim sum, roast meats",
            "Sichuan": "Spicy, numbing (mala)",
            "Hunan": "Hot and sour",
            "Shandong": "Seafood, light"
        },
        "dim_sum": "Small dishes served with tea"
    },
    "italian_food": {
        "category": "World Cuisine",
        "definition": "Masakan Italia dengan pasta, pizza, dan olive oil.",
        "staples": ["Pasta", "Pizza", "Risotto", "Gelato"],
        "principles": "Quality ingredients, simplicity",
        "wine": "Paired with regional wines"
    },
    "pizza": {
        "category": "Italian Food",
        "definition": "Pizza adalah flatbread dengan topping.",
        "origin": "Naples, Italy",
        "styles": {
            "Neapolitan": "Soft, charred, simple toppings",
            "New York": "Large, foldable slices",
            "Chicago": "Deep dish, thick crust",
            "Detroit": "Rectangular, thick, crispy edges"
        },
        "classic": "Margherita (tomato, mozzarella, basil)"
    },
    "pasta_types": {
        "category": "Italian Food",
        "definition": "Berbagai jenis pasta.",
        "types": {
            "Spaghetti": "Long, round strands",
            "Penne": "Tube-shaped, angled cuts",
            "Fettuccine": "Flat, wide ribbons",
            "Rigatoni": "Large tubes with ridges",
            "Fusilli": "Spiral/corkscrew shape",
            "Lasagna": "Flat sheets, layered"
        }
    },
    "thai_food": {
        "category": "World Cuisine",
        "definition": "Masakan Thai dengan balance sweet, sour, salty, spicy.",
        "dishes": ["Pad Thai", "Tom Yum", "Green Curry", "Som Tam"],
        "flavors": "Fish sauce, lime, chili, palm sugar, lemongrass"
    },
    "indian_food": {
        "category": "World Cuisine",
        "definition": "Masakan India dengan rempah-rempah kompleks.",
        "dishes": ["Curry", "Biryani", "Naan", "Tandoori", "Samosa"],
        "spices": ["Turmeric", "Cumin", "Coriander", "Garam masala"],
        "vegetarian": "Large vegetarian tradition"
    },
    "mexican_food": {
        "category": "World Cuisine",
        "definition": "Masakan Meksiko dengan corn, beans, chili.",
        "dishes": ["Tacos", "Burritos", "Quesadilla", "Nachos", "Enchiladas"],
        "staples": ["Tortilla", "Beans", "Rice", "Salsa", "Guacamole"]
    },
    "french_food": {
        "category": "World Cuisine",
        "definition": "French cuisine adalah fondasi gastronomi modern.",
        "techniques": ["Sauté", "Braise", "Flambé", "Julienne"],
        "dishes": ["Croissant", "Coq au vin", "Bouillabaisse", "Ratatouille"],
        "influence": "Mother sauces, fine dining standards"
    },
    
    # ============================================
    # COOKING TECHNIQUES
    # ============================================
    "cooking_methods": {
        "category": "Cooking",
        "definition": "Berbagai teknik memasak.",
        "dry_heat": ["Roasting", "Baking", "Grilling", "Sautéing", "Frying"],
        "wet_heat": ["Boiling", "Steaming", "Poaching", "Simmering", "Braising"],
        "combination": "Braising, stewing"
    },
    "sauteing": {
        "category": "Cooking",
        "definition": "Sauté adalah memasak cepat dengan sedikit minyak, panas tinggi.",
        "key": "High heat, small pieces, keep moving",
        "pan": "Wide, shallow pan"
    },
    "braising": {
        "category": "Cooking",
        "definition": "Braising adalah slow cooking dalam liquid.",
        "steps": "Sear meat, add liquid, cook low and slow",
        "result": "Tender meat, flavorful sauce",
        "dishes": "Pot roast, ossobuco, rendang"
    },
    "grilling": {
        "category": "Cooking",
        "definition": "Grilling adalah memasak dengan direct heat.",
        "types": ["Charcoal", "Gas", "Electric"],
        "tips": "Preheat, oil grates, don't flip too often"
    },
    "baking": {
        "category": "Cooking",
        "definition": "Baking adalah memasak dengan dry heat di oven.",
        "science": "Leavening, Maillard reaction, caramelization",
        "precision": "Baking requires exact measurements"
    },
    "knife_cuts": {
        "category": "Cooking",
        "definition": "Berbagai teknik potong.",
        "cuts": {
            "Dice": "Cubes of various sizes",
            "Julienne": "Thin matchstick strips",
            "Brunoise": "Very small dice",
            "Chiffonade": "Thin ribbon slices (herbs, leafy)",
            "Mince": "Very fine chop"
        }
    },
    
    # ============================================
    # INGREDIENTS
    # ============================================
    "rice_types": {
        "category": "Ingredient",
        "definition": "Jenis-jenis beras.",
        "types": {
            "Long grain": "Fluffy, separate (Basmati, Jasmine)",
            "Short grain": "Sticky (Sushi rice)",
            "Medium grain": "Arborio (risotto)",
            "Brown rice": "Whole grain, nutritious",
            "Black rice": "Nutty, antioxidants"
        }
    },
    "herbs_spices": {
        "category": "Ingredient",
        "definition": "Herbs (daun) vs Spices (biji/kulit/akar).",
        "common_herbs": ["Basil", "Cilantro", "Parsley", "Thyme", "Rosemary"],
        "common_spices": ["Pepper", "Cumin", "Cinnamon", "Paprika", "Turmeric"],
        "indonesian": ["Lengkuas", "Serai", "Daun salam", "Kemiri", "Kluwek"]
    },
    "oils": {
        "category": "Ingredient",
        "definition": "Berbagai minyak untuk memasak.",
        "types": {
            "Olive oil": "Mediterranean, low-medium heat",
            "Vegetable oil": "Neutral, high smoke point",
            "Coconut oil": "Tropical cooking, baking",
            "Sesame oil": "Asian cooking, finishing",
            "Avocado oil": "High smoke point"
        }
    },
    
    # ============================================
    # BEVERAGES
    # ============================================
    "coffee": {
        "category": "Beverage",
        "definition": "Kopi adalah minuman dari biji kopi sangrai.",
        "origins": ["Ethiopia origin", "Indonesia (4th largest producer)"],
        "types": ["Arabica", "Robusta"],
        "drinks": ["Espresso", "Latte", "Cappuccino", "Americano", "Cold brew"],
        "indonesian": ["Kopi Gayo", "Kopi Toraja", "Kopi Luwak"]
    },
    "tea": {
        "category": "Beverage",
        "definition": "Teh adalah minuman dari daun Camellia sinensis.",
        "types": {
            "Green tea": "Unoxidized, Japan/China",
            "Black tea": "Fully oxidized",
            "Oolong": "Partially oxidized",
            "White tea": "Minimally processed",
            "Pu-erh": "Fermented, aged"
        },
        "indonesia": "Teh Sosro, teh tarik"
    },
    "boba": {
        "category": "Beverage",
        "definition": "Boba/Bubble Tea adalah teh dengan tapioca pearls.",
        "origin": "Taiwan, 1980s",
        "components": ["Tea base", "Milk", "Tapioca pearls", "Sweetener"],
        "variations": ["Brown sugar milk", "Fruit tea", "Cheese foam"]
    },
    
    # ============================================
    # DESSERTS
    # ============================================
    "chocolate": {
        "category": "Dessert",
        "definition": "Chocolate dibuat dari biji kakao.",
        "types": {
            "Dark chocolate": "Higher cocoa, less sugar",
            "Milk chocolate": "Milk added, sweeter",
            "White chocolate": "Cocoa butter only, no cocoa solids",
            "Ruby chocolate": "Pink, fruity (new)"
        },
        "health": "Dark chocolate has antioxidants"
    },
    "ice_cream": {
        "category": "Dessert",
        "definition": "Es krim adalah frozen dessert dari susu/krim.",
        "types": {
            "Ice cream": "Cream based, rich",
            "Gelato": "Italian, denser, less butterfat",
            "Sorbet": "Fruit-based, dairy-free",
            "Frozen yogurt": "Yogurt-based, tangy"
        }
    },
    "indonesian_desserts": {
        "category": "Dessert",
        "definition": "Dessert khas Indonesia.",
        "examples": {
            "Es cendol": "Green jelly, coconut milk, palm sugar",
            "Es teler": "Mixed fruits with avocado, coconut",
            "Klepon": "Green rice cake with palm sugar filling",
            "Martabak manis": "Sweet thick pancake with various toppings",
            "Kue lapis": "Layered cake"
        }
    }
}
