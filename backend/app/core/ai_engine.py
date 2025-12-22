"""
WeaR AI Engine - Local AI tanpa pihak ketiga
Sistem AI hybrid dengan knowledge base built-in dan pattern matching.
"""

import re
import json
from typing import Optional
from dataclasses import dataclass
from pathlib import Path


@dataclass
class AIResponse:
    """Response from the AI engine."""
    answer: str
    confidence: float
    source: str  # "knowledge_base", "pattern", "fallback"


class KnowledgeBase:
    """Built-in knowledge base untuk WeaR AI."""
    
    def __init__(self):
        self.knowledge = self._load_knowledge()
    
    def _load_knowledge(self) -> dict:
        """Load knowledge base - expandable."""
        return {
            # Programming Concepts
            "recursion": {
                "definition": "Recursion adalah teknik pemrograman di mana sebuah fungsi memanggil dirinya sendiri untuk menyelesaikan masalah.",
                "example": '''```python
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120
```''',
                "tips": [
                    "Selalu definisikan base case untuk menghentikan rekursi",
                    "Pastikan setiap recursive call mendekati base case",
                    "Hati-hati dengan stack overflow pada rekursi dalam"
                ]
            },
            
            "python": {
                "definition": "Python adalah bahasa pemrograman tingkat tinggi yang mudah dipelajari dengan sintaks yang bersih dan readable.",
                "features": [
                    "Dinamis typing",
                    "Garbage collection otomatis",
                    "Library yang sangat luas",
                    "Multi-paradigm (OOP, functional, procedural)"
                ],
                "example": '''```python
# Hello World
print("Hello, World!")

# Variabel
nama = "WeaR AI"
umur = 1

# List
languages = ["Python", "JavaScript", "Go"]

# Function
def greet(name):
    return f"Halo, {name}!"
```'''
            },
            
            "javascript": {
                "definition": "JavaScript adalah bahasa pemrograman utama untuk web development, berjalan di browser dan server (Node.js).",
                "features": [
                    "Event-driven programming",
                    "Asynchronous dengan Promises/async-await",
                    "First-class functions",
                    "Prototype-based inheritance"
                ],
                "example": '''```javascript
// Variabel
const name = "WeaR AI";
let counter = 0;

// Function
const greet = (name) => `Halo, ${name}!`;

// Async/Await
async function fetchData() {
    const response = await fetch('/api/data');
    return response.json();
}
```'''
            },
            
            "api": {
                "definition": "API (Application Programming Interface) adalah antarmuka yang memungkinkan dua aplikasi berkomunikasi satu sama lain.",
                "types": [
                    "REST API - HTTP-based, resource-oriented",
                    "GraphQL - Query language for APIs",
                    "WebSocket - Real-time bidirectional",
                    "gRPC - High-performance RPC"
                ],
                "example": '''```python
# FastAPI Example
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```'''
            },
            
            "database": {
                "definition": "Database adalah sistem untuk menyimpan, mengorganisir, dan mengelola data secara terstruktur.",
                "types": {
                    "SQL": ["PostgreSQL", "MySQL", "SQLite"],
                    "NoSQL": ["MongoDB", "Redis", "Cassandra"],
                    "Vector": ["Qdrant", "Pinecone", "Weaviate"]
                },
                "example": '''```sql
-- Buat tabel
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255) UNIQUE
);

-- Insert data
INSERT INTO users (name, email) 
VALUES ('John', 'john@example.com');

-- Query data
SELECT * FROM users WHERE name = 'John';
```'''
            },
            
            "git": {
                "definition": "Git adalah sistem version control terdistribusi untuk tracking perubahan kode.",
                "commands": {
                    "git init": "Inisialisasi repository baru",
                    "git clone": "Clone repository dari remote",
                    "git add": "Tambah file ke staging",
                    "git commit": "Simpan perubahan",
                    "git push": "Upload ke remote",
                    "git pull": "Download dari remote",
                    "git branch": "Kelola branches"
                },
                "example": '''```bash
# Setup repo baru
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/user/repo.git
git push -u origin main
```'''
            },
            
            "docker": {
                "definition": "Docker adalah platform untuk mengemas aplikasi dalam container yang portabel.",
                "concepts": [
                    "Image - Template read-only",
                    "Container - Instance dari image",
                    "Dockerfile - Script untuk build image",
                    "Docker Compose - Multi-container orchestration"
                ],
                "example": '''```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "main.py"]
```'''
            },
            
            "fastapi": {
                "definition": "FastAPI adalah framework Python modern untuk membangun API dengan performa tinggi.",
                "features": [
                    "Async support",
                    "Automatic docs (Swagger/OpenAPI)",
                    "Type hints & validation",
                    "Dependency injection"
                ],
                "example": '''```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item, "status": "created"}
```'''
            },
            
            "react": {
                "definition": "React adalah library JavaScript untuk membangun user interface dengan komponen.",
                "concepts": [
                    "Components - Building blocks UI",
                    "Props - Data dari parent ke child",
                    "State - Data internal komponen",
                    "Hooks - useState, useEffect, dll"
                ],
                "example": '''```jsx
import { useState } from 'react';

function Counter() {
    const [count, setCount] = useState(0);
    
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>
                Increment
            </button>
        </div>
    );
}
```'''
            },
            
            "nextjs": {
                "definition": "Next.js adalah framework React untuk production dengan SSR, routing, dan optimizations.",
                "features": [
                    "Server-side rendering (SSR)",
                    "Static site generation (SSG)",
                    "File-based routing",
                    "API routes built-in"
                ],
                "example": '''```jsx
// app/page.tsx
export default function Home() {
    return (
        <main>
            <h1>Welcome to Next.js!</h1>
        </main>
    );
}

// app/api/hello/route.ts
export async function GET() {
    return Response.json({ message: "Hello!" });
}
```'''
            },
            
            "sorting": {
                "definition": "Sorting adalah proses mengurutkan data dalam urutan tertentu.",
                "algorithms": {
                    "Bubble Sort": "O(n²) - Simple tapi lambat",
                    "Quick Sort": "O(n log n) - Cepat, paling umum",
                    "Merge Sort": "O(n log n) - Stabil, divide & conquer",
                    "Heap Sort": "O(n log n) - In-place"
                },
                "example": '''```python
# Quick Sort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Built-in Python
sorted_list = sorted([3, 1, 4, 1, 5, 9])
```'''
            },
            
            "async_await": {
                "definition": "Async/await adalah pattern untuk menangani operasi asynchronous secara lebih readable.",
                "example": '''```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)  # Simulasi I/O
    return "Data fetched!"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```'''
            },
            
            "oop": {
                "definition": "OOP (Object-Oriented Programming) adalah paradigma pemrograman berbasis objek.",
                "principles": [
                    "Encapsulation - Menyembunyikan detail internal",
                    "Inheritance - Mewarisi sifat dari class lain",
                    "Polymorphism - Satu interface, banyak implementasi",
                    "Abstraction - Menyederhanakan kompleksitas"
                ],
                "example": '''```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
print(dog.speak())  # Buddy says Woof!
```'''
            }
        }
    
    def search(self, query: str) -> Optional[dict]:
        """Search knowledge base."""
        query_lower = query.lower()
        
        # Direct match
        for topic, content in self.knowledge.items():
            if topic in query_lower:
                return {"topic": topic, **content}
        
        # Keyword search
        keywords = {
            "fungsi": ["python", "javascript"],
            "loop": ["python", "javascript"],
            "class": ["oop", "python"],
            "database": ["database", "sql"],
            "web": ["api", "fastapi", "react", "nextjs"],
            "urutkan": ["sorting"],
            "sort": ["sorting"],
            "async": ["async_await"],
            "object": ["oop"],
        }
        
        for keyword, topics in keywords.items():
            if keyword in query_lower:
                for topic in topics:
                    if topic in self.knowledge:
                        return {"topic": topic, **self.knowledge[topic]}
        
        return None


class PatternMatcher:
    """Pattern matching untuk pertanyaan umum."""
    
    def __init__(self):
        self.patterns = self._load_patterns()
    
    def _load_patterns(self) -> list:
        return [
            # Greeting
            {
                "pattern": r"(halo|hai|hello|hi|hey)",
                "response": "Halo! 👋 Saya WeaR AI, asisten coding Anda. Ada yang bisa saya bantu?"
            },
            # Identity
            {
                "pattern": r"(siapa kamu|siapa anda|who are you|kamu siapa)",
                "response": "Saya adalah **WeaR AI**, asisten coding yang dirancang untuk membantu Anda dengan programming, development, dan teknologi. Saya berjalan secara lokal di komputer Anda! 🤖"
            },
            # Capabilities
            {
                "pattern": r"(apa yang bisa|what can you|kemampuan|bisa apa)",
                "response": """Saya bisa membantu Anda dengan:

🐍 **Programming** - Python, JavaScript, TypeScript, dan lainnya
🌐 **Web Development** - React, Next.js, FastAPI
📦 **Database** - SQL, NoSQL, design patterns
🛠️ **DevOps** - Docker, Git, deployment
💡 **Konsep** - Algoritma, data structures, architecture

Coba tanyakan sesuatu seperti: *"Jelaskan apa itu recursion"* atau *"Buatkan contoh API dengan FastAPI"*"""
            },
            # Thanks
            {
                "pattern": r"(terima kasih|thanks|thank you|makasih)",
                "response": "Sama-sama! 😊 Senang bisa membantu. Ada yang lain?"
            },
            # How are you
            {
                "pattern": r"(apa kabar|how are you|kabar)",
                "response": "Saya baik-baik saja! Siap membantu Anda coding. Ada yang mau dikerjakan? 💪"
            },
        ]
    
    def match(self, query: str) -> Optional[str]:
        """Match query against patterns."""
        query_lower = query.lower()
        
        for item in self.patterns:
            if re.search(item["pattern"], query_lower):
                return item["response"]
        
        return None


class WeaRAIEngine:
    """
    WeaR AI Engine - Local AI tanpa pihak ketiga.
    
    Ini adalah AI engine yang berjalan sepenuhnya lokal dengan:
    1. Built-in knowledge base tentang programming
    2. Pattern matching untuk pertanyaan umum
    3. Response generation yang terstruktur
    """
    
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.pattern_matcher = PatternMatcher()
        self.conversation_history = []
    
    def generate(self, query: str) -> AIResponse:
        """Generate response untuk query."""
        
        # 1. Try pattern matching first
        pattern_response = self.pattern_matcher.match(query)
        if pattern_response:
            return AIResponse(
                answer=pattern_response,
                confidence=0.95,
                source="pattern"
            )
        
        # 2. Search knowledge base
        knowledge = self.knowledge_base.search(query)
        if knowledge:
            answer = self._format_knowledge_response(knowledge, query)
            return AIResponse(
                answer=answer,
                confidence=0.85,
                source="knowledge_base"
            )
        
        # 3. Fallback response
        return AIResponse(
            answer=self._generate_fallback(query),
            confidence=0.3,
            source="fallback"
        )
    
    def _format_knowledge_response(self, knowledge: dict, query: str) -> str:
        """Format knowledge into readable response."""
        topic = knowledge.get("topic", "")
        
        response_parts = []
        
        # Title
        response_parts.append(f"## {topic.upper()}\n")
        
        # Definition
        if "definition" in knowledge:
            response_parts.append(knowledge["definition"])
            response_parts.append("")
        
        # Features/Concepts
        if "features" in knowledge:
            response_parts.append("### Fitur Utama:")
            for feature in knowledge["features"]:
                response_parts.append(f"- {feature}")
            response_parts.append("")
        
        if "concepts" in knowledge:
            response_parts.append("### Konsep Penting:")
            if isinstance(knowledge["concepts"], list):
                for concept in knowledge["concepts"]:
                    response_parts.append(f"- {concept}")
            elif isinstance(knowledge["concepts"], dict):
                for key, value in knowledge["concepts"].items():
                    response_parts.append(f"- **{key}**: {value}")
            response_parts.append("")
        
        if "principles" in knowledge:
            response_parts.append("### Prinsip:")
            for principle in knowledge["principles"]:
                response_parts.append(f"- {principle}")
            response_parts.append("")
        
        if "types" in knowledge:
            response_parts.append("### Jenis:")
            if isinstance(knowledge["types"], list):
                for t in knowledge["types"]:
                    response_parts.append(f"- {t}")
            elif isinstance(knowledge["types"], dict):
                for category, items in knowledge["types"].items():
                    response_parts.append(f"- **{category}**: {', '.join(items)}")
            response_parts.append("")
        
        if "algorithms" in knowledge:
            response_parts.append("### Algoritma:")
            for algo, desc in knowledge["algorithms"].items():
                response_parts.append(f"- **{algo}**: {desc}")
            response_parts.append("")
        
        if "commands" in knowledge:
            response_parts.append("### Commands:")
            for cmd, desc in knowledge["commands"].items():
                response_parts.append(f"- `{cmd}`: {desc}")
            response_parts.append("")
        
        # Example
        if "example" in knowledge:
            response_parts.append("### Contoh:")
            response_parts.append(knowledge["example"])
            response_parts.append("")
        
        # Tips
        if "tips" in knowledge:
            response_parts.append("### 💡 Tips:")
            for tip in knowledge["tips"]:
                response_parts.append(f"- {tip}")
        
        return "\n".join(response_parts)
    
    def _generate_fallback(self, query: str) -> str:
        """Generate fallback response when no match found."""
        return f"""Maaf, saya belum memiliki informasi lengkap tentang topik ini dalam knowledge base saya.

**Yang bisa Anda lakukan:**
1. Coba pertanyaan yang lebih spesifik
2. Tanyakan tentang: Python, JavaScript, API, Database, Git, Docker, React, Next.js, FastAPI
3. Minta contoh kode dengan menyebut bahasa pemrograman

**Contoh pertanyaan:**
- "Jelaskan apa itu recursion"
- "Buatkan contoh sorting di Python"
- "Apa itu FastAPI?"

---
*WeaR AI terus belajar dan knowledge base akan terus diperluas!* 🚀"""
    
    def add_knowledge(self, topic: str, content: dict) -> None:
        """Add new knowledge to the base."""
        self.knowledge_base.knowledge[topic.lower()] = content
    
    def chat(self, message: str) -> str:
        """Simple chat interface."""
        self.conversation_history.append({"role": "user", "message": message})
        
        response = self.generate(message)
        
        self.conversation_history.append({
            "role": "assistant", 
            "message": response.answer,
            "confidence": response.confidence,
            "source": response.source
        })
        
        return response.answer


# Global engine instance
_engine = None


def get_engine() -> WeaRAIEngine:
    """Get the global AI engine instance."""
    global _engine
    if _engine is None:
        _engine = WeaRAIEngine()
    return _engine


# Convenience function
def ask(question: str) -> str:
    """Quick way to ask the AI a question."""
    engine = get_engine()
    return engine.chat(question)
