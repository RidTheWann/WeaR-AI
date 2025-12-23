"""
WeaR AI Knowledge - Psychology, Mindset & Mental Wellness
Pengetahuan tentang psikologi dan kesejahteraan mental.
Created by RidTheWann
"""

KNOWLEDGE_PSYCHOLOGY = {
    # ============================================
    # PSYCHOLOGY BASICS
    # ============================================
    "psychology_fields": {
        "category": "Psychology",
        "definition": "Cabang-cabang psikologi.",
        "fields": {
            "Clinical": "Mental health treatment",
            "Cognitive": "Mental processes (thinking, memory)",
            "Developmental": "Lifespan changes",
            "Social": "How people influence each other",
            "Industrial-Organizational": "Workplace psychology",
            "Educational": "Learning and teaching"
        }
    },
    "cognitive_biases": {
        "category": "Psychology",
        "definition": "Bias kognitif adalah pola pikir yang menyimpang.",
        "common": {
            "Confirmation bias": "Seeking info that confirms beliefs",
            "Anchoring": "Over-relying on first info received",
            "Availability heuristic": "Judging by what comes to mind easily",
            "Dunning-Kruger": "Incompetent overestimate, experts underestimate",
            "Sunk cost fallacy": "Continuing due to past investment",
            "Hindsight bias": "Thinking you 'knew it all along'"
        }
    },
    "logical_fallacies": {
        "category": "Psychology",
        "definition": "Kesalahan logika dalam argumentasi.",
        "fallacies": {
            "Ad hominem": "Attacking person, not argument",
            "Straw man": "Misrepresenting opponent's argument",
            "False dichotomy": "Only two options when more exist",
            "Appeal to authority": "Expert said it, so it must be true",
            "Slippery slope": "One thing leads to extreme consequence",
            "Bandwagon": "Everyone does it, so it's right"
        }
    },
    "defense_mechanisms": {
        "category": "Psychology",
        "definition": "Mekanisme pertahanan psikologis (Freud).",
        "mechanisms": {
            "Denial": "Refusing to accept reality",
            "Projection": "Attributing own feelings to others",
            "Rationalization": "Logical excuses for irrational behavior",
            "Repression": "Pushing memories to unconscious",
            "Sublimation": "Channeling impulses into productive activity",
            "Displacement": "Redirecting emotions to safer target"
        }
    },
    
    # ============================================
    # PERSONALITY
    # ============================================
    "personality_big_five": {
        "category": "Personality",
        "definition": "Big Five adalah model kepribadian yang diterima luas.",
        "traits": {
            "Openness": "Creativity, curiosity, open to new experiences",
            "Conscientiousness": "Organization, dependability, self-discipline",
            "Extraversion": "Sociability, assertiveness, talkativeness",
            "Agreeableness": "Cooperation, trust, helpfulness",
            "Neuroticism": "Emotional instability, anxiety, moodiness"
        },
        "mnemonic": "OCEAN"
    },
    "mbti": {
        "category": "Personality",
        "definition": "MBTI adalah tipe kepribadian populer (meski kontroversial ilmiahnya).",
        "dimensions": {
            "E/I": "Extraversion/Introversion",
            "S/N": "Sensing/Intuition",
            "T/F": "Thinking/Feeling",
            "J/P": "Judging/Perceiving"
        },
        "types": ["INTJ", "ENFP", "ISTJ", "ENFJ", "etc."],
        "note": "Fun for self-reflection, but not scientifically rigorous"
    },
    "introversion_extraversion": {
        "category": "Personality",
        "definition": "Introvert vs Extrovert adalah tentang sumber energi.",
        "introvert": {
            "traits": "Recharges alone, prefers depth over breadth",
            "not": "Not the same as shy or antisocial"
        },
        "extrovert": {
            "traits": "Recharges socially, seeks stimulation",
            "not": "Not the same as loud or attention-seeking"
        },
        "ambivert": "Mix of both traits"
    },
    "enneagram": {
        "category": "Personality",
        "definition": "Enneagram adalah sistem 9 tipe kepribadian.",
        "types": [
            "1: Reformer (perfectionist)",
            "2: Helper (people-pleaser)",
            "3: Achiever (success-oriented)",
            "4: Individualist (romantic)",
            "5: Investigator (observer)",
            "6: Loyalist (skeptic)",
            "7: Enthusiast (adventurer)",
            "8: Challenger (leader)",
            "9: Peacemaker (mediator)"
        ]
    },
    
    # ============================================
    # MOTIVATION
    # ============================================
    "maslow_hierarchy": {
        "category": "Motivation",
        "definition": "Hierarki kebutuhan Maslow.",
        "levels": [
            "Physiological (food, water, shelter)",
            "Safety (security, stability)",
            "Love/Belonging (relationships, community)",
            "Esteem (respect, achievement)",
            "Self-actualization (reaching full potential)"
        ],
        "concept": "Lower needs must be met before higher ones"
    },
    "intrinsic_extrinsic": {
        "category": "Motivation",
        "definition": "Motivasi intrinsik vs ekstrinsik.",
        "intrinsic": {
            "definition": "Driven by internal reward (enjoyment, curiosity)",
            "examples": "Learning for fun, hobby projects",
            "better_for": "Long-term engagement, creativity"
        },
        "extrinsic": {
            "definition": "Driven by external reward (money, praise)",
            "examples": "Working for salary, grades",
            "warning": "Can undermine intrinsic motivation"
        }
    },
    "flow_state": {
        "category": "Motivation",
        "definition": "Flow state adalah keadaan fokus total dan enjoyment.",
        "characteristics": [
            "Complete concentration",
            "Clear goals",
            "Loss of self-consciousness",
            "Distorted sense of time",
            "Intrinsically rewarding"
        ],
        "coined_by": "Mihaly Csikszentmihalyi",
        "requires": "Challenge matches skill level"
    },
    "habit_formation": {
        "category": "Motivation",
        "definition": "Cara membentuk kebiasaan baru.",
        "habit_loop": {
            "Cue": "Trigger that initiates behavior",
            "Routine": "The behavior itself",
            "Reward": "Benefit that reinforces behavior"
        },
        "time": "21 days (myth) - actually 66 days average",
        "tips": ["Start small", "Stack habits", "Environment design", "Never miss twice"]
    },
    "procrastination_psychology": {
        "category": "Motivation",
        "definition": "Psikologi di balik prokrastinasi.",
        "cause": "Emotion regulation issue, not laziness",
        "triggers": ["Anxiety", "Perfectionism", "Lack of structure", "Task aversion"],
        "solutions": ["Break into small tasks", "Forgive yourself", "Self-compassion", "Just start"]
    },
    
    # ============================================
    # THERAPY APPROACHES
    # ============================================
    "cbt": {
        "category": "Therapy",
        "definition": "CBT (Cognitive Behavioral Therapy) adalah terapi berbasis bukti.",
        "concept": "Thoughts affect feelings and behaviors",
        "techniques": ["Cognitive restructuring", "Behavioral activation", "Exposure"],
        "effective_for": ["Depression", "Anxiety", "OCD", "PTSD"]
    },
    "mindfulness": {
        "category": "Therapy",
        "definition": "Mindfulness adalah kesadaran penuh pada saat ini.",
        "practices": ["Meditation", "Breathing exercises", "Body scan", "Mindful eating"],
        "benefits": ["Reduced stress", "Better focus", "Emotional regulation"],
        "apps": ["Headspace", "Calm", "Insight Timer"]
    },
    "stoicism": {
        "category": "Philosophy",
        "definition": "Stoicism adalah filosofi kuno tentang pengendalian diri.",
        "principles": [
            "Focus on what you can control",
            "Accept what you cannot",
            "Practice negative visualization",
            "Live according to nature/reason"
        ],
        "philosophers": ["Marcus Aurelius", "Seneca", "Epictetus"]
    },
    
    # ============================================
    # RELATIONSHIPS PSYCHOLOGY
    # ============================================
    "gottman_four_horsemen": {
        "category": "Relationships",
        "definition": "4 perilaku yang merusak hubungan (John Gottman).",
        "horsemen": {
            "Criticism": "Attacking partner's character",
            "Contempt": "Disrespect, eye-rolling, sarcasm",
            "Defensiveness": "Excuse-making, not taking responsibility",
            "Stonewalling": "Withdrawing, shutting down"
        },
        "antidotes": ["Gentle startup", "Appreciation", "Responsibility", "Self-soothing"]
    },
    "attachment_theory": {
        "category": "Relationships",
        "definition": "Teori attachment tentang bonding awal.",
        "styles": {
            "Secure": "Comfortable with intimacy and independence",
            "Anxious": "Fears abandonment, needs reassurance",
            "Avoidant": "Uncomfortable with closeness",
            "Disorganized": "Fear of intimacy, contradictory behavior"
        },
        "origin": "Forms in infancy based on caregiver response"
    },
    
    # ============================================
    # COGNITIVE
    # ============================================
    "memory_types": {
        "category": "Cognitive",
        "definition": "Jenis-jenis memori.",
        "types": {
            "Short-term": "Seconds to minutes, limited capacity",
            "Working": "Manipulation of short-term info",
            "Long-term": "Permanent storage",
            "Episodic": "Personal experiences",
            "Semantic": "Facts and knowledge",
            "Procedural": "Skills and how-to"
        }
    },
    "decision_making": {
        "category": "Cognitive",
        "definition": "Psikologi pengambilan keputusan.",
        "systems": {
            "System 1": "Fast, intuitive, automatic",
            "System 2": "Slow, deliberate, analytical"
        },
        "based_on": "Daniel Kahneman's 'Thinking, Fast and Slow'"
    },
    "attention_span": {
        "category": "Cognitive",
        "definition": "Rentang perhatian manusia.",
        "sustained": "10-20 minutes for focused attention",
        "factors": ["Interest", "Complexity", "Environment", "Mental state"],
        "improving": ["Minimize distractions", "Take breaks", "Practice mindfulness"]
    },
    
    # ============================================
    # SUCCESS & ACHIEVEMENT
    # ============================================
    "grit": {
        "category": "Success",
        "definition": "Grit adalah ketekunan dan semangat jangka panjang.",
        "researcher": "Angela Duckworth",
        "formula": "Talent × Effort = Skill, Skill × Effort = Achievement",
        "key": "Effort counts twice!"
    },
    "deliberate_practice": {
        "category": "Success",
        "definition": "Latihan sengaja untuk mencapai keahlian.",
        "elements": [
            "Specific goal",
            "Full concentration",
            "Immediate feedback",
            "Outside comfort zone",
            "Repetition with refinement"
        ],
        "researcher": "Anders Ericsson"
    },
    "imposter_syndrome": {
        "category": "Psychology",
        "definition": "Imposter syndrome adalah merasa tidak layak meski sukses.",
        "characteristics": [
            "Feeling like a fraud",
            "Attributing success to luck",
            "Fear of being 'found out'",
            "Downplaying achievements"
        ],
        "common_in": "High achievers, new roles, minority groups",
        "coping": ["Acknowledge feelings", "Talk about it", "Collect positive evidence", "Accept imperfection"]
    },
    "fixed_vs_growth": {
        "category": "Success",
        "definition": "Fixed vs Growth Mindset (Carol Dweck).",
        "fixed": {
            "belief": "Intelligence is static",
            "response": "Avoids challenges, gives up easily"
        },
        "growth": {
            "belief": "Intelligence can be developed",
            "response": "Embraces challenges, persists through obstacles"
        },
        "power": "The power of 'yet' - I can't do this... yet"
    }
}
