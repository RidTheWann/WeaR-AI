"""
WeaR AI Engine - Enterprise AI Assistant
Sistem AI dengan Advanced Knowledge Base, Fuzzy Logic, dan Context Awareness.
Created by RidTheWann
"""

import re
import json
import logging
import difflib
from typing import Optional, Dict, List, Any, Union
from dataclasses import dataclass, field
from datetime import datetime

# Konfigurasi Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("WeaR_AI")

@dataclass
class AIResponse:
    """Standardized response object."""
    answer: str
    confidence: float
    source: str  # "knowledge_base", "pattern", "context", "fallback"
    metadata: Dict[str, Any] = field(default_factory=dict)

class KnowledgeBase:
    """
    Advanced Knowledge Base dengan data komprehensif.
    Total 200+ topics dari Programming, DevOps, Architecture, Security, AI/ML, dan lainnya.
    """
    
    def __init__(self):
        self.knowledge = self._load_comprehensive_knowledge()
        # Merge dengan extended knowledge
        self._merge_extended_knowledge()
        self.topics = list(self.knowledge.keys())
        logger.info(f"Knowledge Base loaded: {len(self.topics)} topics")
    
    def _merge_extended_knowledge(self):
        """Merge all extended knowledge modules."""
        # Extended Knowledge Part 1
        try:
            from app.core.extended_knowledge import EXTENDED_KNOWLEDGE
            self.knowledge.update(EXTENDED_KNOWLEDGE)
        except ImportError:
            pass
        
        # Extended Knowledge Part 2
        try:
            from app.core.extended_knowledge_2 import EXTENDED_KNOWLEDGE_2
            self.knowledge.update(EXTENDED_KNOWLEDGE_2)
        except ImportError:
            pass
        
        # Extended Knowledge Part 3
        try:
            from app.core.extended_knowledge_3 import EXTENDED_KNOWLEDGE_3
            self.knowledge.update(EXTENDED_KNOWLEDGE_3)
        except ImportError:
            pass
    
    def _load_comprehensive_knowledge(self) -> Dict[str, Any]:
        """
        Database pengetahuan MASIF yang diperluas meniru cakupan informasi internet
        untuk topik teknikal. 100+ topics.
        """
        return {
            # ============================================
            # PROGRAMMING LANGUAGES (15+ languages)
            # ============================================
            "python": {
                "category": "Language",
                "definition": "Python adalah bahasa high-level, interpreted, dengan penekanan pada code readability. Dibuat oleh Guido van Rossum (1991).",
                "features": ["Dynamic Typing", "Garbage Collection", "Huge Ecosystem (PyPI)", "Multi-paradigm (OOP, Functional, Procedural)"],
                "best_for": ["Data Science", "Web Dev (Django/FastAPI/Flask)", "Automation/Scripting", "AI/ML", "Backend APIs"],
                "popular_frameworks": ["Django", "FastAPI", "Flask", "Celery", "SQLAlchemy"],
                "example": "# List Comprehension\nresult = [x**2 for x in range(10) if x % 2 == 0]\nprint(result)  # [0, 4, 16, 36, 64]"
            },
            "javascript": {
                "category": "Language",
                "definition": "JavaScript adalah bahasa pemrograman utama untuk web. Berjalan di browser (client-side) dan server (Node.js).",
                "features": ["Event-driven", "Async/Await", "First-class Functions", "Prototype-based Inheritance"],
                "runtime": ["Browser (V8, SpiderMonkey)", "Node.js", "Deno", "Bun"],
                "popular_frameworks": ["React", "Vue", "Angular", "Express", "Next.js"],
                "example": "const greet = async (name) => `Hello, ${name}!`;\nawait greet('WeaR AI');"
            },
            "typescript": {
                "category": "Language",
                "definition": "TypeScript adalah superset dari JavaScript yang menambahkan static typing opsional. Dikembangkan oleh Microsoft.",
                "benefits": ["Type Safety", "Better IDE Support", "Scalability", "Easier Refactoring"],
                "compiles_to": "JavaScript (ES5/ES6+)",
                "example": "interface User { id: number; name: string; email?: string; }\nconst user: User = { id: 1, name: 'John' };"
            },
            "rust": {
                "category": "Language",
                "definition": "Rust adalah bahasa sistem yang fokus pada keamanan (memory safety) dan performa tanpa garbage collector.",
                "features": ["Ownership & Borrowing", "Zero-cost Abstractions", "Thread Safety Guaranteed", "No Null/Dangling Pointers"],
                "best_for": ["System Programming", "WebAssembly", "CLI Tools", "Game Engines", "Blockchain"],
                "example": "fn main() {\n    let msg = String::from(\"Hello, Rust!\");\n    println!(\"{}\", msg);\n}"
            },
            "go": {
                "category": "Language",
                "definition": "Go (Golang) adalah bahasa open source dari Google. Simpel, efisien, dan kuat di concurrency.",
                "features": ["Goroutines (Lightweight Threads)", "Channels", "Static Typing", "Fast Compilation", "Built-in Garbage Collector"],
                "best_for": ["Cloud/DevOps Tools", "Microservices", "CLI Apps", "Networking"],
                "companies_using": ["Google", "Uber", "Docker", "Kubernetes"],
                "example": "go func() {\n    fmt.Println(\"Concurrent execution!\")\n}()"
            },
            "java": {
                "category": "Language",
                "definition": "Java adalah bahasa OOP yang mature, platform-independent ('Write Once, Run Anywhere'). Dikembangkan Sun Microsystems (1995).",
                "features": ["JVM (Java Virtual Machine)", "Strong Typing", "Garbage Collection", "Multithreading"],
                "best_for": ["Enterprise Apps", "Android Development", "Big Data (Hadoop/Spark)", "Backend Systems"],
                "popular_frameworks": ["Spring Boot", "Hibernate", "Maven", "Gradle"],
                "example": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Java!\");\n    }\n}"
            },
            "kotlin": {
                "category": "Language",
                "definition": "Kotlin adalah bahasa modern untuk JVM, Android, JavaScript, dan Native. Dikembangkan JetBrains.",
                "features": ["Null Safety", "Coroutines", "Extension Functions", "Data Classes"],
                "best_for": ["Android Development (Official)", "Backend (Ktor)", "Multiplatform"],
                "interoperability": "100% interoperable dengan Java",
                "example": "data class User(val name: String, val age: Int)\nval user = User(\"John\", 25)"
            },
            "swift": {
                "category": "Language",
                "definition": "Swift adalah bahasa pemrograman dari Apple untuk iOS, macOS, watchOS, dan tvOS development.",
                "features": ["Type Safety", "Optionals", "Protocol-oriented", "ARC (Automatic Reference Counting)"],
                "best_for": ["iOS/macOS Apps", "Server-side (Vapor)", "Machine Learning (Core ML)"],
                "example": "let greeting = \"Hello, Swift!\"\nprint(greeting)"
            },
            "cpp": {
                "category": "Language",
                "definition": "C++ adalah bahasa general-purpose dengan OOP, generic, dan low-level memory manipulation. Extension dari C.",
                "features": ["Manual Memory Management", "Templates", "Multiple Inheritance", "Operator Overloading"],
                "best_for": ["Game Development (Unreal)", "System Programming", "Embedded Systems", "High-Performance Computing"],
                "standards": ["C++11", "C++14", "C++17", "C++20", "C++23"],
                "example": "#include <iostream>\nint main() {\n    std::cout << \"Hello, C++!\" << std::endl;\n    return 0;\n}"
            },
            "csharp": {
                "category": "Language",
                "definition": "C# adalah bahasa OOP modern dari Microsoft, berjalan di .NET platform.",
                "features": ["Garbage Collection", "LINQ", "Async/Await", "Strong Typing"],
                "best_for": ["Windows Apps", "Game Dev (Unity)", "Enterprise Software", "Web (ASP.NET)"],
                "example": "Console.WriteLine(\"Hello, C#!\");\nvar numbers = new List<int> { 1, 2, 3 };"
            },
            "php": {
                "category": "Language",
                "definition": "PHP adalah bahasa scripting server-side yang populer untuk web development.",
                "features": ["Easy to Learn", "Large Community", "CMS Support (WordPress)"],
                "popular_frameworks": ["Laravel", "Symfony", "CodeIgniter", "WordPress"],
                "market_share": "79% of websites dengan server-side programming",
                "example": "<?php\necho 'Hello, PHP!';\n$arr = ['a', 'b', 'c'];\n?>"
            },
            "ruby": {
                "category": "Language",
                "definition": "Ruby adalah bahasa dinamis yang fokus pada simplicity dan productivity.",
                "philosophy": "Designed for programmer happiness",
                "features": ["Duck Typing", "Blocks", "Mixins", "Metaprogramming"],
                "popular_frameworks": ["Ruby on Rails", "Sinatra"],
                "example": "puts 'Hello, Ruby!'\n5.times { |i| puts i }"
            },
            "sql": {
                "category": "Language",
                "definition": "SQL (Structured Query Language) adalah bahasa standar untuk mengelola database relasional.",
                "operations": ["SELECT (Query)", "INSERT (Add)", "UPDATE (Modify)", "DELETE (Remove)", "JOIN (Combine)"],
                "dialects": ["MySQL", "PostgreSQL", "SQLite", "SQL Server", "Oracle"],
                "example": "SELECT name, email FROM users WHERE age > 18 ORDER BY name LIMIT 10;"
            },
            "bash": {
                "category": "Language",
                "definition": "Bash adalah shell dan command language untuk Unix/Linux systems.",
                "best_for": ["Automation Scripts", "System Administration", "CI/CD Pipelines", "DevOps"],
                "example": "#!/bin/bash\nfor file in *.txt; do\n    echo \"Processing $file\"\ndone"
            },

            # ============================================
            # WEB FRAMEWORKS (20+ frameworks)
            # ============================================
            "react": {
                "category": "Frontend Framework",
                "definition": "React adalah library JavaScript untuk membangun UI dengan komponen. Dikembangkan Facebook.",
                "concepts": ["Components", "JSX", "Virtual DOM", "Hooks (useState, useEffect)", "Props & State"],
                "ecosystem": ["React Router", "Redux", "Next.js", "React Query"],
                "example": "function Counter() {\n  const [count, setCount] = useState(0);\n  return <button onClick={() => setCount(count + 1)}>{count}</button>;\n}"
            },
            "vue": {
                "category": "Frontend Framework",
                "definition": "Vue.js adalah progressive JavaScript framework untuk UI. Mudah dipelajari dengan API yang simpel.",
                "features": ["Reactivity System", "Single-File Components", "Vue Router", "Vuex/Pinia"],
                "example": "<template>\n  <button @click=\"count++\">{{ count }}</button>\n</template>\n<script setup>\nimport { ref } from 'vue'\nconst count = ref(0)\n</script>"
            },
            "angular": {
                "category": "Frontend Framework",
                "definition": "Angular adalah full-featured framework dari Google untuk enterprise web apps.",
                "features": ["TypeScript-first", "Dependency Injection", "RxJS", "CLI", "Two-way Data Binding"],
                "best_for": ["Large Enterprise Apps", "Complex SPAs"],
            },
            "nextjs": {
                "category": "Frontend Framework",
                "definition": "Next.js adalah React framework untuk production dengan SSR, SSG, dan API routes.",
                "features": ["Server-Side Rendering (SSR)", "Static Site Generation (SSG)", "File-based Routing", "API Routes", "Image Optimization"],
                "created_by": "Vercel",
                "example": "// app/page.tsx\nexport default function Home() {\n  return <h1>Welcome to Next.js!</h1>;\n}"
            },
            "fastapi": {
                "category": "Backend Framework",
                "definition": "FastAPI adalah modern Python web framework untuk API dengan performa tinggi.",
                "features": ["Async Support", "Auto OpenAPI Docs", "Type Hints Validation", "Dependency Injection"],
                "performance": "On par with Node.js and Go",
                "example": "from fastapi import FastAPI\napp = FastAPI()\n\n@app.get('/items/{id}')\nasync def get_item(id: int):\n    return {'id': id}"
            },
            "django": {
                "category": "Backend Framework",
                "definition": "Django adalah Python web framework 'batteries included' untuk rapid development.",
                "features": ["ORM", "Admin Panel", "Authentication", "Security Built-in"],
                "motto": "The web framework for perfectionists with deadlines",
                "ecosystem": ["Django REST Framework", "Celery", "Django Channels"]
            },
            "flask": {
                "category": "Backend Framework",
                "definition": "Flask adalah Python micro-framework yang minimalis dan fleksibel.",
                "features": ["Lightweight", "Jinja2 Templates", "Werkzeug WSGI", "Extension-based"],
                "best_for": ["Small Apps", "APIs", "Prototyping", "Learning"]
            },
            "express": {
                "category": "Backend Framework",
                "definition": "Express.js adalah minimal Node.js web framework.",
                "features": ["Middleware", "Routing", "Template Engines", "Error Handling"],
                "ecosystem": ["Passport.js", "Mongoose", "Socket.io"],
                "example": "const express = require('express');\nconst app = express();\napp.get('/', (req, res) => res.send('Hello!'));\napp.listen(3000);"
            },
            "nestjs": {
                "category": "Backend Framework",
                "definition": "NestJS adalah Node.js framework dengan architecture mirip Angular. TypeScript-first.",
                "features": ["Modules", "Controllers", "Services", "Dependency Injection", "GraphQL Support"],
                "inspired_by": "Angular architecture patterns"
            },
            "spring": {
                "category": "Backend Framework",
                "definition": "Spring adalah Java framework enterprise untuk membangun production-ready applications.",
                "modules": ["Spring Boot", "Spring MVC", "Spring Security", "Spring Data", "Spring Cloud"],
                "features": ["Dependency Injection", "AOP", "Transaction Management"]
            },
            "laravel": {
                "category": "Backend Framework",
                "definition": "Laravel adalah PHP framework dengan syntax yang elegan untuk web artisans.",
                "features": ["Eloquent ORM", "Blade Templates", "Artisan CLI", "Queue System", "Scheduling"],
                "ecosystem": ["Laravel Forge", "Laravel Vapor", "Livewire", "Inertia.js"]
            },

            # ============================================
            # DATABASES (15+ databases)
            # ============================================
            "postgresql": {
                "category": "Database",
                "definition": "PostgreSQL adalah object-relational database open source yang powerful dan extensible.",
                "features": ["ACID Compliant", "JSON Support", "Full-text Search", "Extensions (PostGIS)", "CTEs"],
                "best_for": ["Complex Queries", "Geospatial Data", "Analytics", "Enterprise"],
                "comparison": "Lebih feature-rich dari MySQL, cocok untuk complex data"
            },
            "mysql": {
                "category": "Database",
                "definition": "MySQL adalah relational database open source yang populer dan reliable.",
                "features": ["ACID Compliant", "Replication", "Partitioning", "InnoDB/MyISAM"],
                "best_for": ["Web Apps", "CMS (WordPress)", "Read-heavy Workloads"],
                "owned_by": "Oracle Corporation"
            },
            "mongodb": {
                "category": "Database",
                "definition": "MongoDB adalah document-oriented NoSQL database yang stores data dalam format BSON (Binary JSON).",
                "features": ["Flexible Schema", "Horizontal Scaling (Sharding)", "Aggregation Framework", "Atlas (Cloud)"],
                "best_for": ["Prototyping", "Content Management", "Real-time Analytics", "IoT"],
                "example": "db.users.insertOne({ name: 'John', age: 25, tags: ['developer'] })"
            },
            "redis": {
                "category": "Database",
                "definition": "Redis adalah in-memory data structure store. Digunakan sebagai database, cache, dan message broker.",
                "data_structures": ["Strings", "Lists", "Sets", "Sorted Sets", "Hashes", "Streams"],
                "features": ["Sub-millisecond Latency", "Pub/Sub", "Lua Scripting", "Persistence Options"],
                "use_cases": ["Caching", "Session Storage", "Rate Limiting", "Leaderboards", "Real-time Analytics"]
            },
            "elasticsearch": {
                "category": "Database",
                "definition": "Elasticsearch adalah distributed search and analytics engine berbasis Lucene.",
                "features": ["Full-text Search", "Near Real-time", "Scalable", "RESTful API"],
                "use_cases": ["Log Analytics", "Site Search", "APM", "SIEM"],
                "stack": "ELK Stack (Elasticsearch, Logstash, Kibana)"
            },
            "cassandra": {
                "category": "Database",
                "definition": "Apache Cassandra adalah wide-column NoSQL database untuk high availability dan scalability.",
                "features": ["Decentralized", "Linear Scalability", "Tunable Consistency", "CQL"],
                "best_for": ["Time-series Data", "IoT", "Messaging", "High Write Throughput"],
                "used_by": ["Netflix", "Apple", "Instagram"]
            },
            "sqlite": {
                "category": "Database",
                "definition": "SQLite adalah self-contained, serverless, zero-configuration SQL database engine.",
                "features": ["Single File", "No Server Needed", "Cross-platform", "ACID Compliant"],
                "best_for": ["Mobile Apps", "Embedded Systems", "Testing", "Small Apps"]
            },
            "sql_vs_nosql": {
                "category": "Database Concepts",
                "definition": "Perbandingan antara SQL (Relational) dan NoSQL (Non-relational) databases.",
                "sql": {"examples": ["PostgreSQL", "MySQL", "SQLite"], "strengths": "ACID, Complex Joins, Data Integrity"},
                "nosql": {"examples": ["MongoDB", "Redis", "Cassandra"], "strengths": "Scalability, Flexibility, Performance"}
            },

            # ============================================
            # CLOUD & DEVOPS (20+ topics)
            # ============================================
            "docker": {
                "category": "DevOps",
                "definition": "Docker adalah platform untuk mengembangkan, mengirim, dan menjalankan aplikasi dalam containers.",
                "key_concepts": ["Image (Blueprint)", "Container (Running instance)", "Dockerfile", "Volume", "Network"],
                "commands": ["docker build", "docker run", "docker-compose up", "docker push"],
                "example": "FROM python:3.11\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD [\"python\", \"main.py\"]"
            },
            "kubernetes": {
                "category": "DevOps",
                "definition": "Kubernetes (K8s) adalah sistem orkestrasi container open-source untuk automasi deployment, scaling, dan management.",
                "components": ["Pod", "Deployment", "Service", "Ingress", "ConfigMap", "Secret", "Namespace"],
                "features": ["Auto-scaling", "Self-healing", "Load Balancing", "Rolling Updates"],
                "tools": ["kubectl", "Helm", "Lens", "k9s"]
            },
            "aws": {
                "category": "Cloud",
                "definition": "Amazon Web Services adalah platform cloud computing terbesar dengan 200+ services.",
                "popular_services": {
                    "Compute": "EC2, Lambda, ECS, EKS",
                    "Storage": "S3, EBS, Glacier",
                    "Database": "RDS, DynamoDB, ElastiCache",
                    "Networking": "VPC, Route 53, CloudFront"
                },
                "certifications": ["Cloud Practitioner", "Solutions Architect", "Developer", "DevOps Engineer"]
            },
            "gcp": {
                "category": "Cloud",
                "definition": "Google Cloud Platform adalah suite cloud computing services oleh Google.",
                "popular_services": ["Compute Engine", "Cloud Run", "GKE", "BigQuery", "Cloud Storage", "Firestore"],
                "strengths": ["Data Analytics", "Machine Learning", "Kubernetes (GKE)"]
            },
            "azure": {
                "category": "Cloud",
                "definition": "Microsoft Azure adalah cloud computing platform dari Microsoft.",
                "popular_services": ["Virtual Machines", "App Service", "AKS", "Azure Functions", "Cosmos DB", "Blob Storage"],
                "strengths": ["Enterprise Integration", "Hybrid Cloud", ".NET Ecosystem"]
            },
            "ci_cd": {
                "category": "DevOps",
                "definition": "CI/CD adalah Continuous Integration dan Continuous Deployment/Delivery.",
                "ci": "Automated testing setiap code commit untuk mendeteksi bug early",
                "cd": "Automated deployment ke staging/production setelah tests pass",
                "tools": ["GitHub Actions", "GitLab CI", "Jenkins", "CircleCI", "ArgoCD"]
            },
            "terraform": {
                "category": "DevOps",
                "definition": "Terraform adalah Infrastructure as Code (IaC) tool untuk provisioning cloud resources.",
                "features": ["Declarative Syntax", "Multi-cloud Support", "State Management", "Modules"],
                "example": "resource \"aws_instance\" \"web\" {\n  ami           = \"ami-12345\"\n  instance_type = \"t2.micro\"\n}"
            },
            "ansible": {
                "category": "DevOps",
                "definition": "Ansible adalah automation tool untuk configuration management, application deployment, dan task automation.",
                "features": ["Agentless", "YAML Playbooks", "Idempotent", "Large Module Library"],
                "best_for": ["Server Configuration", "Application Deployment", "Orchestration"]
            },
            "nginx": {
                "category": "DevOps",
                "definition": "NGINX adalah high-performance web server, reverse proxy, dan load balancer.",
                "use_cases": ["Serve Static Files", "Reverse Proxy", "Load Balancing", "SSL Termination", "API Gateway"],
                "comparison": "Lebih ringan dan cepat dari Apache untuk high concurrency"
            },
            "linux": {
                "category": "Operating System",
                "definition": "Linux adalah open-source Unix-like operating system kernel.",
                "distributions": ["Ubuntu", "Debian", "CentOS/RHEL", "Arch", "Alpine"],
                "essential_commands": ["ls", "cd", "grep", "find", "chmod", "curl", "ssh", "systemctl"],
                "file_system": ["/ (root)", "/home", "/etc", "/var", "/usr", "/tmp"]
            },
            "git": {
                "category": "Version Control",
                "definition": "Git adalah distributed version control system untuk tracking code changes.",
                "commands": {
                    "git init": "Initialize repository",
                    "git clone": "Clone repository",
                    "git add": "Stage changes",
                    "git commit": "Save changes",
                    "git push/pull": "Sync with remote",
                    "git branch": "Manage branches",
                    "git merge/rebase": "Integrate changes"
                },
                "workflows": ["Git Flow", "GitHub Flow", "Trunk Based Development"]
            },

            # ============================================
            # ARCHITECTURE & DESIGN (15+ topics)
            # ============================================
            "microservices": {
                "category": "Architecture",
                "definition": "Arsitektur di mana aplikasi disusun sebagai kumpulan layanan kecil yang independen.",
                "characteristics": ["Single Responsibility", "Independent Deployment", "Decentralized Data", "API Communication"],
                "pros": ["Scalability", "Technology Agnostic", "Fault Isolation", "Team Autonomy"],
                "cons": ["Network Complexity", "Data Consistency", "Monitoring Difficulty", "DevOps Overhead"],
                "patterns": ["API Gateway", "Service Discovery", "Circuit Breaker", "Saga Pattern"]
            },
            "monolith": {
                "category": "Architecture",
                "definition": "Arsitektur tradisional di mana semua komponen aplikasi tergabung dalam satu codebase.",
                "pros": ["Simple to develop", "Easy debugging", "Single deployment"],
                "cons": ["Hard to scale", "Technology lock-in", "Large codebase"],
                "when_to_use": "Startup, small team, simple application"
            },
            "clean_architecture": {
                "category": "Architecture",
                "definition": "Pola desain software yang memisahkan concerns ke dalam layer cincin. Dependency hanya mengarah ke dalam.",
                "layers": ["Entities (Core Business)", "Use Cases", "Interface Adapters", "Frameworks & Drivers"],
                "benefits": ["Testability", "Independence from Frameworks", "Independence from UI/DB"]
            },
            "solid": {
                "category": "Design Principle",
                "definition": "5 Prinsip desain OOP untuk software yang maintainable dan extensible.",
                "principles": {
                    "S - Single Responsibility": "Class hanya punya satu alasan untuk berubah",
                    "O - Open/Closed": "Open for extension, closed for modification",
                    "L - Liskov Substitution": "Subclass harus bisa menggantikan parent class",
                    "I - Interface Segregation": "Banyak interface spesifik lebih baik dari satu general",
                    "D - Dependency Inversion": "Depend on abstractions, not concretions"
                }
            },
            "design_patterns": {
                "category": "Design Pattern",
                "definition": "Solusi reusable untuk masalah umum dalam software design.",
                "creational": ["Singleton", "Factory", "Builder", "Prototype"],
                "structural": ["Adapter", "Decorator", "Facade", "Proxy"],
                "behavioral": ["Observer", "Strategy", "Command", "State"]
            },
            "ddd": {
                "category": "Architecture",
                "definition": "Domain-Driven Design adalah approach untuk software development yang fokus pada domain kompleks.",
                "concepts": ["Bounded Context", "Ubiquitous Language", "Aggregate", "Entity", "Value Object", "Repository"],
                "strategic_patterns": ["Context Mapping", "Anti-corruption Layer", "Shared Kernel"]
            },
            "event_driven": {
                "category": "Architecture",
                "definition": "Arsitektur di mana flow ditentukan oleh events (state changes yang signifikan).",
                "components": ["Event Producer", "Event Channel", "Event Consumer"],
                "patterns": ["Event Sourcing", "CQRS", "Pub/Sub"],
                "tools": ["Kafka", "RabbitMQ", "Redis Pub/Sub", "AWS SNS/SQS"]
            },
            "rest_api": {
                "category": "Web Architecture",
                "definition": "RESTful API adalah arsitektur untuk web services menggunakan HTTP methods.",
                "principles": ["Stateless", "Client-Server", "Cacheable", "Uniform Interface", "Layered System"],
                "methods": {"GET": "Read", "POST": "Create", "PUT": "Update (full)", "PATCH": "Update (partial)", "DELETE": "Delete"},
                "status_codes": {"2xx": "Success", "3xx": "Redirect", "4xx": "Client Error", "5xx": "Server Error"}
            },
            "graphql": {
                "category": "API",
                "definition": "GraphQL adalah query language untuk API yang memungkinkan client request exact data yang dibutuhkan.",
                "features": ["Single Endpoint", "Strongly Typed Schema", "Introspection", "Subscriptions"],
                "vs_rest": "Menghindari over-fetching dan under-fetching",
                "tools": ["Apollo", "Hasura", "GraphQL Yoga"]
            },
            "websocket": {
                "category": "Protocol",
                "definition": "WebSocket adalah protokol full-duplex communication over TCP untuk real-time apps.",
                "use_cases": ["Chat Applications", "Live Notifications", "Real-time Gaming", "Live Trading"],
                "vs_http": "Persistent connection, bidirectional, low latency"
            },

            # ============================================
            # SECURITY (10+ topics)
            # ============================================
            "jwt": {
                "category": "Security",
                "definition": "JSON Web Token adalah standar untuk secure information transfer antar parties.",
                "structure": ["Header (algorithm)", "Payload (claims)", "Signature"],
                "use_cases": ["Authentication", "Authorization", "Information Exchange"],
                "best_practices": ["Short expiry", "HTTPS only", "Store securely", "Validate signature"]
            },
            "oauth2": {
                "category": "Security",
                "definition": "OAuth 2.0 adalah authorization framework untuk delegated access.",
                "flows": ["Authorization Code", "Implicit", "Client Credentials", "Resource Owner Password"],
                "roles": ["Resource Owner", "Client", "Authorization Server", "Resource Server"]
            },
            "owasp_top_10": {
                "category": "Security",
                "definition": "OWASP Top 10 adalah dokumen awareness tentang critical security risks untuk web apps.",
                "risks": ["Injection", "Broken Authentication", "Sensitive Data Exposure", "XXE", "Broken Access Control", "Security Misconfiguration", "XSS", "Insecure Deserialization", "Components with Vulnerabilities", "Insufficient Logging"]
            },
            "sql_injection": {
                "category": "Security",
                "definition": "SQL Injection adalah attack yang memasukkan malicious SQL melalui user input.",
                "example": "' OR '1'='1' --",
                "prevention": ["Parameterized Queries", "ORM", "Input Validation", "Least Privilege"]
            },
            "xss": {
                "category": "Security",
                "definition": "Cross-Site Scripting adalah attack yang inject malicious scripts ke web pages.",
                "types": ["Stored XSS", "Reflected XSS", "DOM-based XSS"],
                "prevention": ["Output Encoding", "Content Security Policy", "HTTPOnly Cookies"]
            },
            "https_ssl_tls": {
                "category": "Security",
                "definition": "HTTPS menggunakan SSL/TLS untuk encrypted communication antara client dan server.",
                "components": ["Certificate", "Public/Private Key", "Handshake", "Encryption"],
                "benefits": ["Data Encryption", "Data Integrity", "Authentication"]
            },
            "hashing": {
                "category": "Security",
                "definition": "Hashing adalah one-way function untuk mengubah data menjadi fixed-size string.",
                "algorithms": ["bcrypt (passwords)", "SHA-256", "Argon2", "PBKDF2"],
                "use_cases": ["Password Storage", "Data Integrity", "Digital Signatures"]
            },

            # ============================================
            # DATA STRUCTURES & ALGORITHMS (15+ topics)
            # ============================================
            "big_o": {
                "category": "Computer Science",
                "definition": "Big O Notation menggambarkan worst-case time/space complexity algoritma.",
                "complexities": {
                    "O(1)": "Constant - Array access",
                    "O(log n)": "Logarithmic - Binary search",
                    "O(n)": "Linear - Simple loop",
                    "O(n log n)": "Linearithmic - Merge sort",
                    "O(n²)": "Quadratic - Nested loops",
                    "O(2^n)": "Exponential - Recursive fibonacci"
                }
            },
            "array": {
                "category": "Data Structure",
                "definition": "Array adalah collection of elements yang tersimpan di contiguous memory locations.",
                "operations": {"Access": "O(1)", "Search": "O(n)", "Insert": "O(n)", "Delete": "O(n)"},
                "types": ["Static Array", "Dynamic Array (ArrayList/Vector)"]
            },
            "linked_list": {
                "category": "Data Structure",
                "definition": "Linked List adalah collection of nodes dimana setiap node berisi data dan pointer ke node berikutnya.",
                "types": ["Singly Linked", "Doubly Linked", "Circular"],
                "operations": {"Access": "O(n)", "Search": "O(n)", "Insert": "O(1)", "Delete": "O(1)"}
            },
            "stack": {
                "category": "Data Structure",
                "definition": "Stack adalah LIFO (Last In First Out) data structure.",
                "operations": ["push()", "pop()", "peek()", "isEmpty()"],
                "use_cases": ["Function calls", "Undo operations", "Expression parsing", "Backtracking"]
            },
            "queue": {
                "category": "Data Structure",
                "definition": "Queue adalah FIFO (First In First Out) data structure.",
                "operations": ["enqueue()", "dequeue()", "front()", "isEmpty()"],
                "types": ["Simple Queue", "Circular Queue", "Priority Queue", "Deque"]
            },
            "hash_table": {
                "category": "Data Structure",
                "definition": "Hash Table (Hash Map) menyimpan key-value pairs dengan O(1) average lookup.",
                "concepts": ["Hash Function", "Collision Handling", "Load Factor"],
                "collision_resolution": ["Chaining", "Open Addressing"]
            },
            "tree": {
                "category": "Data Structure",
                "definition": "Tree adalah hierarchical data structure dengan nodes connected by edges.",
                "types": ["Binary Tree", "BST", "AVL Tree", "Red-Black Tree", "B-Tree", "Trie"],
                "traversals": ["Inorder", "Preorder", "Postorder", "Level-order (BFS)"]
            },
            "graph": {
                "category": "Data Structure",
                "definition": "Graph adalah collection of vertices (nodes) connected by edges.",
                "types": ["Directed/Undirected", "Weighted/Unweighted", "Cyclic/Acyclic"],
                "representations": ["Adjacency Matrix", "Adjacency List"],
                "algorithms": ["BFS", "DFS", "Dijkstra", "Bellman-Ford", "Prim's", "Kruskal's"]
            },
            "sorting": {
                "category": "Algorithm",
                "definition": "Algoritma untuk mengurutkan elements dalam urutan tertentu.",
                "algorithms": {
                    "Bubble Sort": "O(n²) - Simple, slow",
                    "Selection Sort": "O(n²) - Simple, slow",
                    "Insertion Sort": "O(n²) - Good for small arrays",
                    "Merge Sort": "O(n log n) - Stable, divide & conquer",
                    "Quick Sort": "O(n log n) avg - Fast, in-place",
                    "Heap Sort": "O(n log n) - In-place"
                }
            },
            "searching": {
                "category": "Algorithm",
                "definition": "Algoritma untuk menemukan element dalam data structure.",
                "algorithms": {
                    "Linear Search": "O(n) - Unsorted data",
                    "Binary Search": "O(log n) - Sorted data required",
                    "Hash Lookup": "O(1) - Using hash table"
                }
            },
            "recursion": {
                "category": "Algorithm",
                "definition": "Teknik di mana fungsi memanggil dirinya sendiri untuk solve smaller subproblems.",
                "components": ["Base Case (stopping condition)", "Recursive Case"],
                "examples": ["Factorial", "Fibonacci", "Tree traversal", "Merge sort"],
                "issues": ["Stack Overflow", "Performance (use memoization)"]
            },
            "dynamic_programming": {
                "category": "Algorithm",
                "definition": "Teknik optimization dengan breaking down problems menjadi overlapping subproblems.",
                "approaches": ["Top-down (Memoization)", "Bottom-up (Tabulation)"],
                "classic_problems": ["Fibonacci", "Knapsack", "Longest Common Subsequence", "Coin Change"]
            },

            # ============================================
            # AI & MACHINE LEARNING (10+ topics)
            # ============================================
            "machine_learning": {
                "category": "AI",
                "definition": "Machine Learning adalah subset AI di mana sistem belajar dari data tanpa explicitly programmed.",
                "types": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning"],
                "algorithms": ["Linear Regression", "Decision Trees", "Random Forest", "SVM", "Neural Networks", "K-Means"]
            },
            "deep_learning": {
                "category": "AI",
                "definition": "Deep Learning adalah subset ML menggunakan neural networks dengan banyak layers.",
                "architectures": ["CNN (Images)", "RNN/LSTM (Sequences)", "Transformer (NLP)", "GAN (Generation)"],
                "frameworks": ["TensorFlow", "PyTorch", "Keras", "JAX"]
            },
            "neural_network": {
                "category": "AI",
                "definition": "Neural Network adalah model inspired by biological neurons untuk pattern recognition.",
                "components": ["Input Layer", "Hidden Layers", "Output Layer", "Activation Functions", "Weights & Biases"],
                "training": ["Forward Propagation", "Loss Calculation", "Backpropagation", "Gradient Descent"]
            },
            "nlp": {
                "category": "AI",
                "definition": "Natural Language Processing adalah AI untuk memahami dan generate human language.",
                "tasks": ["Text Classification", "NER", "Sentiment Analysis", "Machine Translation", "Question Answering"],
                "models": ["BERT", "GPT", "T5", "LLaMA"]
            },
            "llm": {
                "category": "AI",
                "definition": "Large Language Model adalah neural network yang trained on massive text data untuk generate text.",
                "examples": ["GPT-4", "Claude", "LLaMA", "Gemini", "Mistral"],
                "use_cases": ["Chatbots", "Code Generation", "Content Writing", "Analysis"]
            },
            "rag": {
                "category": "AI",
                "definition": "Retrieval-Augmented Generation menggabungkan retrieval dari knowledge base dengan LLM generation.",
                "components": ["Document Store", "Embeddings", "Vector Database", "LLM"],
                "benefits": ["Reduced Hallucination", "Up-to-date Information", "Domain-specific Knowledge"]
            },
            "vector_database": {
                "category": "AI/Database",
                "definition": "Database yang optimized untuk storing dan querying vector embeddings.",
                "examples": ["Qdrant", "Pinecone", "Weaviate", "Milvus", "Chroma"],
                "use_cases": ["Semantic Search", "Recommendation Systems", "RAG", "Image Search"]
            },

            # ============================================
            # TESTING (5+ topics)
            # ============================================
            "unit_testing": {
                "category": "Testing",
                "definition": "Testing individual units/components secara isolated.",
                "frameworks": ["pytest (Python)", "Jest (JS)", "JUnit (Java)", "NUnit (C#)"],
                "principles": ["AAA (Arrange-Act-Assert)", "One assertion per test", "Isolation"]
            },
            "integration_testing": {
                "category": "Testing",
                "definition": "Testing interaction antara multiple components/modules.",
                "scope": "Database connections, API calls, Service interactions"
            },
            "e2e_testing": {
                "category": "Testing",
                "definition": "End-to-End testing simulates real user scenarios dari awal sampai akhir.",
                "tools": ["Cypress", "Playwright", "Selenium", "Puppeteer"]
            },
            "tdd": {
                "category": "Testing",
                "definition": "Test-Driven Development: Write test first, then code to pass the test.",
                "cycle": ["Red (Write failing test)", "Green (Make it pass)", "Refactor"]
            }
        }
    
    def search(self, query: str) -> Optional[dict]:
        """
        Smart search dengan fuzzy matching.
        """
        query_lower = query.lower()
        
        # 1. Exact Match (O(1))
        if query_lower in self.knowledge:
            return {"topic": query_lower, **self.knowledge[query_lower]}
        
        # 2. Keyword/Partial Match (O(n))
        for topic, content in self.knowledge.items():
            if topic in query_lower:
                return {"topic": topic, **content}
        
        # 3. Fuzzy Match (handle typos like 'pyton' -> 'python')
        # cutoff=0.6 means 60% similarity required
        matches = difflib.get_close_matches(query_lower, self.topics, n=1, cutoff=0.6)
        if matches:
            best_match = matches[0]
            logger.info(f"Fuzzy match found: '{query}' -> '{best_match}'")
            return {"topic": best_match, **self.knowledge[best_match], "is_fuzzy": True}
            
        return None

class PatternMatcher:
    """Regex based pattern matching untuk interaksi natural."""
    
    def __init__(self):
        self.patterns = [
            # Greeting
            (r"(halo|hai|hello|hi|hey|pagi|siang|malam|selamat)", self._greeting()),
            
            # Identity - Who are you
            (r"(siapa kamu|siapa anda|who are you|kamu siapa|apa itu wear)", self._identity()),
            
            # Creator - Who made you
            (r"(siapa (yang )?(?:buat|membuat|bikin|ciptakan|develop)|who (made|created|built)|pembuat|pencipta|developer|creator)", self._creator()),
            
            # Name origin - Why WeaR
            (r"(arti nama|nama wear|kenapa wear|mengapa wear|asal nama|meaning of wear|why wear|wear dari)", self._name_origin()),
            
            # Capabilities
            (r"(apa yang bisa|what can you|kemampuan|bisa apa|fitur)", self._capabilities()),
            
            # Thanks
            (r"(terima kasih|thanks|thank you|makasih|thx)", "Sama-sama! Senang bisa membantu. Happy coding! 🚀"),
            
            # Exit
            (r"(keluar|exit|bye|dadah|goodbye|sampai jumpa)", "Sampai jumpa! WeaR AI selalu siap membantu. 👋"),
            
            # Help
            (r"(bantuan|help|menu|tolong|guide)", self._get_help_text())
        ]
    
    def _greeting(self):
        return """Halo! 👋 Saya **WeaR AI**, asisten AI cerdas yang siap membantu Anda.

Saya dikembangkan untuk menjadi partner coding dan engineering Anda. Tanyakan apa saja tentang programming, architecture, atau teknologi!

*Ketik 'help' untuk melihat semua topik yang saya kuasai.*"""

    def _identity(self):
        return """## WeaR AI

Saya adalah **WeaR AI** — sebuah Artificial Intelligence Engine yang dirancang untuk membantu developer dan engineer menyelesaikan masalah teknis dengan cepat dan akurat.

### Kemampuan Utama:
- 🧠 **Knowledge Base** — 80+ topik teknikal dari programming hingga cloud
- 🔍 **Smart Search** — Fuzzy matching untuk toleransi typo
- 💬 **Natural Language** — Memahami pertanyaan dalam Bahasa Indonesia dan English
- ⚡ **Instant Response** — Jawaban cepat tanpa delay

### Dibuat oleh:
**RidTheWann** — Software Engineer & AI Enthusiast

*WeaR AI terus berkembang untuk menjadi asisten AI terbaik untuk developer Indonesia.*"""

    def _creator(self):
        return """## Tentang Pembuat WeaR AI

WeaR AI diciptakan oleh **RidTheWann** (Ridwan), seorang Software Engineer yang passionate dalam bidang Artificial Intelligence dan Software Development.

### Visi:
Membangun AI assistant yang powerful dan accessible untuk semua developer Indonesia, tanpa perlu bergantung pada layanan berbayar eksternal.

### Filosofi:
> *"Technology should empower everyone, not just the privileged few."*

WeaR AI dikembangkan dengan cinta dan dedikasi untuk komunitas developer Indonesia. 🇮🇩"""

    def _name_origin(self):
        return """## Asal Nama "WeaR"

Nama **WeaR** memiliki makna khusus yang personal:

```
W  +  R  =  WeaR
│     │
│     └── R (Ridwan) - Sang pencipta
│
└────── We (Wulan) - Inspirasi dan pasangan hidup
```

### Makna:
**WeaR** adalah singkatan dari **We** dan **aR**, yang merepresentasikan:
- **W** → Wulan (pasangan Ridwan)
- **R** → Ridwan (pencipta WeaR AI)

Nama ini melambangkan bahwa di balik setiap inovasi teknologi, ada cinta dan dukungan dari orang-orang terdekat. WeaR AI bukan sekadar project — ini adalah simbol dedikasi dan kasih sayang. ❤️

*"Behind every great code, there's a greater love."*"""

    def _capabilities(self):
        return """## Kemampuan WeaR AI

### 💻 Programming Languages
Python, JavaScript, TypeScript, Rust, Go, Java, Kotlin, Swift, C++, C#, PHP, Ruby, SQL, Bash

### 🎨 Frontend Development
React, Vue.js, Angular, Next.js, Tailwind CSS

### ⚙️ Backend Development
FastAPI, Django, Flask, Express.js, NestJS, Spring Boot, Laravel

### 🗄️ Database
PostgreSQL, MySQL, MongoDB, Redis, Elasticsearch, Cassandra

### ☁️ Cloud & DevOps
Docker, Kubernetes, AWS, GCP, Azure, Terraform, CI/CD, Linux

### 🏗️ Architecture
Microservices, Clean Architecture, SOLID, Design Patterns, DDD

### 🔐 Security
JWT, OAuth2, OWASP Top 10, Encryption, Authentication

### 🤖 AI & Machine Learning
Neural Networks, Deep Learning, NLP, LLM, RAG, Vector Database

*Tanyakan topik apapun dan saya akan memberikan penjelasan yang komprehensif!*"""
    
    def match(self, query: str) -> Optional[str]:
        query_lower = query.lower()
        for pattern, response in self.patterns:
            if re.search(pattern, query_lower):
                return response
        return None

    def _get_help_text(self):
        return """## 🧠 WeaR AI - Knowledge Base (80+ Topics)

**1. Languages:** Python, JavaScript, TypeScript, Rust, Go, Java, Kotlin, Swift, C++, C#, PHP, Ruby, SQL, Bash

**2. Frontend:** React, Vue, Angular, Next.js

**3. Backend:** FastAPI, Django, Flask, Express, NestJS, Spring, Laravel

**4. Database:** PostgreSQL, MySQL, MongoDB, Redis, Elasticsearch, Cassandra, SQLite

**5. Cloud & DevOps:** Docker, Kubernetes, AWS, GCP, Azure, Terraform, Ansible, NGINX, Git, Linux, CI/CD

**6. Architecture:** Microservices, Monolith, Clean Architecture, SOLID, Design Patterns, DDD, Event-Driven

**7. Security:** JWT, OAuth2, OWASP Top 10, SQL Injection, XSS, HTTPS/SSL/TLS, Hashing

**8. Data Structures:** Array, Linked List, Stack, Queue, Hash Table, Tree, Graph

**9. Algorithms:** Sorting, Searching, Recursion, Dynamic Programming, Big O

**10. AI/ML:** Machine Learning, Deep Learning, Neural Networks, NLP, LLM, RAG, Vector Database

**11. Testing:** Unit Testing, Integration Testing, E2E Testing, TDD

*Ketik nama topik untuk mendapatkan penjelasan lengkap!*"""

class WeaRAIEngine:
    """
    Engine Utama.
    Orchestrator untuk NLU (Natural Language Understanding) sederhana.
    """
    
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.pattern_matcher = PatternMatcher()
        self.history = []
        self.max_history = 5
        logger.info("WeaR AI Engine  initialized successfully.")
    
    def generate(self, query: str) -> AIResponse:
        start_time = datetime.now()
        query = query.strip()
        
        # 1. Pattern Matching (Conversational)
        pattern_resp = self.pattern_matcher.match(query)
        if pattern_resp:
            return self._build_response(pattern_resp, 0.95, "pattern")
        
        # 2. Knowledge Base Search (Fuzzy & Direct)
        knowledge = self.knowledge_base.search(query)
        if knowledge:
            formatted_answer = self._format_technical_response(knowledge)
            conf = 0.85 if not knowledge.get("is_fuzzy") else 0.75
            return self._build_response(formatted_answer, conf, "knowledge_base")
            
        # 3. Fallback
        return self._build_response(self._generate_fallback(query), 0.2, "fallback")

    def _format_technical_response(self, data: dict) -> str:
        """Formatter profesional dengan Markdown."""
        parts = [f"## 📚 {data['topic'].title()}"]
        
        if "category" in data:
            parts.append(f"*{data['category']}*")
        
        parts.append(f"\n**Definisi:**\n{data['definition']}\n")
        
        # Dynamic field rendering
        ignored_keys = ["topic", "definition", "category", "is_fuzzy"]
        
        for key, value in data.items():
            if key in ignored_keys:
                continue
            
            header = key.replace("_", " ").title()
            parts.append(f"### {header}:")
            
            if isinstance(value, list):
                for item in value:
                    parts.append(f"- {item}")
            elif isinstance(value, dict):
                for k, v in value.items():
                    parts.append(f"- **{k}**: {v}")
            else:
                if "```" not in str(value) and len(str(value)) > 50:
                    parts.append(value)
                else:
                    parts.append(f"{value}")
            parts.append("")
            
        return "\n".join(parts)

    def _generate_fallback(self, query: str) -> str:
        suggestions = difflib.get_close_matches(query, self.knowledge_base.topics, n=3, cutoff=0.4)
        msg = f"Maaf, saya tidak menemukan informasi spesifik mengenai '{query}' di database lokal.\n"
        
        if suggestions:
            msg += "\n**Mungkin maksud Anda:**\n"
            for s in suggestions:
                msg += f"- {s}\n"
        
        msg += "\n*Tips: Coba keyword seperti 'microservices', 'python', 'docker', atau 'security'.*"
        return msg

    def _build_response(self, answer: str, conf: float, source: str) -> AIResponse:
        return AIResponse(answer=answer, confidence=conf, source=source)

    def chat(self, message: str) -> str:
        """Interface utama untuk user."""
        response = self.generate(message)
        
        # Context management
        self.history.append({"u": message, "a": response.answer})
        if len(self.history) > self.max_history:
            self.history.pop(0)
            
        return response.answer

# --- Singleton Accessor ---
_engine_instance = None

def get_engine():
    global _engine_instance
    if _engine_instance is None:
        _engine_instance = WeaRAIEngine()
    return _engine_instance

def ask(question: str) -> str:
    return get_engine().chat(question)

# --- Main Execution Block (Untuk Testing) ---
if __name__ == "__main__":
    print("--- WeaR AI Initializing ---")
    engine = get_engine()
    
    # Test cases
    test_queries = [
        "Halo",
        "Apa itu Microservices?",
        "Jelaskan tentang Rust",
        "pyton", # Typo test
        "docker vs kubernetes", # Partial match
        "cara masak nasi goreng" # Fallback
    ]
    
    for q in test_queries:
        print(f"\nUser: {q}")
        print("-" * 20)
        print(engine.chat(q))
        print("=" * 40)
