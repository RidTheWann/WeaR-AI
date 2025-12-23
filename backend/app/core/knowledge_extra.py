"""
WeaR AI Knowledge - Tech Tips, Famous Quotes, Trivia & Random Facts
Pengetahuan tentang tips programming, quotes terkenal, dan fakta random.
Created by RidTheWann
"""

KNOWLEDGE_EXTRA = {
    # ============================================
    # PROGRAMMING TIPS & TRICKS
    # ============================================
    "clean_code_tips": {
        "category": "Programming Tips",
        "definition": "Tips untuk menulis clean code.",
        "tips": [
            "Use meaningful variable names",
            "Keep functions small (< 20 lines ideal)",
            "One function = One responsibility",
            "Comment WHY, not WHAT",
            "Avoid deep nesting (max 3 levels)",
            "Return early to reduce nesting"
        ]
    },
    "debugging_tips": {
        "category": "Programming Tips",
        "definition": "Tips untuk debugging efektif.",
        "tips": [
            "Rubber duck debugging - explain to rubber duck",
            "Binary search the bug - comment out half the code",
            "Check the simple things first",
            "Read error messages carefully",
            "Use git bisect untuk find breaking commit",
            "Print/log strategically"
        ]
    },
    "git_tips": {
        "category": "Programming Tips",
        "definition": "Git tips untuk developer.",
        "tips": [
            "git stash untuk save temporary work",
            "git commit --amend untuk fix last commit",
            "git reflog untuk recover lost commits",
            "git bisect untuk find bug-introducing commit",
            "Use meaningful commit messages",
            "Commit often, push when ready"
        ]
    },
    "terminal_tips": {
        "category": "Programming Tips",
        "definition": "Terminal/command line tips.",
        "tips": [
            "Ctrl+R untuk search command history",
            "!! untuk repeat last command",
            "cd - untuk kembali ke directory sebelumnya",
            "Ctrl+A/E untuk jump ke start/end of line",
            "Use aliases untuk common commands"
        ]
    },
    "vscode_tips": {
        "category": "Programming Tips",
        "definition": "VS Code shortcuts dan tips.",
        "shortcuts": {
            "Ctrl+P": "Quick open file",
            "Ctrl+Shift+P": "Command palette",
            "Ctrl+D": "Select next occurrence",
            "Alt+Up/Down": "Move line up/down",
            "Ctrl+/": "Toggle comment",
            "Ctrl+`": "Open terminal"
        }
    },
    "python_tips": {
        "category": "Programming Tips",
        "definition": "Python-specific tips.",
        "tips": [
            "Use list comprehensions",
            "f-strings untuk formatting",
            "Use enumerate() instead of range(len())",
            "Context managers untuk file handling",
            "Use type hints untuk better code",
            "Virtual environments always"
        ]
    },
    "javascript_tips": {
        "category": "Programming Tips",
        "definition": "JavaScript tips dan tricks.",
        "tips": [
            "Use const by default, let when needed",
            "Arrow functions untuk cleaner code",
            "Destructuring untuk readable code",
            "Optional chaining (?.) untuk safe access",
            "Nullish coalescing (??) vs OR (||)",
            "Use async/await over .then chains"
        ]
    },
    "sql_tips": {
        "category": "Programming Tips",
        "definition": "SQL optimization tips.",
        "tips": [
            "Use EXPLAIN untuk analyze queries",
            "Index columns used in WHERE/JOIN",
            "Avoid SELECT * in production",
            "Use proper data types",
            "Batch inserts untuk bulk data",
            "Use CTEs untuk readable complex queries"
        ]
    },
    "api_tips": {
        "category": "Programming Tips",
        "definition": "API design tips.",
        "tips": [
            "Use nouns for endpoints, not verbs",
            "Version your APIs (/v1/)",
            "Return proper HTTP status codes",
            "Implement pagination untuk large datasets",
            "Use rate limiting",
            "Document everything"
        ]
    },
    "security_tips": {
        "category": "Programming Tips",
        "definition": "Security best practices.",
        "tips": [
            "Never trust user input - validate everything",
            "Use parameterized queries (prevent SQL injection)",
            "Hash passwords with bcrypt/argon2",
            "Use HTTPS everywhere",
            "Keep dependencies updated",
            "Implement proper authentication"
        ]
    },
    
    # ============================================
    # FAMOUS QUOTES - PROGRAMMING
    # ============================================
    "programming_quotes": {
        "category": "Quotes",
        "definition": "Famous programming quotes.",
        "quotes": [
            "'Talk is cheap. Show me the code.' - Linus Torvalds",
            "'First, solve the problem. Then, write the code.' - John Johnson",
            "'Any fool can write code that a computer can understand. Good programmers write code that humans can understand.' - Martin Fowler",
            "'The best error message is the one that never shows up.' - Thomas Fuchs",
            "'It's not a bug – it's an undocumented feature.' - Anonymous",
            "'Debugging is twice as hard as writing the code in the first place.' - Brian Kernighan"
        ]
    },
    "tech_quotes": {
        "category": "Quotes",
        "definition": "Famous technology quotes.",
        "quotes": [
            "'The only way to do great work is to love what you do.' - Steve Jobs",
            "'Move fast and break things.' - Mark Zuckerberg",
            "'Information is power. But like all power, there are those who want to keep it for themselves.' - Aaron Swartz",
            "'The best time to plant a tree was 20 years ago. The second best time is now.' - Chinese Proverb",
            "'Stay hungry, stay foolish.' - Steve Jobs"
        ]
    },
    "life_quotes": {
        "category": "Quotes",
        "definition": "Inspirational life quotes.",
        "quotes": [
            "'Be the change you wish to see in the world.' - Gandhi",
            "'In the middle of difficulty lies opportunity.' - Albert Einstein",
            "'The only thing we have to fear is fear itself.' - FDR",
            "'Success is not final, failure is not fatal: it is the courage to continue that counts.' - Winston Churchill",
            "'The journey of a thousand miles begins with a single step.' - Lao Tzu"
        ]
    },
    "motivation_quotes": {
        "category": "Quotes",
        "definition": "Motivational quotes untuk developer.",
        "quotes": [
            "'You don't have to be great to start, but you have to start to be great.' - Zig Ziglar",
            "'The expert in anything was once a beginner.' - Helen Hayes",
            "'Done is better than perfect.' - Sheryl Sandberg",
            "'If you're not embarrassed by the first version of your product, you've launched too late.' - Reid Hoffman"
        ]
    },
    
    # ============================================
    # RANDOM INTERESTING FACTS
    # ============================================
    "random_facts_tech": {
        "category": "Facts",
        "definition": "Random technology facts.",
        "facts": [
            "First computer bug was actual bug - moth in Harvard Mark II (1947)",
            "QWERTY keyboard designed to SLOW DOWN typing (prevent typewriter jams)",
            "Original name of Windows was 'Interface Manager'",
            "First email ever sent was by Ray Tomlinson to himself (1971)",
            "Google's first tweet was in binary: 'I'm feeling lucky'",
            "The first computer programmer was Ada Lovelace (1843)"
        ]
    },
    "random_facts_internet": {
        "category": "Facts",
        "definition": "Random internet facts.",
        "facts": [
            "First website still online: info.cern.ch (1991)",
            "There are ~2 billion websites, but only ~400 million active",
            "Internet weighs ~50 grams (electrons storing data)",
            "First YouTube video: 'Me at the zoo' (April 2005)",
            "First Amazon employee (besides Bezos) was Shel Kaphan",
            "Google processes 8.5 billion searches per day"
        ]
    },
    "random_facts_science": {
        "category": "Facts",
        "definition": "Random science facts.",
        "facts": [
            "Honey never spoils - 3000 year old honey still edible",
            "Octopuses have 3 hearts and blue blood",
            "A day on Venus is longer than a year on Venus",
            "Hot water freezes faster than cold water (Mpemba effect)",
            "The average cloud weighs 1.1 million pounds",
            "There are more trees on Earth than stars in Milky Way"
        ]
    },
    "random_facts_human": {
        "category": "Facts",
        "definition": "Random human body facts.",
        "facts": [
            "Your brain uses 20% of your total energy",
            "Humans share 60% DNA with bananas",
            "You're taller in the morning than evening",
            "Your heart beats 100,000+ times per day",
            "Stomach acid can dissolve metal",
            "You produce enough saliva to fill 2 swimming pools in lifetime"
        ]
    },
    "random_facts_world": {
        "category": "Facts",
        "definition": "Random world facts.",
        "facts": [
            "France has the most time zones (12)",
            "Russia spans 11 time zones",
            "Vatican City is world's smallest country",
            "Indonesia has 17,000+ islands",
            "Antarctica is the largest desert",
            "Africa is the only continent in all 4 hemispheres"
        ]
    },
    "random_facts_space": {
        "category": "Facts",
        "definition": "Random space facts.",
        "facts": [
            "One million Earths could fit inside the Sun",
            "Space is completely silent",
            "There are more stars than grains of sand on Earth",
            "Neutron star teaspoon weighs 6 billion tons",
            "If you could drive to space, it would take 1 hour",
            "The Sun makes up 99.86% of solar system mass"
        ]
    },
    
    # ============================================
    # ACRONYMS & ABBREVIATIONS
    # ============================================
    "tech_acronyms": {
        "category": "Reference",
        "definition": "Common tech acronyms.",
        "acronyms": {
            "API": "Application Programming Interface",
            "REST": "Representational State Transfer",
            "SQL": "Structured Query Language",
            "HTML": "HyperText Markup Language",
            "CSS": "Cascading Style Sheets",
            "URL": "Uniform Resource Locator",
            "HTTP": "HyperText Transfer Protocol",
            "DNS": "Domain Name System",
            "SDK": "Software Development Kit",
            "IDE": "Integrated Development Environment"
        }
    },
    "business_acronyms": {
        "category": "Reference",
        "definition": "Common business acronyms.",
        "acronyms": {
            "ROI": "Return on Investment",
            "KPI": "Key Performance Indicator",
            "CEO": "Chief Executive Officer",
            "CTO": "Chief Technology Officer",
            "B2B": "Business to Business",
            "B2C": "Business to Consumer",
            "SaaS": "Software as a Service",
            "MVP": "Minimum Viable Product"
        }
    },
    "chat_acronyms": {
        "category": "Reference",
        "definition": "Common chat/internet acronyms.",
        "acronyms": {
            "ASAP": "As Soon As Possible",
            "FYI": "For Your Information",
            "IMO/IMHO": "In My (Humble) Opinion",
            "TBH": "To Be Honest",
            "LMAO": "Laughing My Ass Off",
            "SMH": "Shaking My Head",
            "TL;DR": "Too Long; Didn't Read",
            "FOMO": "Fear Of Missing Out",
            "YOLO": "You Only Live Once"
        }
    },
    
    # ============================================
    # PROGRAMMING HUMOR
    # ============================================
    "programming_jokes": {
        "category": "Humor",
        "definition": "Classic programming jokes.",
        "jokes": [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "There are only 10 types of people: those who understand binary and those who don't.",
            "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'",
            "Why do Java developers wear glasses? Because they don't C#.",
            "!false - it's funny because it's true.",
            "console.log('Hello World') - every programmer's first love affair."
        ]
    },
    "it_jokes": {
        "category": "Humor",
        "definition": "IT support jokes.",
        "jokes": [
            "Have you tried turning it off and on again?",
            "It works on my machine.",
            "The code is self-documenting. (It's not.)",
            "We'll fix it in the next sprint.",
            "It's not a bug, it's a feature.",
            "The project will be done in 2 weeks. (Said 6 months ago.)"
        ]
    },
    
    # ============================================
    # EMOJIS MEANING
    # ============================================
    "emoji_meanings": {
        "category": "Reference",
        "definition": "Common emoji meanings in tech/internet context.",
        "emojis": {
            "🚀": "Launch, go fast, exciting",
            "💡": "Idea, insight",
            "🔥": "Hot, trending, great",
            "💀": "Dead (laughing), RIP",
            "🤡": "Clown, foolish behavior",
            "🧠": "Smart, brain power",
            "👀": "Looking, interesting",
            "💯": "100%, perfect, agree",
            "⚡": "Fast, powerful",
            "🎉": "Celebration, congrats"
        }
    },
    
    # ============================================
    # DEVELOPER LIFE
    # ============================================
    "developer_stereotypes": {
        "category": "Culture",
        "definition": "Developer stereotypes (untuk hiburan).",
        "stereotypes": [
            "Morning: Coffee. Afternoon: Coffee. Night: Coffee.",
            "Stack Overflow adalah bestfriend",
            "Mechanical keyboard enthusiast",
            "Dark mode everything",
            "Multiple monitors adalah kebutuhan",
            "Deadline adalah hanya suggestion"
        ]
    },
    "developer_stages": {
        "category": "Culture",
        "definition": "Stages of developer learning.",
        "stages": [
            "1. I know nothing",
            "2. I know everything (Dunning-Kruger peak)",
            "3. I know nothing (Valley of despair)",
            "4. I'm learning and growing",
            "5. I know what I don't know",
            "6. Always a student"
        ]
    },
    "developer_tools": {
        "category": "Culture",
        "definition": "Essential developer tools.",
        "tools": [
            "Terminal - Your command center",
            "Git - Version control salvation",
            "Stack Overflow - When all else fails",
            "Google - The real IDE",
            "Coffee - Liquid productivity",
            "Rubber duck - Best debugger"
        ]
    },
    
    # ============================================
    # KEYBOARD SHORTCUTS
    # ============================================
    "universal_shortcuts": {
        "category": "Reference",
        "definition": "Universal keyboard shortcuts.",
        "shortcuts": {
            "Ctrl+C": "Copy",
            "Ctrl+V": "Paste",
            "Ctrl+X": "Cut",
            "Ctrl+Z": "Undo",
            "Ctrl+Y / Ctrl+Shift+Z": "Redo",
            "Ctrl+S": "Save",
            "Ctrl+F": "Find",
            "Ctrl+A": "Select All",
            "Alt+Tab": "Switch windows",
            "Ctrl+Shift+Esc": "Task Manager (Windows)"
        }
    },
    "browser_shortcuts": {
        "category": "Reference",
        "definition": "Browser keyboard shortcuts.",
        "shortcuts": {
            "Ctrl+T": "New tab",
            "Ctrl+W": "Close tab",
            "Ctrl+Shift+T": "Reopen closed tab",
            "Ctrl+L": "Focus address bar",
            "Ctrl+R / F5": "Refresh",
            "Ctrl+Shift+N": "Incognito/Private",
            "Ctrl+D": "Bookmark page",
            "F12": "Developer tools"
        }
    },
    
    # ============================================
    # CODING CHALLENGES PLATFORMS
    # ============================================
    "coding_platforms": {
        "category": "Resources",
        "definition": "Platforms untuk latihan coding.",
        "platforms": {
            "LeetCode": "Interview prep, algorithm challenges",
            "HackerRank": "Skill certification, practice",
            "Codewars": "Gamified coding challenges (kata)",
            "Exercism": "Mentored learning, many languages",
            "Advent of Code": "Annual December puzzle event",
            "Project Euler": "Mathematical/computational problems"
        }
    },
    "learning_resources": {
        "category": "Resources",
        "definition": "Free learning resources.",
        "resources": {
            "freeCodeCamp": "Free full-stack curriculum",
            "The Odin Project": "Full-stack web development",
            "Coursera/edX": "University courses (audit free)",
            "YouTube": "Traversy Media, Fireship, etc",
            "MDN Web Docs": "Web development documentation",
            "roadmap.sh": "Developer roadmaps"
        }
    },
    
    # ============================================
    # VERSION CONTROL WISDOM
    # ============================================
    "commit_message_guide": {
        "category": "Best Practice",
        "definition": "Good commit message practices.",
        "format": "type(scope): description",
        "types": {
            "feat": "New feature",
            "fix": "Bug fix",
            "docs": "Documentation",
            "style": "Formatting (no logic change)",
            "refactor": "Code restructuring",
            "test": "Adding tests",
            "chore": "Maintenance tasks"
        }
    },
    
    # ============================================
    # TECH COMPANY CULTURE
    # ============================================
    "faang": {
        "category": "Industry",
        "definition": "FAANG/MAANG - Top tech companies.",
        "companies": {
            "Meta (Facebook)": "Social media, metaverse",
            "Apple": "Consumer electronics, services",
            "Amazon": "E-commerce, AWS cloud",
            "Netflix": "Streaming entertainment",
            "Google (Alphabet)": "Search, advertising, cloud"
        },
        "also": "Microsoft often included (MAANG)"
    },
    "startup_culture": {
        "category": "Industry",
        "definition": "Startup culture elements.",
        "elements": [
            "Move fast and break things",
            "Fail fast, learn faster",
            "Flat hierarchy",
            "Wear many hats",
            "Work hard, play hard",
            "Disrupt the industry"
        ]
    },
    
    # ============================================
    # HTTP STATUS CODES EXPLAINED
    # ============================================
    "http_codes_explained": {
        "category": "Reference",
        "definition": "HTTP status codes dengan penjelasan.",
        "codes": {
            "200 OK": "Success! Everything worked.",
            "201 Created": "Success! Resource created.",
            "204 No Content": "Success! Nothing to return.",
            "301 Moved Permanently": "URL changed forever.",
            "400 Bad Request": "Your request is malformed.",
            "401 Unauthorized": "Who are you? Login first.",
            "403 Forbidden": "I know you, but no access.",
            "404 Not Found": "Resource doesn't exist.",
            "418 I'm a teapot": "Easter egg from April Fools RFC.",
            "500 Internal Server Error": "Server broke. Our fault.",
            "502 Bad Gateway": "Upstream server failed.",
            "503 Service Unavailable": "Server overloaded/down."
        }
    },
    
    # ============================================
    # FAMOUS TECH FAILURES
    # ============================================
    "tech_failures": {
        "category": "History",
        "definition": "Famous tech failures dan lessons.",
        "failures": {
            "Google+": "Failed social network, shut down 2019",
            "Windows Vista": "Resource hog, security nightmare",
            "Yahoo turning down Google": "Could have bought for $1M",
            "Blockbuster refusing Netflix": "Offered for $50M, now bankrupt",
            "Kodak ignoring digital": "Invented digital camera but didn't adapt",
            "Nokia smartphone transition": "Once #1, too slow to adapt"
        }
    },
    
    # ============================================
    # TECH ORIGIN STORIES
    # ============================================
    "company_origins": {
        "category": "History",
        "definition": "How famous tech companies started.",
        "origins": {
            "Google": "PhD project in Stanford garage (1998)",
            "Apple": "Steve Jobs' parents' garage (1976)",
            "Amazon": "Jeff Bezos' garage, online bookstore (1994)",
            "Facebook": "Harvard dorm room (2004)",
            "Microsoft": "Paul Allen and Bill Gates, BASIC (1975)",
            "Netflix": "Mail-order DVDs, late fee frustration (1997)"
        }
    },
    "language_origins": {
        "category": "History",
        "definition": "Origins of programming languages.",
        "origins": {
            "Python": "Guido van Rossum, Christmas project (1991)",
            "JavaScript": "Brendan Eich, created in 10 days (1995)",
            "Java": "James Gosling at Sun Microsystems (1995)",
            "C": "Dennis Ritchie at Bell Labs (1972)",
            "Ruby": "Yukihiro Matsumoto, inspired by Perl (1995)",
            "Go": "Google, by Rob Pike and Ken Thompson (2009)"
        }
    },
    
    # ============================================
    # INTERNET MILESTONES
    # ============================================
    "internet_milestones": {
        "category": "History",
        "definition": "Important internet milestones.",
        "milestones": {
            "1969": "ARPANET - first message sent",
            "1983": "TCP/IP adopted - birth of Internet",
            "1989": "World Wide Web invented by Tim Berners-Lee",
            "1991": "First website goes live",
            "1994": "Amazon and Yahoo founded",
            "1998": "Google founded",
            "2004": "Facebook launched",
            "2005": "YouTube launched",
            "2007": "iPhone released, mobile revolution",
            "2009": "Bitcoin created"
        }
    },
}
