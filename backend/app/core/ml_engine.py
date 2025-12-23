"""
WeaR AI - Simple Machine Learning Module
Machine Learning tanpa TensorFlow/PyTorch - Zero Budget AI!
Created by RidTheWann

Ini adalah implementasi ML sederhana yang bisa berjalan di mana saja
tanpa membutuhkan GPU atau library berat.
"""

import math
import random
from typing import List, Dict, Tuple, Any, Optional
from collections import Counter, defaultdict
import re


class TextClassifier:
    """
    Simple Naive Bayes Text Classifier.
    Bisa digunakan untuk klasifikasi intent user, sentiment analysis, dll.
    """
    
    def __init__(self):
        self.word_counts: Dict[str, Counter] = {}
        self.class_counts: Counter = Counter()
        self.vocabulary: set = set()
        self.total_docs = 0
        
    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization."""
        text = text.lower()
        words = re.findall(r'\b\w+\b', text)
        return words
    
    def train(self, texts: List[str], labels: List[str]):
        """
        Train classifier dengan data.
        
        Args:
            texts: List of text documents
            labels: List of labels untuk setiap document
        """
        for text, label in zip(texts, labels):
            self.class_counts[label] += 1
            self.total_docs += 1
            
            if label not in self.word_counts:
                self.word_counts[label] = Counter()
            
            words = self._tokenize(text)
            self.word_counts[label].update(words)
            self.vocabulary.update(words)
    
    def predict(self, text: str) -> Tuple[str, float]:
        """
        Predict class untuk text baru.
        
        Returns:
            Tuple of (predicted_class, confidence)
        """
        words = self._tokenize(text)
        scores = {}
        
        for label in self.class_counts:
            # Log probability of class
            log_prob = math.log(self.class_counts[label] / self.total_docs)
            
            # Total words in this class
            total_words = sum(self.word_counts[label].values())
            vocab_size = len(self.vocabulary)
            
            # Add log probability of each word
            for word in words:
                # Laplace smoothing
                word_count = self.word_counts[label].get(word, 0)
                word_prob = (word_count + 1) / (total_words + vocab_size)
                log_prob += math.log(word_prob)
            
            scores[label] = log_prob
        
        # Get best prediction
        best_label = max(scores, key=scores.get)
        
        # Convert log probs to confidence
        max_score = max(scores.values())
        exp_scores = {k: math.exp(v - max_score) for k, v in scores.items()}
        total = sum(exp_scores.values())
        confidence = exp_scores[best_label] / total
        
        return best_label, confidence


class SentimentAnalyzer:
    """
    Simple rule-based + learning Sentiment Analyzer.
    """
    
    def __init__(self):
        # Positive words (Indonesian + English)
        self.positive_words = {
            # Indonesian
            'bagus', 'baik', 'hebat', 'mantap', 'keren', 'suka', 'senang', 
            'gembira', 'sukses', 'berhasil', 'indah', 'cantik', 'tampan',
            'luar biasa', 'amazing', 'sempurna', 'cinta', 'sayang', 'terbaik',
            # English
            'good', 'great', 'excellent', 'awesome', 'amazing', 'wonderful',
            'fantastic', 'love', 'happy', 'beautiful', 'nice', 'best', 'perfect',
            'brilliant', 'superb', 'outstanding', 'incredible', 'positive'
        }
        
        # Negative words
        self.negative_words = {
            # Indonesian
            'buruk', 'jelek', 'gagal', 'bodoh', 'benci', 'marah', 'sedih',
            'kecewa', 'mengecewakan', 'payah', 'parah', 'menyesal', 'susah',
            'sulit', 'masalah', 'rusak', 'hancur', 'terburuk',
            # English
            'bad', 'terrible', 'awful', 'horrible', 'hate', 'angry', 'sad',
            'disappointed', 'disappointing', 'worst', 'poor', 'negative',
            'failed', 'failure', 'broken', 'wrong', 'stupid', 'dumb'
        }
        
        # Intensifiers
        self.intensifiers = {
            'sangat', 'very', 'really', 'extremely', 'super', 'banget', 
            'sekali', 'amat', 'paling', 'totally', 'absolutely'
        }
        
        # Negators
        self.negators = {
            'tidak', 'bukan', 'tak', 'enggak', 'gak', 'ga', 'no', 'not',
            "don't", "doesn't", "didn't", "won't", "can't", 'never'
        }
    
    def analyze(self, text: str) -> Dict[str, Any]:
        """
        Analyze sentiment of text.
        
        Returns:
            Dict with sentiment, score, and details
        """
        text_lower = text.lower()
        words = re.findall(r'\b\w+\b', text_lower)
        
        positive_count = 0
        negative_count = 0
        intensity = 1.0
        negated = False
        
        for i, word in enumerate(words):
            # Check for negation
            if word in self.negators:
                negated = True
                continue
            
            # Check for intensifiers
            if word in self.intensifiers:
                intensity = 1.5
                continue
            
            # Count sentiment words
            if word in self.positive_words:
                if negated:
                    negative_count += intensity
                    negated = False
                else:
                    positive_count += intensity
            elif word in self.negative_words:
                if negated:
                    positive_count += intensity
                    negated = False
                else:
                    negative_count += intensity
            
            # Reset intensity after use
            intensity = 1.0
        
        # Calculate score (-1 to 1)
        total = positive_count + negative_count
        if total == 0:
            score = 0.0
            sentiment = 'neutral'
        else:
            score = (positive_count - negative_count) / total
            if score > 0.2:
                sentiment = 'positive'
            elif score < -0.2:
                sentiment = 'negative'
            else:
                sentiment = 'neutral'
        
        return {
            'sentiment': sentiment,
            'score': round(score, 3),
            'positive_count': positive_count,
            'negative_count': negative_count,
            'confidence': abs(score)
        }


class IntentClassifier:
    """
    Intent classifier untuk mendeteksi maksud user.
    Pre-trained dengan patterns umum.
    """
    
    def __init__(self):
        self.classifier = TextClassifier()
        self._train_default_intents()
    
    def _train_default_intents(self):
        """Train dengan default intents."""
        training_data = [
            # Greeting
            ("halo", "greeting"),
            ("hai", "greeting"),
            ("hello", "greeting"),
            ("hi", "greeting"),
            ("selamat pagi", "greeting"),
            ("selamat siang", "greeting"),
            ("hey", "greeting"),
            
            # Question
            ("apa itu", "question"),
            ("bagaimana cara", "question"),
            ("what is", "question"),
            ("how to", "question"),
            ("kenapa", "question"),
            ("mengapa", "question"),
            ("why", "question"),
            ("siapa", "question"),
            ("who is", "question"),
            ("kapan", "question"),
            ("when", "question"),
            ("dimana", "question"),
            ("where", "question"),
            
            # Command
            ("tolong", "command"),
            ("buatkan", "command"),
            ("please", "command"),
            ("bisa", "command"),
            ("can you", "command"),
            ("make", "command"),
            ("create", "command"),
            ("generate", "command"),
            
            # Help
            ("bantuan", "help"),
            ("help", "help"),
            ("tolong bantu", "help"),
            ("bingung", "help"),
            ("tidak mengerti", "help"),
            
            # Goodbye
            ("bye", "goodbye"),
            ("dadah", "goodbye"),
            ("sampai jumpa", "goodbye"),
            ("goodbye", "goodbye"),
            ("see you", "goodbye"),
            
            # Thanks
            ("terima kasih", "thanks"),
            ("thanks", "thanks"),
            ("thank you", "thanks"),
            ("makasih", "thanks"),
            
            # Search/Info
            ("cari", "search"),
            ("search", "search"),
            ("find", "search"),
            ("lookup", "search"),
            ("jelaskan", "search"),
            ("explain", "search"),
        ]
        
        texts = [t[0] for t in training_data]
        labels = [t[1] for t in training_data]
        self.classifier.train(texts, labels)
    
    def classify(self, text: str) -> Tuple[str, float]:
        """Classify user intent."""
        return self.classifier.predict(text)


class TextSimilarity:
    """
    Calculate text similarity menggunakan berbagai metode.
    Berguna untuk fuzzy search dan matching.
    """
    
    @staticmethod
    def cosine_similarity(text1: str, text2: str) -> float:
        """
        Calculate cosine similarity antara dua teks.
        """
        # Tokenize
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        # Create vocabulary
        vocab = words1.union(words2)
        
        # Create vectors
        vec1 = [1 if w in words1 else 0 for w in vocab]
        vec2 = [1 if w in words2 else 0 for w in vocab]
        
        # Calculate cosine similarity
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        mag1 = math.sqrt(sum(a * a for a in vec1))
        mag2 = math.sqrt(sum(b * b for b in vec2))
        
        if mag1 == 0 or mag2 == 0:
            return 0.0
        
        return dot_product / (mag1 * mag2)
    
    @staticmethod
    def jaccard_similarity(text1: str, text2: str) -> float:
        """
        Calculate Jaccard similarity (intersection over union).
        """
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        if union == 0:
            return 0.0
        
        return intersection / union
    
    @staticmethod
    def levenshtein_distance(s1: str, s2: str) -> int:
        """
        Calculate Levenshtein (edit) distance.
        """
        if len(s1) < len(s2):
            return TextSimilarity.levenshtein_distance(s2, s1)
        
        if len(s2) == 0:
            return len(s1)
        
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]
    
    @staticmethod
    def similarity_ratio(s1: str, s2: str) -> float:
        """
        Calculate similarity ratio (0-1) based on Levenshtein distance.
        """
        distance = TextSimilarity.levenshtein_distance(s1.lower(), s2.lower())
        max_len = max(len(s1), len(s2))
        if max_len == 0:
            return 1.0
        return 1 - (distance / max_len)


class TFIDFSearch:
    """
    TF-IDF based search untuk knowledge base.
    Lebih baik dari simple fuzzy matching untuk dokumen panjang.
    """
    
    def __init__(self):
        self.documents: Dict[str, str] = {}
        self.word_doc_count: Counter = Counter()
        self.doc_word_freq: Dict[str, Counter] = {}
        self.total_docs = 0
    
    def add_document(self, doc_id: str, content: str):
        """Add document ke index."""
        self.documents[doc_id] = content
        words = content.lower().split()
        
        # Count word frequency in document
        word_freq = Counter(words)
        self.doc_word_freq[doc_id] = word_freq
        
        # Count documents containing each word
        for word in set(words):
            self.word_doc_count[word] += 1
        
        self.total_docs += 1
    
    def _calculate_tfidf(self, word: str, doc_id: str) -> float:
        """Calculate TF-IDF score for word in document."""
        if doc_id not in self.doc_word_freq:
            return 0.0
        
        # Term Frequency
        word_freq = self.doc_word_freq[doc_id]
        tf = word_freq.get(word, 0) / sum(word_freq.values()) if word_freq else 0
        
        # Inverse Document Frequency
        doc_count = self.word_doc_count.get(word, 0)
        if doc_count == 0:
            idf = 0
        else:
            idf = math.log(self.total_docs / doc_count)
        
        return tf * idf
    
    def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """
        Search documents matching query.
        
        Returns:
            List of (doc_id, score) tuples
        """
        query_words = query.lower().split()
        scores = {}
        
        for doc_id in self.documents:
            score = 0
            for word in query_words:
                score += self._calculate_tfidf(word, doc_id)
            scores[doc_id] = score
        
        # Sort by score
        sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_docs[:top_k]


class SimpleNeuralNetwork:
    """
    Simple Neural Network implementation tanpa dependencies.
    Bisa digunakan untuk pembelajaran tentang konsep NN.
    """
    
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights randomly
        self.weights_ih = [[random.uniform(-1, 1) for _ in range(hidden_size)] 
                           for _ in range(input_size)]
        self.weights_ho = [[random.uniform(-1, 1) for _ in range(output_size)] 
                           for _ in range(hidden_size)]
        
        # Biases
        self.bias_h = [random.uniform(-1, 1) for _ in range(hidden_size)]
        self.bias_o = [random.uniform(-1, 1) for _ in range(output_size)]
        
        self.learning_rate = 0.1
    
    @staticmethod
    def sigmoid(x: float) -> float:
        """Sigmoid activation function."""
        try:
            return 1 / (1 + math.exp(-x))
        except OverflowError:
            return 0.0 if x < 0 else 1.0
    
    @staticmethod
    def sigmoid_derivative(x: float) -> float:
        """Derivative of sigmoid."""
        return x * (1 - x)
    
    def forward(self, inputs: List[float]) -> List[float]:
        """Forward pass."""
        # Hidden layer
        self.hidden = []
        for j in range(self.hidden_size):
            sum_val = self.bias_h[j]
            for i in range(self.input_size):
                sum_val += inputs[i] * self.weights_ih[i][j]
            self.hidden.append(self.sigmoid(sum_val))
        
        # Output layer
        outputs = []
        for k in range(self.output_size):
            sum_val = self.bias_o[k]
            for j in range(self.hidden_size):
                sum_val += self.hidden[j] * self.weights_ho[j][k]
            outputs.append(self.sigmoid(sum_val))
        
        return outputs
    
    def train(self, inputs: List[float], targets: List[float]):
        """Train dengan backpropagation."""
        # Forward pass
        outputs = self.forward(inputs)
        
        # Output layer error
        output_errors = [targets[k] - outputs[k] for k in range(self.output_size)]
        output_gradients = [output_errors[k] * self.sigmoid_derivative(outputs[k]) 
                           for k in range(self.output_size)]
        
        # Update weights_ho
        for j in range(self.hidden_size):
            for k in range(self.output_size):
                self.weights_ho[j][k] += self.learning_rate * output_gradients[k] * self.hidden[j]
        
        # Update bias_o
        for k in range(self.output_size):
            self.bias_o[k] += self.learning_rate * output_gradients[k]
        
        # Hidden layer error
        hidden_errors = [0] * self.hidden_size
        for j in range(self.hidden_size):
            for k in range(self.output_size):
                hidden_errors[j] += output_errors[k] * self.weights_ho[j][k]
        
        hidden_gradients = [hidden_errors[j] * self.sigmoid_derivative(self.hidden[j]) 
                           for j in range(self.hidden_size)]
        
        # Update weights_ih
        for i in range(self.input_size):
            for j in range(self.hidden_size):
                self.weights_ih[i][j] += self.learning_rate * hidden_gradients[j] * inputs[i]
        
        # Update bias_h
        for j in range(self.hidden_size):
            self.bias_h[j] += self.learning_rate * hidden_gradients[j]


class LearningSystem:
    """
    Learning system untuk WeaR AI.
    Mengumpulkan feedback dan meningkatkan respons dari waktu ke waktu.
    """
    
    def __init__(self):
        self.feedback_history: List[Dict] = []
        self.query_patterns: Counter = Counter()
        self.successful_responses: Dict[str, str] = {}
    
    def record_interaction(self, query: str, response: str, feedback: Optional[str] = None):
        """Record an interaction for learning."""
        self.query_patterns[query.lower()] += 1
        
        if feedback == 'positive':
            # Store successful response pattern
            key_words = tuple(sorted(query.lower().split()[:3]))
            self.successful_responses[key_words] = response
        
        self.feedback_history.append({
            'query': query,
            'response': response,
            'feedback': feedback
        })
    
    def get_common_queries(self, top_k: int = 10) -> List[Tuple[str, int]]:
        """Get most common queries."""
        return self.query_patterns.most_common(top_k)
    
    def suggest_response(self, query: str) -> Optional[str]:
        """Suggest response based on learned patterns."""
        key_words = tuple(sorted(query.lower().split()[:3]))
        return self.successful_responses.get(key_words)


# Singleton instances
_intent_classifier: Optional[IntentClassifier] = None
_sentiment_analyzer: Optional[SentimentAnalyzer] = None
_learning_system: Optional[LearningSystem] = None


def get_intent_classifier() -> IntentClassifier:
    """Get or create intent classifier."""
    global _intent_classifier
    if _intent_classifier is None:
        _intent_classifier = IntentClassifier()
    return _intent_classifier


def get_sentiment_analyzer() -> SentimentAnalyzer:
    """Get or create sentiment analyzer."""
    global _sentiment_analyzer
    if _sentiment_analyzer is None:
        _sentiment_analyzer = SentimentAnalyzer()
    return _sentiment_analyzer


def get_learning_system() -> LearningSystem:
    """Get or create learning system."""
    global _learning_system
    if _learning_system is None:
        _learning_system = LearningSystem()
    return _learning_system


# Demo function
def demo():
    """Demonstrate ML capabilities."""
    print("=== WeaR AI Machine Learning Demo ===\n")
    
    # Intent Classification
    print("1. Intent Classification:")
    intent_clf = get_intent_classifier()
    test_phrases = ["halo apa kabar", "apa itu python", "terima kasih banyak"]
    for phrase in test_phrases:
        intent, conf = intent_clf.classify(phrase)
        print(f"   '{phrase}' -> {intent} (confidence: {conf:.2f})")
    
    print()
    
    # Sentiment Analysis
    print("2. Sentiment Analysis:")
    sentiment = get_sentiment_analyzer()
    test_texts = [
        "Produk ini sangat bagus dan berkualitas!",
        "Pelayanan buruk, sangat mengecewakan",
        "Biasa saja, tidak ada yang spesial"
    ]
    for text in test_texts:
        result = sentiment.analyze(text)
        print(f"   '{text}'")
        print(f"   -> {result['sentiment']} (score: {result['score']})")
    
    print()
    
    # Text Similarity
    print("3. Text Similarity:")
    text1 = "machine learning adalah cabang AI"
    text2 = "AI adalah bidang yang mencakup machine learning"
    sim = TextSimilarity.cosine_similarity(text1, text2)
    print(f"   Cosine similarity: {sim:.3f}")
    
    print()
    
    # Simple Neural Network
    print("4. Neural Network (XOR Problem):")
    nn = SimpleNeuralNetwork(2, 4, 1)
    # Train on XOR
    training_data = [
        ([0, 0], [0]),
        ([0, 1], [1]),
        ([1, 0], [1]),
        ([1, 1], [0]),
    ]
    for _ in range(10000):
        for inputs, targets in training_data:
            nn.train(inputs, targets)
    
    print("   Trained XOR neural network:")
    for inputs, _ in training_data:
        output = nn.forward(inputs)
        print(f"   {inputs} -> {output[0]:.4f}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    demo()
