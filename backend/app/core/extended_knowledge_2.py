"""
WeaR AI Extended Knowledge Base - Part 2
Ratusan topik tambahan untuk knowledge AI yang lebih masif.
Created by RidTheWann
"""

EXTENDED_KNOWLEDGE_2 = {
    # ============================================
    # ADVANCED PROGRAMMING LANGUAGES (50+ topics)
    # ============================================
    "scala": {
        "category": "Programming Language",
        "definition": "Scala adalah bahasa yang menggabungkan OOP dan functional programming di JVM.",
        "features": ["Type inference", "Pattern matching", "Immutability", "Traits", "Case classes"],
        "frameworks": ["Akka", "Play Framework", "Spark"],
        "use_cases": ["Big Data (Spark)", "Backend services", "Concurrent systems"]
    },
    "haskell": {
        "category": "Programming Language",
        "definition": "Haskell adalah pure functional programming language dengan lazy evaluation.",
        "features": ["Pure functions", "Lazy evaluation", "Strong static typing", "Type inference", "Monads"],
        "concepts": ["Functors", "Applicatives", "Monads", "Type classes"]
    },
    "elixir": {
        "category": "Programming Language",
        "definition": "Elixir adalah functional language di atas Erlang VM untuk scalable systems.",
        "features": ["Fault tolerance", "Concurrency", "Hot code swapping", "Pattern matching"],
        "frameworks": ["Phoenix", "Ecto"],
        "use_cases": ["Real-time apps", "Distributed systems", "Chat applications"]
    },
    "erlang": {
        "category": "Programming Language",
        "definition": "Erlang adalah bahasa untuk highly concurrent, fault-tolerant systems.",
        "features": ["Actor model", "OTP", "Hot code reload", "Distributed computing"],
        "used_by": ["WhatsApp", "Discord", "RabbitMQ", "Ericsson"]
    },
    "clojure": {
        "category": "Programming Language",
        "definition": "Clojure adalah Lisp dialect untuk JVM dengan focus pada immutability.",
        "features": ["Homoiconicity", "Persistent data structures", "Software transactional memory"],
        "syntax": "(defn greet [name] (str \"Hello, \" name))"
    },
    "r_language": {
        "category": "Programming Language",
        "definition": "R adalah bahasa untuk statistical computing dan data visualization.",
        "features": ["Vectorized operations", "Rich plotting", "Statistical packages"],
        "packages": ["ggplot2", "dplyr", "tidyr", "shiny"],
        "use_cases": ["Data Science", "Statistics", "Bioinformatics"]
    },
    "julia": {
        "category": "Programming Language",
        "definition": "Julia adalah high-performance language untuk scientific computing.",
        "features": ["JIT compilation", "Multiple dispatch", "Metaprogramming", "C-speed performance"],
        "use_cases": ["Scientific computing", "Machine Learning", "Numerical analysis"]
    },
    "dart": {
        "category": "Programming Language",
        "definition": "Dart adalah bahasa dari Google untuk client-side development.",
        "features": ["Sound null safety", "AOT & JIT compilation", "Hot reload"],
        "frameworks": ["Flutter"],
        "use_cases": ["Mobile apps", "Web apps", "Desktop apps"]
    },
    "lua": {
        "category": "Programming Language",
        "definition": "Lua adalah lightweight scripting language untuk embedding.",
        "features": ["Embeddable", "Coroutines", "Metatables", "Small footprint"],
        "use_cases": ["Game scripting (Roblox)", "Neovim config", "Redis scripting", "Nginx"]
    },
    "perl": {
        "category": "Programming Language",
        "definition": "Perl adalah bahasa untuk text processing dan scripting.",
        "features": ["Regex built-in", "CPAN modules", "One-liners"],
        "motto": "TMTOWTDI - There's More Than One Way To Do It"
    },
    "groovy": {
        "category": "Programming Language",
        "definition": "Groovy adalah dynamic language untuk JVM dengan Java compatibility.",
        "features": ["Optional typing", "Closures", "Builder syntax"],
        "use_cases": ["Gradle build scripts", "Jenkins pipelines"]
    },
    "ocaml": {
        "category": "Programming Language",
        "definition": "OCaml adalah ML-family language dengan strong type system.",
        "features": ["Algebraic data types", "Pattern matching", "Type inference", "Modules"],
        "used_by": ["Facebook (Hack, Flow)", "Jane Street"]
    },
    "zig": {
        "category": "Programming Language",
        "definition": "Zig adalah low-level language sebagai better C.",
        "features": ["No hidden control flow", "No GC", "Interop with C", "Comptime"],
        "use_cases": ["Systems programming", "Game dev", "Embedded"]
    },
    "nim": {
        "category": "Programming Language",
        "definition": "Nim adalah compiled language dengan Python-like syntax.",
        "features": ["Metaprogramming", "Multiple backends (C, JS)", "GC options"],
        "compiles_to": ["C", "C++", "JavaScript"]
    },
    "crystal": {
        "category": "Programming Language",
        "definition": "Crystal adalah Ruby-syntax language yang compiles ke native.",
        "features": ["Type inference", "Null safety", "Ruby syntax", "C performance"],
        "motto": "Fast as C, slick as Ruby"
    },
    "assembly": {
        "category": "Programming Language",
        "definition": "Assembly adalah low-level language yang directly maps ke machine code.",
        "architectures": ["x86/x64", "ARM", "MIPS", "RISC-V"],
        "use_cases": ["OS kernels", "Bootloaders", "Performance-critical code", "Reverse engineering"]
    },
    "cobol": {
        "category": "Programming Language",
        "definition": "COBOL adalah bahasa legacy untuk business applications.",
        "features": ["English-like syntax", "Record handling", "File processing"],
        "still_used": "Banking, insurance, government systems"
    },
    "fortran": {
        "category": "Programming Language",
        "definition": "Fortran adalah bahasa tertua untuk scientific computing.",
        "features": ["Array operations", "Parallel computing", "High performance"],
        "versions": ["Fortran 77", "Fortran 90", "Fortran 2018"]
    },
    "vhdl": {
        "category": "Hardware Description",
        "definition": "VHDL adalah bahasa untuk mendesain digital circuits.",
        "use_cases": ["FPGA programming", "ASIC design", "Digital systems"]
    },
    "verilog": {
        "category": "Hardware Description",
        "definition": "Verilog adalah HDL untuk digital circuit design.",
        "use_cases": ["FPGA", "ASIC", "Chip design"],
        "variants": ["SystemVerilog"]
    },
    "solidity": {
        "category": "Programming Language",
        "definition": "Solidity adalah bahasa untuk smart contracts di Ethereum.",
        "features": ["Contract-oriented", "Inheritance", "Libraries"],
        "concepts": ["Gas", "EVM", "ABI", "Events"]
    },
    
    # ============================================
    # FRAMEWORKS & LIBRARIES DETAIL (50+ topics)
    # ============================================
    "redux": {
        "category": "State Management",
        "definition": "Redux adalah predictable state container untuk JavaScript apps.",
        "principles": ["Single source of truth", "State is read-only", "Pure reducers"],
        "concepts": ["Store", "Actions", "Reducers", "Middleware"],
        "alternatives": ["Zustand", "MobX", "Recoil", "Jotai"]
    },
    "mobx": {
        "category": "State Management",
        "definition": "MobX adalah reactive state management dengan automatic tracking.",
        "concepts": ["Observable", "Computed", "Actions", "Reactions"],
        "vs_redux": "Less boilerplate, more magical"
    },
    "rxjs": {
        "category": "Library",
        "definition": "RxJS adalah reactive programming library untuk JavaScript.",
        "concepts": ["Observable", "Operators", "Subjects", "Schedulers"],
        "operators": ["map", "filter", "mergeMap", "switchMap", "debounceTime"]
    },
    "lodash": {
        "category": "Library",
        "definition": "Lodash adalah JavaScript utility library.",
        "functions": ["_.map", "_.filter", "_.reduce", "_.debounce", "_.throttle", "_.cloneDeep"],
        "note": "Banyak yang sudah native di ES6+"
    },
    "numpy": {
        "category": "Library",
        "definition": "NumPy adalah fundamental package untuk scientific computing di Python.",
        "features": ["N-dimensional arrays", "Broadcasting", "Linear algebra", "FFT"],
        "example": "import numpy as np\narr = np.array([1, 2, 3])"
    },
    "pandas": {
        "category": "Library",
        "definition": "Pandas adalah library untuk data manipulation dan analysis.",
        "structures": ["DataFrame", "Series"],
        "operations": ["read_csv", "groupby", "merge", "pivot_table", "fillna"],
        "example": "df = pd.read_csv('data.csv')\ndf.groupby('category').mean()"
    },
    "matplotlib": {
        "category": "Library",
        "definition": "Matplotlib adalah plotting library untuk Python.",
        "plots": ["Line", "Bar", "Scatter", "Histogram", "Pie", "Heatmap"],
        "example": "import matplotlib.pyplot as plt\nplt.plot([1,2,3], [1,4,9])\nplt.show()"
    },
    "seaborn": {
        "category": "Library",
        "definition": "Seaborn adalah statistical visualization library di atas Matplotlib.",
        "plots": ["heatmap", "pairplot", "violinplot", "boxplot", "jointplot"],
        "themes": "Built-in beautiful themes"
    },
    "scikit_learn": {
        "category": "Library",
        "definition": "Scikit-learn adalah machine learning library untuk Python.",
        "algorithms": ["Linear Regression", "Decision Trees", "SVM", "KMeans", "Random Forest"],
        "workflow": "fit(X_train, y_train) → predict(X_test) → score()",
        "utils": ["train_test_split", "StandardScaler", "GridSearchCV"]
    },
    "scipy": {
        "category": "Library",
        "definition": "SciPy adalah library untuk scientific dan technical computing.",
        "modules": ["scipy.stats", "scipy.optimize", "scipy.signal", "scipy.sparse"]
    },
    "pytorch": {
        "category": "Deep Learning",
        "definition": "PyTorch adalah deep learning framework dengan dynamic computation graphs.",
        "features": ["Dynamic graphs", "Pythonic", "TorchScript", "CUDA support"],
        "components": ["torch.Tensor", "torch.nn", "torch.optim", "torch.utils.data"],
        "used_by": ["Meta", "Tesla", "OpenAI"]
    },
    "tensorflow": {
        "category": "Deep Learning",
        "definition": "TensorFlow adalah end-to-end ML platform dari Google.",
        "features": ["Keras API", "TensorBoard", "TF Lite", "TF.js"],
        "versions": "TF 2.x menggunakan eager execution by default"
    },
    "keras": {
        "category": "Deep Learning",
        "definition": "Keras adalah high-level neural network API.",
        "layers": ["Dense", "Conv2D", "LSTM", "Dropout", "BatchNormalization"],
        "api": "model.compile() → model.fit() → model.predict()"
    },
    "huggingface": {
        "category": "AI/ML",
        "definition": "Hugging Face adalah platform untuk sharing ML models.",
        "libraries": ["Transformers", "Datasets", "Tokenizers", "Accelerate"],
        "models": ["BERT", "GPT-2", "T5", "Stable Diffusion", "LLaMA"]
    },
    "langchain": {
        "category": "AI/ML",
        "definition": "LangChain adalah framework untuk developing LLM applications.",
        "components": ["Prompts", "Chains", "Agents", "Memory", "Callbacks"],
        "integrations": ["OpenAI", "Anthropic", "Ollama", "Pinecone", "Chroma"]
    },
    "celery": {
        "category": "Library",
        "definition": "Celery adalah distributed task queue untuk Python.",
        "brokers": ["Redis", "RabbitMQ"],
        "features": ["Async tasks", "Scheduled tasks", "Retries", "Task chains"]
    },
    "sqlalchemy": {
        "category": "Library",
        "definition": "SQLAlchemy adalah Python SQL toolkit dan ORM.",
        "patterns": ["Core (SQL Expression)", "ORM (Object Relational Mapper)"],
        "features": ["Unit of Work", "Identity Map", "Migrations (Alembic)"]
    },
    "prisma": {
        "category": "ORM",
        "definition": "Prisma adalah next-generation ORM untuk Node.js dan TypeScript.",
        "components": ["Prisma Client", "Prisma Migrate", "Prisma Studio"],
        "features": ["Type-safe queries", "Auto-completion", "Schema-first"]
    },
    "sequelize": {
        "category": "ORM",
        "definition": "Sequelize adalah ORM untuk Node.js dengan support multiple databases.",
        "databases": ["PostgreSQL", "MySQL", "SQLite", "MSSQL"],
        "features": ["Migrations", "Associations", "Transactions"]
    },
    "mongoose": {
        "category": "ODM",
        "definition": "Mongoose adalah ODM untuk MongoDB di Node.js.",
        "features": ["Schema definition", "Validation", "Middleware", "Virtuals"],
        "example": "const User = mongoose.model('User', userSchema)"
    },
    "graphql_js": {
        "category": "Library",
        "definition": "GraphQL.js adalah reference implementation GraphQL untuk JavaScript.",
        "tools": ["Apollo Server", "Apollo Client", "Relay"],
        "concepts": ["Schema", "Resolvers", "Queries", "Mutations", "Subscriptions"]
    },
    "socket_io": {
        "category": "Library",
        "definition": "Socket.io adalah library untuk real-time bidirectional communication.",
        "features": ["WebSocket fallback", "Rooms", "Namespaces", "Auto-reconnection"],
        "example": "io.on('connection', socket => socket.emit('hello'))"
    },
    "jest": {
        "category": "Testing",
        "definition": "Jest adalah JavaScript testing framework dari Meta.",
        "features": ["Zero config", "Snapshot testing", "Mocking", "Code coverage"],
        "example": "test('adds 1+2=3', () => expect(1+2).toBe(3))"
    },
    "pytest": {
        "category": "Testing",
        "definition": "pytest adalah testing framework untuk Python.",
        "features": ["Simple syntax", "Fixtures", "Parametrize", "Plugins"],
        "example": "def test_add():\n    assert 1 + 2 == 3"
    },
    "cypress": {
        "category": "Testing",
        "definition": "Cypress adalah E2E testing framework untuk web.",
        "features": ["Time travel", "Real browser", "Auto-wait", "Screenshots"],
        "example": "cy.visit('/').cy.get('button').click()"
    },
    "playwright": {
        "category": "Testing",
        "definition": "Playwright adalah E2E testing library dari Microsoft.",
        "browsers": ["Chromium", "Firefox", "WebKit"],
        "features": ["Auto-wait", "Codegen", "Tracing", "Multiple contexts"]
    },
    "storybook": {
        "category": "Development Tool",
        "definition": "Storybook adalah tool untuk developing UI components in isolation.",
        "features": ["Component explorer", "Addons", "Documentation", "Testing"]
    },
    
    # ============================================
    # DEVOPS & CLOUD DEEP DIVE (50+ topics)
    # ============================================
    "docker_compose": {
        "category": "DevOps",
        "definition": "Docker Compose adalah tool untuk defining multi-container apps.",
        "file": "docker-compose.yml",
        "commands": ["up", "down", "build", "logs", "exec"],
        "example": "services:\n  web:\n    build: .\n  db:\n    image: postgres"
    },
    "dockerfile": {
        "category": "DevOps",
        "definition": "Dockerfile adalah script untuk building Docker images.",
        "instructions": ["FROM", "RUN", "COPY", "WORKDIR", "CMD", "EXPOSE", "ENV"],
        "best_practices": ["Multi-stage builds", "Minimize layers", ".dockerignore"]
    },
    "kubernetes_pods": {
        "category": "Kubernetes",
        "definition": "Pod adalah smallest deployable unit di Kubernetes.",
        "contains": "One or more containers dengan shared storage/network",
        "types": ["Single container", "Multi-container (sidecar)"]
    },
    "kubernetes_services": {
        "category": "Kubernetes",
        "definition": "Service menyediakan stable endpoint untuk Pods.",
        "types": ["ClusterIP", "NodePort", "LoadBalancer", "ExternalName"]
    },
    "kubernetes_deployments": {
        "category": "Kubernetes",
        "definition": "Deployment mengelola ReplicaSets dan declarative updates.",
        "features": ["Rolling updates", "Rollback", "Scaling", "Self-healing"]
    },
    "kubernetes_ingress": {
        "category": "Kubernetes",
        "definition": "Ingress manages external access ke services dalam cluster.",
        "controllers": ["NGINX Ingress", "Traefik", "HAProxy"],
        "features": ["Path routing", "Host routing", "TLS termination"]
    },
    "helm": {
        "category": "Kubernetes",
        "definition": "Helm adalah package manager untuk Kubernetes.",
        "concepts": ["Charts", "Releases", "Values", "Templates"],
        "commands": ["install", "upgrade", "rollback", "uninstall"]
    },
    "prometheus": {
        "category": "Monitoring",
        "definition": "Prometheus adalah monitoring dan alerting toolkit.",
        "features": ["Pull-based metrics", "PromQL", "Alert Manager", "Service discovery"],
        "metrics_types": ["Counter", "Gauge", "Histogram", "Summary"]
    },
    "grafana": {
        "category": "Monitoring",
        "definition": "Grafana adalah platform untuk metrics visualization.",
        "features": ["Dashboards", "Alerts", "Plugins", "Multiple data sources"],
        "datasources": ["Prometheus", "Elasticsearch", "InfluxDB", "CloudWatch"]
    },
    "elk_stack": {
        "category": "Logging",
        "definition": "ELK Stack adalah Elasticsearch, Logstash, Kibana untuk logging.",
        "components": {
            "Elasticsearch": "Search & analytics engine",
            "Logstash": "Log processing pipeline",
            "Kibana": "Visualization"
        },
        "alternative": "EFK (Fluentd instead of Logstash)"
    },
    "jenkins": {
        "category": "CI/CD",
        "definition": "Jenkins adalah open-source automation server.",
        "features": ["Pipeline as code", "Plugins", "Distributed builds"],
        "pipeline": "Jenkinsfile dengan stages dan steps"
    },
    "github_actions": {
        "category": "CI/CD",
        "definition": "GitHub Actions adalah CI/CD platform integrated dengan GitHub.",
        "concepts": ["Workflows", "Jobs", "Steps", "Actions", "Runners"],
        "triggers": ["push", "pull_request", "schedule", "workflow_dispatch"]
    },
    "gitlab_cicd": {
        "category": "CI/CD",
        "definition": "GitLab CI/CD adalah built-in CI/CD di GitLab.",
        "file": ".gitlab-ci.yml",
        "concepts": ["Stages", "Jobs", "Runners", "Artifacts", "Cache"]
    },
    "argocd": {
        "category": "GitOps",
        "definition": "Argo CD adalah declarative GitOps CD tool untuk Kubernetes.",
        "features": ["Git as source of truth", "Auto-sync", "Rollback", "Multi-cluster"]
    },
    "vault": {
        "category": "Security",
        "definition": "HashiCorp Vault adalah secrets management tool.",
        "features": ["Dynamic secrets", "Encryption as service", "Leasing", "Revocation"],
        "auth_methods": ["Token", "AppRole", "Kubernetes", "AWS IAM"]
    },
    "consul": {
        "category": "Infrastructure",
        "definition": "Consul adalah service mesh dan service discovery tool.",
        "features": ["Service discovery", "Health checking", "KV store", "Multi-datacenter"]
    },
    "istio": {
        "category": "Service Mesh",
        "definition": "Istio adalah service mesh untuk microservices.",
        "features": ["Traffic management", "Security (mTLS)", "Observability"],
        "components": ["Envoy proxy", "Istiod", "Ingress/Egress Gateway"]
    },
    "pulumi": {
        "category": "IaC",
        "definition": "Pulumi adalah infrastructure as code dengan general-purpose languages.",
        "languages": ["TypeScript", "Python", "Go", "C#"],
        "vs_terraform": "Uses real programming languages instead of HCL"
    },
    "cloudformation": {
        "category": "AWS",
        "definition": "CloudFormation adalah AWS IaC service.",
        "format": "YAML atau JSON templates",
        "concepts": ["Stacks", "Resources", "Parameters", "Outputs", "Intrinsic Functions"]
    },
    "aws_lambda": {
        "category": "AWS",
        "definition": "Lambda adalah serverless compute service dari AWS.",
        "triggers": ["API Gateway", "S3", "DynamoDB", "SQS", "CloudWatch"],
        "limits": "15 min timeout, 10GB memory, 10GB /tmp"
    },
    "aws_ec2": {
        "category": "AWS",
        "definition": "EC2 adalah virtual servers di AWS cloud.",
        "types": ["On-Demand", "Reserved", "Spot", "Dedicated"],
        "components": ["AMI", "Instance Types", "Security Groups", "EBS", "VPC"]
    },
    "aws_s3": {
        "category": "AWS",
        "definition": "S3 adalah object storage service dari AWS.",
        "features": ["Versioning", "Lifecycle policies", "Encryption", "Static hosting"],
        "storage_classes": ["Standard", "Intelligent-Tiering", "Glacier", "Deep Archive"]
    },
    "aws_rds": {
        "category": "AWS",
        "definition": "RDS adalah managed relational database service.",
        "engines": ["PostgreSQL", "MySQL", "MariaDB", "Oracle", "SQL Server", "Aurora"],
        "features": ["Multi-AZ", "Read replicas", "Automated backups"]
    },
    "aws_dynamodb": {
        "category": "AWS",
        "definition": "DynamoDB adalah fully managed NoSQL database.",
        "features": ["Single-digit millisecond latency", "Auto-scaling", "Global tables"],
        "concepts": ["Partition key", "Sort key", "GSI", "LSI"]
    },
    "gcp_compute": {
        "category": "GCP",
        "definition": "Compute Engine adalah VM service dari Google Cloud.",
        "features": ["Preemptible VMs", "Custom machine types", "Live migration"]
    },
    "gcp_bigquery": {
        "category": "GCP",
        "definition": "BigQuery adalah serverless data warehouse dari Google.",
        "features": ["Petabyte-scale", "Standard SQL", "ML built-in", "Streaming inserts"]
    },
    "azure_functions": {
        "category": "Azure",
        "definition": "Azure Functions adalah serverless compute dari Microsoft.",
        "triggers": ["HTTP", "Timer", "Blob", "Queue", "Event Grid"],
        "languages": ["C#", "JavaScript", "Python", "Java", "PowerShell"]
    },
    
    # ============================================
    # SECURITY DEEP DIVE (30+ topics)
    # ============================================
    "csrf": {
        "category": "Security",
        "definition": "CSRF (Cross-Site Request Forgery) adalah attack yang forces user melakukan unwanted actions.",
        "prevention": ["CSRF tokens", "SameSite cookies", "Check Referer header"],
        "example": "Attacker membuat form tersembunyi yang submit ke bank.com/transfer"
    },
    "clickjacking": {
        "category": "Security",
        "definition": "Clickjacking menyembunyikan malicious content di balik legitimate UI.",
        "prevention": ["X-Frame-Options: DENY", "CSP frame-ancestors"]
    },
    "csp": {
        "category": "Security",
        "definition": "CSP (Content Security Policy) mengontrol resources yang boleh dimuat.",
        "directives": ["default-src", "script-src", "style-src", "img-src", "frame-ancestors"],
        "example": "Content-Security-Policy: default-src 'self'"
    },
    "cors_security": {
        "category": "Security",
        "definition": "CORS misconfiguration bisa expose data ke unauthorized origins.",
        "risks": "Wildcard (*) dengan credentials, reflecting Origin header",
        "best_practice": "Whitelist specific origins"
    },
    "ssrf": {
        "category": "Security",
        "definition": "SSRF (Server-Side Request Forgery) forces server melakukan requests ke internal resources.",
        "targets": ["Internal APIs", "Cloud metadata endpoints", "Local files"],
        "prevention": ["Whitelist URLs", "Block internal IPs", "Disable redirects"]
    },
    "xxe": {
        "category": "Security",
        "definition": "XXE (XML External Entity) adalah attack via XML parsers.",
        "impact": ["File disclosure", "SSRF", "DoS"],
        "prevention": "Disable external entities di XML parser"
    },
    "deserialization": {
        "category": "Security",
        "definition": "Insecure deserialization bisa lead ke RCE.",
        "languages": ["Java (ObjectInputStream)", "PHP (unserialize)", "Python (pickle)"],
        "prevention": ["Input validation", "Integrity checks", "Avoid native serialization"]
    },
    "path_traversal": {
        "category": "Security",
        "definition": "Path traversal mengakses files di luar intended directory.",
        "pattern": "../../../etc/passwd",
        "prevention": ["Validate input", "Use allowlist", "Chroot/sandbox"]
    },
    "command_injection": {
        "category": "Security",
        "definition": "Command injection mengeksekusi arbitrary OS commands.",
        "example": "; rm -rf /",
        "prevention": ["Parameterized commands", "Avoid shell=True", "Input validation"]
    },
    "ldap_injection": {
        "category": "Security",
        "definition": "LDAP Injection memanipulasi LDAP queries.",
        "prevention": ["Escape special characters", "Parameterized queries"]
    },
    "timing_attack": {
        "category": "Security",
        "definition": "Timing attack mengekstrak info dari response time differences.",
        "example": "Password comparison yang return early on mismatch",
        "prevention": "Constant-time comparison functions"
    },
    "brute_force": {
        "category": "Security",
        "definition": "Brute force adalah mencoba semua possible combinations.",
        "prevention": ["Rate limiting", "CAPTCHA", "Account lockout", "Strong passwords"]
    },
    "credential_stuffing": {
        "category": "Security",
        "definition": "Credential stuffing menggunakan leaked credentials dari breaches lain.",
        "prevention": ["MFA", "Breach detection", "Password rotation"]
    },
    "session_hijacking": {
        "category": "Security",
        "definition": "Session hijacking adalah stealing session ID untuk impersonate user.",
        "methods": ["XSS", "Network sniffing", "Session fixation"],
        "prevention": ["HttpOnly cookies", "Secure flag", "Session rotation"]
    },
    "cryptography_basics": {
        "category": "Security",
        "definition": "Cryptography adalah ilmu mengamankan komunikasi.",
        "types": {
            "Symmetric": "Same key for encrypt/decrypt (AES)",
            "Asymmetric": "Public/Private key pair (RSA)"
        },
        "concepts": ["Encryption", "Hashing", "Digital signatures", "Key exchange"]
    },
    "aes": {
        "category": "Security",
        "definition": "AES (Advanced Encryption Standard) adalah symmetric encryption standard.",
        "key_sizes": ["128-bit", "192-bit", "256-bit"],
        "modes": ["ECB", "CBC", "GCM", "CTR"]
    },
    "rsa": {
        "category": "Security",
        "definition": "RSA adalah asymmetric encryption algorithm.",
        "key_sizes": ["2048-bit", "4096-bit (recommended)"],
        "use_cases": ["Key exchange", "Digital signatures", "Encrypting small data"]
    },
    "bcrypt": {
        "category": "Security",
        "definition": "bcrypt adalah password hashing function dengan built-in salt.",
        "features": ["Work factor (cost)", "Built-in salt", "Slow by design"],
        "alternatives": ["Argon2 (recommended)", "scrypt"]
    },
    "argon2": {
        "category": "Security",
        "definition": "Argon2 adalah password hashing algorithm (PHC winner).",
        "variants": ["Argon2d (GPU resistant)", "Argon2i (side-channel resistant)", "Argon2id (hybrid)"],
        "recommended": "Argon2id untuk passwords"
    },
    "zero_trust": {
        "category": "Security",
        "definition": "Zero Trust adalah security model: never trust, always verify.",
        "principles": ["Verify explicitly", "Least privilege", "Assume breach"],
        "components": ["Strong identity", "Device health", "Micro-segmentation"]
    },
    "pentesting": {
        "category": "Security",
        "definition": "Penetration Testing adalah simulating attacks untuk find vulnerabilities.",
        "phases": ["Reconnaissance", "Scanning", "Exploitation", "Post-exploitation", "Reporting"],
        "tools": ["Burp Suite", "Nmap", "Metasploit", "OWASP ZAP"]
    },
    "sast": {
        "category": "Security",
        "definition": "SAST (Static Application Security Testing) menganalisis source code.",
        "tools": ["Semgrep", "SonarQube", "Checkmarx", "Snyk"],
        "when": "During development, CI/CD pipeline"
    },
    "dast": {
        "category": "Security",
        "definition": "DAST (Dynamic Application Security Testing) testing running application.",
        "tools": ["OWASP ZAP", "Burp Suite", "Acunetix"],
        "when": "Staging/Production testing"
    },
    
    # ============================================
    # AI/ML DEEP DIVE (40+ topics)
    # ============================================
    "supervised_learning": {
        "category": "Machine Learning",
        "definition": "Supervised learning menggunakan labeled data untuk training.",
        "types": {
            "Classification": "Predict categories (spam/not spam)",
            "Regression": "Predict continuous values (price)"
        },
        "algorithms": ["Linear Regression", "Logistic Regression", "Decision Trees", "SVM", "Neural Networks"]
    },
    "unsupervised_learning": {
        "category": "Machine Learning",
        "definition": "Unsupervised learning menemukan patterns di unlabeled data.",
        "types": {
            "Clustering": "Group similar items (KMeans)",
            "Dimensionality Reduction": "Reduce features (PCA)"
        },
        "algorithms": ["KMeans", "DBSCAN", "Hierarchical Clustering", "PCA", "t-SNE"]
    },
    "reinforcement_learning": {
        "category": "Machine Learning",
        "definition": "RL learns melalui trial and error dengan rewards.",
        "concepts": ["Agent", "Environment", "State", "Action", "Reward"],
        "algorithms": ["Q-Learning", "DQN", "PPO", "A3C"],
        "use_cases": ["Games (AlphaGo)", "Robotics", "Recommendations"]
    },
    "cnn": {
        "category": "Deep Learning",
        "definition": "CNN (Convolutional Neural Network) untuk image dan spatial data.",
        "layers": ["Convolutional", "Pooling", "Flatten", "Dense"],
        "architectures": ["LeNet", "AlexNet", "VGG", "ResNet", "EfficientNet"],
        "use_cases": ["Image classification", "Object detection", "Face recognition"]
    },
    "rnn": {
        "category": "Deep Learning",
        "definition": "RNN (Recurrent Neural Network) untuk sequential data.",
        "problem": "Vanishing gradient untuk long sequences",
        "variants": ["LSTM", "GRU"],
        "use_cases": ["Language modeling", "Time series", "Speech recognition"]
    },
    "lstm": {
        "category": "Deep Learning",
        "definition": "LSTM (Long Short-Term Memory) adalah RNN yang bisa learn long-term dependencies.",
        "gates": ["Forget gate", "Input gate", "Output gate"],
        "use_cases": ["Text generation", "Machine translation", "Time series forecasting"]
    },
    "transformer": {
        "category": "Deep Learning",
        "definition": "Transformer adalah architecture dengan self-attention mechanism.",
        "components": ["Multi-head attention", "Positional encoding", "Feed-forward layers"],
        "models": ["BERT", "GPT", "T5", "LLaMA"],
        "paper": "Attention Is All You Need (2017)"
    },
    "attention_mechanism": {
        "category": "Deep Learning",
        "definition": "Attention memungkinkan model focus pada relevant parts of input.",
        "types": ["Self-attention", "Cross-attention", "Multi-head attention"],
        "formula": "Attention(Q,K,V) = softmax(QK^T/√d)V"
    },
    "bert": {
        "category": "NLP",
        "definition": "BERT (Bidirectional Encoder Representations from Transformers) untuk NLU.",
        "training": ["Masked Language Modeling", "Next Sentence Prediction"],
        "variants": ["RoBERTa", "ALBERT", "DistilBERT"],
        "use_cases": ["Question answering", "Sentiment analysis", "NER"]
    },
    "gpt": {
        "category": "NLP",
        "definition": "GPT (Generative Pre-trained Transformer) untuk text generation.",
        "versions": ["GPT-1", "GPT-2", "GPT-3", "GPT-4"],
        "training": "Autoregressive language modeling",
        "use_cases": ["Text generation", "Summarization", "Translation", "Code generation"]
    },
    "fine_tuning": {
        "category": "Machine Learning",
        "definition": "Fine-tuning adalah adapting pre-trained model ke specific task.",
        "techniques": ["Full fine-tuning", "LoRA", "QLoRA", "Prefix tuning"],
        "steps": ["Load pre-trained model", "Prepare task data", "Train on task data"]
    },
    "transfer_learning": {
        "category": "Machine Learning",
        "definition": "Transfer learning menggunakan knowledge dari satu task ke task lain.",
        "types": ["Feature extraction", "Fine-tuning"],
        "example": "ImageNet pre-trained model untuk medical imaging"
    },
    "embedding": {
        "category": "Machine Learning",
        "definition": "Embedding adalah dense vector representation of data.",
        "types": ["Word embeddings", "Sentence embeddings", "Image embeddings"],
        "models": ["Word2Vec", "GloVe", "FastText", "CLIP", "OpenAI Embeddings"]
    },
    "word2vec": {
        "category": "NLP",
        "definition": "Word2Vec adalah technique untuk learning word embeddings.",
        "architectures": ["Skip-gram", "CBOW (Continuous Bag of Words)"],
        "property": "king - man + woman = queen"
    },
    "tokenization": {
        "category": "NLP",
        "definition": "Tokenization adalah breaking text menjadi tokens.",
        "types": ["Word tokenization", "Subword (BPE, WordPiece)", "Character"],
        "tokenizers": ["SentencePiece", "tiktoken", "Hugging Face Tokenizers"]
    },
    "named_entity_recognition": {
        "category": "NLP",
        "definition": "NER mengidentifikasi dan mengklasifikasikan entities dalam text.",
        "entity_types": ["PERSON", "ORGANIZATION", "LOCATION", "DATE", "MONEY"],
        "models": ["SpaCy", "BERT-based NER"]
    },
    "sentiment_analysis": {
        "category": "NLP",
        "definition": "Sentiment Analysis menentukan emotional tone dari text.",
        "outputs": ["Positive", "Negative", "Neutral"],
        "approaches": ["Rule-based", "ML classifiers", "Deep learning"]
    },
    "object_detection": {
        "category": "Computer Vision",
        "definition": "Object Detection menemukan dan mengklasifikasikan objects dalam gambar.",
        "models": ["YOLO", "Faster R-CNN", "SSD", "DETR"],
        "output": "Bounding boxes dengan class labels"
    },
    "semantic_segmentation": {
        "category": "Computer Vision",
        "definition": "Semantic Segmentation mengklasifikasikan setiap pixel dalam gambar.",
        "models": ["U-Net", "DeepLab", "SegNet"],
        "use_cases": ["Medical imaging", "Autonomous driving", "Satellite imagery"]
    },
    "gan": {
        "category": "Deep Learning",
        "definition": "GAN (Generative Adversarial Network) untuk generating new data.",
        "components": ["Generator", "Discriminator"],
        "variants": ["DCGAN", "StyleGAN", "CycleGAN", "Pix2Pix"],
        "use_cases": ["Image generation", "Super resolution", "Style transfer"]
    },
    "diffusion_model": {
        "category": "Deep Learning",
        "definition": "Diffusion Models generate data dengan denoising process.",
        "process": ["Add noise gradually", "Learn to denoise"],
        "models": ["Stable Diffusion", "DALL-E", "Midjourney"],
        "use_cases": ["Image generation", "Video generation", "Audio synthesis"]
    },
    "prompt_engineering": {
        "category": "AI/ML",
        "definition": "Prompt Engineering adalah crafting inputs untuk optimal LLM outputs.",
        "techniques": ["Zero-shot", "Few-shot", "Chain-of-thought", "Self-consistency"],
        "best_practices": ["Be specific", "Provide examples", "Break down tasks"]
    },
    "rag_detailed": {
        "category": "AI/ML",
        "definition": "RAG menggabungkan retrieval dengan generation untuk grounded responses.",
        "pipeline": ["Query → Retrieve relevant docs → Include in context → Generate response"],
        "components": ["Embeddings", "Vector DB", "Retriever", "LLM"],
        "benefits": ["Reduced hallucination", "Up-to-date info", "Traceable sources"]
    },
    "hallucination": {
        "category": "AI/ML",
        "definition": "Hallucination adalah LLM menghasilkan false atau fabricated information.",
        "causes": ["Training data gaps", "Overconfidence", "Pattern completion"],
        "mitigation": ["RAG", "Fact checking", "Temperature tuning", "Confidence scores"]
    },
    "mlops": {
        "category": "AI/ML",
        "definition": "MLOps adalah practices untuk deploying dan maintaining ML models.",
        "components": ["Data versioning", "Experiment tracking", "Model registry", "Monitoring"],
        "tools": ["MLflow", "Weights & Biases", "DVC", "Kubeflow"]
    },
    "feature_engineering": {
        "category": "Machine Learning",
        "definition": "Feature Engineering adalah creating features dari raw data.",
        "techniques": ["Normalization", "One-hot encoding", "Binning", "Polynomial features"],
        "importance": "Often more impactful than model selection"
    },
    "hyperparameter_tuning": {
        "category": "Machine Learning",
        "definition": "Tuning parameters yang tidak di-learn selama training.",
        "methods": ["Grid Search", "Random Search", "Bayesian Optimization"],
        "tools": ["Optuna", "Ray Tune", "Hyperopt"]
    },
    "cross_validation": {
        "category": "Machine Learning",
        "definition": "Cross-validation adalah technique untuk evaluasi model robustness.",
        "types": ["K-Fold", "Stratified K-Fold", "Leave-One-Out", "Time Series Split"],
        "purpose": "Avoid overfitting pada specific train/test split"
    },
    "overfitting": {
        "category": "Machine Learning",
        "definition": "Overfitting adalah model yang perform baik di training tapi buruk di new data.",
        "signs": "High training accuracy, low validation accuracy",
        "solutions": ["More data", "Regularization", "Dropout", "Early stopping", "Cross-validation"]
    },
    "underfitting": {
        "category": "Machine Learning",
        "definition": "Underfitting adalah model yang terlalu simple untuk capture patterns.",
        "signs": "Low accuracy di training AND validation",
        "solutions": ["More features", "More complex model", "Less regularization", "Train longer"]
    },
    "bias_variance": {
        "category": "Machine Learning",
        "definition": "Bias-Variance tradeoff adalah balance antara underfitting dan overfitting.",
        "components": {
            "Bias": "Error dari simplifying assumptions",
            "Variance": "Error dari sensitivity to training data"
        },
        "goal": "Minimize total error (bias² + variance + irreducible error)"
    },
    "confusion_matrix": {
        "category": "Machine Learning",
        "definition": "Confusion matrix menampilkan prediction results untuk classification.",
        "components": ["True Positives", "False Positives", "True Negatives", "False Negatives"],
        "metrics": ["Accuracy", "Precision", "Recall", "F1-Score"]
    },
    "precision_recall": {
        "category": "Machine Learning",
        "definition": "Precision dan Recall adalah classification metrics.",
        "formulas": {
            "Precision": "TP / (TP + FP) - How many selected are relevant",
            "Recall": "TP / (TP + FN) - How many relevant are selected"
        },
        "tradeoff": "Increasing one often decreases the other"
    },
    "roc_auc": {
        "category": "Machine Learning",
        "definition": "ROC-AUC mengukur classifier performance across thresholds.",
        "roc_curve": "TPR vs FPR at different thresholds",
        "auc": "Area Under Curve (1 = perfect, 0.5 = random)",
        "use_case": "Comparing classifiers, threshold selection"
    },
    
    # ============================================
    # COMPUTER SCIENCE FUNDAMENTALS (30+ topics)
    # ============================================
    "operating_system": {
        "category": "Computer Science",
        "definition": "OS adalah software yang manages hardware dan provides services untuk programs.",
        "functions": ["Process management", "Memory management", "File system", "I/O", "Security"],
        "types": ["Windows", "Linux", "macOS", "Android", "iOS"]
    },
    "process": {
        "category": "Operating System",
        "definition": "Process adalah program yang sedang dieksekusi.",
        "states": ["New", "Ready", "Running", "Waiting", "Terminated"],
        "components": ["Code", "Data", "Stack", "Heap", "PCB"]
    },
    "thread": {
        "category": "Operating System",
        "definition": "Thread adalah unit of execution dalam process.",
        "vs_process": "Threads share memory, processes isolated",
        "types": ["User threads", "Kernel threads"]
    },
    "memory_management": {
        "category": "Operating System",
        "definition": "Memory management mengalokasikan dan dealokasikan memory.",
        "concepts": ["Virtual memory", "Paging", "Segmentation", "Page table"],
        "algorithms": ["First fit", "Best fit", "Worst fit"]
    },
    "virtual_memory": {
        "category": "Operating System",
        "definition": "Virtual memory menyediakan illusion of more memory than physically available.",
        "concepts": ["Page", "Frame", "Page table", "TLB", "Page fault"],
        "benefit": ["More memory", "Process isolation", "Memory protection"]
    },
    "deadlock": {
        "category": "Operating System",
        "definition": "Deadlock terjadi ketika processes saling menunggu resources.",
        "conditions": ["Mutual exclusion", "Hold and wait", "No preemption", "Circular wait"],
        "solutions": ["Prevention", "Avoidance (Banker's)", "Detection", "Recovery"]
    },
    "file_system": {
        "category": "Operating System",
        "definition": "File system mengatur bagaimana data disimpan dan diakses.",
        "types": ["ext4 (Linux)", "NTFS (Windows)", "APFS (macOS)", "FAT32"],
        "concepts": ["Inodes", "Directory structure", "Access control"]
    },
    "compiler": {
        "category": "Computer Science",
        "definition": "Compiler menerjemahkan source code ke machine code.",
        "phases": ["Lexical Analysis", "Syntax Analysis", "Semantic Analysis", "Optimization", "Code Generation"],
        "vs_interpreter": "Compiles entire program vs line-by-line execution"
    },
    "interpreter": {
        "category": "Computer Science",
        "definition": "Interpreter mengeksekusi code line by line tanpa compilation.",
        "examples": ["Python interpreter", "JavaScript engines (V8)"],
        "hybrid": "JIT compilation (Java, JS modern)"
    },
    "garbage_collection": {
        "category": "Computer Science",
        "definition": "GC otomatis membebaskan memory yang tidak lagi digunakan.",
        "algorithms": ["Mark-and-sweep", "Reference counting", "Generational GC"],
        "languages": ["Java", "Python", "Go", "JavaScript"]
    },
    "cache_memory": {
        "category": "Computer Science",
        "definition": "Cache adalah fast memory antara CPU dan main memory.",
        "levels": ["L1 (fastest, smallest)", "L2", "L3 (slowest, largest)"],
        "concepts": ["Cache hit/miss", "Locality of reference"]
    },
    "cpu_architecture": {
        "category": "Computer Science",
        "definition": "CPU architecture menentukan instruction set dan design.",
        "types": ["CISC (x86)", "RISC (ARM)", "RISC-V"],
        "components": ["ALU", "Control Unit", "Registers", "Cache"]
    },
    "binary_number": {
        "category": "Computer Science",
        "definition": "Binary adalah base-2 number system (0 dan 1).",
        "conversions": "Decimal 10 = Binary 1010",
        "operations": ["Addition", "Subtraction", "Multiplication using shifts"]
    },
    "hexadecimal": {
        "category": "Computer Science",
        "definition": "Hexadecimal adalah base-16 number system.",
        "digits": "0-9, A-F",
        "use_cases": ["Memory addresses", "Color codes (#FF5733)", "MAC addresses"]
    },
    "floating_point": {
        "category": "Computer Science",
        "definition": "Floating point merepresentasikan real numbers dengan precision terbatas.",
        "standard": "IEEE 754 (32-bit float, 64-bit double)",
        "issues": ["Rounding errors", "0.1 + 0.2 ≠ 0.3 exactly"]
    },
    "endianness": {
        "category": "Computer Science",
        "definition": "Endianness adalah byte order dalam memory.",
        "types": {
            "Big Endian": "MSB first (network byte order)",
            "Little Endian": "LSB first (x86)"
        }
    },
    "turing_machine": {
        "category": "Computer Science",
        "definition": "Turing Machine adalah theoretical model of computation.",
        "components": ["Infinite tape", "Head", "State machine", "Transition rules"],
        "significance": "Defines what is computable"
    },
    "complexity_classes": {
        "category": "Computer Science",
        "definition": "Complexity classes mengkategorikan problems by computational resources.",
        "classes": {
            "P": "Solvable in polynomial time",
            "NP": "Verifiable in polynomial time",
            "NP-Complete": "Hardest in NP",
            "NP-Hard": "At least as hard as NP-Complete"
        }
    },
    "np_complete": {
        "category": "Computer Science",
        "definition": "NP-Complete problems adalah yang paling sulit di NP.",
        "examples": ["Traveling Salesman", "Boolean Satisfiability", "Knapsack", "Graph Coloring"],
        "significance": "If any NP-Complete is in P, then P = NP"
    },
    "data_compression": {
        "category": "Computer Science",
        "definition": "Compression mengurangi size data untuk storage atau transmission.",
        "types": {
            "Lossless": "Exact reconstruction (ZIP, PNG)",
            "Lossy": "Approximate (JPEG, MP3)"
        },
        "algorithms": ["Huffman coding", "LZW", "DEFLATE"]
    },
}
