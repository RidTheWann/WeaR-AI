"""
WeaR AI - Natural Language Response Generator
Membuat respons AI lebih natural dan conversational!
Created by RidTheWann
"""

import random
from typing import List, Dict, Optional, Tuple


class ConversationalResponder:
    """
    Generate natural, conversational responses.
    Makes AI responses feel more human-like.
    """
    
    def __init__(self):
        # Opening phrases - variasi untuk memulai jawaban
        self.openers = {
            "explain": [
                "Oke, jadi begini...",
                "Baik! Mari saya jelaskan.",
                "Nah, ini menarik!",
                "Pertanyaan bagus!",
                "Ah, ini topik yang sering ditanyakan.",
                "Sip, saya jelaskan ya.",
                "Tentu! Jadi...",
                "Oke, simak ya.",
            ],
            "greeting": [
                "Hai juga! 👋",
                "Halo! Senang bisa membantu.",
                "Hey! Ada yang bisa saya bantu?",
                "Hai! Saya WeaR AI, siap membantu!",
                "Halo! Apa kabar hari ini?",
                "Hi! Silakan tanya apa saja.",
            ],
            "help": [
                "Tentu, saya bantu!",
                "Oke, mari kita lihat...",
                "Sip, saya coba tolong ya.",
                "Tidak masalah! Mari kita selesaikan.",
                "Oke, saya di sini untuk membantu.",
            ],
            "technical": [
                "Secara teknis...",
                "Dari segi teknis,",
                "Begini penjelasan teknisnya:",
                "Secara konsep,",
            ],
        }
        
        # Transition phrases - untuk menghubungkan kalimat
        self.transitions = [
            "Selain itu,",
            "Yang menarik adalah,",
            "Perlu diingat juga,",
            "Oh iya,",
            "Ngomong-ngomong,",
            "Satu hal lagi,",
            "Dan yang tidak kalah penting,",
        ]
        
        # Closing phrases - untuk menutup jawaban
        self.closers = [
            "Semoga membantu! 😊",
            "Ada yang ingin ditanyakan lagi?",
            "Kalau masih bingung, tanya aja ya!",
            "Semoga jelas ya!",
            "Hope that helps!",
            "Jangan ragu bertanya lagi!",
            "Kalau butuh penjelasan lebih detail, bilang aja.",
        ]
        
        # Filler words untuk natural flow
        self.fillers = [
            "basically",
            "intinya",
            "singkatnya",
            "jadi",
            "nah",
            "gitu deh",
        ]
        
        # Emoji untuk personality
        self.emojis = {
            "happy": ["😊", "🙂", "😄", "👍"],
            "thinking": ["🤔", "💭", "🧐"],
            "tech": ["💻", "🔧", "⚙️", "🛠️"],
            "success": ["✅", "🎉", "👏"],
            "info": ["📝", "💡", "📌"],
            "warning": ["⚠️", "🔔"],
        }
        
        # Response templates untuk berbagai konteks
        self.templates = {
            "definition": [
                "{opener} **{topic}** adalah {definition}. {extra}",
                "{opener} Jadi, **{topic}** itu {definition}. {extra}",
                "{opener} Simpelnya, **{topic}** = {definition}. {extra}",
            ],
            "howto": [
                "{opener} Untuk {goal}, caranya:\n\n{steps}\n\n{closer}",
                "{opener} Langkah-langkahnya:\n\n{steps}\n\n{closer}",
                "{opener} Gampang kok! Begini caranya:\n\n{steps}\n\n{closer}",
            ],
            "comparison": [
                "{opener} Perbedaan utama antara **{a}** dan **{b}**:\n\n{comparison}\n\n{closer}",
                "{opener} Mari kita bandingkan:\n\n**{a}**: {a_desc}\n\n**{b}**: {b_desc}\n\n{closer}",
            ],
            "list": [
                "{opener} Berikut ini beberapa {topic}:\n\n{items}\n\n{closer}",
                "{opener} Ada beberapa {topic} yang perlu kamu tahu:\n\n{items}",
            ],
            "recommendation": [
                "{opener} Untuk {context}, saya rekomendasikan:\n\n{recommendations}\n\n{closer}",
                "{opener} Ini rekomendasi saya untuk {context}:\n\n{recommendations}",
            ],
        }
        
        # Casual phrases untuk tone yang friendly
        self.casual_phrases = {
            "agreement": ["Setuju!", "Bener banget!", "Exactly!", "Tepat sekali!"],
            "uncertainty": ["Hmm, sepertinya...", "Kalau tidak salah...", "Mungkin..."],
            "emphasis": ["yang paling penting", "yang krusial", "key point-nya"],
            "example": ["misalnya", "contohnya", "seperti", "kayak"],
        }
    
    def get_opener(self, context: str = "explain") -> str:
        """Get random opening phrase based on context."""
        openers = self.openers.get(context, self.openers["explain"])
        return random.choice(openers)
    
    def get_closer(self) -> str:
        """Get random closing phrase."""
        return random.choice(self.closers)
    
    def get_transition(self) -> str:
        """Get random transition phrase."""
        return random.choice(self.transitions)
    
    def get_emoji(self, mood: str = "happy") -> str:
        """Get random emoji based on mood."""
        emojis = self.emojis.get(mood, self.emojis["happy"])
        return random.choice(emojis)
    
    def make_natural(self, text: str) -> str:
        """
        Make text more natural and conversational.
        Adds casual elements without being unprofessional.
        """
        # Add occasional emoji
        if random.random() > 0.7:
            text = text + " " + self.get_emoji()
        
        return text
    
    def format_list(self, items: List[str], numbered: bool = True) -> str:
        """Format items as a natural list."""
        if numbered:
            return "\n".join(f"{i+1}. {item}" for i, item in enumerate(items))
        else:
            return "\n".join(f"• {item}" for item in items)
    
    def generate_response(self, template_type: str, **kwargs) -> str:
        """
        Generate response from template.
        
        Args:
            template_type: Type of response (definition, howto, list, etc.)
            **kwargs: Variables to fill in template
        """
        templates = self.templates.get(template_type, self.templates["definition"])
        template = random.choice(templates)
        
        # Add default values
        kwargs.setdefault("opener", self.get_opener())
        kwargs.setdefault("closer", self.get_closer())
        kwargs.setdefault("extra", "")
        
        try:
            return template.format(**kwargs)
        except KeyError:
            return kwargs.get("fallback", "Maaf, saya tidak mengerti pertanyaan tersebut.")


class ResponseEnhancer:
    """
    Enhance AI responses to be more natural and engaging.
    """
    
    def __init__(self):
        self.responder = ConversationalResponder()
        
        # Patterns untuk mendeteksi jenis pertanyaan
        self.question_patterns = {
            "what_is": ["apa itu", "apakah", "what is", "what's", "apa yang dimaksud"],
            "how_to": ["bagaimana", "cara", "how to", "gimana", "how can"],
            "why": ["mengapa", "kenapa", "why", "kok bisa"],
            "when": ["kapan", "when"],
            "where": ["dimana", "where", "di mana"],
            "who": ["siapa", "who"],
            "which": ["yang mana", "which", "mana yang"],
            "compare": ["perbedaan", "bedanya", "difference", "vs", "versus", "beda"],
            "recommend": ["rekomendasi", "recommend", "saran", "suggest", "terbaik", "best"],
            "list": ["sebutkan", "list", "apa saja", "berikan contoh"],
        }
    
    def detect_question_type(self, query: str) -> str:
        """Detect the type of question."""
        query_lower = query.lower()
        
        for qtype, patterns in self.question_patterns.items():
            for pattern in patterns:
                if pattern in query_lower:
                    return qtype
        
        return "general"
    
    def enhance(self, response: str, query: str = "", add_opener: bool = True, 
                add_closer: bool = True) -> str:
        """
        Enhance a response to be more natural.
        
        Args:
            response: Original response text
            query: Original user query (for context)
            add_opener: Whether to add opening phrase
            add_closer: Whether to add closing phrase
        """
        # Detect question type for appropriate opener
        qtype = self.detect_question_type(query)
        
        # Map question type to opener context
        opener_context = {
            "what_is": "explain",
            "how_to": "help",
            "why": "explain",
            "compare": "technical",
            "recommend": "help",
        }.get(qtype, "explain")
        
        parts = []
        
        # Add opener if needed
        if add_opener and not response.startswith(("Hai", "Halo", "Hi", "Hey")):
            opener = self.responder.get_opener(opener_context)
            parts.append(opener)
        
        # Add main response
        parts.append(response)
        
        # Add closer if needed and response is substantial
        if add_closer and len(response) > 100:
            # Only add closer sometimes for variety
            if random.random() > 0.5:
                closer = self.responder.get_closer()
                parts.append(closer)
        
        return "\n\n".join(parts)
    
    def add_personality(self, response: str) -> str:
        """Add personality elements to response."""
        # Occasionally add emoji
        if random.random() > 0.6:
            response = response + " " + self.responder.get_emoji()
        
        return response


class SmartResponseGenerator:
    """
    Generate smart, context-aware responses.
    """
    
    def __init__(self):
        self.enhancer = ResponseEnhancer()
        self.responder = ConversationalResponder()
        
        # Common Indonesian slang/casual mappings
        self.casual_synonyms = {
            "adalah": ["itu", "merupakan", "yaitu"],
            "sangat": ["banget", "sekali", "super"],
            "bagus": ["keren", "mantap", "oke", "sip"],
            "menggunakan": ["pakai", "pake", "gunakan"],
            "tidak": ["nggak", "gak", "enggak"],
        }
        
        # Greeting responses with personality
        self.greeting_responses = [
            "Hai! 👋 Saya WeaR AI, siap membantu kamu hari ini. Ada yang bisa dibantu?",
            "Halo! Senang bertemu denganmu. Mau tanya apa nih?",
            "Hey! WeaR AI di sini. Tanya apa aja, saya siap jawab! 😊",
            "Hi! Apa kabar? Saya WeaR AI. Silakan bertanya!",
            "Halo! 🙌 Ada yang bisa saya bantu hari ini?",
        ]
        
        # Help responses
        self.help_responses = [
            "Tentu, saya bantu! Coba jelaskan lebih detail masalahmu.",
            "Oke, mari kita selesaikan bareng. Apa yang terjadi?",
            "Sip! Jelaskan situasinya, saya coba carikan solusi.",
            "Tidak masalah! Ceritakan lebih lanjut, saya di sini untuk bantu.",
        ]
        
        # Thinking phrases
        self.thinking = [
            "Hmm, menarik...",
            "Ini pertanyaan bagus!",
            "Oke, sebentar saya pikirkan...",
        ]
    
    def generate_greeting(self) -> str:
        """Generate a friendly greeting."""
        return random.choice(self.greeting_responses)
    
    def generate_help_response(self) -> str:
        """Generate a helpful response."""
        return random.choice(self.help_responses)
    
    def wrap_code(self, code: str, language: str = "") -> str:
        """Wrap code in markdown code block."""
        return f"```{language}\n{code}\n```"
    
    def format_definition(self, topic: str, definition: str, extras: List[str] = None) -> str:
        """Format a definition response naturally."""
        opener = self.responder.get_opener("explain")
        
        response = f"{opener}\n\n**{topic}** adalah {definition}."
        
        if extras:
            response += "\n\n" + self.responder.get_transition() + " " + " ".join(extras)
        
        if random.random() > 0.5:
            response += "\n\n" + self.responder.get_closer()
        
        return response
    
    def format_steps(self, goal: str, steps: List[str]) -> str:
        """Format step-by-step instructions naturally."""
        opener = self.responder.get_opener("help")
        
        formatted_steps = self.responder.format_list(steps, numbered=True)
        
        response = f"{opener}\n\nUntuk {goal}, ikuti langkah berikut:\n\n{formatted_steps}"
        response += "\n\n" + self.responder.get_closer()
        
        return response


# Singleton instances
_enhancer: Optional[ResponseEnhancer] = None
_generator: Optional[SmartResponseGenerator] = None


def get_response_enhancer() -> ResponseEnhancer:
    """Get singleton ResponseEnhancer instance."""
    global _enhancer
    if _enhancer is None:
        _enhancer = ResponseEnhancer()
    return _enhancer


def get_smart_generator() -> SmartResponseGenerator:
    """Get singleton SmartResponseGenerator instance."""
    global _generator
    if _generator is None:
        _generator = SmartResponseGenerator()
    return _generator


def demo_natural_responses():
    """Demo natural response generation."""
    print("=== WeaR AI Natural Response Demo ===\n")
    
    enhancer = get_response_enhancer()
    generator = get_smart_generator()
    
    # 1. Greeting
    print("1. Greeting Response:")
    print(f"   {generator.generate_greeting()}")
    
    # 2. Definition
    print("\n2. Definition Response:")
    response = generator.format_definition(
        "Python",
        "bahasa pemrograman tingkat tinggi yang mudah dipelajari",
        ["Diciptakan oleh Guido van Rossum pada 1991."]
    )
    print(f"   {response}")
    
    # 3. Steps
    print("\n3. Step-by-Step Response:")
    response = generator.format_steps(
        "install Python",
        ["Download dari python.org", "Jalankan installer", "Centang 'Add to PATH'", "Selesai!"]
    )
    print(f"   {response}")
    
    # 4. Enhanced response
    print("\n4. Enhanced Response:")
    basic = "Docker adalah platform kontainerisasi yang memungkinkan aplikasi berjalan dalam lingkungan terisolasi."
    enhanced = enhancer.enhance(basic, "apa itu docker")
    print(f"   Basic: {basic}")
    print(f"   Enhanced: {enhanced}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    demo_natural_responses()
