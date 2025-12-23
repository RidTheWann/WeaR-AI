"""
WeaR AI Knowledge - History, Geography, Countries & World Facts
Pengetahuan tentang sejarah dunia, negara, geografi, dan fakta menarik.
Created by RidTheWann
"""

KNOWLEDGE_WORLD = {
    # ============================================
    # WORLD HISTORY
    # ============================================
    "world_war_1": {
        "category": "History",
        "definition": "World War I (1914-1918) adalah global war yang dimulai di Europe.",
        "trigger": "Assassination of Archduke Franz Ferdinand",
        "major_powers": {
            "Allies": "France, UK, Russia, Italy, US",
            "Central Powers": "Germany, Austria-Hungary, Ottoman Empire"
        },
        "casualties": "~20 million dead",
        "ended": "Treaty of Versailles"
    },
    "world_war_2": {
        "category": "History",
        "definition": "World War II (1939-1945) adalah global war terbesar dalam sejarah.",
        "start": "Germany invades Poland (September 1, 1939)",
        "major_powers": {
            "Allies": "US, UK, USSR, France, China",
            "Axis": "Germany, Japan, Italy"
        },
        "casualties": "~70-85 million dead",
        "ended": "Germany surrender (May), Japan surrender after atomic bombs (August 1945)"
    },
    "cold_war": {
        "category": "History",
        "definition": "Cold War (1947-1991) adalah geopolitical tension antara US dan Soviet Union.",
        "aspects": ["Nuclear arms race", "Space race", "Proxy wars", "Ideological conflict"],
        "ended": "Dissolution of Soviet Union (1991)"
    },
    "industrial_revolution": {
        "category": "History",
        "definition": "Industrial Revolution adalah transition ke manufacturing processes (18-19th century).",
        "origin": "Britain",
        "innovations": ["Steam engine", "Spinning jenny", "Railways"],
        "impact": "Urbanization, capitalism, labor movements"
    },
    "french_revolution": {
        "category": "History",
        "definition": "French Revolution (1789-1799) menggulingkan monarchy dan establish republic.",
        "motto": "Liberté, Égalité, Fraternité",
        "events": ["Storming of Bastille", "Reign of Terror", "Rise of Napoleon"]
    },
    "american_revolution": {
        "category": "History",
        "definition": "American Revolution (1775-1783) adalah war of independence dari Britain.",
        "declaration": "July 4, 1776",
        "key_figures": ["George Washington", "Thomas Jefferson", "Benjamin Franklin"]
    },
    "renaissance": {
        "category": "History",
        "definition": "Renaissance (14-17th century) adalah cultural rebirth di Europe.",
        "origin": "Italy (Florence)",
        "artists": ["Leonardo da Vinci", "Michelangelo", "Raphael"],
        "themes": "Humanism, art, science, exploration"
    },
    "ancient_egypt": {
        "category": "History",
        "definition": "Ancient Egypt adalah civilization di Nile River (~3100-30 BCE).",
        "achievements": ["Pyramids", "Hieroglyphics", "Mummification", "Medicine"],
        "famous_rulers": ["Cleopatra", "Tutankhamun", "Ramesses II"]
    },
    "roman_empire": {
        "category": "History",
        "definition": "Roman Empire adalah one of the largest empires in ancient history.",
        "peak": "117 CE under Trajan",
        "legacy": ["Latin language", "Law", "Architecture", "Christianity spread"],
        "fall": "476 CE (Western Roman Empire)"
    },
    "ancient_greece": {
        "category": "History",
        "definition": "Ancient Greece adalah cradle of Western civilization.",
        "contributions": ["Democracy", "Philosophy", "Olympics", "Theater", "Mathematics"],
        "philosophers": ["Socrates", "Plato", "Aristotle"]
    },
    "silk_road": {
        "category": "History",
        "definition": "Silk Road adalah ancient trade routes connecting East dan West.",
        "traded": ["Silk", "Spices", "Ideas", "Religions"],
        "significance": "Cultural exchange between civilizations"
    },
    "colonialism": {
        "category": "History",
        "definition": "Colonialism adalah practice of acquiring political control over other countries.",
        "era": "15th-20th century",
        "major_powers": ["Britain", "France", "Spain", "Portugal", "Netherlands"],
        "decolonization": "Mostly 1940s-1970s"
    },
    
    # ============================================
    # INDONESIA
    # ============================================
    "indonesia": {
        "category": "Country",
        "definition": "Indonesia adalah negara kepulauan terbesar di dunia dengan 17,000+ pulau.",
        "capital": "Jakarta (akan pindah ke Nusantara)",
        "population": "~275 million (4th largest)",
        "languages": "Bahasa Indonesia (official), 700+ regional languages",
        "islands": ["Sumatra", "Java", "Kalimantan", "Sulawesi", "Papua"]
    },
    "pancasila": {
        "category": "Indonesia",
        "definition": "Pancasila adalah dasar negara Indonesia dengan 5 sila.",
        "sila": [
            "Ketuhanan Yang Maha Esa",
            "Kemanusiaan yang Adil dan Beradab",
            "Persatuan Indonesia",
            "Kerakyatan yang Dipimpin oleh Hikmat Kebijaksanaan",
            "Keadilan Sosial bagi Seluruh Rakyat Indonesia"
        ]
    },
    "kemerdekaan_indonesia": {
        "category": "Indonesia",
        "definition": "Proklamasi Kemerdekaan Indonesia pada 17 Agustus 1945.",
        "proklamator": ["Soekarno", "Mohammad Hatta"],
        "penjajahan": "Belanda ~350 tahun, Jepang ~3.5 tahun"
    },
    "bahasa_indonesia": {
        "category": "Language",
        "definition": "Bahasa Indonesia adalah bahasa resmi Indonesia, based on Malay.",
        "alphabet": "Latin",
        "speakers": "~270 million",
        "words": ["Terima kasih", "Selamat pagi", "Apa kabar"]
    },
    "bali": {
        "category": "Indonesia",
        "definition": "Bali adalah pulau wisata terkenal dengan budaya Hindu.",
        "attractions": ["Temple", "Rice terraces", "Beaches", "Arts"],
        "nickname": "Island of the Gods"
    },
    "wayang": {
        "category": "Indonesia",
        "definition": "Wayang adalah traditional puppet theater di Indonesia.",
        "types": ["Wayang kulit (shadow)", "Wayang golek (rod)", "Wayang orang (human)"],
        "unesco": "Intangible Cultural Heritage"
    },
    "batik": {
        "category": "Indonesia",
        "definition": "Batik adalah technique of wax-resist dyeing pada fabric.",
        "origin": "Java, Indonesia",
        "unesco": "Intangible Cultural Heritage (2009)",
        "batik_day": "2 Oktober"
    },
    "rendang": {
        "category": "Food",
        "definition": "Rendang adalah masakan daging dengan bumbu kaya rempah dari Minangkabau.",
        "recognition": "Voted 'World's Most Delicious Food' by CNN",
        "origin": "Sumatra Barat"
    },
    "nasi_goreng": {
        "category": "Food",
        "definition": "Nasi goreng adalah fried rice khas Indonesia.",
        "ingredients": "Rice, kecap manis, shallots, garlic, chili, egg",
        "variations": ["Nasi goreng kampung", "Nasi goreng seafood", "Nasi goreng spesial"]
    },
    
    # ============================================
    # MAJOR COUNTRIES
    # ============================================
    "united_states": {
        "category": "Country",
        "definition": "United States adalah negara dengan 50 states di North America.",
        "capital": "Washington, D.C.",
        "population": "~330 million",
        "economy": "Largest economy (GDP)",
        "facts": ["50 states", "Hollywood", "Silicon Valley", "NASA"]
    },
    "china": {
        "category": "Country",
        "definition": "China adalah negara dengan populasi terbesar di dunia.",
        "capital": "Beijing",
        "population": "~1.4 billion",
        "economy": "2nd largest economy",
        "landmarks": ["Great Wall", "Forbidden City", "Terracotta Army"]
    },
    "japan": {
        "category": "Country",
        "definition": "Japan adalah island nation di East Asia dengan budaya unik.",
        "capital": "Tokyo",
        "population": "~125 million",
        "culture": ["Anime", "Manga", "Sushi", "Cherry blossoms", "Technology"]
    },
    "india": {
        "category": "Country",
        "definition": "India adalah negara dengan populasi terbesar kedua di dunia.",
        "capital": "New Delhi",
        "population": "~1.4 billion",
        "landmarks": ["Taj Mahal", "Ganges River"],
        "industries": ["IT", "Bollywood", "Spices"]
    },
    "united_kingdom": {
        "category": "Country",
        "definition": "UK terdiri dari England, Scotland, Wales, dan Northern Ireland.",
        "capital": "London",
        "government": "Constitutional monarchy",
        "landmarks": ["Big Ben", "Buckingham Palace", "Stonehenge"]
    },
    "germany": {
        "category": "Country",
        "definition": "Germany adalah economic powerhouse di Central Europe.",
        "capital": "Berlin",
        "population": "~84 million",
        "known_for": ["Engineering", "Beer", "Cars (BMW, Mercedes, VW)"]
    },
    "france": {
        "category": "Country",
        "definition": "France adalah negara dengan budaya dan kuliner terkenal.",
        "capital": "Paris",
        "landmarks": ["Eiffel Tower", "Louvre", "Notre-Dame"],
        "known_for": ["Wine", "Fashion", "Art", "Cuisine"]
    },
    "australia": {
        "category": "Country",
        "definition": "Australia adalah negara sekaligus benua dengan fauna unik.",
        "capital": "Canberra",
        "population": "~26 million",
        "unique_fauna": ["Kangaroo", "Koala", "Platypus", "Crocodiles"]
    },
    "brazil": {
        "category": "Country",
        "definition": "Brazil adalah negara terbesar di South America.",
        "capital": "Brasília",
        "population": "~215 million",
        "known_for": ["Amazon rainforest", "Carnival", "Football", "Coffee"]
    },
    "russia": {
        "category": "Country",
        "definition": "Russia adalah negara terbesar di dunia berdasarkan area.",
        "capital": "Moscow",
        "area": "~17.1 million km² (11% of world's land)",
        "landmarks": ["Kremlin", "Red Square", "Trans-Siberian Railway"]
    },
    "south_korea": {
        "category": "Country",
        "definition": "South Korea adalah tech hub dengan K-pop dan K-drama culture.",
        "capital": "Seoul",
        "population": "~52 million",
        "culture": ["K-pop", "K-drama", "Samsung", "Hyundai"]
    },
    "singapore": {
        "category": "Country",
        "definition": "Singapore adalah city-state dengan ekonomi maju di Southeast Asia.",
        "population": "~5.5 million",
        "known_for": ["Clean city", "Finance hub", "Marina Bay Sands"],
        "languages": "English, Mandarin, Malay, Tamil"
    },
    "malaysia": {
        "category": "Country",
        "definition": "Malaysia adalah negara tetangga Indonesia di Southeast Asia.",
        "capital": "Kuala Lumpur",
        "landmarks": ["Petronas Towers", "Langkawi"],
        "known_for": ["Diverse cuisine", "Tropical rainforests"]
    },
    
    # ============================================
    # GEOGRAPHY
    # ============================================
    "continents": {
        "category": "Geography",
        "definition": "7 benua di dunia.",
        "list": ["Asia", "Africa", "North America", "South America", "Antarctica", "Europe", "Australia/Oceania"],
        "largest": "Asia (~30% of land area)"
    },
    "oceans": {
        "category": "Geography",
        "definition": "5 samudra di dunia.",
        "list": ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"],
        "largest": "Pacific Ocean (covers 46% of ocean surface)"
    },
    "mount_everest": {
        "category": "Geography",
        "definition": "Mount Everest adalah gunung tertinggi di dunia.",
        "height": "8,848.86 meters (29,031.7 ft)",
        "location": "Nepal/Tibet border (Himalayas)",
        "first_summit": "Edmund Hillary & Tenzing Norgay (1953)"
    },
    "amazon_river": {
        "category": "Geography",
        "definition": "Amazon River adalah sungai dengan volume air terbesar.",
        "length": "~6,400 km (2nd longest after Nile)",
        "rainforest": "Amazon rainforest adalah 'lungs of Earth'"
    },
    "sahara_desert": {
        "category": "Geography",
        "definition": "Sahara adalah hot desert terbesar di dunia.",
        "area": "~9.2 million km² (almost size of USA)",
        "location": "North Africa"
    },
    "great_barrier_reef": {
        "category": "Geography",
        "definition": "Great Barrier Reef adalah coral reef system terbesar di dunia.",
        "location": "Australia",
        "size": "~344,400 km²",
        "threat": "Climate change, coral bleaching"
    },
    "time_zones": {
        "category": "Geography",
        "definition": "Time zones membagi Earth menjadi 24 zones berdasarkan UTC.",
        "utc": "Coordinated Universal Time (reference)",
        "indonesia": "WIB (UTC+7), WITA (UTC+8), WIT (UTC+9)"
    },
    "equator": {
        "category": "Geography",
        "definition": "Equator adalah imaginary line yang membagi Earth menjadi Northern dan Southern hemispheres.",
        "latitude": "0°",
        "countries": "13 countries (including Indonesia, Brazil, Kenya)"
    },
    
    # ============================================
    # WONDERS & LANDMARKS
    # ============================================
    "seven_wonders_ancient": {
        "category": "History",
        "definition": "7 Keajaiban Dunia Kuno.",
        "list": [
            "Great Pyramid of Giza (still standing)",
            "Hanging Gardens of Babylon",
            "Statue of Zeus at Olympia",
            "Temple of Artemis at Ephesus",
            "Mausoleum at Halicarnassus",
            "Colossus of Rhodes",
            "Lighthouse of Alexandria"
        ]
    },
    "seven_wonders_modern": {
        "category": "Geography",
        "definition": "7 Keajaiban Dunia Modern (New7Wonders).",
        "list": [
            "Great Wall of China",
            "Petra (Jordan)",
            "Christ the Redeemer (Brazil)",
            "Machu Picchu (Peru)",
            "Chichen Itza (Mexico)",
            "Colosseum (Italy)",
            "Taj Mahal (India)"
        ]
    },
    "eiffel_tower": {
        "category": "Landmark",
        "definition": "Eiffel Tower adalah iron lattice tower di Paris.",
        "height": "330 meters",
        "built": "1889 (World's Fair)",
        "designer": "Gustave Eiffel",
        "visitors": "~7 million per year"
    },
    "great_wall_china": {
        "category": "Landmark",
        "definition": "Great Wall of China adalah series walls untuk defense.",
        "length": "~21,196 km (all sections)",
        "built": "7th century BC - 1644 AD",
        "myth": "NOT visible from space with naked eye"
    },
    "statue_of_liberty": {
        "category": "Landmark",
        "definition": "Statue of Liberty adalah copper statue gift dari France ke USA.",
        "location": "New York Harbor",
        "dedicated": "1886",
        "height": "93 meters (with pedestal)"
    },
    "taj_mahal": {
        "category": "Landmark",
        "definition": "Taj Mahal adalah ivory-white marble mausoleum di India.",
        "location": "Agra, India",
        "built_by": "Shah Jahan untuk istrinya Mumtaz Mahal",
        "completed": "1653"
    },
    "machu_picchu": {
        "category": "Landmark",
        "definition": "Machu Picchu adalah 15th-century Inca citadel di Peru.",
        "altitude": "2,430 meters",
        "rediscovered": "1911 by Hiram Bingham"
    },
    "pyramids_giza": {
        "category": "Landmark",
        "definition": "Pyramids of Giza adalah ancient Egyptian pyramids, termasuk Great Pyramid.",
        "age": "~4,500 years old",
        "great_pyramid": "146.6 meters originally, now 138.5 meters"
    },
    "colosseum": {
        "category": "Landmark",
        "definition": "Colosseum adalah ancient Roman amphitheater di Rome.",
        "capacity": "50,000-80,000 spectators",
        "built": "70-80 AD",
        "used_for": "Gladiatorial contests, public spectacles"
    },
    "petra": {
        "category": "Landmark",
        "definition": "Petra adalah archaeological city carved into rock di Jordan.",
        "famous": "Al-Khazneh (The Treasury)",
        "age": "~2,000+ years",
        "nickname": "Rose City"
    },
    "borobudur": {
        "category": "Landmark",
        "definition": "Borobudur adalah candi Buddha terbesar di dunia di Indonesia.",
        "location": "Magelang, Jawa Tengah",
        "built": "9th century",
        "unesco": "World Heritage Site"
    },
    "prambanan": {
        "category": "Landmark",
        "definition": "Prambanan adalah candi Hindu terbesar di Indonesia.",
        "location": "Yogyakarta, Indonesia",
        "built": "9th century",
        "dedicated_to": "Trimurti (Brahma, Vishnu, Shiva)"
    },
}
