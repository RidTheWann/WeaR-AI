"""
WeaR AI Knowledge - Computers, Hardware, Operating Systems & Tech Products
Pengetahuan tentang komputer, hardware, dan OS.
Created by RidTheWann
"""

KNOWLEDGE_COMPUTERS = {
    # ============================================
    # COMPUTER COMPONENTS
    # ============================================
    "cpu": {
        "category": "Hardware",
        "definition": "CPU (Central Processing Unit) adalah otak komputer.",
        "function": "Menjalankan instruksi dan kalkulasi",
        "specs": ["Clock speed (GHz)", "Cores", "Threads", "Cache"],
        "brands": ["Intel (Core i3/i5/i7/i9)", "AMD (Ryzen 3/5/7/9)", "Apple (M1/M2/M3)"],
        "architecture": ["x86-64", "ARM"]
    },
    "gpu": {
        "category": "Hardware",
        "definition": "GPU (Graphics Processing Unit) untuk rendering grafis dan AI.",
        "use_cases": ["Gaming", "3D rendering", "AI/ML training", "Crypto mining"],
        "brands": ["NVIDIA (GeForce RTX)", "AMD (Radeon RX)", "Intel (Arc)"],
        "vram": "Video RAM untuk storing textures/data"
    },
    "ram": {
        "category": "Hardware",
        "definition": "RAM (Random Access Memory) adalah temporary storage untuk running programs.",
        "volatile": "Data hilang saat power off",
        "types": ["DDR4", "DDR5"],
        "recommendations": {
            "Basic use": "8GB",
            "Programming": "16GB",
            "Heavy work": "32GB+",
            "AI/ML": "64GB+"
        }
    },
    "storage": {
        "category": "Hardware",
        "definition": "Storage menyimpan data secara permanen.",
        "types": {
            "HDD": "Hard Disk Drive - slower, cheaper, higher capacity",
            "SSD": "Solid State Drive - faster, more expensive",
            "NVMe": "Fastest SSD via PCIe connection"
        },
        "speed": "NVMe > SATA SSD > HDD"
    },
    "motherboard": {
        "category": "Hardware",
        "definition": "Motherboard menghubungkan semua komponen komputer.",
        "components": ["CPU socket", "RAM slots", "PCIe slots", "SATA ports", "USB ports"],
        "form_factors": ["ATX", "Micro-ATX", "Mini-ITX"]
    },
    "power_supply": {
        "category": "Hardware",
        "definition": "PSU (Power Supply Unit) menyuplai daya ke komponen.",
        "rating": "80 Plus certification (efficiency)",
        "wattage": "Sesuaikan dengan kebutuhan GPU + CPU"
    },
    "cooling": {
        "category": "Hardware",
        "definition": "Cooling system menjaga suhu komponen.",
        "types": ["Air cooler", "AIO liquid cooler", "Custom water cooling"],
        "importance": "Overheating = throttling = slower performance"
    },
    
    # ============================================
    # OPERATING SYSTEMS
    # ============================================
    "windows_os": {
        "category": "Operating System",
        "definition": "Windows adalah OS paling populer untuk PC.",
        "developer": "Microsoft",
        "versions": ["Windows 11", "Windows 10", "Windows 7"],
        "market_share": "~70% desktop OS",
        "strengths": ["Software compatibility", "Gaming", "Enterprise"]
    },
    "macos": {
        "category": "Operating System",
        "definition": "macOS adalah OS untuk Mac computers.",
        "developer": "Apple",
        "versions": ["Sonoma", "Ventura", "Monterey"],
        "based_on": "Unix (Darwin kernel)",
        "strengths": ["Design/creative work", "Development", "Ecosystem"]
    },
    "linux_os": {
        "category": "Operating System",
        "definition": "Linux adalah free, open-source OS.",
        "creator": "Linus Torvalds (1991)",
        "distributions": ["Ubuntu", "Fedora", "Debian", "Arch", "CentOS"],
        "use_cases": ["Servers", "Development", "Embedded systems"],
        "market_share": "~96% web servers"
    },
    "ubuntu": {
        "category": "Operating System",
        "definition": "Ubuntu adalah distribusi Linux paling populer.",
        "developer": "Canonical",
        "based_on": "Debian",
        "beginner_friendly": True,
        "versions": "LTS (Long Term Support) releases setiap 2 tahun"
    },
    "android_os": {
        "category": "Operating System",
        "definition": "Android adalah mobile OS untuk smartphones.",
        "developer": "Google",
        "based_on": "Linux kernel",
        "market_share": "~70% mobile OS globally",
        "open_source": "AOSP (Android Open Source Project)"
    },
    "ios_os": {
        "category": "Operating System",
        "definition": "iOS adalah mobile OS untuk iPhone.",
        "developer": "Apple",
        "based_on": "Darwin (like macOS)",
        "closed": "Tidak open source",
        "market_share": "~27% mobile (higher in USA)"
    },
    
    # ============================================
    # LAPTOP/COMPUTER TYPES
    # ============================================
    "laptop_types": {
        "category": "Computer",
        "definition": "Berbagai jenis laptop untuk kebutuhan berbeda.",
        "types": {
            "Ultrabook": "Thin, light, portable (MacBook Air, Dell XPS)",
            "Gaming laptop": "Powerful GPU, cooling (ROG, Razer)",
            "Workstation": "Professional work (ThinkPad, Precision)",
            "2-in-1": "Laptop + tablet (Surface Pro)",
            "Chromebook": "Chrome OS, cloud-focused, affordable"
        }
    },
    "desktop_vs_laptop": {
        "category": "Computer",
        "definition": "Perbandingan desktop dan laptop.",
        "desktop": {
            "pros": ["More powerful", "Upgradeable", "Better cooling", "Cheaper per performance"],
            "cons": ["Not portable", "Needs monitor/peripherals"]
        },
        "laptop": {
            "pros": ["Portable", "All-in-one", "Battery powered"],
            "cons": ["Limited upgrades", "Thermal throttling", "More expensive"]
        }
    },
    
    # ============================================
    # SMARTPHONES
    # ============================================
    "iphone": {
        "category": "Smartphone",
        "definition": "iPhone adalah smartphone premium dari Apple.",
        "first": "iPhone (2007) - revolutionized smartphones",
        "latest": "iPhone 15 series",
        "features": ["iOS", "App Store", "Apple ecosystem", "Privacy focus"]
    },
    "samsung_galaxy": {
        "category": "Smartphone",
        "definition": "Samsung Galaxy adalah line smartphone Android populer.",
        "series": ["S series (flagship)", "A series (mid-range)", "Z series (foldable)"],
        "os": "Android with One UI"
    },
    "xiaomi": {
        "category": "Smartphone",
        "definition": "Xiaomi adalah brand China dengan value flagship.",
        "series": ["Mi", "Redmi (budget)", "Poco (value flagship)"],
        "ecosystem": "Smart home devices juga"
    },
    
    # ============================================
    # PERIPHERALS
    # ============================================
    "mechanical_keyboard": {
        "category": "Peripheral",
        "definition": "Mechanical keyboard menggunakan switch individual per key.",
        "switches": {
            "Cherry MX Blue": "Clicky, tactile (typing)",
            "Cherry MX Red": "Linear, smooth (gaming)",
            "Cherry MX Brown": "Tactile, quiet (versatile)"
        },
        "benefits": ["Durability", "Feel", "Customization"]
    },
    "monitor": {
        "category": "Peripheral",
        "definition": "Monitor adalah display untuk komputer.",
        "specs": {
            "Resolution": "1080p, 1440p, 4K, 8K",
            "Refresh rate": "60Hz (standard), 144Hz+ (gaming)",
            "Panel": "IPS (color), VA (contrast), TN (speed)",
            "Response time": "Lower is better (1ms gaming)"
        }
    },
    "mouse": {
        "category": "Peripheral",
        "definition": "Mouse adalah input device untuk pointing.",
        "types": ["Wired", "Wireless", "Gaming", "Ergonomic", "Trackball"],
        "specs": ["DPI (sensitivity)", "Polling rate", "Weight"]
    },
    
    # ============================================
    # NETWORKING HARDWARE
    # ============================================
    "router": {
        "category": "Networking",
        "definition": "Router menghubungkan devices ke internet.",
        "function": "Mengarahkan traffic antar networks",
        "features": ["WiFi (802.11ac, WiFi 6)", "Ethernet ports", "QoS"]
    },
    "modem": {
        "category": "Networking",
        "definition": "Modem mengubah sinyal ISP ke data digital.",
        "types": ["Cable modem", "DSL modem", "Fiber ONT"],
        "vs_router": "Modem connects to ISP, router distributes to devices"
    },
    "network_switch": {
        "category": "Networking",
        "definition": "Switch menghubungkan devices dalam local network.",
        "vs_hub": "Switch is smarter - sends data only to intended device"
    },
    "ethernet": {
        "category": "Networking",
        "definition": "Ethernet adalah wired network connection.",
        "speeds": ["100Mbps (Fast Ethernet)", "1Gbps (Gigabit)", "10Gbps"],
        "cable": "Cat5e (1Gbps), Cat6 (10Gbps short), Cat6a/7 (10Gbps+)"
    },
    "wifi": {
        "category": "Networking",
        "definition": "WiFi adalah wireless network technology.",
        "standards": {
            "802.11n (WiFi 4)": "Up to 600Mbps",
            "802.11ac (WiFi 5)": "Up to 3.5Gbps",
            "802.11ax (WiFi 6)": "Up to 9.6Gbps, better in crowds"
        },
        "bands": ["2.4GHz (range)", "5GHz (speed)", "6GHz (WiFi 6E)"]
    },
    
    # ============================================
    # CLOUD SERVICES
    # ============================================
    "aws": {
        "category": "Cloud",
        "definition": "AWS (Amazon Web Services) adalah cloud provider terbesar.",
        "market_share": "~32%",
        "services": ["EC2 (compute)", "S3 (storage)", "Lambda (serverless)", "RDS (database)"],
        "regions": "30+ regions globally"
    },
    "azure": {
        "category": "Cloud",
        "definition": "Azure adalah cloud platform Microsoft.",
        "market_share": "~22%",
        "strengths": ["Enterprise", "Microsoft integration", "Hybrid cloud"]
    },
    "gcp": {
        "category": "Cloud",
        "definition": "GCP (Google Cloud Platform) adalah cloud service Google.",
        "market_share": "~10%",
        "strengths": ["Data analytics", "ML/AI", "Kubernetes (invented by Google)"]
    },
    "cloud_computing": {
        "category": "Cloud",
        "definition": "Cloud computing menyediakan resources on-demand via internet.",
        "models": {
            "IaaS": "Infrastructure (VMs, storage)",
            "PaaS": "Platform (development environment)",
            "SaaS": "Software (Gmail, Office 365)"
        },
        "benefits": ["Scalability", "Cost efficiency", "Accessibility"]
    },
    
    # ============================================
    # TECH PRODUCTS
    # ============================================
    "tesla_car": {
        "category": "Tech",
        "definition": "Tesla adalah electric vehicle company.",
        "models": ["Model S", "Model 3", "Model X", "Model Y", "Cybertruck"],
        "features": ["Autopilot", "Supercharger network", "OTA updates"],
        "ceo": "Elon Musk"
    },
    "apple_watch": {
        "category": "Tech",
        "definition": "Apple Watch adalah smartwatch populer.",
        "features": ["Health tracking", "Notifications", "Apple Pay", "ECG"],
        "os": "watchOS"
    },
    "smart_home": {
        "category": "Tech",
        "definition": "Smart home menghubungkan devices untuk automation.",
        "assistants": ["Alexa (Amazon)", "Google Assistant", "Siri (Apple)"],
        "devices": ["Smart lights", "Smart locks", "Thermostats", "Cameras"],
        "protocols": ["WiFi", "Zigbee", "Z-Wave", "Thread/Matter"]
    },
    "vr_headset": {
        "category": "Tech",
        "definition": "VR headset untuk virtual reality experience.",
        "products": ["Meta Quest", "PlayStation VR", "Valve Index", "Apple Vision Pro"],
        "ar_vs_vr": "VR = full immersion, AR = overlay on real world"
    },
    
    # ============================================
    # GAMING CONSOLES
    # ============================================
    "playstation": {
        "category": "Gaming",
        "definition": "PlayStation adalah console gaming dari Sony.",
        "latest": "PlayStation 5 (2020)",
        "exclusives": ["God of War", "Spider-Man", "The Last of Us", "Horizon"],
        "online": "PlayStation Plus"
    },
    "xbox": {
        "category": "Gaming",
        "definition": "Xbox adalah console gaming dari Microsoft.",
        "latest": "Xbox Series X/S (2020)",
        "exclusives": ["Halo", "Forza", "Gears of War"],
        "service": "Xbox Game Pass (subscription)"
    },
    "nintendo_switch": {
        "category": "Gaming",
        "definition": "Nintendo Switch adalah hybrid console (portable + TV).",
        "released": "2017",
        "exclusives": ["Zelda", "Mario", "Pokemon", "Animal Crossing"],
        "innovation": "First successful hybrid console"
    },
    "steam_deck": {
        "category": "Gaming",
        "definition": "Steam Deck adalah handheld PC gaming dari Valve.",
        "os": "SteamOS (Linux-based)",
        "plays": "PC games on the go",
        "released": "2022"
    }
}
