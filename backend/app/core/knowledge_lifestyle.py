"""
WeaR AI Knowledge - Food, Health, Sports & Entertainment
Pengetahuan tentang makanan, kesehatan, olahraga, musik, film, dan hiburan.
Created by RidTheWann
"""

KNOWLEDGE_LIFESTYLE = {
    # ============================================
    # FOOD & CULINARY
    # ============================================
    "coffee": {
        "category": "Food",
        "definition": "Coffee adalah brewed drink dari roasted coffee beans.",
        "types": ["Espresso", "Americano", "Latte", "Cappuccino", "Cold Brew", "Pour Over"],
        "caffeine": "~95mg per 8oz cup",
        "regions": ["Ethiopia (origin)", "Brazil", "Colombia", "Vietnam", "Indonesia"]
    },
    "kopi_indonesia": {
        "category": "Food",
        "definition": "Indonesia adalah salah satu penghasil kopi terbesar.",
        "varieties": ["Kopi Luwak", "Toraja", "Gayo", "Mandailing", "Java"],
        "kopi_luwak": "Kopi dari biji yang dimakan civet cat, termahal di dunia"
    },
    "tea": {
        "category": "Food",
        "definition": "Tea adalah beverage dari daun Camellia sinensis.",
        "types": ["Green", "Black", "Oolong", "White", "Pu-erh"],
        "caffeine": "~47mg per 8oz cup"
    },
    "pizza": {
        "category": "Food",
        "definition": "Pizza adalah flatbread dengan toppings dari Italy.",
        "origin": "Naples, Italy",
        "styles": ["Neapolitan", "New York", "Chicago Deep Dish", "Sicilian"]
    },
    "sushi": {
        "category": "Food",
        "definition": "Sushi adalah Japanese dish dengan vinegared rice dan seafood/vegetables.",
        "types": ["Nigiri", "Maki (roll)", "Sashimi (no rice)", "Temaki (hand roll)"],
        "etiquette": "Eat in one bite, dip fish side in soy sauce"
    },
    "ramen": {
        "category": "Food",
        "definition": "Ramen adalah Japanese noodle soup dengan rich broth.",
        "broths": ["Shoyu (soy)", "Miso", "Tonkotsu (pork bone)", "Shio (salt)"],
        "distinction": "Different dari instant noodles"
    },
    "italian_cuisine": {
        "category": "Food",
        "definition": "Italian cuisine terkenal dengan pasta, pizza, dan ingredients sederhana.",
        "staples": ["Pasta", "Olive oil", "Tomatoes", "Cheese", "Wine"],
        "dishes": ["Carbonara", "Bolognese", "Risotto", "Tiramisu"]
    },
    "thai_cuisine": {
        "category": "Food",
        "definition": "Thai cuisine terkenal dengan balance of flavors.",
        "flavors": ["Sweet", "Sour", "Salty", "Spicy", "Bitter"],
        "dishes": ["Pad Thai", "Tom Yum", "Green Curry", "Mango Sticky Rice"]
    },
    "mexican_cuisine": {
        "category": "Food",
        "definition": "Mexican cuisine kaya dengan spices dan corn-based dishes.",
        "staples": ["Corn tortillas", "Beans", "Chili peppers", "Avocado"],
        "dishes": ["Tacos", "Burritos", "Enchiladas", "Guacamole"]
    },
    "vegetarian": {
        "category": "Food",
        "definition": "Vegetarian diet excludes meat tapi allows dairy dan eggs.",
        "types": ["Lacto-ovo", "Lacto", "Ovo"],
        "reasons": ["Health", "Environment", "Animal welfare", "Religion"]
    },
    "vegan": {
        "category": "Food",
        "definition": "Vegan diet excludes ALL animal products.",
        "excludes": ["Meat", "Dairy", "Eggs", "Honey"],
        "protein_sources": ["Tofu", "Tempeh", "Legumes", "Nuts", "Seitan"]
    },
    "michelin_star": {
        "category": "Food",
        "definition": "Michelin stars adalah restaurant rating system.",
        "ratings": ["1 star (very good)", "2 stars (excellent)", "3 stars (exceptional)"],
        "origin": "Michelin Guide, made by tire company"
    },
    "umami": {
        "category": "Food",
        "definition": "Umami adalah fifth basic taste (savory).",
        "discovered": "Kikunae Ikeda (1908)",
        "sources": ["MSG", "Parmesan", "Soy sauce", "Mushrooms", "Tomatoes"]
    },
    "chocolate": {
        "category": "Food",
        "definition": "Chocolate dibuat dari cacao beans.",
        "types": ["Dark", "Milk", "White"],
        "facts": "Aztecs used cacao as currency, contains theobromine"
    },
    
    # ============================================
    # HEALTH & FITNESS
    # ============================================
    "exercise": {
        "category": "Health",
        "definition": "Exercise adalah physical activity untuk improve health.",
        "types": ["Cardio", "Strength training", "Flexibility", "Balance"],
        "recommendation": "150 min moderate atau 75 min vigorous per week"
    },
    "cardio": {
        "category": "Fitness",
        "definition": "Cardio adalah exercise yang raise heart rate.",
        "examples": ["Running", "Swimming", "Cycling", "HIIT", "Dancing"],
        "benefits": ["Heart health", "Weight loss", "Endurance", "Mood"]
    },
    "strength_training": {
        "category": "Fitness",
        "definition": "Strength training builds muscle menggunakan resistance.",
        "methods": ["Free weights", "Machines", "Bodyweight", "Resistance bands"],
        "benefits": ["Muscle mass", "Bone density", "Metabolism", "Posture"]
    },
    "yoga": {
        "category": "Fitness",
        "definition": "Yoga adalah practice combining postures, breathing, dan meditation.",
        "styles": ["Hatha", "Vinyasa", "Ashtanga", "Bikram", "Yin"],
        "benefits": ["Flexibility", "Stress relief", "Strength", "Balance"]
    },
    "hiit": {
        "category": "Fitness",
        "definition": "HIIT (High-Intensity Interval Training) alternates intense dan rest periods.",
        "structure": "30 sec sprint, 30 sec rest (varies)",
        "benefits": "Efficient, burns calories, improves cardiovascular health"
    },
    "nutrition": {
        "category": "Health",
        "definition": "Nutrition adalah study of how food affects body.",
        "macros": ["Carbohydrates", "Proteins", "Fats"],
        "micros": ["Vitamins", "Minerals"]
    },
    "protein": {
        "category": "Nutrition",
        "definition": "Protein adalah macronutrient untuk building dan repairing tissues.",
        "sources": ["Meat", "Fish", "Eggs", "Dairy", "Legumes", "Tofu"],
        "recommended": "0.8g per kg body weight (more untuk athletes)"
    },
    "calories": {
        "category": "Nutrition",
        "definition": "Calorie adalah unit of energy dari food.",
        "daily_need": "~2000 calories (varies by activity, size, age)",
        "weight_loss": "Calories in < Calories out"
    },
    "sleep": {
        "category": "Health",
        "definition": "Sleep adalah essential untuk physical dan mental restoration.",
        "recommended": "7-9 hours untuk adults",
        "stages": ["Light (N1, N2)", "Deep (N3)", "REM"],
        "tips": ["Consistent schedule", "Dark room", "No screens before bed"]
    },
    "hydration": {
        "category": "Health",
        "definition": "Hydration adalah maintaining adequate body water level.",
        "recommendation": "~8 cups (2L) water per day",
        "signs_dehydration": ["Thirst", "Dark urine", "Fatigue", "Headache"]
    },
    "mental_health": {
        "category": "Health",
        "definition": "Mental health mencakup emotional, psychological, dan social well-being.",
        "conditions": ["Depression", "Anxiety", "PTSD", "Bipolar"],
        "importance": "Seek help if struggling, it's okay to not be okay"
    },
    "bmi": {
        "category": "Health",
        "definition": "BMI (Body Mass Index) adalah weight relative to height.",
        "formula": "Weight (kg) / Height² (m²)",
        "ranges": ["<18.5 Underweight", "18.5-24.9 Normal", "25-29.9 Overweight", ">30 Obese"],
        "limitation": "Doesn't account for muscle mass"
    },
    "intermittent_fasting": {
        "category": "Health",
        "definition": "Intermittent fasting adalah cycling antara fasting dan eating.",
        "methods": ["16:8 (16h fast, 8h eat)", "5:2 (5 normal, 2 low cal)", "24h fast"],
        "benefits": "Weight loss, metabolic health (research ongoing)"
    },
    
    # ============================================
    # SPORTS
    # ============================================
    "football_soccer": {
        "category": "Sports",
        "definition": "Football/Soccer adalah sport paling populer di dunia.",
        "players": "11 per team",
        "major_events": ["FIFA World Cup", "UEFA Champions League", "Premier League"],
        "legends": ["Pelé", "Maradona", "Messi", "Ronaldo"]
    },
    "basketball": {
        "category": "Sports",
        "definition": "Basketball adalah sport dengan 5 players per team.",
        "nba": "National Basketball Association (US)",
        "legends": ["Michael Jordan", "LeBron James", "Kobe Bryant", "Kareem"]
    },
    "badminton": {
        "category": "Sports",
        "definition": "Badminton adalah racquet sport populer di Asia.",
        "indonesia": "Powerhouse negara badminton",
        "legends_indo": ["Susi Susanti", "Taufik Hidayat", "Greysia/Apriyani"]
    },
    "tennis": {
        "category": "Sports",
        "definition": "Tennis adalah racquet sport dengan singles atau doubles.",
        "grand_slams": ["Australian Open", "French Open", "Wimbledon", "US Open"],
        "goats": ["Federer", "Nadal", "Djokovic", "Serena Williams"]
    },
    "formula_one": {
        "category": "Sports",
        "definition": "F1 adalah highest class of international auto racing.",
        "teams": ["Red Bull", "Ferrari", "Mercedes", "McLaren"],
        "champions": ["Schumacher (7)", "Hamilton (7)", "Verstappen"]
    },
    "olympics": {
        "category": "Sports",
        "definition": "Olympics adalah international multi-sport event setiap 4 tahun.",
        "types": ["Summer Olympics", "Winter Olympics", "Paralympics"],
        "origin": "Ancient Greece (776 BC), modern revival 1896"
    },
    "world_cup": {
        "category": "Sports",
        "definition": "FIFA World Cup adalah international football tournament.",
        "frequency": "Every 4 years",
        "most_wins": "Brazil (5 times)",
        "2022": "Argentina won in Qatar"
    },
    "esports": {
        "category": "Sports",
        "definition": "Esports adalah professional competitive video gaming.",
        "popular_games": ["League of Legends", "Dota 2", "CS2", "Valorant"],
        "prize_pools": "The International Dota 2 ~$40M",
        "growth": "Now recognized by Asian Games"
    },
    "gym": {
        "category": "Fitness",
        "definition": "Gym adalah facility untuk exercise dengan equipment.",
        "equipment": ["Treadmill", "Weights", "Machines", "Rowing machine"],
        "etiquette": ["Wipe equipment", "Rerack weights", "Don't hog machines"]
    },
    "marathon": {
        "category": "Sports",
        "definition": "Marathon adalah long-distance race of 42.195 km (26.2 miles).",
        "origin": "Greek legend of Pheidippides",
        "world_record": "Kelvin Kiptum 2:00:35 (2023)"
    },
    
    # ============================================
    # MUSIC
    # ============================================
    "music_genres": {
        "category": "Music",
        "definition": "Music genres kategorize music by style dan characteristics.",
        "major": ["Pop", "Rock", "Hip-Hop", "R&B", "Electronic", "Classical", "Jazz", "Country"]
    },
    "pop_music": {
        "category": "Music",
        "definition": "Pop music adalah popular music dengan catchy melodies.",
        "characteristics": "Accessible, hook-driven, mainstream appeal",
        "artists": ["Michael Jackson", "Madonna", "Taylor Swift", "The Weeknd"]
    },
    "rock_music": {
        "category": "Music",
        "definition": "Rock music originated in 1950s, guitar-driven.",
        "subgenres": ["Classic Rock", "Punk", "Metal", "Alternative", "Indie"],
        "legends": ["The Beatles", "Led Zeppelin", "Queen", "Nirvana"]
    },
    "hip_hop": {
        "category": "Music",
        "definition": "Hip-hop adalah culture dan music genre dengan rapping dan beats.",
        "elements": ["MCing", "DJing", "Breakdancing", "Graffiti"],
        "legends": ["Tupac", "Notorious B.I.G.", "Jay-Z", "Kendrick Lamar"]
    },
    "kpop": {
        "category": "Music",
        "definition": "K-pop adalah Korean pop music dengan performance focus.",
        "characteristics": "Choreography, visuals, fan culture",
        "groups": ["BTS", "BLACKPINK", "EXO", "TWICE", "Stray Kids"]
    },
    "classical_music": {
        "category": "Music",
        "definition": "Classical music adalah art music rooted dalam Western traditions.",
        "periods": ["Baroque", "Classical", "Romantic", "Modern"],
        "composers": ["Bach", "Mozart", "Beethoven", "Chopin"]
    },
    "edm": {
        "category": "Music",
        "definition": "EDM (Electronic Dance Music) dibuat dengan electronic production.",
        "subgenres": ["House", "Techno", "Trance", "Dubstep", "Drum & Bass"],
        "djs": ["Avicii", "Martin Garrix", "Deadmau5", "Skrillex"]
    },
    "spotify": {
        "category": "Music",
        "definition": "Spotify adalah music streaming platform terbesar.",
        "launched": "2008 (Sweden)",
        "users": "500+ million",
        "features": ["Playlists", "Discover Weekly", "Wrapped"]
    },
    "grammy": {
        "category": "Music",
        "definition": "Grammy Awards adalah penghargaan musik prestisius.",
        "categories": "Album of the Year, Record of the Year, Song of the Year, etc.",
        "most_wins": "Georg Solti (31)"
    },
    
    # ============================================
    # FILM & TV
    # ============================================
    "hollywood": {
        "category": "Entertainment",
        "definition": "Hollywood adalah center of American film industry di Los Angeles.",
        "major_studios": ["Disney", "Warner Bros", "Universal", "Paramount", "Sony"],
        "history": "Started early 1900s"
    },
    "oscar": {
        "category": "Entertainment",
        "definition": "Academy Awards (Oscars) adalah penghargaan film paling prestisius.",
        "categories": ["Best Picture", "Director", "Actor", "Actress", "Screenplay"],
        "most_wins_film": "Titanic, Lord of the Rings ROTK, Ben-Hur (11 each)"
    },
    "netflix": {
        "category": "Entertainment",
        "definition": "Netflix adalah streaming service dengan original content.",
        "started": "1997 (DVD rental), streaming 2007",
        "hit_shows": ["Stranger Things", "Squid Game", "Wednesday"]
    },
    "marvel_cinematic_universe": {
        "category": "Entertainment",
        "definition": "MCU adalah shared universe superhero films dari Marvel Studios.",
        "phases": "Phase 1-6 (Infinity Saga, Multiverse Saga)",
        "highest_grossing": "Avengers: Endgame ($2.79B)"
    },
    "star_wars": {
        "category": "Entertainment",
        "definition": "Star Wars adalah epic space opera franchise.",
        "creator": "George Lucas (1977)",
        "trilogies": ["Original", "Prequel", "Sequel"],
        "famous_line": "May the Force be with you"
    },
    "anime_popular": {
        "category": "Entertainment",
        "definition": "Most popular anime series dan films.",
        "series": ["Naruto", "One Piece", "Attack on Titan", "Demon Slayer", "Death Note"],
        "films": ["Spirited Away", "Your Name", "Akira"]
    },
    "korean_drama": {
        "category": "Entertainment",
        "definition": "K-Drama adalah Korean television dramas dengan global popularity.",
        "hits": ["Squid Game", "Crash Landing on You", "Goblin", "Reply series"],
        "platform": "Netflix popularized globally"
    },
    "sitcom": {
        "category": "Entertainment",
        "definition": "Sitcom adalah situation comedy TV show.",
        "classics": ["Friends", "The Office", "Seinfeld", "How I Met Your Mother"],
        "format": "Usually 22-30 minutes per episode"
    },
    "documentary": {
        "category": "Entertainment",
        "definition": "Documentary adalah non-fiction film untuk educate atau inform.",
        "types": ["Nature", "True crime", "Historical", "Social issues"],
        "platforms": "Netflix, Discovery+, YouTube"
    },
    "podcast": {
        "category": "Entertainment",
        "definition": "Podcast adalah digital audio show available for streaming/download.",
        "popular": ["Joe Rogan", "Serial", "This American Life", "Deddy Corbuzier"],
        "platforms": ["Spotify", "Apple Podcasts", "YouTube"]
    },
    
    # ============================================
    # TECHNOLOGY CULTURE
    # ============================================
    "smartphone": {
        "category": "Technology",
        "definition": "Smartphone adalah mobile phone dengan computer capabilities.",
        "major_os": ["iOS (Apple)", "Android (Google)"],
        "first_iphone": "2007, changed the industry"
    },
    "social_media_addiction": {
        "category": "Psychology",
        "definition": "Social media addiction adalah excessive use affecting daily life.",
        "signs": ["Constant checking", "FOMO", "Comparison", "Sleep issues"],
        "digital_detox": "Taking breaks dari social media"
    },
    "screen_time": {
        "category": "Technology",
        "definition": "Screen time adalah time spent using devices dengan screens.",
        "average": "7+ hours/day untuk adults",
        "recommendations": "Limit untuk health, especially before sleep"
    },
    "remote_work": {
        "category": "Work",
        "definition": "Remote work adalah working dari location selain office.",
        "tools": ["Zoom", "Slack", "Teams", "Notion"],
        "post_covid": "Hybrid work becoming norm"
    },
    "work_life_balance": {
        "category": "Work",
        "definition": "Work-life balance adalah equilibrium antara work dan personal life.",
        "importance": "Prevents burnout, improves well-being",
        "tips": ["Set boundaries", "Take breaks", "Use vacation time"]
    },
    "side_hustle": {
        "category": "Work",
        "definition": "Side hustle adalah additional work selain main job.",
        "examples": ["Freelancing", "Content creation", "E-commerce", "Tutoring"],
        "purpose": "Extra income, passion project, skill development"
    },
    "minimalism": {
        "category": "Lifestyle",
        "definition": "Minimalism adalah intentionally living dengan less.",
        "areas": ["Possessions", "Digital", "Schedule", "Finances"],
        "benefit": "Focus on what matters, reduce stress"
    },
    "sustainability": {
        "category": "Lifestyle",
        "definition": "Sustainability adalah meeting needs tanpa compromising future.",
        "practices": ["Reduce, Reuse, Recycle", "Sustainable products", "Lower carbon footprint"],
        "importance": "Climate change, resource depletion"
    },
}
