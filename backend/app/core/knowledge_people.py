"""
WeaR AI Knowledge - Famous People, Inventors & Influential Figures
Pengetahuan tentang orang-orang terkenal dan berpengaruh.
Created by RidTheWann
"""

KNOWLEDGE_PEOPLE = {
    # ============================================
    # TECH ENTREPRENEURS
    # ============================================
    "elon_musk": {
        "category": "Tech",
        "definition": "Elon Musk adalah entrepreneur dibalik Tesla, SpaceX, X, dll.",
        "companies": ["Tesla", "SpaceX", "X (Twitter)", "Neuralink", "The Boring Company", "xAI"],
        "born": "1971, South Africa",
        "net_worth": "Richest person in the world (fluctuates)"
    },
    "steve_jobs": {
        "category": "Tech",
        "definition": "Steve Jobs adalah co-founder Apple dan visionary product designer.",
        "companies": ["Apple", "Pixar", "NeXT"],
        "products": ["Mac", "iPod", "iPhone", "iPad"],
        "quote": "Stay hungry, stay foolish.",
        "died": "2011"
    },
    "bill_gates": {
        "category": "Tech",
        "definition": "Bill Gates adalah co-founder Microsoft.",
        "achievements": ["Microsoft Windows", "Bill & Melinda Gates Foundation"],
        "born": "1955",
        "philanthropy": "Donated $50B+ to charity"
    },
    "mark_zuckerberg": {
        "category": "Tech",
        "definition": "Mark Zuckerberg adalah founder Facebook (Meta).",
        "companies": ["Meta (Facebook, Instagram, WhatsApp)"],
        "born": "1984",
        "started": "Harvard dorm room, 2004"
    },
    "jeff_bezos": {
        "category": "Tech",
        "definition": "Jeff Bezos adalah founder Amazon.",
        "companies": ["Amazon", "Blue Origin", "Washington Post"],
        "started": "Garage, 1994 (online bookstore)",
        "born": "1964"
    },
    "sundar_pichai": {
        "category": "Tech",
        "definition": "Sundar Pichai adalah CEO Google/Alphabet.",
        "led": "Chrome, Android before becoming CEO",
        "born": "India, 1972"
    },
    "satya_nadella": {
        "category": "Tech",
        "definition": "Satya Nadella adalah CEO Microsoft.",
        "focus": "Cloud computing, AI, culture transformation",
        "born": "India, 1967"
    },
    "jensen_huang": {
        "category": "Tech",
        "definition": "Jensen Huang adalah founder dan CEO NVIDIA.",
        "achievement": "Made NVIDIA the AI chip leader",
        "born": "Taiwan, 1963"
    },
    "linus_torvalds": {
        "category": "Tech",
        "definition": "Linus Torvalds adalah creator Linux dan Git.",
        "linux": "Started as hobby project (1991)",
        "quote": "Talk is cheap. Show me the code.",
        "born": "Finland, 1969"
    },
    
    # ============================================
    # SCIENTISTS
    # ============================================
    "albert_einstein": {
        "category": "Science",
        "definition": "Albert Einstein adalah physicist dibalik Theory of Relativity.",
        "achievements": ["E=mc²", "Special/General Relativity", "Photoelectric effect (Nobel Prize)"],
        "lived": "1879-1955",
        "quote": "Imagination is more important than knowledge."
    },
    "isaac_newton": {
        "category": "Science",
        "definition": "Isaac Newton adalah physicist yang formulated laws of motion dan gravity.",
        "achievements": ["Laws of Motion", "Universal Gravitation", "Calculus (co-inventor)"],
        "lived": "1643-1727",
        "apple_story": "Possibly inspired gravity idea"
    },
    "marie_curie": {
        "category": "Science",
        "definition": "Marie Curie adalah scientist yang discovered radioactivity.",
        "achievements": ["Discovered Polonium dan Radium", "2 Nobel Prizes (Physics, Chemistry)"],
        "first": "First woman Nobel Prize, first person with 2",
        "lived": "1867-1934"
    },
    "nikola_tesla": {
        "category": "Science",
        "definition": "Nikola Tesla adalah inventor dibalik AC electricity dan banyak innovations.",
        "inventions": ["AC motor", "Tesla coil", "Radio (disputed)", "Wireless transmission"],
        "lived": "1856-1943",
        "unit": "Tesla (magnetic flux density)"
    },
    "charles_darwin": {
        "category": "Science",
        "definition": "Charles Darwin adalah naturalist dibalik Theory of Evolution.",
        "work": "On the Origin of Species (1859)",
        "concept": "Natural selection",
        "lived": "1809-1882"
    },
    "stephen_hawking": {
        "category": "Science",
        "definition": "Stephen Hawking adalah physicist theoretical famous untuk black hole theories.",
        "work": "A Brief History of Time",
        "achievements": ["Hawking radiation", "Black hole thermodynamics"],
        "lived": "1942-2018"
    },
    "ada_lovelace": {
        "category": "Science",
        "definition": "Ada Lovelace dianggap sebagai programmer pertama di dunia.",
        "work": "Wrote first algorithm for Analytical Engine (1843)",
        "lived": "1815-1852",
        "legacy": "Ada programming language named after her"
    },
    "alan_turing": {
        "category": "Science",
        "definition": "Alan Turing adalah father of computer science dan AI.",
        "achievements": ["Turing machine", "Enigma code breaking", "Turing test"],
        "lived": "1912-1954"
    },
    
    # ============================================
    # BUSINESS LEADERS
    # ============================================
    "warren_buffett": {
        "category": "Business",
        "definition": "Warren Buffett adalah investor legendaris, 'Oracle of Omaha'.",
        "company": "Berkshire Hathaway",
        "philosophy": "Value investing, long-term thinking",
        "born": "1930"
    },
    "jack_ma": {
        "category": "Business",
        "definition": "Jack Ma adalah founder Alibaba.",
        "companies": ["Alibaba", "Ant Group"],
        "story": "Rejected from 30 jobs, including KFC",
        "born": "China, 1964"
    },
    "richard_branson": {
        "category": "Business",
        "definition": "Richard Branson adalah founder Virgin Group.",
        "companies": ["Virgin Records", "Virgin Atlantic", "Virgin Galactic"],
        "style": "Adventure, risk-taking"
    },
    "oprah_winfrey": {
        "category": "Business",
        "definition": "Oprah Winfrey adalah media mogul dan philanthropist.",
        "achievements": ["The Oprah Winfrey Show", "OWN network", "Harpo Productions"],
        "influence": "One of most influential women"
    },
    
    # ============================================
    # ARTISTS & MUSICIANS
    # ============================================
    "leonardo_da_vinci": {
        "category": "Art",
        "definition": "Leonardo da Vinci adalah Renaissance polymath - artist, scientist, inventor.",
        "works": ["Mona Lisa", "The Last Supper", "Vitruvian Man"],
        "inventions": "Designed helicopters, tanks centuries ahead",
        "lived": "1452-1519"
    },
    "vincent_van_gogh": {
        "category": "Art",
        "definition": "Van Gogh adalah post-impressionist painter dengan style distinctive.",
        "works": ["Starry Night", "Sunflowers", "Self-portraits"],
        "tragic": "Only sold 1 painting during lifetime",
        "lived": "1853-1890"
    },
    "pablo_picasso": {
        "category": "Art",
        "definition": "Picasso adalah influential artist, co-founder Cubism.",
        "works": ["Guernica", "Les Demoiselles d'Avignon"],
        "periods": "Blue, Rose, African, Cubist, etc.",
        "lived": "1881-1973"
    },
    "michael_jackson": {
        "category": "Music",
        "definition": "Michael Jackson adalah 'King of Pop'.",
        "albums": ["Thriller (best-selling album ever)", "Bad", "Dangerous"],
        "moves": "Moonwalk",
        "lived": "1958-2009"
    },
    "beatles": {
        "category": "Music",
        "definition": "The Beatles adalah band paling influential dalam sejarah musik.",
        "members": ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],
        "era": "1960s",
        "hits": ["Hey Jude", "Let It Be", "Yesterday"]
    },
    "beethoven": {
        "category": "Music",
        "definition": "Ludwig van Beethoven adalah composer classical era.",
        "works": ["Symphony No. 5", "Für Elise", "Moonlight Sonata"],
        "remarkable": "Composed masterpieces while deaf",
        "lived": "1770-1827"
    },
    "mozart": {
        "category": "Music",
        "definition": "Wolfgang Amadeus Mozart adalah prodigy composer.",
        "works": "600+ compositions",
        "prodigy": "Composed from age 5",
        "lived": "1756-1791"
    },
    
    # ============================================
    # LEADERS & ACTIVISTS
    # ============================================
    "nelson_mandela": {
        "category": "Politics",
        "definition": "Nelson Mandela adalah anti-apartheid leader dan first Black president South Africa.",
        "imprisoned": "27 years (Robben Island)",
        "presidency": "1994-1999",
        "lived": "1918-2013"
    },
    "martin_luther_king": {
        "category": "Activism",
        "definition": "Martin Luther King Jr. adalah civil rights leader di Amerika.",
        "speech": "I Have a Dream (1963)",
        "approach": "Nonviolent resistance",
        "lived": "1929-1968"
    },
    "mahatma_gandhi": {
        "category": "Activism",
        "definition": "Gandhi adalah leader kemerdekaan India melalui nonviolent resistance.",
        "method": "Satyagraha (nonviolent civil disobedience)",
        "quote": "Be the change you wish to see in the world.",
        "lived": "1869-1948"
    },
    "malala_yousafzai": {
        "category": "Activism",
        "definition": "Malala adalah advocate untuk girls' education, youngest Nobel laureate.",
        "survived": "Taliban shooting (2012)",
        "nobel": "2014 (age 17)",
        "born": "Pakistan, 1997"
    },
    "greta_thunberg": {
        "category": "Activism",
        "definition": "Greta Thunberg adalah climate activist dari Sweden.",
        "movement": "Fridays for Future",
        "started": "School strike at age 15 (2018)",
        "born": "2003"
    },
    
    # ============================================
    # INDONESIAN FIGURES
    # ============================================
    "soekarno": {
        "category": "Indonesia",
        "definition": "Soekarno adalah proklamator dan presiden pertama Indonesia.",
        "achievement": "Proklamasi Kemerdekaan 17 Agustus 1945",
        "philosophy": "Marhaenisme, NASAKOM",
        "lived": "1901-1970"
    },
    "mohammad_hatta": {
        "category": "Indonesia",
        "definition": "Mohammad Hatta adalah proklamator dan wakil presiden pertama.",
        "title": "Bung Hatta",
        "known_for": "Ekonom, koperasi",
        "lived": "1902-1980"
    },
    "ki_hajar_dewantara": {
        "category": "Indonesia",
        "definition": "Ki Hajar Dewantara adalah Bapak Pendidikan Nasional Indonesia.",
        "founded": "Taman Siswa (1922)",
        "motto": "Ing ngarsa sung tuladha, ing madya mangun karsa, tut wuri handayani",
        "lived": "1889-1959"
    },
    "ra_kartini": {
        "category": "Indonesia",
        "definition": "R.A. Kartini adalah pahlawan emansipasi wanita Indonesia.",
        "book": "Habis Gelap Terbitlah Terang (kumpulan surat)",
        "hari_kartini": "21 April",
        "lived": "1879-1904"
    },
    "bj_habibie": {
        "category": "Indonesia",
        "definition": "B.J. Habibie adalah presiden ke-3 dan insinyur pesawat.",
        "achievement": "Membangun industri pesawat Indonesia (N-250)",
        "title": "Mr. Crack (keahlian dalam fatigue)",
        "lived": "1936-2019"
    },
    "pramoedya_ananta_toer": {
        "category": "Indonesia",
        "definition": "Pramoedya adalah sastrawan besar Indonesia.",
        "works": ["Bumi Manusia", "Tetralogi Buru"],
        "nominated": "Multiple Nobel Literature nominations",
        "lived": "1925-2006"
    },
}
