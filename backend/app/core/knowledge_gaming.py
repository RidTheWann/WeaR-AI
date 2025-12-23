"""
WeaR AI Knowledge - Video Games, Gaming Culture & Esports
Pengetahuan tentang video game dan budaya gaming.
Created by RidTheWann
"""

KNOWLEDGE_GAMING = {
    # ============================================
    # GAMING PLATFORMS
    # ============================================
    "pc_gaming": {
        "category": "Platform",
        "definition": "PC Gaming adalah gaming di komputer pribadi.",
        "advantages": ["Best graphics", "Modding", "Mouse+keyboard precision", "Upgrade options"],
        "platforms": ["Steam", "Epic Games Store", "GOG", "Battle.net"],
        "hardware": ["GPU", "CPU", "RAM", "Monitor refresh rate"]
    },
    "console_gaming": {
        "category": "Platform",
        "definition": "Console gaming adalah gaming di dedicated gaming consoles.",
        "consoles": ["PlayStation", "Xbox", "Nintendo Switch"],
        "advantages": ["Ease of use", "Exclusives", "Local multiplayer", "Optimization"]
    },
    "mobile_gaming": {
        "category": "Platform",
        "definition": "Mobile gaming adalah gaming di smartphone/tablet.",
        "platforms": ["iOS", "Android"],
        "popular_games": ["Mobile Legends", "PUBG Mobile", "Free Fire", "Genshin Impact"],
        "monetization": ["Free-to-play", "In-app purchases", "Gacha"]
    },
    
    # ============================================
    # GAME GENRES
    # ============================================
    "fps_games": {
        "category": "Genre",
        "definition": "FPS (First-Person Shooter) game dari sudut pandang first-person.",
        "games": ["Call of Duty", "Counter-Strike", "Valorant", "Overwatch", "Apex Legends"],
        "skills": "Aim, reflexes, map knowledge, team coordination"
    },
    "moba_games": {
        "category": "Genre",
        "definition": "MOBA (Multiplayer Online Battle Arena) adalah 5v5 team battles.",
        "games": ["League of Legends", "Dota 2", "Mobile Legends", "Arena of Valor"],
        "objective": "Destroy enemy base/Nexus/Ancient",
        "roles": ["Carry", "Support", "Jungler", "Tank", "Mage"]
    },
    "battle_royale": {
        "category": "Genre",
        "definition": "Battle Royale: last player/team standing wins.",
        "games": ["Fortnite", "PUBG", "Apex Legends", "Free Fire", "Warzone"],
        "mechanics": "Drop, loot, shrinking zone, survive"
    },
    "rpg_games": {
        "category": "Genre",
        "definition": "RPG (Role-Playing Game) dengan character progression.",
        "subgenres": {
            "JRPG": "Japanese style (Final Fantasy, Persona)",
            "ARPG": "Action RPG (Diablo, Path of Exile)",
            "MMORPG": "Massively Multiplayer (WoW, FFXIV)"
        }
    },
    "open_world": {
        "category": "Genre",
        "definition": "Open world games dengan exploration bebas.",
        "games": ["GTA V", "Red Dead Redemption 2", "Elden Ring", "Zelda: TOTK", "Skyrim"],
        "freedom": "Non-linear gameplay, explore anywhere"
    },
    "survival_games": {
        "category": "Genre",
        "definition": "Survival games fokus pada bertahan hidup.",
        "games": ["Minecraft", "Rust", "ARK", "Valheim", "Subnautica"],
        "mechanics": "Gather, craft, build, survive threats"
    },
    "sports_games": {
        "category": "Genre",
        "definition": "Sports games mensimulasikan olahraga nyata.",
        "franchises": {
            "FIFA/EA FC": "Football/Soccer",
            "NBA 2K": "Basketball",
            "Madden": "American Football",
            "F1": "Formula 1 racing"
        }
    },
    "horror_games": {
        "category": "Genre",
        "definition": "Horror games designed untuk menakutkan.",
        "games": ["Resident Evil", "Silent Hill", "Outlast", "Amnesia", "Phasmophobia"],
        "subgenres": ["Survival horror", "Psychological horror", "Jump scare focused"]
    },
    "simulation_games": {
        "category": "Genre",
        "definition": "Simulation games mensimulasikan aktivitas real-world.",
        "types": {
            "Life sim": "The Sims, Stardew Valley",
            "Vehicle sim": "Microsoft Flight Simulator, Euro Truck",
            "Management": "Cities: Skylines, Planet Zoo"
        }
    },
    
    # ============================================
    # ICONIC GAMES
    # ============================================
    "minecraft": {
        "category": "Game",
        "definition": "Minecraft adalah sandbox game dengan infinite possibilities.",
        "developer": "Mojang (now Microsoft)",
        "released": "2011 (full)",
        "sales": "Best-selling game ever (300+ million)",
        "modes": ["Survival", "Creative", "Hardcore", "Adventure"]
    },
    "gta_5": {
        "category": "Game",
        "definition": "Grand Theft Auto V adalah open-world crime game.",
        "developer": "Rockstar Games",
        "released": "2013 (still popular!)",
        "sales": "Second best-selling (200+ million)",
        "online": "GTA Online still has massive player base"
    },
    "fortnite": {
        "category": "Game",
        "definition": "Fortnite adalah free-to-play battle royale dengan building.",
        "developer": "Epic Games",
        "released": "2017",
        "cultural_impact": "Dances, crossovers, concerts in-game",
        "free_to_play": "Monetized through cosmetics, Battle Pass"
    },
    "league_of_legends": {
        "category": "Game",
        "definition": "League of Legends adalah MOBA paling populer di dunia.",
        "developer": "Riot Games",
        "released": "2009",
        "esports": "Largest esports scene (Worlds Championship)",
        "champions": "160+ playable champions"
    },
    "valorant": {
        "category": "Game",
        "definition": "Valorant adalah tactical FPS dengan abilities.",
        "developer": "Riot Games",
        "released": "2020",
        "concept": "CS:GO meets Overwatch",
        "esports": "VCT (Valorant Champions Tour)"
    },
    "elden_ring": {
        "category": "Game",
        "definition": "Elden Ring adalah open-world action RPG dari FromSoftware.",
        "developer": "FromSoftware",
        "released": "2022",
        "collaboration": "George R.R. Martin (worldbuilding)",
        "difficulty": "Soulslike, challenging but fair",
        "awards": "Game of the Year 2022"
    },
    "zelda_totk": {
        "category": "Game",
        "definition": "The Legend of Zelda: Tears of the Kingdom adalah masterpiece Nintendo.",
        "platform": "Nintendo Switch",
        "released": "2023",
        "predecessor": "Sequel to Breath of the Wild",
        "features": "Ultrahand, Fuse, Ascend abilities"
    },
    "mobile_legends": {
        "category": "Game",
        "definition": "Mobile Legends adalah MOBA mobile populer di Asia Tenggara.",
        "developer": "Moonton",
        "popular_in": "Indonesia, Philippines, Malaysia",
        "esports": "MPL (Mobile Legends Professional League)"
    },
    "genshin_impact": {
        "category": "Game",
        "definition": "Genshin Impact adalah free-to-play open-world gacha game.",
        "developer": "miHoYo/HoYoverse",
        "released": "2020",
        "comparison": "Often compared to Zelda: BOTW",
        "monetization": "Gacha system for characters"
    },
    
    # ============================================
    # ESPORTS
    # ============================================
    "esports": {
        "category": "Esports",
        "definition": "Esports adalah kompetitif gaming secara profesional.",
        "prize_pools": "The International (Dota 2) had $40M+ prize pool",
        "structure": "Leagues, tournaments, world championships",
        "careers": ["Pro player", "Coach", "Analyst", "Caster", "Content creator"]
    },
    "esports_titles": {
        "category": "Esports",
        "definition": "Game esports utama.",
        "games": {
            "League of Legends": "Worlds Championship",
            "Dota 2": "The International",
            "CS2": "Majors, ESL Pro League",
            "Valorant": "VCT Champions",
            "Mobile Legends": "M-Series, MPL"
        }
    },
    "esports_teams": {
        "category": "Esports",
        "definition": "Tim esports terkenal.",
        "teams": ["T1", "Cloud9", "Team Liquid", "Fnatic", "G2 Esports", "NAVI", "ONIC Esports"],
        "indonesia": ["ONIC", "RRQ", "EVOS", "Bigetron"]
    },
    
    # ============================================
    # GAMING TERMS
    # ============================================
    "gaming_terms": {
        "category": "Gaming",
        "definition": "Common gaming terminology.",
        "terms": {
            "GG": "Good Game",
            "AFK": "Away From Keyboard",
            "NPC": "Non-Player Character",
            "DLC": "Downloadable Content",
            "Nerf": "Make weaker (balancing)",
            "Buff": "Make stronger",
            "Meta": "Most Effective Tactics Available",
            "Grind": "Repetitive tasks for rewards",
            "Noob/Newbie": "New player",
            "Carry": "Player who leads team to victory"
        }
    },
    "game_ratings": {
        "category": "Gaming",
        "definition": "Game rating systems.",
        "systems": {
            "ESRB": "US (E, E10+, T, M, AO)",
            "PEGI": "Europe (3, 7, 12, 16, 18)",
            "USK": "Germany"
        }
    },
    "game_monetization": {
        "category": "Gaming",
        "definition": "Cara game menghasilkan uang.",
        "models": {
            "Premium": "Pay once, own forever (AAA games)",
            "Free-to-play": "Free with optional purchases",
            "Subscription": "Monthly fee (WoW, FFXIV)",
            "Gacha": "Random character/item draws",
            "Battle Pass": "Seasonal paid progression"
        }
    },
    
    # ============================================
    # GAME COMPANIES
    # ============================================
    "nintendo": {
        "category": "Company",
        "definition": "Nintendo adalah game company legendaris Jepang.",
        "founded": "1889 (playing cards), video games 1970s",
        "franchises": ["Mario", "Zelda", "Pokémon", "Animal Crossing", "Smash Bros"],
        "consoles": ["Switch", "Wii", "DS/3DS", "NES/SNES", "GameBoy"]
    },
    "sony_playstation": {
        "category": "Company",
        "definition": "Sony Interactive Entertainment membuat PlayStation.",
        "consoles": ["PS1", "PS2", "PS3", "PS4", "PS5"],
        "exclusives": ["God of War", "Spider-Man", "The Last of Us", "Horizon"],
        "psn": "PlayStation Network"
    },
    "microsoft_xbox": {
        "category": "Company",
        "definition": "Microsoft Gaming membuat Xbox.",
        "consoles": ["Xbox", "Xbox 360", "Xbox One", "Series X/S"],
        "acquired": ["Bethesda", "Activision Blizzard"],
        "game_pass": "Xbox Game Pass subscription service"
    },
    "valve": {
        "category": "Company",
        "definition": "Valve membuat Steam dan game legendary.",
        "games": ["Half-Life", "Portal", "Counter-Strike", "Dota 2", "Team Fortress"],
        "steam": "Largest PC gaming platform",
        "steam_deck": "Handheld gaming PC"
    },
    "riot_games": {
        "category": "Company",
        "definition": "Riot Games membuat League of Legends dan Valorant.",
        "games": ["League of Legends", "Valorant", "Teamfight Tactics", "Wild Rift"],
        "owned_by": "Tencent",
        "esports": "Runs major esports leagues"
    },
    
    # ============================================
    # GAMING CULTURE
    # ============================================
    "streamers": {
        "category": "Culture",
        "definition": "Streamers adalah content creators yang live stream gaming.",
        "platforms": ["Twitch", "YouTube Gaming", "Facebook Gaming"],
        "popular": ["Ninja", "Pokimane", "xQc", "Shroud", "DrDisrespect"],
        "indonesia": ["Windah Basudara", "MiawAug", "Reza Arap"]
    },
    "gaming_events": {
        "category": "Culture",
        "definition": "Event gaming besar.",
        "events": {
            "E3": "Electronic Entertainment Expo",
            "Gamescom": "Germany, largest gaming event",
            "Tokyo Game Show": "Japan",
            "The Game Awards": "Annual awards ceremony"
        }
    },
    "speedrunning": {
        "category": "Culture",
        "definition": "Speedrunning adalah completing games secepat mungkin.",
        "categories": ["Any%", "100%", "Glitchless"],
        "community": "Games Done Quick (charity marathons)",
        "records": "Tracked on Speedrun.com"
    },
    "modding": {
        "category": "Culture",
        "definition": "Modding adalah memodifikasi games dengan custom content.",
        "platforms": ["Nexus Mods", "Steam Workshop", "CurseForge"],
        "popular_modded": ["Skyrim", "Minecraft", "GTA V", "Stardew Valley"],
        "total_conversion": "Some mods become standalone games"
    }
}
