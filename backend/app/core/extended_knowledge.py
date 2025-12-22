"""
WeaR AI Extended Knowledge Base
Ratusan topik tambahan untuk memperluas pengetahuan AI.
Created by RidTheWann
"""

# Extended knowledge untuk di-merge dengan main knowledge base

EXTENDED_KNOWLEDGE = {
    # ============================================
    # PROGRAMMING CONCEPTS (50+ topics)
    # ============================================
    "variable": {
        "category": "Programming Basics",
        "definition": "Variable adalah wadah untuk menyimpan data yang dapat berubah nilainya.",
        "types": ["Integer", "Float", "String", "Boolean", "Array/List", "Object/Dict"],
        "example": "name = 'WeaR AI'  # String\nage = 1  # Integer\nis_active = True  # Boolean"
    },
    "function": {
        "category": "Programming Basics",
        "definition": "Function adalah blok kode yang dapat dipanggil berulang kali untuk melakukan tugas tertentu.",
        "components": ["Parameters", "Return Value", "Function Body", "Docstring"],
        "types": ["Regular Function", "Lambda/Anonymous", "Generator", "Async Function"],
        "example": "def greet(name):\n    return f'Hello, {name}!'\n\nresult = greet('World')"
    },
    "loop": {
        "category": "Programming Basics",
        "definition": "Loop adalah struktur kontrol untuk mengeksekusi blok kode berulang kali.",
        "types": {
            "for": "Iterasi dengan jumlah yang diketahui",
            "while": "Iterasi selama kondisi true",
            "do-while": "Minimal eksekusi sekali (tidak ada di Python)"
        },
        "control": ["break (keluar loop)", "continue (skip iterasi)", "else (setelah loop selesai)"]
    },
    "conditional": {
        "category": "Programming Basics",
        "definition": "Conditional adalah struktur untuk mengeksekusi kode berdasarkan kondisi.",
        "syntax": ["if", "else", "elif/else if", "switch/match"],
        "operators": ["== (equal)", "!= (not equal)", "> < >= <=", "and, or, not"]
    },
    "class": {
        "category": "OOP",
        "definition": "Class adalah blueprint untuk membuat object dengan properties dan methods.",
        "components": ["Constructor (__init__)", "Attributes", "Methods", "Inheritance"],
        "example": "class Dog:\n    def __init__(self, name):\n        self.name = name\n    def bark(self):\n        return 'Woof!'"
    },
    "object": {
        "category": "OOP",
        "definition": "Object adalah instance dari class yang memiliki state dan behavior.",
        "concepts": ["Instance", "Attributes", "Methods", "Identity"]
    },
    "inheritance": {
        "category": "OOP",
        "definition": "Inheritance memungkinkan class mewarisi properties dan methods dari class lain.",
        "types": ["Single", "Multiple", "Multilevel", "Hierarchical"],
        "keywords": ["extends (Java)", ": (Python)", "super()"]
    },
    "polymorphism": {
        "category": "OOP",
        "definition": "Polymorphism memungkinkan object berbeda merespons method yang sama dengan cara berbeda.",
        "types": ["Method Overriding", "Method Overloading", "Duck Typing"]
    },
    "encapsulation": {
        "category": "OOP",
        "definition": "Encapsulation adalah bundling data dan methods, serta menyembunyikan detail internal.",
        "access_modifiers": ["public", "private (_)", "protected (__)"]
    },
    "abstraction": {
        "category": "OOP",
        "definition": "Abstraction adalah menyembunyikan kompleksitas dan menampilkan hanya interface yang diperlukan.",
        "implementation": ["Abstract Class", "Interface", "Protocol"]
    },
    "exception": {
        "category": "Programming",
        "definition": "Exception adalah event yang mengganggu alur normal program execution.",
        "handling": ["try", "except/catch", "finally", "raise/throw"],
        "common_exceptions": ["ValueError", "TypeError", "IndexError", "KeyError", "FileNotFoundError"]
    },
    "decorator": {
        "category": "Python",
        "definition": "Decorator adalah function yang memodifikasi behavior function lain.",
        "use_cases": ["Logging", "Authentication", "Caching", "Timing"],
        "example": "@timer\ndef slow_function():\n    pass"
    },
    "generator": {
        "category": "Python",
        "definition": "Generator adalah function yang menghasilkan sequence of values menggunakan yield.",
        "benefits": ["Memory Efficient", "Lazy Evaluation", "Infinite Sequences"],
        "example": "def count_up():\n    n = 0\n    while True:\n        yield n\n        n += 1"
    },
    "context_manager": {
        "category": "Python",
        "definition": "Context Manager mengelola resources dengan setup dan cleanup otomatis.",
        "syntax": "with open('file.txt') as f:\n    content = f.read()",
        "methods": ["__enter__", "__exit__"]
    },
    "closure": {
        "category": "Programming",
        "definition": "Closure adalah function yang mengingat environment di mana ia dibuat.",
        "use_cases": ["Data Hiding", "Function Factories", "Callbacks"]
    },
    "lambda": {
        "category": "Programming",
        "definition": "Lambda adalah anonymous function yang ditulis dalam satu ekspresi.",
        "syntax": {"Python": "lambda x: x * 2", "JavaScript": "(x) => x * 2", "Java": "x -> x * 2"}
    },
    "list_comprehension": {
        "category": "Python",
        "definition": "List comprehension adalah cara ringkas untuk membuat list dari iterable.",
        "syntax": "[expression for item in iterable if condition]",
        "example": "squares = [x**2 for x in range(10) if x % 2 == 0]"
    },
    "async_programming": {
        "category": "Programming",
        "definition": "Async programming memungkinkan eksekusi non-blocking untuk operasi I/O.",
        "concepts": ["Event Loop", "Coroutines", "Futures/Promises", "await"],
        "use_cases": ["Web Servers", "API Calls", "File I/O", "Database Queries"]
    },
    "threading": {
        "category": "Programming",
        "definition": "Threading memungkinkan eksekusi concurrent dalam satu process.",
        "concepts": ["Thread", "Lock", "Semaphore", "Deadlock", "Race Condition"],
        "vs_multiprocessing": "Threading untuk I/O-bound, Multiprocessing untuk CPU-bound"
    },
    "multiprocessing": {
        "category": "Programming",
        "definition": "Multiprocessing menggunakan multiple processes untuk parallel execution.",
        "benefits": ["True Parallelism", "Bypass GIL (Python)", "Isolation"],
        "concepts": ["Process", "Pool", "Queue", "Pipe"]
    },
    "api_design": {
        "category": "Software Engineering",
        "definition": "API Design adalah seni merancang interface yang intuitif dan consistent.",
        "principles": ["Consistency", "Simplicity", "Versioning", "Documentation", "Error Handling"],
        "best_practices": ["Use nouns for resources", "HTTP methods correctly", "Pagination", "Rate limiting"]
    },
    "testing_pyramid": {
        "category": "Testing",
        "definition": "Testing Pyramid menunjukkan proporsi ideal berbagai jenis test.",
        "layers": {
            "Unit Tests": "70% - Fast, isolated",
            "Integration Tests": "20% - Component interaction",
            "E2E Tests": "10% - Full user journey"
        }
    },
    "mocking": {
        "category": "Testing",
        "definition": "Mocking adalah teknik mengganti dependencies dengan fake objects untuk testing.",
        "types": ["Mock", "Stub", "Spy", "Fake"],
        "libraries": ["unittest.mock (Python)", "Jest (JS)", "Mockito (Java)"]
    },
    "code_review": {
        "category": "Software Engineering",
        "definition": "Code Review adalah proses systematic memeriksa kode oleh peers.",
        "checklist": ["Logic correctness", "Code style", "Performance", "Security", "Test coverage"],
        "tools": ["GitHub PR", "GitLab MR", "Gerrit", "Crucible"]
    },
    "refactoring": {
        "category": "Software Engineering",
        "definition": "Refactoring adalah mengubah struktur kode tanpa mengubah behavior.",
        "techniques": ["Extract Method", "Rename Variable", "Move Class", "Replace Conditional with Polymorphism"],
        "when": ["Code smells", "Before adding features", "After bug fixes"]
    },
    "code_smell": {
        "category": "Software Engineering",
        "definition": "Code Smell adalah indikasi masalah dalam kode yang mungkin perlu refactoring.",
        "examples": ["Long Method", "Duplicate Code", "God Class", "Feature Envy", "Magic Numbers"]
    },
    "technical_debt": {
        "category": "Software Engineering",
        "definition": "Technical Debt adalah implied cost dari rework karena memilih solusi cepat.",
        "types": ["Deliberate", "Accidental", "Bit Rot"],
        "management": ["Track in backlog", "Pay down regularly", "Prevent with standards"]
    },
    "agile": {
        "category": "Methodology",
        "definition": "Agile adalah metodologi iterative yang fokus pada delivering value dengan cepat.",
        "values": ["Individuals over processes", "Working software over documentation", "Customer collaboration", "Responding to change"],
        "frameworks": ["Scrum", "Kanban", "XP", "SAFe"]
    },
    "scrum": {
        "category": "Methodology",
        "definition": "Scrum adalah Agile framework dengan sprints, roles, dan ceremonies.",
        "roles": ["Product Owner", "Scrum Master", "Development Team"],
        "events": ["Sprint Planning", "Daily Standup", "Sprint Review", "Retrospective"],
        "artifacts": ["Product Backlog", "Sprint Backlog", "Increment"]
    },
    "kanban": {
        "category": "Methodology",
        "definition": "Kanban adalah visual workflow management dengan WIP limits.",
        "principles": ["Visualize work", "Limit WIP", "Manage flow", "Continuous improvement"],
        "columns": ["To Do", "In Progress", "Review", "Done"]
    },
    
    # ============================================
    # WEB DEVELOPMENT (40+ topics)
    # ============================================
    "html": {
        "category": "Web",
        "definition": "HTML (HyperText Markup Language) adalah bahasa markup untuk struktur web pages.",
        "elements": ["<div>", "<span>", "<p>", "<h1>-<h6>", "<a>", "<img>", "<form>", "<table>"],
        "semantic": ["<header>", "<nav>", "<main>", "<article>", "<section>", "<footer>"]
    },
    "css": {
        "category": "Web",
        "definition": "CSS (Cascading Style Sheets) adalah bahasa untuk styling HTML elements.",
        "concepts": ["Selectors", "Box Model", "Flexbox", "Grid", "Responsive Design"],
        "preprocessors": ["SASS", "LESS", "Stylus"]
    },
    "flexbox": {
        "category": "CSS",
        "definition": "Flexbox adalah CSS layout mode untuk distribusi ruang dalam container.",
        "container_properties": ["display: flex", "flex-direction", "justify-content", "align-items"],
        "item_properties": ["flex-grow", "flex-shrink", "flex-basis", "order"]
    },
    "css_grid": {
        "category": "CSS",
        "definition": "CSS Grid adalah 2D layout system untuk complex layouts.",
        "properties": ["grid-template-columns", "grid-template-rows", "grid-gap", "grid-area"]
    },
    "responsive_design": {
        "category": "Web",
        "definition": "Responsive Design adalah approach agar website terlihat baik di semua devices.",
        "techniques": ["Media Queries", "Fluid Grids", "Flexible Images", "Mobile First"],
        "breakpoints": ["320px (mobile)", "768px (tablet)", "1024px (desktop)", "1440px (large)"]
    },
    "dom": {
        "category": "Web",
        "definition": "DOM (Document Object Model) adalah API untuk HTML/XML documents.",
        "methods": ["getElementById", "querySelector", "createElement", "appendChild"],
        "manipulation": "JavaScript dapat mengubah content, structure, dan style via DOM"
    },
    "ajax": {
        "category": "Web",
        "definition": "AJAX memungkinkan update web page tanpa full reload.",
        "modern_api": "fetch() API menggantikan XMLHttpRequest",
        "example": "fetch('/api/data').then(r => r.json()).then(data => console.log(data))"
    },
    "cors": {
        "category": "Web Security",
        "definition": "CORS (Cross-Origin Resource Sharing) mengontrol akses resources antar origins.",
        "headers": ["Access-Control-Allow-Origin", "Access-Control-Allow-Methods", "Access-Control-Allow-Headers"],
        "preflight": "OPTIONS request untuk complex requests"
    },
    "cookie": {
        "category": "Web",
        "definition": "Cookie adalah small data yang disimpan browser untuk state management.",
        "attributes": ["Expires/Max-Age", "HttpOnly", "Secure", "SameSite", "Path", "Domain"],
        "vs_storage": "Cookies dikirim ke server, localStorage/sessionStorage tidak"
    },
    "session": {
        "category": "Web",
        "definition": "Session menyimpan state user di server side.",
        "storage": ["In-memory", "Database", "Redis", "File"],
        "identification": "Session ID via cookie atau URL"
    },
    "localstorage": {
        "category": "Web",
        "definition": "localStorage menyimpan data di browser tanpa expiration.",
        "limit": "~5-10MB per origin",
        "api": ["setItem(key, value)", "getItem(key)", "removeItem(key)", "clear()"]
    },
    "pwa": {
        "category": "Web",
        "definition": "PWA (Progressive Web App) adalah web app dengan native-like experience.",
        "features": ["Offline Support", "Push Notifications", "Installable", "Responsive"],
        "requirements": ["HTTPS", "Service Worker", "Web App Manifest"]
    },
    "service_worker": {
        "category": "Web",
        "definition": "Service Worker adalah script yang berjalan di background untuk offline/caching.",
        "lifecycle": ["Register", "Install", "Activate", "Fetch"],
        "use_cases": ["Offline caching", "Background sync", "Push notifications"]
    },
    "spa": {
        "category": "Web Architecture",
        "definition": "SPA (Single Page Application) memuat satu HTML dan update content via JavaScript.",
        "pros": ["Fast navigation", "Rich UX", "Less server load"],
        "cons": ["SEO challenges", "Initial load", "JavaScript dependency"],
        "frameworks": ["React", "Vue", "Angular"]
    },
    "ssr": {
        "category": "Web Architecture",
        "definition": "SSR (Server-Side Rendering) merender HTML di server sebelum dikirim ke client.",
        "benefits": ["SEO friendly", "Faster FCP", "Works without JS"],
        "frameworks": ["Next.js", "Nuxt.js", "Remix"]
    },
    "ssg": {
        "category": "Web Architecture",
        "definition": "SSG (Static Site Generation) menghasilkan HTML statis saat build time.",
        "benefits": ["Super fast", "CDN-friendly", "Secure"],
        "tools": ["Next.js", "Gatsby", "Hugo", "Jekyll", "Astro"]
    },
    "bundler": {
        "category": "Web Tooling",
        "definition": "Bundler menggabungkan dan mengoptimasi JavaScript modules.",
        "tools": ["Webpack", "Vite", "Rollup", "Parcel", "esbuild"],
        "features": ["Tree shaking", "Code splitting", "Minification", "Hot reload"]
    },
    "npm": {
        "category": "Web Tooling",
        "definition": "npm adalah package manager untuk JavaScript/Node.js.",
        "commands": ["npm install", "npm run", "npm publish", "npm update"],
        "files": ["package.json", "package-lock.json", "node_modules/"]
    },
    "yarn": {
        "category": "Web Tooling",
        "definition": "Yarn adalah alternatif npm dengan focus pada speed dan security.",
        "features": ["Parallel installation", "Workspaces", "Plug'n'Play"]
    },
    "tailwindcss": {
        "category": "CSS Framework",
        "definition": "Tailwind CSS adalah utility-first CSS framework.",
        "approach": "Menggunakan utility classes langsung di HTML",
        "example": "<div class=\"flex items-center justify-between p-4 bg-blue-500\">"
    },
    "bootstrap": {
        "category": "CSS Framework",
        "definition": "Bootstrap adalah CSS framework dengan pre-built components.",
        "components": ["Navbar", "Cards", "Modals", "Forms", "Grid System"],
        "version": "Bootstrap 5 (no jQuery dependency)"
    },
    
    # ============================================
    # NETWORKING (20+ topics)
    # ============================================
    "http": {
        "category": "Protocol",
        "definition": "HTTP (Hypertext Transfer Protocol) adalah protokol untuk transfer data di web.",
        "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"],
        "versions": ["HTTP/1.1", "HTTP/2", "HTTP/3 (QUIC)"]
    },
    "https": {
        "category": "Protocol",
        "definition": "HTTPS adalah HTTP dengan encryption via TLS/SSL.",
        "benefits": ["Encryption", "Data Integrity", "Authentication"],
        "certificate": "SSL Certificate dari CA (Certificate Authority)"
    },
    "tcp": {
        "category": "Protocol",
        "definition": "TCP (Transmission Control Protocol) adalah reliable, connection-oriented protocol.",
        "features": ["Reliable delivery", "Ordered packets", "Error checking", "Flow control"],
        "handshake": "3-way handshake (SYN, SYN-ACK, ACK)"
    },
    "udp": {
        "category": "Protocol",
        "definition": "UDP (User Datagram Protocol) adalah fast, connectionless protocol.",
        "features": ["No connection setup", "No guaranteed delivery", "Low latency"],
        "use_cases": ["Video streaming", "Gaming", "DNS", "VoIP"]
    },
    "ip_address": {
        "category": "Networking",
        "definition": "IP Address adalah unique identifier untuk device di network.",
        "versions": {
            "IPv4": "32-bit, e.g., 192.168.1.1",
            "IPv6": "128-bit, e.g., 2001:0db8:85a3::8a2e:0370:7334"
        },
        "types": ["Public", "Private", "Static", "Dynamic"]
    },
    "dns": {
        "category": "Networking",
        "definition": "DNS (Domain Name System) menerjemahkan domain name ke IP address.",
        "records": ["A (IPv4)", "AAAA (IPv6)", "CNAME", "MX", "TXT", "NS"],
        "process": "Browser → DNS Resolver → Root → TLD → Authoritative"
    },
    "load_balancing": {
        "category": "Infrastructure",
        "definition": "Load Balancing mendistribusikan traffic ke multiple servers.",
        "algorithms": ["Round Robin", "Least Connections", "IP Hash", "Weighted"],
        "types": ["Layer 4 (TCP)", "Layer 7 (HTTP)"],
        "tools": ["NGINX", "HAProxy", "AWS ELB", "Cloudflare"]
    },
    "cdn": {
        "category": "Infrastructure",
        "definition": "CDN (Content Delivery Network) menyebarkan content ke edge servers global.",
        "benefits": ["Reduced latency", "High availability", "DDoS protection"],
        "providers": ["Cloudflare", "AWS CloudFront", "Akamai", "Fastly"]
    },
    "proxy": {
        "category": "Networking",
        "definition": "Proxy adalah intermediary server antara client dan target server.",
        "types": {
            "Forward Proxy": "Client → Proxy → Internet",
            "Reverse Proxy": "Internet → Proxy → Server"
        },
        "use_cases": ["Caching", "Security", "Load balancing", "Anonymity"]
    },
    "vpn": {
        "category": "Networking",
        "definition": "VPN (Virtual Private Network) membuat encrypted tunnel untuk private communication.",
        "protocols": ["OpenVPN", "WireGuard", "IPSec", "L2TP"],
        "use_cases": ["Privacy", "Remote access", "Bypass geo-restrictions"]
    },
    "firewall": {
        "category": "Security",
        "definition": "Firewall mengontrol network traffic berdasarkan security rules.",
        "types": ["Packet filtering", "Stateful inspection", "Application layer", "Next-gen (NGFW)"],
        "tools": ["iptables", "ufw", "pfSense", "AWS Security Groups"]
    },
    "ssh": {
        "category": "Protocol",
        "definition": "SSH (Secure Shell) adalah protokol untuk secure remote access.",
        "features": ["Encrypted connection", "Key-based auth", "Port forwarding", "SFTP"],
        "command": "ssh user@hostname -p 22"
    },
    
    # ============================================
    # MATH & ALGORITHMS (30+ topics)
    # ============================================
    "binary_search": {
        "category": "Algorithm",
        "definition": "Binary Search mencari element dalam sorted array dengan membagi setengah setiap langkah.",
        "complexity": "O(log n)",
        "requirement": "Array harus sorted",
        "example": "def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target: return mid\n        elif arr[mid] < target: left = mid + 1\n        else: right = mid - 1\n    return -1"
    },
    "bfs": {
        "category": "Algorithm",
        "definition": "BFS (Breadth-First Search) menjelajahi graph level by level.",
        "complexity": "O(V + E)",
        "data_structure": "Queue",
        "use_cases": ["Shortest path (unweighted)", "Level-order traversal", "Connected components"]
    },
    "dfs": {
        "category": "Algorithm",
        "definition": "DFS (Depth-First Search) menjelajahi graph sejauh mungkin sebelum backtrack.",
        "complexity": "O(V + E)",
        "data_structure": "Stack / Recursion",
        "use_cases": ["Path finding", "Topological sort", "Cycle detection"]
    },
    "dijkstra": {
        "category": "Algorithm",
        "definition": "Dijkstra's Algorithm mencari shortest path dari source ke semua nodes.",
        "complexity": "O((V + E) log V) with priority queue",
        "requirement": "Non-negative edge weights",
        "use_cases": ["GPS Navigation", "Network routing"]
    },
    "two_pointer": {
        "category": "Algorithm Technique",
        "definition": "Two Pointer menggunakan dua pointer untuk traverse array/string efisien.",
        "patterns": ["Opposite directions", "Same direction", "Sliding window"],
        "use_cases": ["Pair sum", "Remove duplicates", "Palindrome check"]
    },
    "sliding_window": {
        "category": "Algorithm Technique",
        "definition": "Sliding Window memproses subset contiguous elements secara efisien.",
        "types": ["Fixed size", "Variable size"],
        "use_cases": ["Max sum subarray", "Longest substring", "Averages"]
    },
    "divide_conquer": {
        "category": "Algorithm Technique",
        "definition": "Divide and Conquer membagi problem menjadi subproblems, solve, lalu combine.",
        "steps": ["Divide", "Conquer (recursive)", "Combine"],
        "examples": ["Merge Sort", "Quick Sort", "Binary Search"]
    },
    "greedy": {
        "category": "Algorithm Technique",
        "definition": "Greedy Algorithm membuat optimal choice di setiap langkah.",
        "characteristics": ["Local optimum", "No backtracking", "May not be globally optimal"],
        "examples": ["Activity Selection", "Huffman Coding", "Dijkstra"]
    },
    "backtracking": {
        "category": "Algorithm Technique",
        "definition": "Backtracking adalah DFS dengan constraint checking untuk pruning.",
        "template": "if valid: add to solution; recurse; if fail: remove (backtrack)",
        "examples": ["N-Queens", "Sudoku Solver", "Permutations", "Subsets"]
    },
    "binary_tree": {
        "category": "Data Structure",
        "definition": "Binary Tree adalah tree di mana setiap node punya maksimal 2 children.",
        "types": ["Full", "Complete", "Perfect", "Balanced"],
        "traversals": ["Inorder (L-Root-R)", "Preorder (Root-L-R)", "Postorder (L-R-Root)"]
    },
    "bst": {
        "category": "Data Structure",
        "definition": "BST (Binary Search Tree) adalah binary tree dengan left < root < right.",
        "operations": {"Search": "O(log n)", "Insert": "O(log n)", "Delete": "O(log n)"},
        "worst_case": "O(n) untuk skewed tree"
    },
    "heap": {
        "category": "Data Structure",
        "definition": "Heap adalah complete binary tree dengan heap property.",
        "types": {
            "Min Heap": "Parent <= Children",
            "Max Heap": "Parent >= Children"
        },
        "operations": {"Insert": "O(log n)", "Extract": "O(log n)", "Peek": "O(1)"},
        "use_cases": ["Priority Queue", "Heap Sort", "Top K elements"]
    },
    "trie": {
        "category": "Data Structure",
        "definition": "Trie (Prefix Tree) menyimpan strings dengan shared prefixes.",
        "operations": "Insert, Search, StartsWith - O(m) where m = word length",
        "use_cases": ["Autocomplete", "Spell checker", "IP routing"]
    },
    "fibonacci": {
        "category": "Algorithm",
        "definition": "Fibonacci sequence: setiap angka adalah jumlah 2 angka sebelumnya.",
        "sequence": "0, 1, 1, 2, 3, 5, 8, 13, 21, 34...",
        "implementations": {
            "Recursive": "O(2^n) - exponential",
            "Memoization": "O(n) - top-down DP",
            "Tabulation": "O(n) - bottom-up DP",
            "Matrix": "O(log n) - matrix exponentiation"
        }
    },
    "prime_number": {
        "category": "Math",
        "definition": "Prime number hanya bisa dibagi 1 dan dirinya sendiri.",
        "examples": "2, 3, 5, 7, 11, 13, 17, 19, 23, 29...",
        "check": "Loop sampai √n",
        "sieve": "Sieve of Eratosthenes untuk generate primes"
    },
    "gcd_lcm": {
        "category": "Math",
        "definition": "GCD (Greatest Common Divisor) dan LCM (Least Common Multiple).",
        "gcd_algorithm": "Euclidean: gcd(a, b) = gcd(b, a % b)",
        "lcm_formula": "lcm(a, b) = (a * b) / gcd(a, b)"
    },
    "bit_manipulation": {
        "category": "Programming",
        "definition": "Bit Manipulation mengoperasikan data di level binary.",
        "operators": ["& (AND)", "| (OR)", "^ (XOR)", "~ (NOT)", "<< (left shift)", ">> (right shift)"],
        "tricks": ["x & 1 (odd check)", "x ^ x = 0", "x & (x-1) (clear lowest bit)"]
    },
    
    # ============================================
    # SYSTEM DESIGN (20+ topics)
    # ============================================
    "scalability": {
        "category": "System Design",
        "definition": "Scalability adalah kemampuan sistem menangani growth.",
        "types": {
            "Vertical (Scale Up)": "Add more power to existing machine",
            "Horizontal (Scale Out)": "Add more machines"
        }
    },
    "caching": {
        "category": "System Design",
        "definition": "Caching menyimpan data frequently accessed untuk faster retrieval.",
        "levels": ["Browser cache", "CDN", "Application cache", "Database cache"],
        "strategies": ["Cache-aside", "Write-through", "Write-behind"],
        "eviction": ["LRU", "LFU", "FIFO", "TTL"]
    },
    "database_sharding": {
        "category": "System Design",
        "definition": "Sharding mendistribusikan data ke multiple database instances.",
        "strategies": ["Range-based", "Hash-based", "Directory-based"],
        "challenges": ["Cross-shard queries", "Rebalancing", "Hotspots"]
    },
    "database_replication": {
        "category": "System Design",
        "definition": "Replication menyalin data ke multiple database servers.",
        "types": ["Master-Slave", "Master-Master", "Leaderless"],
        "benefits": ["High availability", "Read scalability", "Fault tolerance"]
    },
    "cap_theorem": {
        "category": "System Design",
        "definition": "CAP Theorem: distributed system hanya bisa guarantee 2 dari 3.",
        "components": {
            "Consistency": "All nodes see same data",
            "Availability": "Every request gets response",
            "Partition Tolerance": "System works despite network failures"
        }
    },
    "acid": {
        "category": "Database",
        "definition": "ACID adalah properties untuk reliable database transactions.",
        "properties": {
            "Atomicity": "All or nothing",
            "Consistency": "Valid state to valid state",
            "Isolation": "Transactions don't interfere",
            "Durability": "Committed data persists"
        }
    },
    "base": {
        "category": "Database",
        "definition": "BASE adalah alternative to ACID untuk distributed systems.",
        "properties": {
            "Basically Available": "System guarantees availability",
            "Soft State": "State may change over time",
            "Eventual Consistency": "Will become consistent eventually"
        }
    },
    "message_queue": {
        "category": "System Design",
        "definition": "Message Queue menyimpan messages untuk async processing.",
        "tools": ["RabbitMQ", "Kafka", "AWS SQS", "Redis"],
        "patterns": ["Point-to-Point", "Pub/Sub"],
        "use_cases": ["Task queues", "Event streaming", "Decoupling services"]
    },
    "rate_limiting": {
        "category": "System Design",
        "definition": "Rate Limiting membatasi request frequency untuk protect resources.",
        "algorithms": ["Token Bucket", "Leaky Bucket", "Fixed Window", "Sliding Window"],
        "implementation": ["API Gateway", "Application level", "Redis"]
    },
    "circuit_breaker": {
        "category": "System Design",
        "definition": "Circuit Breaker mencegah cascading failures dengan stop calls ke failing service.",
        "states": ["Closed (normal)", "Open (failing)", "Half-Open (testing)"],
        "library": "Resilience4j, Hystrix (deprecated)"
    },
    "api_gateway": {
        "category": "System Design",
        "definition": "API Gateway adalah single entry point untuk all client requests.",
        "features": ["Routing", "Authentication", "Rate limiting", "Load balancing", "Caching"],
        "tools": ["Kong", "AWS API Gateway", "NGINX", "Traefik"]
    },
    "service_discovery": {
        "category": "System Design",
        "definition": "Service Discovery memungkinkan services menemukan satu sama lain.",
        "patterns": ["Client-side discovery", "Server-side discovery"],
        "tools": ["Consul", "Eureka", "Kubernetes DNS"]
    },
    "saga_pattern": {
        "category": "System Design",
        "definition": "Saga Pattern mengelola distributed transactions dengan sequence of local transactions.",
        "types": ["Choreography (event-based)", "Orchestration (central coordinator)"],
        "compensation": "Rollback via compensating transactions"
    },
    "cqrs": {
        "category": "System Design",
        "definition": "CQRS (Command Query Responsibility Segregation) memisahkan read dan write models.",
        "benefits": ["Optimized read/write", "Scalability", "Flexibility"],
        "often_with": "Event Sourcing"
    },
    "event_sourcing": {
        "category": "System Design",
        "definition": "Event Sourcing menyimpan state changes sebagai sequence of events.",
        "benefits": ["Audit trail", "Temporal queries", "Event replay"],
        "challenges": ["Eventual consistency", "Event versioning", "Storage growth"]
    },
    
    # ============================================
    # GENERAL TECH KNOWLEDGE (30+ topics)
    # ============================================
    "ascii": {
        "category": "Computer Science",
        "definition": "ASCII adalah encoding standard yang merepresentasikan text dalam computers.",
        "range": "0-127 (7-bit)",
        "examples": {"A": 65, "a": 97, "0": 48, "space": 32}
    },
    "unicode": {
        "category": "Computer Science",
        "definition": "Unicode adalah universal character encoding yang support semua bahasa.",
        "formats": ["UTF-8 (variable, most common)", "UTF-16", "UTF-32"],
        "total": "143,000+ characters"
    },
    "json": {
        "category": "Data Format",
        "definition": "JSON (JavaScript Object Notation) adalah lightweight data interchange format.",
        "types": ["String", "Number", "Boolean", "null", "Array", "Object"],
        "example": "{\"name\": \"WeaR AI\", \"version\": 1}"
    },
    "xml": {
        "category": "Data Format",
        "definition": "XML (eXtensible Markup Language) adalah markup language untuk structured data.",
        "vs_json": "More verbose, support attributes, schema validation",
        "use_cases": ["Config files", "SOAP APIs", "Document formats (DOCX)"]
    },
    "yaml": {
        "category": "Data Format",
        "definition": "YAML adalah human-readable data serialization format.",
        "features": ["Indentation-based", "Comments", "Anchors & Aliases"],
        "use_cases": ["Config files", "Docker Compose", "Kubernetes", "CI/CD"]
    },
    "regex": {
        "category": "Programming",
        "definition": "Regex (Regular Expression) adalah pattern untuk matching text.",
        "metacharacters": [".", "*", "+", "?", "^", "$", "[]", "()", "\\"],
        "examples": {
            "Email": r"[\\w.-]+@[\\w.-]+\\.[a-zA-Z]{2,}",
            "Phone": r"\\d{3}-\\d{3}-\\d{4}"
        }
    },
    "markdown": {
        "category": "Format",
        "definition": "Markdown adalah lightweight markup language untuk formatting text.",
        "syntax": ["# Heading", "**bold**", "*italic*", "[link](url)", "```code```", "- list"]
    },
    "base64": {
        "category": "Encoding",
        "definition": "Base64 adalah encoding yang converts binary data ke ASCII string.",
        "use_cases": ["Email attachments", "Data URLs", "API authentication"],
        "ratio": "Encoded is ~33% larger than original"
    },
    "timestamp": {
        "category": "Programming",
        "definition": "Timestamp adalah representasi waktu, biasanya seconds since epoch.",
        "epoch": "January 1, 1970, 00:00:00 UTC",
        "formats": ["Unix timestamp", "ISO 8601 (2024-01-15T10:30:00Z)"]
    },
    "uuid": {
        "category": "Programming",
        "definition": "UUID (Universally Unique Identifier) adalah 128-bit identifier.",
        "format": "8-4-4-4-12 hexadecimal: 550e8400-e29b-41d4-a716-446655440000",
        "versions": ["v1 (time-based)", "v4 (random)", "v5 (name-based)"]
    },
    "semantic_versioning": {
        "category": "Software Engineering",
        "definition": "Semantic Versioning (SemVer) adalah versioning scheme: MAJOR.MINOR.PATCH.",
        "rules": {
            "MAJOR": "Breaking changes",
            "MINOR": "New features, backward compatible",
            "PATCH": "Bug fixes, backward compatible"
        },
        "example": "2.1.3 → Major=2, Minor=1, Patch=3"
    },
    "open_source": {
        "category": "Software",
        "definition": "Open Source adalah software dengan source code yang publicly available.",
        "licenses": ["MIT", "Apache 2.0", "GPL", "BSD"],
        "platforms": ["GitHub", "GitLab", "Bitbucket"]
    },
    "ide": {
        "category": "Development Tools",
        "definition": "IDE (Integrated Development Environment) adalah software untuk coding.",
        "popular": ["VS Code", "IntelliJ IDEA", "PyCharm", "WebStorm", "Vim/Neovim"],
        "features": ["Syntax highlighting", "Autocomplete", "Debugging", "Git integration"]
    },
    "virtualization": {
        "category": "Infrastructure",
        "definition": "Virtualization membuat virtual version of hardware/OS resources.",
        "types": ["Hardware (VMs)", "OS-level (Containers)", "Application"],
        "hypervisors": ["VMware", "VirtualBox", "Hyper-V", "KVM"]
    },
    "container": {
        "category": "Infrastructure",
        "definition": "Container adalah lightweight, isolated environment untuk running applications.",
        "vs_vm": "Containers share host OS kernel, more lightweight than VMs",
        "tools": ["Docker", "Podman", "containerd"]
    },
    "serverless": {
        "category": "Cloud",
        "definition": "Serverless adalah execution model di mana cloud provider manages infrastructure.",
        "services": ["AWS Lambda", "Google Cloud Functions", "Azure Functions", "Vercel"],
        "pricing": "Pay per execution, not for idle time",
        "limitations": ["Cold starts", "Execution time limits", "Vendor lock-in"]
    },
    "edge_computing": {
        "category": "Computing",
        "definition": "Edge Computing memproses data dekat dengan source (edge of network).",
        "benefits": ["Low latency", "Bandwidth savings", "Privacy"],
        "examples": ["CDN edge workers", "IoT processing", "AR/VR"]
    },
    "blockchain": {
        "category": "Technology",
        "definition": "Blockchain adalah distributed ledger dengan records dalam linked blocks.",
        "concepts": ["Decentralization", "Immutability", "Consensus", "Smart Contracts"],
        "platforms": ["Bitcoin", "Ethereum", "Solana", "Polygon"]
    },
    "api_versioning": {
        "category": "API Design",
        "definition": "API Versioning strategies untuk maintain backward compatibility.",
        "approaches": {
            "URL Path": "/api/v1/users",
            "Query Param": "/api/users?version=1",
            "Header": "Accept: application/vnd.api+json; version=1"
        }
    },
    "idempotency": {
        "category": "API Design",
        "definition": "Idempotent operation produces sama result walau dipanggil berkali-kali.",
        "http_methods": {
            "Idempotent": "GET, PUT, DELETE",
            "Not Idempotent": "POST"
        },
        "implementation": "Idempotency key untuk ensure exactly-once semantics"
    },
    "webhook": {
        "category": "API",
        "definition": "Webhook adalah HTTP callback yang triggered oleh event di source system.",
        "vs_polling": "Push-based, lebih efficient dari polling",
        "use_cases": ["Payment notifications", "Git hooks", "Chat integrations"]
    },
}
