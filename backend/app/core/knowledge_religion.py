"""
WeaR AI Knowledge - Religion, Spirituality, and World Beliefs
Pengetahuan tentang agama dan kepercayaan dunia.
Created by RidTheWann
"""

KNOWLEDGE_RELIGION = {
    # ============================================
    # WORLD RELIGIONS
    # ============================================
    "islam": {
        "category": "Religion",
        "definition": "Islam adalah agama monoteis dengan 1.9 miliar pengikut.",
        "founder": "Nabi Muhammad SAW (570-632 M)",
        "holy_book": "Al-Quran",
        "pillars": ["Syahadat", "Sholat", "Zakat", "Puasa", "Haji"],
        "beliefs": ["Allah SWT", "Malaikat", "Kitab", "Rasul", "Hari Akhir", "Qada & Qadar"],
        "holy_places": ["Mekah", "Madinah", "Al-Aqsa"],
        "population": "24% world population"
    },
    "christianity": {
        "category": "Religion",
        "definition": "Kristen adalah agama terbesar dengan 2.4 miliar pengikut.",
        "founder": "Yesus Kristus",
        "holy_book": "Alkitab (Bible)",
        "branches": ["Katolik", "Protestan", "Ortodoks"],
        "beliefs": ["Trinity", "Salvation", "Resurrection"],
        "holy_places": ["Yerusalem", "Vatikan", "Bethlehem"],
        "population": "31% world population"
    },
    "hinduism": {
        "category": "Religion",
        "definition": "Hindu adalah agama tertua yang masih dipraktikkan.",
        "origin": "India, 4000+ years ago",
        "books": ["Vedas", "Upanishads", "Bhagavad Gita"],
        "beliefs": ["Brahman", "Karma", "Dharma", "Reincarnation", "Moksha"],
        "deities": ["Brahma", "Vishnu", "Shiva"],
        "population": "~1.2 billion (15%)"
    },
    "buddhism": {
        "category": "Religion",
        "definition": "Buddha adalah agama/filosofi yang fokus pada enlightenment.",
        "founder": "Siddhartha Gautama (Buddha), ~500 BCE",
        "teachings": ["Four Noble Truths", "Eightfold Path", "Middle Way"],
        "branches": ["Theravada", "Mahayana", "Vajrayana"],
        "beliefs": ["Karma", "Nirvana", "No self (Anatta)"],
        "population": "~500 million (7%)"
    },
    "judaism": {
        "category": "Religion",
        "definition": "Yudaisme adalah agama monoteis tertua dari Abrahamic traditions.",
        "origin": "~3500 years ago",
        "holy_book": "Torah (Tanakh)",
        "beliefs": ["One God", "Covenant", "Messiah will come"],
        "practices": ["Sabbath", "Kosher", "Bar/Bat Mitzvah"],
        "population": "~14 million"
    },
    "sikhism": {
        "category": "Religion",
        "definition": "Sikhisme adalah agama monoteis dari Punjab, India.",
        "founder": "Guru Nanak (1469)",
        "holy_book": "Guru Granth Sahib",
        "practices": ["5 Ks (Kesh, Kangha, Kara, Kachera, Kirpan)"],
        "beliefs": ["One God", "Equality", "Service"],
        "population": "~30 million"
    },
    "confucianism": {
        "category": "Philosophy/Religion",
        "definition": "Konfusianisme adalah sistem etika/filosofi dari China.",
        "founder": "Konfusius (551-479 BCE)",
        "teachings": ["Ren (benevolence)", "Li (ritual)", "Filial piety"],
        "influence": "Shaped East Asian culture"
    },
    "taoism": {
        "category": "Philosophy/Religion",
        "definition": "Taoisme adalah filosofi/agama dari China.",
        "founder": "Laozi (604 BCE)",
        "book": "Tao Te Ching",
        "concepts": ["Tao (The Way)", "Wu wei (non-action)", "Yin-Yang"],
        "goal": "Harmony with Tao"
    },
    "animism": {
        "category": "Religion",
        "definition": "Animisme adalah kepercayaan bahwa semua memiliki roh.",
        "beliefs": "Spirits in nature, ancestors",
        "practice": "Indigenous cultures worldwide",
        "indonesia": "Underlying many Indonesian beliefs"
    },
    
    # ============================================
    # INDONESIAN RELIGIONS
    # ============================================
    "religion_indonesia": {
        "category": "Indonesia",
        "definition": "Indonesia mengakui 6 agama resmi.",
        "religions": ["Islam (87%)", "Kristen Protestan (7%)", "Katolik (2.9%)", 
                     "Hindu (1.7%)", "Buddha (0.7%)", "Konghucu (0.05%)"],
        "pancasila": "Sila pertama: Ketuhanan Yang Maha Esa"
    },
    "kejawen": {
        "category": "Indonesia",
        "definition": "Kejawen adalah spiritualitas Jawa tradisional.",
        "elements": ["Kebatinan", "Ancestor veneration", "Harmony with universe"],
        "syncretism": "Often blended with Islam or other religions"
    },
    "balinese_hinduism": {
        "category": "Indonesia",
        "definition": "Hindu Bali adalah bentuk unik Hinduisme di Bali.",
        "features": ["Temple ceremonies", "Offerings (canang sari)", "Nyepi"],
        "beliefs": "Blend of Hinduism, Buddhism, and animism"
    },
    
    # ============================================
    # RELIGIOUS PRACTICES
    # ============================================
    "prayer": {
        "category": "Practice",
        "definition": "Doa adalah komunikasi dengan Tuhan/divine.",
        "islam": "Sholat 5 waktu",
        "christianity": "Personal prayer, Lord's Prayer",
        "buddhism": "Meditation, chanting",
        "hinduism": "Puja, mantras"
    },
    "fasting": {
        "category": "Practice",
        "definition": "Puasa adalah menahan diri dari makan untuk spiritual purposes.",
        "islam": "Ramadan (1 bulan)",
        "christianity": "Lent (40 days)",
        "judaism": "Yom Kippur",
        "hinduism": "Various fasting days"
    },
    "pilgrimage": {
        "category": "Practice",
        "definition": "Ziarah ke tempat suci.",
        "islam": "Haji ke Mekah",
        "christianity": "Jerusalem, Vatican, Lourdes",
        "hinduism": "Varanasi, Kashi",
        "buddhism": "Bodh Gaya, Lumbini"
    },
    "meditation": {
        "category": "Practice",
        "definition": "Meditasi adalah praktik fokus pikiran untuk clarity/calm.",
        "types": ["Mindfulness", "Transcendental", "Zen", "Vipassana"],
        "benefits": ["Stress reduction", "Focus", "Emotional health"]
    },
    
    # ============================================
    # RELIGIOUS LANDMARKS
    # ============================================
    "mecca": {
        "category": "Holy Place",
        "definition": "Mekah adalah kota tersuci dalam Islam.",
        "features": ["Masjidil Haram", "Ka'bah", "Hajj destination"],
        "location": "Saudi Arabia"
    },
    "jerusalem": {
        "category": "Holy Place",
        "definition": "Jerusalem adalah kota suci bagi 3 agama Abrahamik.",
        "islam": "Al-Aqsa Mosque, Dome of the Rock",
        "christianity": "Church of Holy Sepulchre",
        "judaism": "Western Wall, Temple Mount"
    },
    "vatican": {
        "category": "Holy Place",
        "definition": "Vatican adalah pusat Gereja Katolik.",
        "features": ["St. Peter's Basilica", "Sistine Chapel"],
        "leader": "Pope",
        "smallest_country": "Smallest country in the world"
    },
    "borobudur": {
        "category": "Holy Place",
        "definition": "Borobudur adalah candi Buddha terbesar di dunia.",
        "location": "Magelang, Jawa Tengah, Indonesia",
        "built": "Abad ke-8, Dinasti Syailendra",
        "structure": "10 level, 72 stupas, 504 Buddha statues"
    },
    "prambanan": {
        "category": "Holy Place",
        "definition": "Prambanan adalah candi Hindu terbesar di Indonesia.",
        "location": "Yogyakarta, Indonesia",
        "dedicated": "Trimurti (Brahma, Vishnu, Shiva)",
        "built": "Abad ke-9"
    },
    
    # ============================================
    # PHILOSOPHY OF LIFE
    # ============================================
    "golden_rule": {
        "category": "Ethics",
        "definition": "The Golden Rule: Treat others as you want to be treated.",
        "universal": "Found in virtually all religions and cultures",
        "christianity": "Do unto others as you would have them do unto you",
        "islam": "None of you believes until he wishes for his brother what he wishes for himself",
        "confucianism": "What you do not want done to yourself, do not do to others"
    },
    "karma_concept": {
        "category": "Philosophy",
        "definition": "Karma: Actions have consequences.",
        "hinduism": "Determines next life",
        "buddhism": "Shapes future experiences",
        "jainism": "Particles attach to soul",
        "pop_culture": "What goes around comes around"
    },
    "afterlife": {
        "category": "Philosophy",
        "definition": "Beliefs tentang kehidupan setelah kematian.",
        "islam": "Akhirat (Surga/Neraka)",
        "christianity": "Heaven/Hell",
        "hinduism": "Reincarnation → Moksha",
        "buddhism": "Rebirth → Nirvana",
        "atheism": "No afterlife"
    },
    "purpose_of_life": {
        "category": "Philosophy",
        "definition": "Berbagai pandangan tentang tujuan hidup.",
        "religious": "Worship God, achieve salvation/enlightenment",
        "secular": "Create meaning, help others, be happy",
        "existentialist": "Create your own meaning",
        "nihilism": "No inherent meaning"
    }
}
