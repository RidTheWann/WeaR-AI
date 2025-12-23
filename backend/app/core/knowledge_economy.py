"""
WeaR AI Knowledge - Economy, Finance, Crypto & Markets
Pengetahuan tentang ekonomi, keuangan, dan pasar.
Created by RidTheWann
"""

KNOWLEDGE_ECONOMY = {
    # ============================================
    # CRYPTOCURRENCY
    # ============================================
    "bitcoin_detailed": {
        "category": "Crypto",
        "definition": "Bitcoin (BTC) adalah cryptocurrency pertama dan terbesar.",
        "creator": "Satoshi Nakamoto (pseudonym), 2009",
        "supply": "21 million max supply",
        "halving": "Block reward halves every ~4 years",
        "use_cases": ["Store of value", "Digital gold", "Payments"],
        "volatility": "Highly volatile, not for risk-averse"
    },
    "ethereum_detailed": {
        "category": "Crypto",
        "definition": "Ethereum (ETH) adalah platform smart contracts terbesar.",
        "creator": "Vitalik Buterin, 2015",
        "features": ["Smart contracts", "DApps", "DeFi", "NFTs"],
        "eth2": "Transitioned to Proof of Stake (The Merge, 2022)",
        "gas": "Transaction fees paid in ETH"
    },
    "altcoins": {
        "category": "Crypto",
        "definition": "Altcoins adalah cryptocurrency selain Bitcoin.",
        "major": {
            "Ethereum (ETH)": "Smart contract platform",
            "Solana (SOL)": "Fast, low fees",
            "Cardano (ADA)": "Research-driven",
            "XRP": "Cross-border payments",
            "Polkadot (DOT)": "Interoperability",
            "Dogecoin (DOGE)": "Meme coin, Elon's favorite"
        }
    },
    "stablecoin": {
        "category": "Crypto",
        "definition": "Stablecoin adalah crypto yang pegged ke asset stabil.",
        "types": {
            "Fiat-backed": "USDT, USDC - backed by USD reserves",
            "Crypto-backed": "DAI - backed by crypto collateral",
            "Algorithmic": "Use algorithms to maintain peg (risky)"
        }
    },
    "defi": {
        "category": "Crypto",
        "definition": "DeFi (Decentralized Finance) adalah layanan keuangan di blockchain.",
        "services": ["Lending", "Borrowing", "Trading (DEX)", "Yield farming", "Staking"],
        "platforms": ["Uniswap", "Aave", "Compound", "Curve"],
        "risks": ["Smart contract bugs", "Impermanent loss", "Rug pulls"]
    },
    "nft_detailed": {
        "category": "Crypto",
        "definition": "NFT (Non-Fungible Token) adalah token unik di blockchain.",
        "use_cases": ["Digital art", "Collectibles", "Gaming items", "Music", "Tickets"],
        "famous": ["Bored Apes", "CryptoPunks", "Art Blocks"],
        "controversy": "Environmental concerns, speculation, scams"
    },
    "crypto_wallet": {
        "category": "Crypto",
        "definition": "Crypto wallet menyimpan private keys untuk access crypto.",
        "types": {
            "Hot wallet": "Online, convenient but less secure",
            "Cold wallet": "Offline, very secure (Ledger, Trezor)",
            "Exchange wallet": "On exchange, you don't control keys"
        },
        "phrase": "Not your keys, not your crypto"
    },
    "crypto_risks": {
        "category": "Crypto",
        "definition": "Risiko dalam cryptocurrency.",
        "risks": [
            "Extreme volatility",
            "Regulatory uncertainty",
            "Scams and rug pulls",
            "Exchange hacks",
            "Lost private keys = lost forever",
            "DYOR - Do Your Own Research"
        ]
    },
    
    # ============================================
    # STOCK MARKET
    # ============================================
    "stock_market": {
        "category": "Finance",
        "definition": "Stock market adalah tempat jual beli saham perusahaan.",
        "major_exchanges": {
            "NYSE": "New York Stock Exchange, largest",
            "NASDAQ": "Tech-heavy exchange",
            "IDX": "Indonesia Stock Exchange (BEI)"
        }
    },
    "stock_basics": {
        "category": "Finance",
        "definition": "Basics tentang saham.",
        "terms": {
            "Stock/Share": "Ownership in a company",
            "Dividend": "Company profit distributed to shareholders",
            "Market Cap": "Company value = share price × shares",
            "P/E Ratio": "Price / Earnings - valuation metric",
            "Bull market": "Rising prices",
            "Bear market": "Falling prices (20%+ decline)"
        }
    },
    "index_funds": {
        "category": "Finance",
        "definition": "Index funds track market index, passive investing.",
        "examples": {
            "S&P 500": "500 largest US companies",
            "NASDAQ 100": "100 largest NASDAQ stocks",
            "IDX30": "30 most liquid Indonesian stocks"
        },
        "benefits": ["Diversification", "Low fees", "Historically good returns"]
    },
    "etf": {
        "category": "Finance",
        "definition": "ETF (Exchange-Traded Fund) adalah fund yang traded seperti stock.",
        "vs_mutual_fund": "ETF trades throughout day, mutual fund once daily",
        "types": ["Index ETF", "Sector ETF", "Bond ETF", "Commodity ETF"]
    },
    "bonds": {
        "category": "Finance",
        "definition": "Bonds adalah debt securities - you lend money to issuer.",
        "types": {
            "Government bonds": "Issued by government (SBN, ORI in Indonesia)",
            "Corporate bonds": "Issued by companies",
            "Municipal bonds": "Issued by local governments"
        },
        "risk": "Generally lower risk than stocks, lower returns"
    },
    
    # ============================================
    # PERSONAL FINANCE
    # ============================================
    "budgeting": {
        "category": "Personal Finance",
        "definition": "Cara mengatur keuangan pribadi.",
        "methods": {
            "50/30/20": "50% needs, 30% wants, 20% savings",
            "Zero-based": "Every rupiah has a job",
            "Pay yourself first": "Save before spending"
        },
        "apps": ["Money Lover", "Mint", "YNAB"]
    },
    "emergency_fund": {
        "category": "Personal Finance",
        "definition": "Dana darurat untuk situasi tak terduga.",
        "recommended": "3-6 months of expenses",
        "purpose": "Job loss, medical emergency, unexpected repairs",
        "where": "Easily accessible savings account"
    },
    "investing_basics": {
        "category": "Personal Finance",
        "definition": "Dasar-dasar investasi.",
        "principles": [
            "Start early (compound interest)",
            "Diversify (don't put eggs in one basket)",
            "Invest regularly (dollar-cost averaging)",
            "Long-term mindset",
            "Understand what you invest in"
        ]
    },
    "compound_interest": {
        "category": "Personal Finance",
        "definition": "Compound interest adalah bunga berbunga.",
        "formula": "A = P(1 + r/n)^(nt)",
        "power": "Einstein allegedly called it '8th wonder of the world'",
        "example": "10% yearly: money doubles in ~7 years (Rule of 72)"
    },
    "debt_management": {
        "category": "Personal Finance",
        "definition": "Cara mengelola hutang.",
        "strategies": {
            "Avalanche": "Pay highest interest first (save money)",
            "Snowball": "Pay smallest debt first (psychological win)"
        },
        "good_debt": "Mortgage, education (invest in future)",
        "bad_debt": "Credit card, consumer debt (high interest)"
    },
    "retirement_planning": {
        "category": "Personal Finance",
        "definition": "Perencanaan pensiun.",
        "indonesia": {
            "BPJS Ketenagakerjaan": "Government pension",
            "DPLK": "Employer pension",
            "Personal savings": "Beyond official programs"
        },
        "rule": "Save 15-20% of income for retirement"
    },
    "insurance_basics": {
        "category": "Personal Finance",
        "definition": "Basics asuransi.",
        "types": {
            "Health insurance": "Medical expenses (BPJS Kesehatan in Indonesia)",
            "Life insurance": "For dependents if you die",
            "Vehicle insurance": "Car/motorcycle protection",
            "Property insurance": "Home/business protection"
        },
        "tip": "Don't mix insurance with investment (avoid unit-link)"
    },
    
    # ============================================
    # ECONOMIC CONCEPTS
    # ============================================
    "inflation_detailed": {
        "category": "Economics",
        "definition": "Inflasi adalah kenaikan harga barang/jasa secara umum.",
        "causes": {
            "Demand-pull": "Too much demand",
            "Cost-push": "Rising production costs",
            "Monetary": "Too much money supply"
        },
        "effects": "Purchasing power decreases, savers lose",
        "target": "Most central banks target ~2%"
    },
    "interest_rates": {
        "category": "Economics",
        "definition": "Interest rate adalah cost of borrowing money.",
        "central_bank": "Bank Indonesia sets BI Rate",
        "effects": {
            "high_rates": "Borrowing expensive, saving attractive, slows economy",
            "low_rates": "Borrowing cheap, stimulates economy"
        }
    },
    "recession": {
        "category": "Economics",
        "definition": "Recession adalah penurunan ekonomi signifikan.",
        "technical": "2+ consecutive quarters of GDP decline",
        "signs": ["Rising unemployment", "Falling GDP", "Reduced spending"],
        "recovery": "Expansionary policy (lower rates, stimulus)"
    },
    "currency": {
        "category": "Economics",
        "definition": "Mata uang dunia.",
        "major": {
            "USD": "US Dollar - world reserve currency",
            "EUR": "Euro - European Union",
            "JPY": "Japanese Yen",
            "GBP": "British Pound",
            "CNY": "Chinese Yuan",
            "IDR": "Indonesian Rupiah"
        },
        "exchange_rate": "Value of one currency vs another"
    },
    
    # ============================================
    # BUSINESS MODELS
    # ============================================
    "business_models": {
        "category": "Business",
        "definition": "Common business models.",
        "models": {
            "Subscription": "Netflix, Spotify - recurring revenue",
            "Freemium": "Free basic, paid premium",
            "Marketplace": "Tokopedia, Shopee - connect buyers/sellers",
            "SaaS": "Software as Service - B2B subscriptions",
            "Advertising": "Google, Facebook - free service, sell ads",
            "E-commerce": "Sell products online"
        }
    },
    "startup_funding": {
        "category": "Business",
        "definition": "Tahapan funding startup.",
        "stages": {
            "Bootstrapping": "Self-funded",
            "Pre-seed": "Friends, family, angel investors",
            "Seed": "Early institutional investors",
            "Series A": "Scaling product-market fit",
            "Series B+": "Scaling growth",
            "IPO": "Initial Public Offering - go public"
        }
    },
    "unicorn": {
        "category": "Business",
        "definition": "Unicorn adalah startup dengan valuasi $1+ billion.",
        "indonesia": ["Gojek", "Tokopedia (now GoTo)", "Traveloka", "Bukalapak", "OVO"],
        "global": ["SpaceX", "Stripe", "SHEIN", "Discord"]
    },
    
    # ============================================
    # INDONESIA ECONOMY
    # ============================================
    "indonesia_economy": {
        "category": "Indonesia",
        "definition": "Overview ekonomi Indonesia.",
        "gdp_rank": "~16th largest economy (2024)",
        "growth": "5%+ GDP growth target",
        "sectors": ["Agriculture", "Manufacturing", "Services", "Mining"],
        "challenges": ["Infrastructure", "Inequality", "Bureaucracy"]
    },
    "bank_indonesia": {
        "category": "Indonesia",
        "definition": "Bank Indonesia adalah bank sentral Indonesia.",
        "functions": ["Monetary policy", "Rupiah stability", "Financial system stability"],
        "bi_rate": "Benchmark interest rate"
    },
    "ojk": {
        "category": "Indonesia",
        "definition": "OJK (Otoritas Jasa Keuangan) adalah regulator keuangan Indonesia.",
        "regulates": ["Banks", "Insurance", "Capital markets", "Fintech"],
        "check_before_invest": "Always verify investment is OJK-registered"
    }
}
