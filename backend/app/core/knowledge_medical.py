"""
WeaR AI Knowledge - Medicine, Health & Medical Science
Pengetahuan tentang kesehatan dan ilmu kedokteran.
Created by RidTheWann
"""

KNOWLEDGE_MEDICAL = {
    # ============================================
    # HUMAN BODY SYSTEMS
    # ============================================
    "cardiovascular_system": {
        "category": "Human Body",
        "definition": "Sistem kardiovaskular adalah sistem peredaran darah.",
        "components": ["Heart", "Blood vessels (arteries, veins, capillaries)", "Blood"],
        "function": "Transport oxygen, nutrients, hormones; remove waste",
        "heart_rate": "60-100 bpm (resting adult)"
    },
    "respiratory_system": {
        "category": "Human Body",
        "definition": "Sistem pernapasan mengambil oksigen dan mengeluarkan CO2.",
        "components": ["Lungs", "Trachea", "Bronchi", "Diaphragm"],
        "breathing_rate": "12-20 breaths/min (adult)",
        "lung_capacity": "~6 liters"
    },
    "nervous_system": {
        "category": "Human Body",
        "definition": "Sistem saraf mengontrol semua fungsi tubuh.",
        "parts": {
            "CNS": "Central Nervous System (brain, spinal cord)",
            "PNS": "Peripheral Nervous System (nerves throughout body)"
        },
        "neurons": "86 billion neurons in human brain"
    },
    "digestive_system": {
        "category": "Human Body",
        "definition": "Sistem pencernaan memproses makanan menjadi nutrisi.",
        "organs": ["Mouth", "Esophagus", "Stomach", "Small intestine", "Large intestine", "Liver", "Pancreas"],
        "duration": "24-72 hours to fully digest food"
    },
    "immune_system": {
        "category": "Human Body",
        "definition": "Sistem imun melindungi tubuh dari patogen.",
        "components": ["White blood cells", "Lymph nodes", "Thymus", "Spleen", "Antibodies"],
        "types": ["Innate immunity", "Adaptive immunity"]
    },
    "endocrine_system": {
        "category": "Human Body",
        "definition": "Sistem endokrin mengatur hormon.",
        "glands": ["Pituitary", "Thyroid", "Adrenal", "Pancreas", "Gonads"],
        "hormones": ["Insulin", "Cortisol", "Testosterone", "Estrogen", "Adrenaline"]
    },
    "skeletal_system": {
        "category": "Human Body",
        "definition": "Sistem rangka memberikan struktur tubuh.",
        "bones": "206 bones in adult human",
        "functions": ["Support", "Protection", "Movement", "Blood cell production", "Mineral storage"]
    },
    "muscular_system": {
        "category": "Human Body",
        "definition": "Sistem otot memungkinkan gerakan.",
        "types": {
            "Skeletal": "Voluntary movement",
            "Cardiac": "Heart muscle",
            "Smooth": "Internal organs"
        },
        "muscles": "600+ muscles in human body"
    },
    
    # ============================================
    # COMMON DISEASES
    # ============================================
    "diabetes": {
        "category": "Disease",
        "definition": "Diabetes adalah penyakit metabolik dengan kadar gula darah tinggi.",
        "types": {
            "Type 1": "Autoimmune, body doesn't produce insulin",
            "Type 2": "Body doesn't use insulin properly (most common)"
        },
        "management": "Diet, exercise, medication, insulin",
        "complications": "Heart disease, kidney damage, vision problems"
    },
    "hypertension": {
        "category": "Disease",
        "definition": "Hipertensi adalah tekanan darah tinggi.",
        "normal": "<120/80 mmHg",
        "high": ">130/80 mmHg",
        "risks": ["Heart attack", "Stroke", "Kidney disease"],
        "causes": ["Genetics", "Diet (salt)", "Obesity", "Stress"]
    },
    "heart_disease": {
        "category": "Disease",
        "definition": "Penyakit jantung adalah penyebab kematian #1 di dunia.",
        "types": ["Coronary artery disease", "Heart failure", "Arrhythmia"],
        "prevention": ["Healthy diet", "Exercise", "No smoking", "Manage stress"],
        "warning_signs": "Chest pain, shortness of breath, fatigue"
    },
    "cancer": {
        "category": "Disease",
        "definition": "Kanker adalah pertumbuhan sel abnormal yang tidak terkontrol.",
        "common_types": ["Lung", "Breast", "Colorectal", "Prostate", "Skin"],
        "treatment": ["Surgery", "Chemotherapy", "Radiation", "Immunotherapy"],
        "prevention": "Avoid tobacco, healthy diet, exercise, screening"
    },
    "stroke": {
        "category": "Disease",
        "definition": "Stroke adalah gangguan aliran darah ke otak.",
        "types": ["Ischemic (blood clot)", "Hemorrhagic (bleeding)"],
        "fast_symptoms": "Face drooping, Arm weakness, Speech difficulty, Time to call emergency",
        "time_critical": "Golden hour - treatment within hours crucial"
    },
    "asthma": {
        "category": "Disease",
        "definition": "Asma adalah penyakit pernapasan kronis.",
        "symptoms": ["Wheezing", "Coughing", "Shortness of breath", "Chest tightness"],
        "triggers": ["Allergens", "Exercise", "Cold air", "Stress"],
        "treatment": "Bronchodilators, inhaled steroids"
    },
    "covid19": {
        "category": "Disease",
        "definition": "COVID-19 adalah penyakit pernapasan dari coronavirus SARS-CoV-2.",
        "emerged": "Wuhan, China, late 2019",
        "pandemic": "Declared pandemic March 2020",
        "variants": ["Alpha", "Beta", "Delta", "Omicron"],
        "prevention": "Vaccination, masks, distancing"
    },
    "dementia_alzheimers": {
        "category": "Disease",
        "definition": "Demensia adalah penurunan fungsi kognitif, Alzheimer penyebab utamanya.",
        "symptoms": ["Memory loss", "Confusion", "Difficulty with daily tasks"],
        "risk_factors": ["Age", "Genetics", "Head injury"],
        "prevention": "Mental activity, social engagement, exercise, healthy diet"
    },
    
    # ============================================
    # NUTRITION
    # ============================================
    "macronutrients": {
        "category": "Nutrition",
        "definition": "Makronutrien adalah nutrisi yang dibutuhkan dalam jumlah besar.",
        "types": {
            "Carbohydrates": "Energy source (4 cal/g)",
            "Proteins": "Building blocks, repair (4 cal/g)",
            "Fats": "Energy storage, hormones (9 cal/g)"
        }
    },
    "vitamins": {
        "category": "Nutrition",
        "definition": "Vitamin adalah nutrisi penting untuk fungsi tubuh.",
        "water_soluble": ["C", "B-complex"],
        "fat_soluble": ["A", "D", "E", "K"],
        "deficiency": "Can cause various diseases"
    },
    "minerals": {
        "category": "Nutrition",
        "definition": "Mineral adalah nutrisi anorganik penting.",
        "major": ["Calcium", "Phosphorus", "Potassium", "Sodium", "Magnesium"],
        "trace": ["Iron", "Zinc", "Iodine", "Selenium"]
    },
    "hydration": {
        "category": "Nutrition",
        "definition": "Hidrasi penting untuk semua fungsi tubuh.",
        "recommendation": "~8 glasses (2 liters) per day",
        "body_water": "60% of adult body is water",
        "functions": "Temperature regulation, nutrient transport, waste removal"
    },
    "calories": {
        "category": "Nutrition",
        "definition": "Kalori adalah unit energi dari makanan.",
        "average_needs": "2000-2500 cal/day (varies by age, sex, activity)",
        "weight_gain": "Excess calories stored as fat",
        "weight_loss": "Calorie deficit needed (safely 500-1000 cal/day deficit)"
    },
    
    # ============================================
    # MENTAL HEALTH
    # ============================================
    "depression": {
        "category": "Mental Health",
        "definition": "Depresi adalah gangguan mood yang serius.",
        "symptoms": ["Persistent sadness", "Loss of interest", "Fatigue", "Sleep changes", "Hopelessness"],
        "treatment": ["Therapy (CBT)", "Medication (antidepressants)", "Lifestyle changes"],
        "help": "Seek professional help - it's treatable"
    },
    "anxiety_disorder": {
        "category": "Mental Health",
        "definition": "Gangguan kecemasan melibatkan kekhawatiran berlebihan.",
        "types": ["Generalized anxiety", "Panic disorder", "Social anxiety", "Phobias"],
        "symptoms": ["Excessive worry", "Restlessness", "Racing heart", "Tension"],
        "treatment": ["CBT", "Medication", "Relaxation techniques"]
    },
    "stress_management": {
        "category": "Mental Health",
        "definition": "Cara mengelola stres.",
        "techniques": [
            "Exercise regularly",
            "Sleep enough",
            "Deep breathing",
            "Meditation/mindfulness",
            "Social support",
            "Time management"
        ]
    },
    "sleep_health": {
        "category": "Mental Health",
        "definition": "Tidur yang cukup penting untuk kesehatan.",
        "recommended": "7-9 hours for adults",
        "stages": ["Light sleep", "Deep sleep", "REM sleep"],
        "tips": ["Consistent schedule", "Dark room", "No screens before bed", "Limit caffeine"]
    },
    
    # ============================================
    # MEDICATIONS
    # ============================================
    "antibiotics": {
        "category": "Medication",
        "definition": "Antibiotik membunuh atau menghambat bakteri.",
        "examples": ["Amoxicillin", "Azithromycin", "Ciprofloxacin"],
        "warning": "Not effective against viruses",
        "resistance": "Overuse creates resistant bacteria - finish full course"
    },
    "painkillers": {
        "category": "Medication",
        "definition": "Obat penghilang rasa sakit.",
        "types": {
            "OTC": "Paracetamol, Ibuprofen, Aspirin",
            "Prescription": "Codeine, Tramadol, Morphine"
        },
        "warning": "Follow dosage instructions, addiction risk with opioids"
    },
    "vaccines": {
        "category": "Medication",
        "definition": "Vaksin mengajarkan sistem imun melawan patogen.",
        "how_works": "Contains weakened/inactive pathogen or parts",
        "herd_immunity": "Protects those who can't be vaccinated",
        "common": ["MMR", "Tetanus", "Flu", "COVID", "Hepatitis"]
    },
    
    # ============================================
    # FIRST AID
    # ============================================
    "cpr": {
        "category": "First Aid",
        "definition": "CPR (Cardiopulmonary Resuscitation) untuk serangan jantung.",
        "steps": [
            "Call emergency (118/119)",
            "Check responsiveness",
            "Begin chest compressions (100-120/min)",
            "30 compressions, 2 rescue breaths"
        ],
        "hands_only": "Continuous chest compressions if untrained"
    },
    "choking": {
        "category": "First Aid",
        "definition": "Cara menangani tersedak.",
        "heimlich": [
            "Stand behind person",
            "Wrap arms around waist",
            "Make fist above navel",
            "Quick upward thrusts"
        ]
    },
    "burns": {
        "category": "First Aid",
        "definition": "Penanganan luka bakar.",
        "degrees": ["1st (superficial)", "2nd (blisters)", "3rd (severe)"],
        "treatment": "Cool with running water (10-20 min), cover, seek medical help"
    },
    "bleeding": {
        "category": "First Aid",
        "definition": "Penanganan pendarahan.",
        "steps": [
            "Apply pressure with clean cloth",
            "Elevate injured area",
            "Continue pressure until bleeding stops",
            "Call emergency if severe"
        ]
    },
    
    # ============================================
    # INDONESIA HEALTHCARE
    # ============================================
    "bpjs_kesehatan": {
        "category": "Indonesia",
        "definition": "BPJS Kesehatan adalah asuransi kesehatan nasional Indonesia.",
        "coverage": "Hospitalization, outpatient, medication",
        "tiers": ["Kelas 1", "Kelas 2", "Kelas 3"],
        "facilities": "Puskesmas, Rumah Sakit"
    },
    "puskesmas": {
        "category": "Indonesia",
        "definition": "Puskesmas adalah fasilitas kesehatan tingkat pertama.",
        "services": "General check-up, immunization, maternal care",
        "location": "Setiap kecamatan memiliki puskesmas"
    }
}
