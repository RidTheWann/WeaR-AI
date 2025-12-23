"""
WeaR AI Knowledge - Business, Finance, Psychology & Philosophy
Pengetahuan tentang bisnis, keuangan, startup, psikologi, dan filosofi.
Created by RidTheWann
"""

KNOWLEDGE_BUSINESS = {
    # ============================================
    # BUSINESS & ENTREPRENEURSHIP
    # ============================================
    "startup": {
        "category": "Business",
        "definition": "Startup adalah young company founded untuk develop unique product/service.",
        "stages": ["Idea", "Seed", "Early Stage", "Growth", "Expansion", "Exit"],
        "funding": ["Bootstrapping", "Angel investors", "Venture Capital", "IPO"]
    },
    "unicorn": {
        "category": "Business",
        "definition": "Unicorn adalah privately held startup valued at $1+ billion.",
        "examples": ["SpaceX", "Stripe", "Canva", "Discord"],
        "indonesia": ["GoTo", "Bukalapak", "Traveloka", "OVO", "Tokopedia"]
    },
    "mvp": {
        "category": "Business",
        "definition": "MVP (Minimum Viable Product) adalah product dengan enough features untuk early customers.",
        "purpose": "Validate idea dengan minimum resources",
        "approach": "Build → Measure → Learn (Lean Startup)"
    },
    "pivot": {
        "category": "Business",
        "definition": "Pivot adalah fundamental change dalam business strategy.",
        "famous_pivots": ["YouTube (dating site)", "Slack (gaming company)", "Instagram (Burbn check-in app)"]
    },
    "product_market_fit": {
        "category": "Business",
        "definition": "Product-Market Fit adalah when product satisfies strong market demand.",
        "indicator": "Customers actively recommend product, retention high",
        "quote": "The only thing that matters is getting to product/market fit - Marc Andreessen"
    },
    "venture_capital": {
        "category": "Finance",
        "definition": "Venture Capital adalah financing untuk high-potential startups.",
        "rounds": ["Pre-seed", "Seed", "Series A", "Series B", "Series C+"],
        "famous_vcs": ["Sequoia", "Andreessen Horowitz", "Y Combinator"]
    },
    "ipo": {
        "category": "Finance",
        "definition": "IPO (Initial Public Offering) adalah first sale of stock to public.",
        "process": "Private company → Public company traded on stock exchange",
        "examples": ["Google (2004)", "Facebook (2012)", "Airbnb (2020)"]
    },
    "roi": {
        "category": "Finance",
        "definition": "ROI (Return on Investment) mengukur profitability of investment.",
        "formula": "ROI = (Gain - Cost) / Cost × 100%",
        "example": "Invest $100, get $150 → ROI = 50%"
    },
    "burn_rate": {
        "category": "Business",
        "definition": "Burn rate adalah rate at which company spends money.",
        "runway": "Cash / Monthly Burn Rate = Months of runway",
        "example": "$1M cash, $100K/month burn = 10 months runway"
    },
    "revenue_model": {
        "category": "Business",
        "definition": "Revenue model adalah how company makes money.",
        "types": [
            "Subscription (Netflix, Spotify)",
            "Freemium (Dropbox, LinkedIn)",
            "Marketplace (Uber, Airbnb)",
            "Advertising (Google, Facebook)",
            "Transaction fee (Stripe, PayPal)"
        ]
    },
    "saas": {
        "category": "Business",
        "definition": "SaaS (Software as a Service) adalah software delivery via subscription.",
        "examples": ["Salesforce", "Slack", "Zoom", "Notion"],
        "metrics": ["MRR", "ARR", "Churn rate", "LTV", "CAC"]
    },
    "b2b_b2c": {
        "category": "Business",
        "definition": "B2B (Business to Business) vs B2C (Business to Consumer).",
        "b2b": "Companies selling to other companies (Salesforce, AWS)",
        "b2c": "Companies selling to consumers (Netflix, Amazon)"
    },
    "marketing_funnel": {
        "category": "Marketing",
        "definition": "Marketing funnel adalah customer journey dari awareness ke purchase.",
        "stages": ["Awareness", "Interest", "Consideration", "Intent", "Purchase", "Loyalty"],
        "aida": "Attention, Interest, Desire, Action"
    },
    "growth_hacking": {
        "category": "Marketing",
        "definition": "Growth hacking adalah experimental, low-cost strategies untuk grow.",
        "tactics": ["Viral loops", "Referral programs", "A/B testing", "Content marketing"],
        "famous": "Dropbox referral program (500MB per referral)"
    },
    "customer_acquisition_cost": {
        "category": "Business",
        "definition": "CAC adalah cost to acquire one customer.",
        "formula": "Total Marketing Cost / Number of Customers Acquired",
        "goal": "LTV (Lifetime Value) should be > 3x CAC"
    },
    "churn_rate": {
        "category": "Business",
        "definition": "Churn rate adalah percentage of customers yang stop using product.",
        "formula": "Lost Customers / Total Customers × 100%",
        "good_churn": "<5% monthly untuk SaaS"
    },
    "okr": {
        "category": "Management",
        "definition": "OKR (Objectives and Key Results) adalah goal-setting framework.",
        "structure": "Objective (what) + Key Results (measurable how)",
        "origin": "Intel, popularized by Google"
    },
    "kpi": {
        "category": "Management",
        "definition": "KPI (Key Performance Indicator) adalah measurable value indicating success.",
        "examples": ["Revenue", "Customer satisfaction", "Conversion rate", "Employee turnover"]
    },
    "pnl": {
        "category": "Finance",
        "definition": "P&L (Profit and Loss) statement menunjukkan revenue, costs, and profit.",
        "components": ["Revenue", "COGS", "Gross Profit", "Operating Expenses", "Net Income"]
    },
    "equity": {
        "category": "Finance",
        "definition": "Equity adalah ownership interest dalam company.",
        "startup": "Founders dan investors own equity (shares)",
        "dilution": "Ownership percentage decreases saat new shares issued"
    },
    "valuation": {
        "category": "Finance",
        "definition": "Valuation adalah estimated worth of company.",
        "methods": ["Revenue multiple", "DCF", "Comparable companies"],
        "example": "Company with $10M ARR at 10x multiple = $100M valuation"
    },
    "term_sheet": {
        "category": "Finance",
        "definition": "Term sheet adalah non-binding agreement outlining investment terms.",
        "key_terms": ["Valuation", "Investment amount", "Board seats", "Liquidation preference"]
    },
    "bootstrapping": {
        "category": "Business",
        "definition": "Bootstrapping adalah building company without external funding.",
        "pros": ["Full ownership", "Focus on profitability", "No investor pressure"],
        "examples": ["Mailchimp", "Basecamp", "Zoho"]
    },
    
    # ============================================
    # PERSONAL FINANCE
    # ============================================
    "compound_interest": {
        "category": "Finance",
        "definition": "Compound interest adalah interest on interest.",
        "formula": "A = P(1 + r/n)^(nt)",
        "quote": "Compound interest is the eighth wonder of the world - Einstein",
        "example": "$1000 at 7% for 30 years = $7,612"
    },
    "investing": {
        "category": "Finance",
        "definition": "Investing adalah putting money into assets untuk grow wealth.",
        "types": ["Stocks", "Bonds", "Real Estate", "Mutual Funds", "ETFs", "Crypto"],
        "principle": "Higher risk = Higher potential return"
    },
    "stock_market": {
        "category": "Finance",
        "definition": "Stock market adalah marketplace untuk buying/selling company shares.",
        "major_indices": ["S&P 500", "Dow Jones", "NASDAQ", "IHSG (Indonesia)"],
        "exchanges": ["NYSE", "NASDAQ", "BEI (Indonesia)"]
    },
    "diversification": {
        "category": "Finance",
        "definition": "Diversification adalah spreading investments untuk reduce risk.",
        "saying": "Don't put all your eggs in one basket",
        "approach": "Mix of stocks, bonds, real estate, etc."
    },
    "inflation": {
        "category": "Economics",
        "definition": "Inflation adalah increase in prices over time, reducing purchasing power.",
        "target": "Central banks typically target ~2% inflation",
        "example": "Rp 100,000 buys less today than 10 years ago"
    },
    "recession": {
        "category": "Economics",
        "definition": "Recession adalah period of economic decline (2+ quarters negative GDP).",
        "characteristics": ["Rising unemployment", "Falling spending", "Market decline"]
    },
    "cryptocurrency": {
        "category": "Finance",
        "definition": "Cryptocurrency adalah digital currency menggunakan cryptography.",
        "examples": ["Bitcoin", "Ethereum", "Solana"],
        "technology": "Blockchain as distributed ledger"
    },
    "bitcoin": {
        "category": "Finance",
        "definition": "Bitcoin adalah first dan largest cryptocurrency.",
        "creator": "Satoshi Nakamoto (pseudonym, 2009)",
        "features": ["Decentralized", "Limited supply (21 million)", "Proof of Work"]
    },
    "passive_income": {
        "category": "Finance",
        "definition": "Passive income adalah income dengan minimal active work.",
        "sources": ["Dividends", "Rental income", "Royalties", "Interest", "Digital products"]
    },
    "budgeting": {
        "category": "Finance",
        "definition": "Budgeting adalah planning how to spend money.",
        "50_30_20": "50% needs, 30% wants, 20% savings",
        "tools": ["Spreadsheets", "Budgeting apps"]
    },
    "emergency_fund": {
        "category": "Finance",
        "definition": "Emergency fund adalah savings untuk unexpected expenses.",
        "recommended": "3-6 months of expenses",
        "purpose": "Job loss, medical emergency, car repair"
    },
    
    # ============================================
    # PSYCHOLOGY
    # ============================================
    "cognitive_bias": {
        "category": "Psychology",
        "definition": "Cognitive bias adalah systematic errors dalam thinking.",
        "common_biases": [
            "Confirmation bias (seek confirming info)",
            "Anchoring (over-rely on first info)",
            "Dunning-Kruger (overestimate own ability)",
            "Sunk cost fallacy (continue because of past investment)"
        ]
    },
    "confirmation_bias": {
        "category": "Psychology",
        "definition": "Confirmation bias adalah tendency untuk seek information yang confirms beliefs.",
        "example": "Only reading news yang align dengan political view",
        "counter": "Actively seek opposing viewpoints"
    },
    "dunning_kruger": {
        "category": "Psychology",
        "definition": "Dunning-Kruger effect: unskilled overestimate ability, experts underestimate.",
        "graph": "Peak of confidence at low skill, then dip, then rise again",
        "stages": ["Mount Stupid", "Valley of Despair", "Slope of Enlightenment"]
    },
    "imposter_syndrome": {
        "category": "Psychology",
        "definition": "Imposter syndrome adalah feeling of being fraud despite evidence of success.",
        "common_in": "High achievers, new roles, creative fields",
        "counter": "Recognize it's common, track achievements"
    },
    "procrastination": {
        "category": "Psychology",
        "definition": "Procrastination adalah delaying tasks meskipun knowing negative consequences.",
        "causes": ["Fear of failure", "Perfectionism", "Lack of motivation"],
        "solutions": ["Break tasks smaller", "Set deadlines", "Remove distractions"]
    },
    "motivation": {
        "category": "Psychology",
        "definition": "Motivation adalah internal/external drive untuk do something.",
        "types": ["Intrinsic (internal satisfaction)", "Extrinsic (rewards/punishment)"],
        "theories": ["Maslow's hierarchy", "Self-determination theory"]
    },
    "maslow_hierarchy": {
        "category": "Psychology",
        "definition": "Maslow's Hierarchy of Needs adalah theory of human motivation.",
        "levels": [
            "Physiological (food, water, sleep)",
            "Safety (security, health)",
            "Love/Belonging (relationships)",
            "Esteem (respect, recognition)",
            "Self-actualization (full potential)"
        ]
    },
    "flow_state": {
        "category": "Psychology",
        "definition": "Flow adalah mental state of complete immersion in activity.",
        "characteristics": ["Loss of time awareness", "High focus", "Enjoyment"],
        "conditions": "Skill matches challenge level",
        "coined_by": "Mihaly Csikszentmihalyi"
    },
    "growth_mindset": {
        "category": "Psychology",
        "definition": "Growth mindset adalah belief bahwa abilities can be developed.",
        "vs_fixed": "Fixed: 'I'm bad at math' | Growth: 'I can learn math'",
        "coined_by": "Carol Dweck"
    },
    "emotional_intelligence": {
        "category": "Psychology",
        "definition": "EQ adalah ability to understand dan manage emotions.",
        "components": ["Self-awareness", "Self-regulation", "Motivation", "Empathy", "Social skills"],
        "importance": "Often more important than IQ untuk success"
    },
    "habit_formation": {
        "category": "Psychology",
        "definition": "Habit formation processes a behavior menjadi automatic.",
        "habit_loop": "Cue → Routine → Reward",
        "21_days": "Myth - actually 66 days average (varies widely)",
        "book": "Atomic Habits by James Clear"
    },
    "delayed_gratification": {
        "category": "Psychology",
        "definition": "Delayed gratification adalah resisting immediate reward untuk bigger later reward.",
        "marshmallow_test": "Kids who waited had better life outcomes",
        "application": "Saving money, studying, healthy eating"
    },
    "stress": {
        "category": "Psychology",
        "definition": "Stress adalah body's response to demands atau threats.",
        "types": ["Acute (short-term)", "Chronic (long-term, harmful)"],
        "management": ["Exercise", "Sleep", "Meditation", "Social support"]
    },
    "meditation": {
        "category": "Psychology",
        "definition": "Meditation adalah practice untuk training attention dan awareness.",
        "types": ["Mindfulness", "Transcendental", "Guided", "Loving-kindness"],
        "benefits": ["Reduced stress", "Better focus", "Emotional regulation"]
    },
    "mindfulness": {
        "category": "Psychology",
        "definition": "Mindfulness adalah being fully present in the moment.",
        "practice": "Focus on breath, bodily sensations, surroundings",
        "apps": ["Headspace", "Calm", "Insight Timer"]
    },
    
    # ============================================
    # PHILOSOPHY
    # ============================================
    "stoicism": {
        "category": "Philosophy",
        "definition": "Stoicism mengajarkan focus on what you can control.",
        "practitioners": ["Marcus Aurelius", "Seneca", "Epictetus"],
        "principles": ["Control what you can", "Accept what you can't", "Focus on virtue"]
    },
    "existentialism": {
        "category": "Philosophy",
        "definition": "Existentialism focuses on individual freedom dan meaning.",
        "thinkers": ["Sartre", "Camus", "Kierkegaard", "Nietzsche"],
        "key_idea": "Existence precedes essence - you define your own meaning"
    },
    "nihilism": {
        "category": "Philosophy",
        "definition": "Nihilism adalah belief bahwa life has no inherent meaning.",
        "types": ["Existential", "Moral", "Cosmic"],
        "response": "Many see it as starting point, not endpoint"
    },
    "utilitarianism": {
        "category": "Philosophy",
        "definition": "Utilitarianism: best action maximizes happiness untuk most people.",
        "thinkers": ["Jeremy Bentham", "John Stuart Mill"],
        "trolley_problem": "Classic thought experiment"
    },
    "socratic_method": {
        "category": "Philosophy",
        "definition": "Socratic method adalah learning through series of questions.",
        "purpose": "Stimulate critical thinking, expose gaps in reasoning",
        "origin": "Socrates (ancient Greek philosopher)"
    },
    "occams_razor": {
        "category": "Philosophy",
        "definition": "Occam's Razor: simplest explanation is usually correct.",
        "application": "Don't multiply entities beyond necessity",
        "example": "Horse sound? Probably horse, not zebra"
    },
    "cogito_ergo_sum": {
        "category": "Philosophy",
        "definition": "'I think, therefore I am' - René Descartes.",
        "meaning": "The act of thinking proves existence",
        "context": "Foundational statement in philosophy"
    },
    "ethics": {
        "category": "Philosophy",
        "definition": "Ethics adalah study of moral principles.",
        "branches": ["Normative (what should we do)", "Meta-ethics (nature of morality)", "Applied ethics"],
        "theories": ["Utilitarianism", "Deontology", "Virtue ethics"]
    },
    "free_will": {
        "category": "Philosophy",
        "definition": "Free will adalah ability to choose actions without constraint.",
        "debate": ["Determinism (no free will)", "Libertarianism (yes)", "Compatibilism (both)"]
    },
    "the_absurd": {
        "category": "Philosophy",
        "definition": "The Absurd adalah conflict antara human search for meaning dan meaningless universe.",
        "albert_camus": "'One must imagine Sisyphus happy'",
        "responses": ["Embrace absurdity", "Create own meaning"]
    },
    "ikigai": {
        "category": "Philosophy",
        "definition": "Ikigai adalah Japanese concept untuk 'reason for being'.",
        "intersection": ["What you love", "What you're good at", "What world needs", "What you can be paid for"],
        "origin": "Okinawa, Japan (one of Blue Zones)"
    },
    "wabi_sabi": {
        "category": "Philosophy",
        "definition": "Wabi-sabi adalah Japanese aesthetic embracing imperfection.",
        "meaning": "Finding beauty in impermanence dan incompleteness",
        "application": "Cracked pottery, weathered wood"
    },
    "kaizen": {
        "category": "Philosophy/Business",
        "definition": "Kaizen adalah Japanese philosophy of continuous improvement.",
        "meaning": "Small incremental changes over time",
        "application": "Manufacturing (Toyota), personal development"
    },
    "zen": {
        "category": "Philosophy",
        "definition": "Zen adalah school of Mahayana Buddhism emphasizing meditation.",
        "practice": ["Zazen (sitting meditation)", "Koans (paradoxical riddles)"],
        "influence": "Minimalism, martial arts, tea ceremony"
    },
}
