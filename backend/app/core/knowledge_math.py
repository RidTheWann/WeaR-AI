"""
WeaR AI Knowledge - Mathematics, Logic, Numbers & Puzzles
Pengetahuan tentang matematika, logika, dan teka-teki.
Created by RidTheWann
"""

KNOWLEDGE_MATH = {
    # ============================================
    # MATHEMATICAL CONSTANTS
    # ============================================
    "e_number": {
        "category": "Mathematics",
        "definition": "e (Euler's number) adalah basis natural logarithm.",
        "value": "2.71828182845904523536...",
        "applications": ["Compound interest", "Probability", "Calculus"],
        "formula": "lim(n→∞) (1 + 1/n)^n"
    },
    "phi": {
        "category": "Mathematics",
        "definition": "Phi (φ) adalah Golden Ratio.",
        "value": "1.61803398875...",
        "formula": "(1 + √5) / 2",
        "appearances": ["Fibonacci sequence", "Art", "Architecture", "Nature"]
    },
    "imaginary_number": {
        "category": "Mathematics",
        "definition": "Imaginary number i adalah √(-1).",
        "properties": ["i² = -1", "i³ = -i", "i⁴ = 1"],
        "complex": "a + bi (real + imaginary)"
    },
    "zero": {
        "category": "Mathematics",
        "definition": "Zero (0) adalah angka yang melambangkan ketiadaan.",
        "facts": [
            "Dikembangkan di India dan Mesopotamia",
            "0! = 1 (by convention)",
            "Division by 0 is undefined",
            "0 bukan positif maupun negatif"
        ]
    },
    "googol": {
        "category": "Mathematics",
        "definition": "Googol adalah 10^100 (1 diikuti 100 nol).",
        "origin": "Named by 9-year-old Milton Sirotta",
        "fun_fact": "Google named after this number (misspelled)"
    },
    "googolplex": {
        "category": "Mathematics",
        "definition": "Googolplex adalah 10^googol = 10^(10^100).",
        "perspective": "More than atoms in observable universe"
    },
    
    # ============================================
    # GEOMETRY
    # ============================================
    "circle": {
        "category": "Geometry",
        "definition": "Lingkaran adalah set titik dengan jarak sama dari pusat.",
        "formulas": {
            "Circumference": "2πr",
            "Area": "πr²",
            "Diameter": "2r"
        }
    },
    "triangle": {
        "category": "Geometry",
        "definition": "Segitiga adalah polygon dengan 3 sisi.",
        "types": ["Equilateral", "Isosceles", "Scalene", "Right"],
        "area": "½ × base × height",
        "sum_angles": "180°"
    },
    "square": {
        "category": "Geometry",
        "definition": "Persegi adalah quadrilateral dengan 4 sisi sama dan 4 sudut 90°.",
        "area": "s²",
        "perimeter": "4s",
        "diagonal": "s√2"
    },
    "cube": {
        "category": "Geometry",
        "definition": "Kubus adalah 3D shape dengan 6 faces persegi sama.",
        "volume": "s³",
        "surface_area": "6s²",
        "edges": 12,
        "vertices": 8
    },
    "sphere": {
        "category": "Geometry",
        "definition": "Bola adalah 3D shape dengan semua titik berjarak sama dari pusat.",
        "volume": "4/3 πr³",
        "surface_area": "4πr²"
    },
    
    # ============================================
    # NUMBER THEORY
    # ============================================
    "perfect_number": {
        "category": "Number Theory",
        "definition": "Perfect number sama dengan jumlah divisor-nya (excluding itself).",
        "examples": "6 (1+2+3=6), 28 (1+2+4+7+14=28), 496, 8128"
    },
    "factorial": {
        "category": "Mathematics",
        "definition": "Factorial (n!) adalah product angka dari 1 sampai n.",
        "examples": "5! = 5×4×3×2×1 = 120",
        "special": "0! = 1 (by definition)"
    },
    "modular_arithmetic": {
        "category": "Mathematics",
        "definition": "Modular arithmetic: menghitung dengan remainders.",
        "example": "17 mod 5 = 2 (17 ÷ 5 = 3 remainder 2)",
        "applications": ["Cryptography", "Hash functions", "Calendar calculations"]
    },
    
    # ============================================
    # LOGIC
    # ============================================
    "boolean_logic": {
        "category": "Logic",
        "definition": "Boolean logic beroperasi dengan TRUE dan FALSE.",
        "operators": {
            "AND": "True if both true",
            "OR": "True if at least one true",
            "NOT": "Inverts value",
            "XOR": "True if exactly one true"
        }
    },
    "truth_table": {
        "category": "Logic",
        "definition": "Truth table menunjukkan semua kemungkinan nilai operasi logika.",
        "and_table": "T∧T=T, T∧F=F, F∧T=F, F∧F=F",
        "or_table": "T∨T=T, T∨F=T, F∨T=T, F∨F=F"
    },
    "logical_fallacy": {
        "category": "Logic",
        "definition": "Logical fallacy adalah kesalahan dalam reasoning.",
        "common": [
            "Ad hominem (attack person, not argument)",
            "Strawman (misrepresent opponent's argument)",
            "False dichotomy (only 2 options when more exist)",
            "Slippery slope (unwarranted chain of events)",
            "Appeal to authority (authority doesn't guarantee truth)"
        ]
    },
    "paradox": {
        "category": "Logic",
        "definition": "Paradox adalah statement yang kontradiksi diri sendiri.",
        "examples": [
            "This statement is false (liar's paradox)",
            "Grandfather paradox (time travel)",
            "Ship of Theseus (identity)",
            "Zeno's paradoxes (motion)"
        ]
    },
    
    # ============================================
    # FAMOUS THEOREMS
    # ============================================
    "fermats_last_theorem": {
        "category": "Mathematics",
        "definition": "No three positive integers satisfy a^n + b^n = c^n for n > 2.",
        "history": "Fermat claimed proof in 1637, proved by Andrew Wiles in 1995",
        "took": "358 years to prove"
    },
    "euclidean_geometry": {
        "category": "Mathematics",
        "definition": "Geometry berdasarkan postulates Euclid.",
        "fifth_postulate": "Parallel lines never meet (controversial, led to non-Euclidean geometry)"
    },
    "set_theory": {
        "category": "Mathematics",
        "definition": "Set theory adalah study of collections of objects.",
        "operations": ["Union (∪)", "Intersection (∩)", "Difference (-)", "Complement"],
        "symbols": ["∈ (element of)", "⊂ (subset)", "∅ (empty set)"]
    },
    
    # ============================================
    # PUZZLES & BRAIN TEASERS
    # ============================================
    "monty_hall": {
        "category": "Puzzle",
        "definition": "Monty Hall problem: should you switch doors?",
        "setup": "3 doors, 1 prize. You pick one, host opens another (no prize), should you switch?",
        "answer": "YES! Switching gives 2/3 chance, staying gives 1/3",
        "counterintuitive": "Most people intuitively think 50/50"
    },
    "prisoners_dilemma": {
        "category": "Game Theory",
        "definition": "Two prisoners choose to cooperate or betray.",
        "outcome": "Best individual result is betray, but both betray = worst collective",
        "applications": ["Economics", "Politics", "Biology", "AI"]
    },
    "tower_of_hanoi": {
        "category": "Puzzle",
        "definition": "Move stack of disks from one peg to another, one at a time.",
        "rules": "Never place larger disk on smaller",
        "minimum_moves": "2^n - 1 (for n disks)"
    },
    "eight_queens": {
        "category": "Puzzle",
        "definition": "Place 8 queens on chessboard so none attack each other.",
        "solutions": "92 distinct solutions",
        "algorithm": "Classic backtracking problem"
    },
    "sudoku": {
        "category": "Puzzle",
        "definition": "Fill 9x9 grid so each row, column, and 3x3 box has 1-9.",
        "difficulty": "Based on number of given digits and their positions",
        "minimum_clues": "17 (proven minimum for unique solution)"
    },
    "rubiks_cube": {
        "category": "Puzzle",
        "definition": "3D combination puzzle dengan 6 faces of 9 squares.",
        "combinations": "43 quintillion (43,252,003,274,489,856,000)",
        "god_number": "20 moves or less can solve any configuration",
        "world_record": "~3.13 seconds (human), <1 second (robot)"
    },
    
    # ============================================
    # STATISTICS
    # ============================================
    "mean_median_mode": {
        "category": "Statistics",
        "definition": "Measures of central tendency.",
        "mean": "Average = sum / count",
        "median": "Middle value when sorted",
        "mode": "Most frequent value"
    },
    "standard_deviation": {
        "category": "Statistics",
        "definition": "Standard deviation mengukur spread data dari mean.",
        "interpretation": "Higher = more spread out",
        "68_95_99": "68% within 1 SD, 95% within 2, 99.7% within 3"
    },
    "correlation": {
        "category": "Statistics",
        "definition": "Correlation mengukur strength hubungan antara 2 variables.",
        "range": "-1 to 1 (negative, none, positive)",
        "warning": "Correlation ≠ causation!"
    },
    "bayes_theorem": {
        "category": "Statistics",
        "definition": "Bayes' theorem menghitung conditional probability.",
        "formula": "P(A|B) = P(B|A) × P(A) / P(B)",
        "applications": ["Machine learning", "Medical diagnosis", "Spam filters"]
    },
    "regression": {
        "category": "Statistics",
        "definition": "Regression memodelkan relationship antara variables.",
        "linear": "y = mx + b (straight line)",
        "applications": ["Prediction", "Trend analysis", "Machine learning"]
    },
    "normal_distribution": {
        "category": "Statistics",
        "definition": "Normal distribution adalah bell curve yang symmetric.",
        "properties": "Mean = Median = Mode (at center)",
        "examples": "Heights, test scores, measurement errors"
    },
    
    # ============================================
    # ECONOMICS CONCEPTS
    # ============================================
    "supply_demand": {
        "category": "Economics",
        "definition": "Supply and demand menentukan harga dan quantity di market.",
        "law_of_demand": "Price ↑ = Quantity demanded ↓",
        "law_of_supply": "Price ↑ = Quantity supplied ↑",
        "equilibrium": "Where supply meets demand"
    },
    "gdp": {
        "category": "Economics",
        "definition": "GDP (Gross Domestic Product) adalah total value barang/jasa yang diproduksi.",
        "formula": "GDP = C + I + G + (X - M)",
        "components": ["Consumption", "Investment", "Government spending", "Net exports"]
    },
    "opportunity_cost": {
        "category": "Economics",
        "definition": "Opportunity cost adalah value dari alternatif terbaik yang dikorbankan.",
        "example": "Kuliah = foregone salary + tuition (not just tuition)"
    },
    "marginal_utility": {
        "category": "Economics",
        "definition": "Marginal utility adalah additional satisfaction dari consuming one more unit.",
        "diminishing": "Each additional unit typically gives less satisfaction"
    },
    "elasticity": {
        "category": "Economics",
        "definition": "Elasticity mengukur responsiveness terhadap price change.",
        "elastic": "Demand changes significantly with price",
        "inelastic": "Demand barely changes (necessities like medicine)"
    },
    "game_theory": {
        "category": "Economics",
        "definition": "Game theory adalah study of strategic decision-making.",
        "concepts": ["Nash equilibrium", "Dominant strategy", "Zero-sum game"],
        "founder": "John von Neumann, John Nash"
    },
    "compound_interest_math": {
        "category": "Economics",
        "definition": "Rumus compound interest.",
        "formula": "A = P(1 + r/n)^(nt)",
        "variables": "P=principal, r=rate, n=compounds/year, t=years",
        "rule_of_72": "Years to double ≈ 72 / interest rate"
    },
}
