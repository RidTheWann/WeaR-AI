"""
WeaR AI Knowledge - Security, Hacking, Privacy & Cybersecurity
Pengetahuan tentang keamanan digital dan cybersecurity.
Created by RidTheWann
"""

KNOWLEDGE_SECURITY = {
    # ============================================
    # SECURITY FUNDAMENTALS
    # ============================================
    "cia_triad": {
        "category": "Security",
        "definition": "CIA Triad adalah fundamental security principles.",
        "principles": {
            "Confidentiality": "Data hanya accessible oleh authorized users",
            "Integrity": "Data tidak diubah tanpa authorization",
            "Availability": "Data accessible when needed"
        }
    },
    "authentication": {
        "category": "Security",
        "definition": "Authentication memverifikasi identitas user.",
        "factors": {
            "Something you know": "Password, PIN",
            "Something you have": "Phone, security key",
            "Something you are": "Fingerprint, face"
        },
        "mfa": "Multi-Factor Authentication (2+ factors)"
    },
    "authorization": {
        "category": "Security",
        "definition": "Authorization menentukan apa yang boleh dilakukan user.",
        "vs_authentication": "Authentication = who you are, Authorization = what you can do",
        "models": ["RBAC (Role-Based)", "ABAC (Attribute-Based)", "ACL"]
    },
    "encryption": {
        "category": "Security",
        "definition": "Encryption mengubah data menjadi unreadable tanpa key.",
        "types": {
            "Symmetric": "Same key untuk encrypt/decrypt (AES)",
            "Asymmetric": "Public key + private key (RSA)"
        },
        "uses": ["HTTPS", "End-to-end messaging", "Disk encryption"]
    },
    "hashing": {
        "category": "Security",
        "definition": "Hashing mengubah data menjadi fixed-size string (one-way).",
        "algorithms": ["MD5 (broken)", "SHA-256", "bcrypt (passwords)", "Argon2"],
        "use_cases": ["Password storage", "File integrity", "Digital signatures"]
    },
    
    # ============================================
    # ATTACK TYPES
    # ============================================
    "phishing": {
        "category": "Attack",
        "definition": "Phishing adalah social engineering untuk steal credentials.",
        "methods": ["Fake emails", "Fake websites", "SMS (smishing)", "Voice (vishing)"],
        "prevention": ["Check URL carefully", "Don't click suspicious links", "Use 2FA"]
    },
    "sql_injection": {
        "category": "Attack",
        "definition": "SQL injection menyisipkan malicious SQL ke input.",
        "example": "' OR '1'='1",
        "impact": "Data theft, data modification, authentication bypass",
        "prevention": "Parameterized queries (prepared statements)"
    },
    "xss": {
        "category": "Attack",
        "definition": "XSS (Cross-Site Scripting) menyisipkan malicious scripts.",
        "types": ["Stored XSS", "Reflected XSS", "DOM-based XSS"],
        "impact": "Session hijacking, defacement, malware",
        "prevention": "Input sanitization, output encoding, CSP"
    },
    "csrf": {
        "category": "Attack",
        "definition": "CSRF (Cross-Site Request Forgery) tricks user untuk execute unwanted actions.",
        "example": "Hidden form yang submit request ke bank",
        "prevention": "CSRF tokens, SameSite cookies"
    },
    "ddos": {
        "category": "Attack",
        "definition": "DDoS (Distributed Denial of Service) overwhelming server dengan traffic.",
        "methods": ["Volumetric", "Protocol attacks", "Application layer"],
        "mitigation": "CDN, rate limiting, traffic analysis"
    },
    "man_in_the_middle": {
        "category": "Attack",
        "definition": "MITM attack intercepts communication antara dua pihak.",
        "how": "Attacker positions between victim and server",
        "prevention": "HTTPS, VPN, certificate pinning"
    },
    "brute_force": {
        "category": "Attack",
        "definition": "Brute force mencoba semua kemungkinan password.",
        "variants": ["Dictionary attack", "Credential stuffing"],
        "prevention": "Strong passwords, rate limiting, account lockout, 2FA"
    },
    "ransomware": {
        "category": "Malware",
        "definition": "Ransomware mengenkripsi files dan demands payment.",
        "famous": ["WannaCry", "NotPetya", "REvil"],
        "prevention": "Backups, updates, email security, user training"
    },
    "zero_day": {
        "category": "Attack",
        "definition": "Zero-day adalah vulnerability yang belum diketahui vendor.",
        "danger": "No patch available yet",
        "value": "Sold for millions on black market"
    },
    
    # ============================================
    # SECURITY TOOLS
    # ============================================
    "vpn": {
        "category": "Security Tool",
        "definition": "VPN (Virtual Private Network) mengenkripsi internet traffic.",
        "uses": ["Privacy", "Bypass geo-restrictions", "Secure public WiFi"],
        "providers": ["NordVPN", "ExpressVPN", "ProtonVPN", "Mullvad"],
        "caveat": "VPN provider can still see traffic"
    },
    "firewall": {
        "category": "Security Tool",
        "definition": "Firewall memfilter network traffic berdasarkan rules.",
        "types": ["Network firewall", "Host firewall", "WAF (Web Application)"],
        "actions": "Allow, block, or monitor traffic"
    },
    "antivirus": {
        "category": "Security Tool",
        "definition": "Antivirus mendeteksi dan remove malware.",
        "methods": ["Signature-based", "Heuristic", "Behavioral analysis"],
        "products": ["Windows Defender", "Malwarebytes", "Kaspersky", "Bitdefender"]
    },
    "password_manager": {
        "category": "Security Tool",
        "definition": "Password manager menyimpan dan generate strong passwords.",
        "products": ["Bitwarden", "1Password", "LastPass", "KeePass"],
        "benefit": "Unique strong password for every site"
    },
    "2fa_apps": {
        "category": "Security Tool",
        "definition": "Authenticator apps generate time-based codes.",
        "apps": ["Google Authenticator", "Authy", "Microsoft Authenticator"],
        "totp": "Time-based One-Time Password (6 digits, 30 seconds)"
    },
    
    # ============================================
    # SECURITY CONCEPTS
    # ============================================
    "zero_trust": {
        "category": "Security Concept",
        "definition": "Zero Trust: Never trust, always verify.",
        "principle": "Assume breach, verify every access request",
        "vs_traditional": "Traditional: Trust inside network"
    },
    "least_privilege": {
        "category": "Security Concept",
        "definition": "Least privilege: Give minimum access needed.",
        "example": "Intern tidak perlu admin access"
    },
    "defense_in_depth": {
        "category": "Security Concept",
        "definition": "Multiple layers of security.",
        "layers": ["Perimeter", "Network", "Host", "Application", "Data"]
    },
    "social_engineering": {
        "category": "Security Concept",
        "definition": "Manipulating people untuk reveal information.",
        "techniques": ["Phishing", "Pretexting", "Baiting", "Tailgating"],
        "defense": "Security awareness training"
    },
    "security_audit": {
        "category": "Security Concept",
        "definition": "Review of security controls dan practices.",
        "types": ["Vulnerability assessment", "Penetration testing", "Compliance audit"]
    },
    "penetration_testing": {
        "category": "Security Concept",
        "definition": "Authorized simulated attack untuk find vulnerabilities.",
        "types": ["Black box", "White box", "Grey box"],
        "phases": ["Reconnaissance", "Scanning", "Exploitation", "Reporting"]
    },
    
    # ============================================
    # PRIVACY
    # ============================================
    "data_privacy": {
        "category": "Privacy",
        "definition": "Control over personal data collection dan use.",
        "regulations": ["GDPR (EU)", "CCPA (California)", "LGPD (Brazil)"],
        "rights": ["Access", "Rectification", "Erasure", "Portability"]
    },
    "gdpr": {
        "category": "Privacy",
        "definition": "GDPR adalah EU regulation untuk data protection.",
        "applies_to": "Any company processing EU residents' data",
        "fines": "Up to €20M or 4% global revenue",
        "requirements": ["Consent", "Right to forget", "Data portability", "Breach notification"]
    },
    "cookies": {
        "category": "Privacy",
        "definition": "Cookies adalah small data files stored di browser.",
        "types": {
            "Session": "Deleted when browser closes",
            "Persistent": "Stays until expiration",
            "Third-party": "From other domains (tracking)"
        },
        "consent": "Required in EU (cookie banners)"
    },
    "tracking": {
        "category": "Privacy",
        "definition": "Websites dan apps melacak behavior user.",
        "methods": ["Cookies", "Fingerprinting", "Pixels", "Local storage"],
        "prevention": ["Privacy browsers", "Extensions (uBlock)", "VPN"]
    },
    "end_to_end_encryption": {
        "category": "Privacy",
        "definition": "E2EE: Only sender dan receiver can read messages.",
        "apps": ["Signal", "WhatsApp", "iMessage"],
        "limitation": "Provider cannot access content (even if ordered by court)"
    },
    
    # ============================================
    # HACKING CULTURE
    # ============================================
    "hacker_types": {
        "category": "Hacking",
        "definition": "Different types of hackers.",
        "types": {
            "White hat": "Ethical hackers, help find vulnerabilities",
            "Black hat": "Malicious hackers, break law",
            "Grey hat": "Between - may break law but not malicious",
            "Script kiddie": "Uses existing tools without understanding"
        }
    },
    "bug_bounty": {
        "category": "Hacking",
        "definition": "Programs that pay untuk finding vulnerabilities.",
        "platforms": ["HackerOne", "Bugcrowd", "Synack"],
        "payouts": "From $50 to $1M+ untuk critical bugs"
    },
    "ctf": {
        "category": "Hacking",
        "definition": "CTF (Capture The Flag) adalah security competition.",
        "types": ["Jeopardy (challenges)", "Attack-Defense"],
        "skills": "Web, crypto, forensics, reverse engineering, pwn"
    },
    "kali_linux": {
        "category": "Hacking",
        "definition": "Kali Linux adalah OS untuk penetration testing.",
        "tools": "Hundreds of security tools pre-installed",
        "use": "By security professionals dan students"
    },
    
    # ============================================
    # SECURITY CERTIFICATIONS
    # ============================================
    "security_certs": {
        "category": "Career",
        "definition": "Popular cybersecurity certifications.",
        "entry": ["CompTIA Security+", "CEH (Certified Ethical Hacker)"],
        "intermediate": ["SSCP", "CySA+"],
        "advanced": ["CISSP", "OSCP", "CISM"],
        "oscp": "Offensive Security Certified Professional (hands-on exam)"
    },
    
    # ============================================
    # FAMOUS HACKS
    # ============================================
    "famous_hacks": {
        "category": "History",
        "definition": "Notable security breaches dalam sejarah.",
        "incidents": {
            "Yahoo 2013": "3 billion accounts breached",
            "Equifax 2017": "147 million SSNs exposed",
            "SolarWinds 2020": "Supply chain attack, hit US government",
            "Colonial Pipeline 2021": "Ransomware shut down fuel pipeline",
            "Log4j 2021": "Massive vulnerability in logging library"
        }
    },
    "famous_hackers": {
        "category": "History",
        "definition": "Notable hackers dalam sejarah.",
        "people": {
            "Kevin Mitnick": "Most wanted hacker in 90s, now security consultant",
            "Adrian Lamo": "Hacked NYT, reported Chelsea Manning",
            "Gary McKinnon": "Hacked US military looking for UFO info",
            "Anonymous": "Hacktivist collective"
        }
    }
}
