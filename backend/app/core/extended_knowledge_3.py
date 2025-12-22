"""
WeaR AI Extended Knowledge Base - Part 3
Pengetahuan tambahan: Software Engineering, Career, Best Practices, dan Real-World Topics.
Created by RidTheWann
"""

EXTENDED_KNOWLEDGE_3 = {
    # ============================================
    # SOFTWARE ENGINEERING PRACTICES (30+ topics)
    # ============================================
    "git_workflow": {
        "category": "Version Control",
        "definition": "Git Workflow adalah structured approach untuk branching dan merging.",
        "popular_workflows": {
            "Git Flow": "develop, feature, release, hotfix branches",
            "GitHub Flow": "Main + feature branches, PR-based",
            "Trunk Based": "Short-lived branches, frequent merges to main"
        }
    },
    "git_commands": {
        "category": "Version Control",
        "definition": "Essential Git commands untuk version control.",
        "basics": ["git init", "git clone", "git add", "git commit", "git push", "git pull"],
        "branching": ["git branch", "git checkout", "git merge", "git rebase"],
        "advanced": ["git stash", "git cherry-pick", "git bisect", "git reflog"]
    },
    "git_rebase": {
        "category": "Version Control",
        "definition": "Rebase memindahkan commits ke base branch yang berbeda.",
        "vs_merge": "Cleaner history vs preserving merge context",
        "golden_rule": "Never rebase public/shared branches",
        "interactive": "git rebase -i HEAD~3 untuk squash/edit commits"
    },
    "pull_request": {
        "category": "Version Control",
        "definition": "Pull Request adalah mechanism untuk proposing code changes.",
        "best_practices": ["Small PRs", "Descriptive title", "Self-review first", "Add reviewers"],
        "checklist": ["Tests pass", "Code reviewed", "Documentation updated", "No conflicts"]
    },
    "monorepo": {
        "category": "Software Engineering",
        "definition": "Monorepo menyimpan multiple projects dalam satu repository.",
        "pros": ["Shared code", "Atomic changes", "Unified CI/CD"],
        "cons": ["Complex builds", "Large repo size", "Tight coupling risk"],
        "tools": ["Nx", "Turborepo", "Lerna", "Bazel"]
    },
    "microservices_vs_monolith": {
        "category": "Architecture",
        "definition": "Perbandingan dua architectural approaches.",
        "monolith": {
            "pros": ["Simple deployment", "Easy debugging", "Strong consistency"],
            "cons": ["Scaling limitations", "Tech stack locked", "Large codebase"]
        },
        "microservices": {
            "pros": ["Independent scaling", "Tech flexibility", "Team autonomy"],
            "cons": ["Operational complexity", "Network latency", "Data consistency"]
        }
    },
    "twelve_factor_app": {
        "category": "Software Engineering",
        "definition": "12-Factor App adalah methodology untuk building SaaS apps.",
        "factors": [
            "Codebase", "Dependencies", "Config", "Backing services",
            "Build/release/run", "Processes", "Port binding", "Concurrency",
            "Disposability", "Dev/prod parity", "Logs", "Admin processes"
        ]
    },
    "documentation": {
        "category": "Software Engineering",
        "definition": "Documentation menjelaskan how dan why dari software.",
        "types": ["README", "API docs", "Architecture docs", "Runbooks", "User guides"],
        "tools": ["Swagger/OpenAPI", "Sphinx", "JSDoc", "Docusaurus"]
    },
    "code_coverage": {
        "category": "Testing",
        "definition": "Code coverage mengukur persentase code yang di-test.",
        "types": ["Line", "Branch", "Function", "Statement"],
        "tools": ["pytest-cov", "Istanbul/nyc", "JaCoCo"],
        "note": "High coverage ≠ good tests. Quality over quantity."
    },
    "dependency_injection": {
        "category": "Design Pattern",
        "definition": "DI adalah providing dependencies dari external source.",
        "benefits": ["Loose coupling", "Testability", "Flexibility"],
        "frameworks": ["Spring (Java)", "Angular", "FastAPI (Depends)"]
    },
    "inversion_of_control": {
        "category": "Design Pattern",
        "definition": "IoC memindahkan control flow ke framework/container.",
        "forms": ["Dependency Injection", "Service Locator", "Template Method"],
        "hollywood_principle": "Don't call us, we'll call you"
    },
    "dry": {
        "category": "Programming Principle",
        "definition": "DRY: Don't Repeat Yourself - avoid code duplication.",
        "benefit": "Single source of truth, easier maintenance",
        "warning": "Premature abstraction bisa worse than duplication"
    },
    "kiss": {
        "category": "Programming Principle",
        "definition": "KISS: Keep It Simple, Stupid - simplicity over complexity.",
        "application": "Choose straightforward solutions over clever ones"
    },
    "yagni": {
        "category": "Programming Principle",
        "definition": "YAGNI: You Aren't Gonna Need It - don't build unused features.",
        "benefit": "Avoid wasted effort on speculative features"
    },
    "separation_of_concerns": {
        "category": "Programming Principle",
        "definition": "SoC memisahkan program menjadi distinct sections.",
        "examples": ["MVC pattern", "Frontend/Backend separation", "Layered architecture"]
    },
    "law_of_demeter": {
        "category": "Programming Principle",
        "definition": "LoD: Talk only to your immediate friends.",
        "rule": "Method should only call methods on: self, parameters, created objects, direct components",
        "violation": "obj.getA().getB().getC() - train wreck"
    },
    "composition_over_inheritance": {
        "category": "Programming Principle",
        "definition": "Prefer composing objects over class inheritance.",
        "benefit": "More flexible, avoids inheritance hierarchy issues",
        "implementation": "Has-a relationship instead of is-a"
    },
    "code_formatting": {
        "category": "Software Engineering",
        "definition": "Consistent code style untuk readability.",
        "formatters": ["Prettier (JS)", "Black (Python)", "gofmt (Go)", "rustfmt (Rust)"],
        "linters": ["ESLint", "Flake8/Ruff", "golangci-lint"]
    },
    "pair_programming": {
        "category": "Practice",
        "definition": "Two developers working together at one workstation.",
        "roles": ["Driver (writes code)", "Navigator (reviews, thinks ahead)"],
        "benefits": ["Knowledge sharing", "Fewer bugs", "Team building"]
    },
    "mob_programming": {
        "category": "Practice",
        "definition": "Whole team works together on same problem.",
        "setup": "One screen, one keyboard, frequent driver rotation",
        "benefits": ["Team alignment", "No knowledge silos"]
    },
    
    # ============================================
    # DATABASE ADVANCED (30+ topics)
    # ============================================
    "normalization": {
        "category": "Database",
        "definition": "Normalization mengorganisasi data untuk reduce redundancy.",
        "forms": {
            "1NF": "Atomic values, no repeating groups",
            "2NF": "1NF + no partial dependencies",
            "3NF": "2NF + no transitive dependencies",
            "BCNF": "Every determinant is a candidate key"
        }
    },
    "denormalization": {
        "category": "Database",
        "definition": "Denormalization menambahkan redundancy untuk better read performance.",
        "when": "Read-heavy workloads, reporting, data warehouses",
        "trade_off": "Faster reads vs slower writes, data inconsistency risk"
    },
    "indexing": {
        "category": "Database",
        "definition": "Index adalah data structure untuk faster data retrieval.",
        "types": ["B-tree", "Hash", "Full-text", "GiST/GIN (PostgreSQL)"],
        "trade_off": "Faster reads vs slower writes, storage overhead"
    },
    "query_optimization": {
        "category": "Database",
        "definition": "Techniques untuk improving query performance.",
        "techniques": ["EXPLAIN ANALYZE", "Add indexes", "Avoid SELECT *", "Use JOINs wisely"],
        "common_issues": ["N+1 queries", "Missing indexes", "Unoptimized subqueries"]
    },
    "n_plus_one": {
        "category": "Database",
        "definition": "N+1 problem: 1 query untuk parent, N queries untuk children.",
        "solution": "Eager loading / JOIN",
        "example": "SELECT * FROM posts; + N x SELECT * FROM comments WHERE post_id = ?"
    },
    "transaction_isolation": {
        "category": "Database",
        "definition": "Isolation levels menentukan bagaimana transactions melihat data.",
        "levels": {
            "Read Uncommitted": "Dirty reads possible",
            "Read Committed": "No dirty reads",
            "Repeatable Read": "No non-repeatable reads",
            "Serializable": "Full isolation"
        }
    },
    "deadlock_db": {
        "category": "Database",
        "definition": "Deadlock terjadi ketika transactions saling menunggu locks.",
        "prevention": ["Lock ordering", "Timeout", "Deadlock detection"],
        "handling": "Retry transaction yang di-rollback"
    },
    "stored_procedure": {
        "category": "Database",
        "definition": "Stored procedure adalah precompiled SQL yang tersimpan di database.",
        "pros": ["Performance", "Reduced network traffic", "Security"],
        "cons": ["Harder to version control", "Vendor lock-in", "Testing difficulty"]
    },
    "database_trigger": {
        "category": "Database",
        "definition": "Trigger adalah code yang automatic execute on data changes.",
        "events": ["INSERT", "UPDATE", "DELETE"],
        "use_cases": ["Audit logging", "Derived data", "Validation"]
    },
    "connection_pooling": {
        "category": "Database",
        "definition": "Connection pool maintains reusable database connections.",
        "benefit": "Avoid connection overhead per request",
        "tools": ["PgBouncer", "HikariCP", "SQLAlchemy pool"]
    },
    "sql_joins": {
        "category": "Database",
        "definition": "JOINs menggabungkan rows dari multiple tables.",
        "types": {
            "INNER JOIN": "Matching rows only",
            "LEFT JOIN": "All from left + matching from right",
            "RIGHT JOIN": "All from right + matching from left",
            "FULL JOIN": "All from both",
            "CROSS JOIN": "Cartesian product"
        }
    },
    "sql_window_functions": {
        "category": "Database",
        "definition": "Window functions perform calculations across row sets.",
        "functions": ["ROW_NUMBER()", "RANK()", "LAG()", "LEAD()", "SUM() OVER()"],
        "syntax": "function() OVER (PARTITION BY col ORDER BY col)"
    },
    "cte": {
        "category": "Database",
        "definition": "CTE (Common Table Expression) adalah temporary named result set.",
        "syntax": "WITH cte_name AS (SELECT ...) SELECT * FROM cte_name",
        "benefit": "Readability, recursive queries"
    },
    "nosql_types": {
        "category": "Database",
        "definition": "NoSQL databases untuk specific use cases.",
        "types": {
            "Document": "MongoDB, CouchDB",
            "Key-Value": "Redis, DynamoDB",
            "Wide-Column": "Cassandra, HBase",
            "Graph": "Neo4j, Amazon Neptune"
        }
    },
    "graph_database": {
        "category": "Database",
        "definition": "Graph DB menyimpan data sebagai nodes dan relationships.",
        "use_cases": ["Social networks", "Recommendation engines", "Fraud detection"],
        "query_language": "Cypher (Neo4j), Gremlin"
    },
    "time_series_db": {
        "category": "Database",
        "definition": "Time-series DB optimized untuk timestamped data.",
        "databases": ["InfluxDB", "TimescaleDB", "Prometheus"],
        "use_cases": ["Metrics", "IoT data", "Financial data"]
    },
    "data_warehouse": {
        "category": "Database",
        "definition": "Data warehouse adalah central repository untuk analytics.",
        "characteristics": ["Subject-oriented", "Integrated", "Time-variant", "Non-volatile"],
        "tools": ["Snowflake", "BigQuery", "Redshift", "Databricks"]
    },
    "olap_vs_oltp": {
        "category": "Database",
        "definition": "Two database usage patterns.",
        "oltp": {
            "purpose": "Transactional operations",
            "queries": "Simple, many short transactions",
            "design": "Normalized"
        },
        "olap": {
            "purpose": "Analytics, reporting",
            "queries": "Complex, aggregations",
            "design": "Denormalized, star/snowflake schema"
        }
    },
    "etl": {
        "category": "Data Engineering",
        "definition": "ETL: Extract, Transform, Load data pipeline.",
        "steps": ["Extract from sources", "Transform (clean, enrich)", "Load to target"],
        "tools": ["Apache Airflow", "dbt", "Fivetran", "Talend"]
    },
    
    # ============================================
    # CAREER & SOFT SKILLS (20+ topics)
    # ============================================
    "interview_prep": {
        "category": "Career",
        "definition": "Preparation untuk software engineering interviews.",
        "areas": ["Data Structures", "Algorithms", "System Design", "Behavioral"],
        "resources": ["LeetCode", "System Design Primer", "Cracking the Coding Interview"]
    },
    "behavioral_interview": {
        "category": "Career",
        "definition": "Interview yang mengevaluasi soft skills dan past experiences.",
        "method": "STAR: Situation, Task, Action, Result",
        "topics": ["Leadership", "Conflict resolution", "Failures/Learnings", "Teamwork"]
    },
    "system_design_interview": {
        "category": "Career",
        "definition": "Interview untuk designing large-scale systems.",
        "approach": ["Requirements", "High-level design", "Deep dive", "Trade-offs"],
        "common_topics": ["URL shortener", "Twitter", "Chat system", "Video streaming"]
    },
    "resume_tips": {
        "category": "Career",
        "definition": "Tips untuk membuat resume yang effective.",
        "format": ["Contact info", "Summary", "Experience (STAR)", "Skills", "Education"],
        "tips": ["Quantify achievements", "Tailor to job", "One page", "Keywords"]
    },
    "negotiation": {
        "category": "Career",
        "definition": "Salary negotiation tips.",
        "tips": ["Research market rate", "Let them name first", "Consider total comp", "Get it in writing"],
        "resources": ["levels.fyi", "Glassdoor", "Blind"]
    },
    "time_management": {
        "category": "Soft Skills",
        "definition": "Managing time effectively untuk productivity.",
        "techniques": ["Pomodoro", "Time blocking", "Eisenhower Matrix", "Eat the frog"],
        "tools": ["Calendar", "Task managers", "Focus apps"]
    },
    "communication": {
        "category": "Soft Skills",
        "definition": "Effective communication skills untuk engineers.",
        "types": ["Written (docs, emails)", "Verbal (meetings, presentations)", "Code (readable code)"],
        "tips": ["Be concise", "Know your audience", "Active listening"]
    },
    "mentorship": {
        "category": "Career",
        "definition": "Relationship untuk guiding professional development.",
        "benefits_mentee": ["Guidance", "Network", "Faster growth"],
        "benefits_mentor": ["Leadership skills", "Fresh perspectives", "Giving back"]
    },
    "developer_experience": {
        "category": "Software Engineering",
        "definition": "DX adalah kemudahan developer dalam menggunakan tools/APIs.",
        "factors": ["Documentation", "Error messages", "Onboarding", "Tooling"],
        "examples": "Stripe API, Vercel, Firebase"
    },
    "burnout": {
        "category": "Career",
        "definition": "Burnout adalah exhaustion dari prolonged stress.",
        "signs": ["Exhaustion", "Cynicism", "Reduced productivity"],
        "prevention": ["Set boundaries", "Take breaks", "Sustainable pace", "Seek support"]
    },
    
    # ============================================
    # INTERNET & WEB STANDARDS (20+ topics)
    # ============================================
    "http_status_codes": {
        "category": "Web",
        "definition": "HTTP status codes indicate request result.",
        "categories": {
            "1xx": "Informational",
            "2xx": "Success (200 OK, 201 Created)",
            "3xx": "Redirect (301 Moved, 304 Not Modified)",
            "4xx": "Client Error (400 Bad Request, 401, 403, 404)",
            "5xx": "Server Error (500, 502, 503)"
        }
    },
    "http_headers": {
        "category": "Web",
        "definition": "HTTP headers contain metadata about request/response.",
        "common": {
            "Content-Type": "MIME type of body",
            "Authorization": "Auth credentials",
            "Cache-Control": "Caching directives",
            "User-Agent": "Client information"
        }
    },
    "mime_types": {
        "category": "Web",
        "definition": "MIME type menunjukkan format content.",
        "examples": {
            "text/html": "HTML pages",
            "application/json": "JSON data",
            "image/png": "PNG images",
            "multipart/form-data": "File uploads"
        }
    },
    "web_accessibility": {
        "category": "Web",
        "definition": "Accessibility membuat web usable untuk semua orang.",
        "standards": ["WCAG 2.1", "WAI-ARIA"],
        "practices": ["Alt text", "Keyboard nav", "Color contrast", "Semantic HTML"],
        "tools": ["axe", "Lighthouse", "Screen readers"]
    },
    "seo_basics": {
        "category": "Web",
        "definition": "SEO (Search Engine Optimization) untuk visibility di search.",
        "factors": ["Content quality", "Keywords", "Backlinks", "Site speed", "Mobile-friendly"],
        "technical": ["Meta tags", "Sitemap", "robots.txt", "Structured data"]
    },
    "web_performance": {
        "category": "Web",
        "definition": "Web performance optimization untuk faster loading.",
        "metrics": ["LCP", "FID", "CLS", "TTFB"],
        "techniques": ["Compression", "Caching", "Lazy loading", "Code splitting", "CDN"]
    },
    "core_web_vitals": {
        "category": "Web",
        "definition": "Google's metrics untuk user experience.",
        "metrics": {
            "LCP": "Largest Contentful Paint < 2.5s",
            "FID": "First Input Delay < 100ms",
            "CLS": "Cumulative Layout Shift < 0.1"
        }
    },
    "oauth_flow": {
        "category": "Security",
        "definition": "OAuth 2.0 authorization flows.",
        "flows": {
            "Authorization Code": "Server apps (most secure)",
            "PKCE": "Mobile/SPA (recommended)",
            "Client Credentials": "Machine-to-machine",
            "Implicit": "Deprecated"
        }
    },
    "openid_connect": {
        "category": "Security",
        "definition": "OIDC adalah identity layer di atas OAuth 2.0.",
        "adds": ["ID Token (JWT)", "UserInfo endpoint", "Standard claims"],
        "providers": ["Google", "Okta", "Auth0", "Keycloak"]
    },
    "webauthn": {
        "category": "Security",
        "definition": "WebAuthn adalah passwordless authentication standard.",
        "methods": ["Biometrics", "Security keys (YubiKey)", "Platform authenticators"],
        "benefits": ["Phishing resistant", "No passwords to steal"]
    },
    
    # ============================================
    # MOBILE DEVELOPMENT (15+ topics)
    # ============================================
    "flutter": {
        "category": "Mobile",
        "definition": "Flutter adalah Google's UI toolkit untuk cross-platform apps.",
        "language": "Dart",
        "rendering": "Own rendering engine (Skia)",
        "platforms": ["iOS", "Android", "Web", "Desktop"],
        "widgets": ["StatelessWidget", "StatefulWidget", "Material/Cupertino"]
    },
    "react_native": {
        "category": "Mobile",
        "definition": "React Native adalah framework untuk native mobile apps dengan React.",
        "language": "JavaScript/TypeScript",
        "rendering": "Native components",
        "architecture": "New Architecture (Fabric, TurboModules)"
    },
    "swift_programming": {
        "category": "Mobile",
        "definition": "Swift adalah bahasa Apple untuk iOS/macOS development.",
        "features": ["Type safety", "Optionals", "Protocol-oriented", "Concurrency (async/await)"],
        "frameworks": ["SwiftUI", "UIKit", "Combine"]
    },
    "kotlin_android": {
        "category": "Mobile",
        "definition": "Kotlin adalah preferred language untuk Android development.",
        "features": ["Null safety", "Coroutines", "Extension functions", "Data classes"],
        "frameworks": ["Jetpack Compose", "Android SDK", "Ktor"]
    },
    "mobile_architecture": {
        "category": "Mobile",
        "definition": "Architecture patterns untuk mobile apps.",
        "patterns": {
            "MVC": "Model-View-Controller",
            "MVP": "Model-View-Presenter",
            "MVVM": "Model-View-ViewModel",
            "Clean Architecture": "Layered with dependency rule"
        }
    },
    "app_lifecycle": {
        "category": "Mobile",
        "definition": "Application lifecycle states.",
        "android": ["onCreate", "onStart", "onResume", "onPause", "onStop", "onDestroy"],
        "ios": ["Not Running", "Inactive", "Active", "Background", "Suspended"]
    },
    "push_notifications": {
        "category": "Mobile",
        "definition": "Push notifications untuk engaging users.",
        "services": ["FCM (Firebase)", "APNs (Apple)", "OneSignal"],
        "types": ["Alert", "Silent/Background", "Rich media"]
    },
    "app_store_submission": {
        "category": "Mobile",
        "definition": "Process publishing apps ke stores.",
        "platforms": {
            "iOS": "App Store Connect, review 24-48h",
            "Android": "Google Play Console, review hours"
        },
        "requirements": ["Screenshots", "Description", "Privacy policy", "App review guidelines"]
    },
    
    # ============================================
    # MISCELLANEOUS TECH (20+ topics)
    # ============================================
    "websocket": {
        "category": "Protocol",
        "definition": "WebSocket adalah full-duplex communication protocol.",
        "vs_http": "Persistent connection vs request-response",
        "use_cases": ["Real-time apps", "Chat", "Live updates", "Gaming"],
        "alternatives": ["Server-Sent Events", "Long polling", "WebRTC"]
    },
    "grpc": {
        "category": "Protocol",
        "definition": "gRPC adalah high-performance RPC framework dari Google.",
        "features": ["Protocol Buffers", "HTTP/2", "Streaming", "Code generation"],
        "vs_rest": "Binary vs text, bidirectional vs request-response"
    },
    "protocol_buffers": {
        "category": "Data Format",
        "definition": "Protocol Buffers adalah language-neutral serialization format.",
        "features": ["Binary", "Schema required", "Backward compatible", "Smaller than JSON"],
        "file": ".proto files define schema"
    },
    "mqtt": {
        "category": "Protocol",
        "definition": "MQTT adalah lightweight messaging protocol untuk IoT.",
        "pattern": "Publish/Subscribe",
        "qos_levels": ["At most once", "At least once", "Exactly once"],
        "use_cases": ["IoT sensors", "Mobile messaging", "Telemetry"]
    },
    "iot": {
        "category": "Technology",
        "definition": "Internet of Things: jaringan physical devices dengan connectivity.",
        "components": ["Sensors", "Connectivity", "Data processing", "User interface"],
        "protocols": ["MQTT", "CoAP", "HTTP", "Bluetooth", "Zigbee"]
    },
    "webassembly": {
        "category": "Web",
        "definition": "WebAssembly adalah binary instruction format untuk browser.",
        "features": ["Near-native speed", "Language agnostic", "Secure sandbox"],
        "languages": ["Rust", "C/C++", "Go", "AssemblyScript"],
        "use_cases": ["Games", "Image processing", "CAD", "Compilers"]
    },
    "wasm_runtime": {
        "category": "Technology",
        "definition": "WebAssembly runtimes di luar browser.",
        "runtimes": ["Wasmtime", "Wasmer", "WasmEdge"],
        "use_cases": ["Serverless", "Plugin systems", "Edge computing"]
    },
    "ffmpeg": {
        "category": "Tool",
        "definition": "FFmpeg adalah complete multimedia processing tool.",
        "capabilities": ["Transcode", "Stream", "Filter", "Record"],
        "example": "ffmpeg -i input.mp4 -c:v libx264 output.mkv"
    },
    "imagemagick": {
        "category": "Tool",
        "definition": "ImageMagick adalah image manipulation tool.",
        "operations": ["Resize", "Crop", "Convert format", "Composite"],
        "example": "convert input.png -resize 50% output.jpg"
    },
    "cron": {
        "category": "Linux",
        "definition": "Cron adalah time-based job scheduler di Unix.",
        "syntax": "minute hour day month weekday command",
        "example": "0 */2 * * * /script.sh (every 2 hours)"
    },
    "systemd": {
        "category": "Linux",
        "definition": "systemd adalah init system dan service manager.",
        "commands": ["systemctl start/stop/restart", "systemctl enable/disable", "journalctl"],
        "files": ".service unit files"
    },
    "make": {
        "category": "Build Tool",
        "definition": "Make adalah build automation tool.",
        "file": "Makefile",
        "syntax": "target: dependencies\\n\\tcommands",
        "use_cases": ["C/C++ builds", "Task runner", "Automation"]
    },
    "cmake": {
        "category": "Build Tool",
        "definition": "CMake adalah cross-platform build system generator.",
        "file": "CMakeLists.txt",
        "output": "Generates Makefiles or IDE projects"
    },
    "npm_scripts": {
        "category": "JavaScript",
        "definition": "npm scripts untuk running tasks dalam package.json.",
        "predefined": ["start", "test", "build"],
        "custom": "npm run <script-name>",
        "example": "\"scripts\": { \"dev\": \"vite\", \"build\": \"vite build\" }"
    },
    "environment_variables": {
        "category": "Programming",
        "definition": "Environment variables untuk configuration tanpa hardcoding.",
        "access": {
            "Python": "os.environ['VAR']",
            "Node": "process.env.VAR",
            "Shell": "$VAR atau ${VAR}"
        },
        "tools": [".env files", "dotenv library", "Secret managers"]
    },
    "feature_flags": {
        "category": "Software Engineering",
        "definition": "Feature flags toggle fitur on/off tanpa deploy.",
        "use_cases": ["Gradual rollout", "A/B testing", "Kill switch", "Beta features"],
        "tools": ["LaunchDarkly", "Unleash", "ConfigCat"]
    },
    "observability": {
        "category": "DevOps",
        "definition": "Observability adalah kemampuan memahami system internal dari external outputs.",
        "pillars": {
            "Metrics": "Numerical measurements over time",
            "Logs": "Discrete events",
            "Traces": "Request flow across services"
        },
        "tools": ["Prometheus/Grafana", "ELK", "Jaeger/Zipkin", "Datadog"]
    },
    "distributed_tracing": {
        "category": "DevOps",
        "definition": "Distributed tracing tracks requests across services.",
        "concepts": ["Trace ID", "Span", "Parent/Child spans"],
        "tools": ["Jaeger", "Zipkin", "OpenTelemetry"],
        "standards": ["OpenTelemetry", "OpenTracing", "W3C Trace Context"]
    },
    "opentelemetry": {
        "category": "DevOps",
        "definition": "OpenTelemetry adalah unified observability framework.",
        "components": ["API", "SDK", "Collectors", "Exporters"],
        "signals": ["Traces", "Metrics", "Logs (emerging)"]
    },
}
