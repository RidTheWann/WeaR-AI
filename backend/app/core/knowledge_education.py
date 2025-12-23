"""
WeaR AI Knowledge - Education, Learning & Study Tips
Pengetahuan tentang pendidikan, belajar, dan study tips.
Created by RidTheWann
"""

KNOWLEDGE_EDUCATION = {
    # ============================================
    # STUDY TECHNIQUES
    # ============================================
    "study_techniques": {
        "category": "Learning",
        "definition": "Teknik belajar yang efektif.",
        "techniques": {
            "Active recall": "Test yourself instead of re-reading",
            "Spaced repetition": "Review at increasing intervals",
            "Pomodoro": "25 min focus, 5 min break",
            "Feynman technique": "Explain in simple terms",
            "Mind mapping": "Visual connections between concepts"
        }
    },
    "active_recall": {
        "category": "Learning",
        "definition": "Active recall adalah mengingat informasi tanpa melihat notes.",
        "methods": [
            "Flashcards (Anki app)",
            "Practice tests",
            "Teach someone else",
            "Write from memory"
        ],
        "why_works": "Forces brain to strengthen neural pathways"
    },
    "spaced_repetition": {
        "category": "Learning",
        "definition": "Spaced repetition adalah review dengan interval meningkat.",
        "schedule": "1 day → 3 days → 1 week → 2 weeks → 1 month",
        "apps": ["Anki", "Quizlet", "Memrise"],
        "forgetting_curve": "Ebbinghaus - we forget quickly without review"
    },
    "feynman_technique": {
        "category": "Learning",
        "definition": "Feynman technique adalah menjelaskan konsep dengan sederhana.",
        "steps": [
            "Pick a concept",
            "Explain it to a 12-year-old",
            "Identify gaps in your explanation",
            "Review and simplify"
        ],
        "named_after": "Richard Feynman, physicist"
    },
    "note_taking": {
        "category": "Learning",
        "definition": "Metode mencatat yang efektif.",
        "methods": {
            "Cornell method": "Divide page: notes, cues, summary",
            "Mind maps": "Visual, connects ideas",
            "Outline method": "Hierarchical bullet points",
            "Zettelkasten": "Linked notes system"
        },
        "digital": "Notion, Obsidian, Roam Research"
    },
    "concentration": {
        "category": "Learning",
        "definition": "Tips meningkatkan konsentrasi.",
        "tips": [
            "Eliminate distractions (phone away)",
            "Set specific goals for session",
            "Take regular breaks",
            "Study at your peak hours",
            "Stay hydrated and fed",
            "Use focus music/white noise"
        ]
    },
    "memory_palace": {
        "category": "Learning",
        "definition": "Memory palace adalah teknik menghafal dengan visualisasi lokasi.",
        "steps": [
            "Choose a familiar place",
            "Create mental path through it",
            "Place items to remember along path",
            "Walk through mentally to recall"
        ],
        "used_by": "Memory champions, ancient Greeks"
    },
    "procrastination": {
        "category": "Learning",
        "definition": "Cara mengatasi prokrastinasi.",
        "tips": [
            "Break tasks into small steps",
            "Start with just 2 minutes",
            "Remove distractions",
            "Set deadlines",
            "Reward yourself",
            "Understand why you procrastinate"
        ]
    },
    
    # ============================================
    # EDUCATION SYSTEMS
    # ============================================
    "indonesia_education": {
        "category": "Education System",
        "definition": "Sistem pendidikan Indonesia.",
        "levels": {
            "SD": "Sekolah Dasar (Elementary) - 6 years",
            "SMP": "Sekolah Menengah Pertama (Junior High) - 3 years",
            "SMA/SMK": "Senior High/Vocational - 3 years",
            "PT": "Perguruan Tinggi (University) - 4+ years"
        },
        "curriculum": "Kurikulum Merdeka (current)"
    },
    "university_degrees": {
        "category": "Education System",
        "definition": "Jenjang pendidikan tinggi.",
        "degrees": {
            "S1 (Sarjana)": "Bachelor's degree - 4 years",
            "S2 (Magister)": "Master's degree - 2 years",
            "S3 (Doktor)": "Doctoral/PhD - 3-5 years",
            "D3 (Diploma)": "Associate degree - 3 years"
        }
    },
    "top_universities": {
        "category": "Education",
        "definition": "Universitas top di dunia dan Indonesia.",
        "global": ["MIT", "Stanford", "Harvard", "Cambridge", "Oxford"],
        "indonesia": ["UI", "ITB", "UGM", "Unair", "IPB", "ITS"],
        "rankings": "QS World Rankings, THE Rankings"
    },
    "scholarships": {
        "category": "Education",
        "definition": "Beasiswa untuk melanjutkan pendidikan.",
        "indonesia": {
            "LPDP": "Government scholarship for Masters/PhD",
            "Beasiswa Unggulan": "Kemendikbud scholarship",
            "Djarum": "Private foundation scholarship"
        },
        "international": ["Fulbright (USA)", "Chevening (UK)", "DAAD (Germany)", "MEXT (Japan)"]
    },
    
    # ============================================
    # ONLINE LEARNING
    # ============================================
    "online_learning": {
        "category": "Education",
        "definition": "Platform belajar online.",
        "platforms": {
            "Coursera": "University courses, certificates",
            "edX": "Harvard, MIT courses",
            "Udemy": "Skill-based courses",
            "Khan Academy": "Free K-12 education",
            "Codecademy": "Programming courses",
            "YouTube": "Free everything"
        }
    },
    "mooc": {
        "category": "Education",
        "definition": "MOOC (Massive Open Online Course) adalah kursus online terbuka.",
        "benefits": ["Free or low cost", "Flexible schedule", "World-class content"],
        "downsides": ["Low completion rates", "Less structured", "No face-to-face"]
    },
    "self_learning": {
        "category": "Education",
        "definition": "Tips belajar mandiri (autodidact).",
        "tips": [
            "Set clear learning goals",
            "Create structured curriculum",
            "Build projects to apply knowledge",
            "Find communities (Discord, Reddit)",
            "Teach others what you learn",
            "Be consistent"
        ]
    },
    
    # ============================================
    # LANGUAGE LEARNING
    # ============================================
    "language_learning": {
        "category": "Learning",
        "definition": "Tips belajar bahasa baru.",
        "methods": {
            "Immersion": "Surround yourself with the language",
            "Spaced repetition": "Vocab cards (Anki)",
            "Comprehensible input": "Content slightly above level",
            "Speaking practice": "iTalki, language exchange",
            "Consume media": "Movies, music, podcasts"
        }
    },
    "language_apps": {
        "category": "Learning",
        "definition": "Aplikasi untuk belajar bahasa.",
        "apps": {
            "Duolingo": "Gamified, good for beginners",
            "Anki": "Flashcards with spaced repetition",
            "HelloTalk": "Language exchange with natives",
            "Tandem": "Language partner matching",
            "Pimsleur": "Audio-based learning"
        }
    },
    "cefr_levels": {
        "category": "Learning",
        "definition": "CEFR adalah standar level kemampuan bahasa.",
        "levels": {
            "A1": "Beginner - basic phrases",
            "A2": "Elementary - simple conversations",
            "B1": "Intermediate - independent user",
            "B2": "Upper Intermediate - fluent conversation",
            "C1": "Advanced - complex texts",
            "C2": "Mastery - native-like"
        }
    },
    
    # ============================================
    # EXAMS & TESTS
    # ============================================
    "exam_prep": {
        "category": "Education",
        "definition": "Tips persiapan ujian.",
        "tips": [
            "Start early, don't cram",
            "Practice with past papers",
            "Teach material to others",
            "Get enough sleep before exam",
            "Use active recall",
            "Take care of health"
        ]
    },
    "standardized_tests": {
        "category": "Education",
        "definition": "Tes standar internasional.",
        "tests": {
            "TOEFL/IELTS": "English proficiency",
            "GRE": "Graduate school (USA)",
            "GMAT": "Business school",
            "SAT/ACT": "US undergraduate",
            "JLPT": "Japanese proficiency"
        }
    },
    "toefl_ielts": {
        "category": "Education",
        "definition": "Tes kemampuan bahasa Inggris.",
        "toefl": {
            "format": "iBT (internet-based), 4 sections",
            "score": "0-120",
            "accepted": "Mainly USA universities"
        },
        "ielts": {
            "format": "Academic or General, 4 sections",
            "score": "0-9 band",
            "accepted": "UK, Australia, widely accepted"
        }
    },
    
    # ============================================
    # SKILLS
    # ============================================
    "21st_century_skills": {
        "category": "Skills",
        "definition": "Skill penting di abad 21.",
        "skills": {
            "Critical thinking": "Analyze, evaluate, solve problems",
            "Creativity": "Generate new ideas",
            "Collaboration": "Work effectively with others",
            "Communication": "Express ideas clearly",
            "Digital literacy": "Navigate technology",
            "Adaptability": "Embrace change"
        }
    },
    "growth_mindset": {
        "category": "Learning",
        "definition": "Growth mindset vs Fixed mindset.",
        "growth": "Abilities can be developed through effort",
        "fixed": "Abilities are static and unchangeable",
        "developed_by": "Carol Dweck research",
        "benefits": "Embraces challenges, persists through obstacles"
    },
    "learning_styles": {
        "category": "Learning",
        "definition": "Gaya belajar berbeda (controversial).",
        "types": {
            "Visual": "Learn through seeing",
            "Auditory": "Learn through hearing",
            "Kinesthetic": "Learn through doing",
            "Read/Write": "Learn through reading/writing"
        },
        "note": "Scientific evidence is mixed - best to use multiple approaches"
    },
    
    # ============================================
    # TEACHING
    # ============================================
    "teaching_methods": {
        "category": "Education",
        "definition": "Metode pengajaran.",
        "methods": {
            "Lecture": "Traditional, teacher-centered",
            "Discussion": "Interactive, student participation",
            "Project-based": "Learn by doing projects",
            "Flipped classroom": "Watch at home, practice in class",
            "Gamification": "Learning through games"
        }
    },
    "tutoring": {
        "category": "Education",
        "definition": "Tips menjadi tutor yang baik.",
        "tips": [
            "Assess student's level first",
            "Ask questions, don't just tell",
            "Use analogies and examples",
            "Be patient",
            "Encourage mistakes as learning",
            "Give positive reinforcement"
        ]
    }
}
