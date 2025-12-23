"""
WeaR AI - Advanced Neural Network Module
Neural Networks yang lebih canggih tanpa TensorFlow/PyTorch!
Created by RidTheWann

Features:
- Multi-layer Perceptron (MLP) dengan hidden layers fleksibel
- Multiple activation functions (Sigmoid, ReLU, Tanh)
- Batch training support
- Model save/load (tanpa pickle dependency)
- Text encoding untuk NLP tasks
"""

import math
import random
import json
from typing import List, Dict, Tuple, Any, Optional, Callable
from collections import Counter


class ActivationFunctions:
    """Available activation functions."""
    
    @staticmethod
    def sigmoid(x: float) -> float:
        """Sigmoid: output between 0 and 1."""
        try:
            return 1 / (1 + math.exp(-max(-500, min(500, x))))
        except OverflowError:
            return 0.0 if x < 0 else 1.0
    
    @staticmethod
    def sigmoid_derivative(x: float) -> float:
        """Derivative of sigmoid (x is already activated value)."""
        return x * (1 - x)
    
    @staticmethod
    def relu(x: float) -> float:
        """ReLU: max(0, x)."""
        return max(0, x)
    
    @staticmethod
    def relu_derivative(x: float) -> float:
        """Derivative of ReLU."""
        return 1.0 if x > 0 else 0.0
    
    @staticmethod
    def tanh(x: float) -> float:
        """Tanh: output between -1 and 1."""
        try:
            return math.tanh(max(-500, min(500, x)))
        except OverflowError:
            return -1.0 if x < 0 else 1.0
    
    @staticmethod
    def tanh_derivative(x: float) -> float:
        """Derivative of tanh (x is already activated value)."""
        return 1 - x * x
    
    @staticmethod
    def softmax(values: List[float]) -> List[float]:
        """Softmax for output layer (multi-class classification)."""
        max_val = max(values)
        exp_values = [math.exp(v - max_val) for v in values]
        sum_exp = sum(exp_values)
        return [v / sum_exp for v in exp_values]


class Layer:
    """Single neural network layer."""
    
    def __init__(self, input_size: int, output_size: int, 
                 activation: str = 'sigmoid', learning_rate: float = 0.1):
        self.input_size = input_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        
        # Xavier/Glorot initialization for better training
        limit = math.sqrt(6 / (input_size + output_size))
        self.weights = [
            [random.uniform(-limit, limit) for _ in range(output_size)]
            for _ in range(input_size)
        ]
        self.biases = [random.uniform(-0.1, 0.1) for _ in range(output_size)]
        
        # Set activation function
        if activation == 'sigmoid':
            self.activate = ActivationFunctions.sigmoid
            self.activate_derivative = ActivationFunctions.sigmoid_derivative
        elif activation == 'relu':
            self.activate = ActivationFunctions.relu
            self.activate_derivative = ActivationFunctions.relu_derivative
        elif activation == 'tanh':
            self.activate = ActivationFunctions.tanh
            self.activate_derivative = ActivationFunctions.tanh_derivative
        else:
            self.activate = ActivationFunctions.sigmoid
            self.activate_derivative = ActivationFunctions.sigmoid_derivative
        
        # Cache for backpropagation
        self.inputs: List[float] = []
        self.outputs: List[float] = []
    
    def forward(self, inputs: List[float]) -> List[float]:
        """Forward pass through this layer."""
        self.inputs = inputs
        self.outputs = []
        
        for j in range(self.output_size):
            total = self.biases[j]
            for i in range(self.input_size):
                total += inputs[i] * self.weights[i][j]
            self.outputs.append(self.activate(total))
        
        return self.outputs
    
    def backward(self, errors: List[float]) -> List[float]:
        """Backward pass - update weights and return errors for previous layer."""
        # Calculate gradients
        gradients = [
            errors[j] * self.activate_derivative(self.outputs[j])
            for j in range(self.output_size)
        ]
        
        # Calculate errors for previous layer
        prev_errors = [0.0] * self.input_size
        for i in range(self.input_size):
            for j in range(self.output_size):
                prev_errors[i] += gradients[j] * self.weights[i][j]
        
        # Update weights and biases
        for i in range(self.input_size):
            for j in range(self.output_size):
                self.weights[i][j] += self.learning_rate * gradients[j] * self.inputs[i]
        
        for j in range(self.output_size):
            self.biases[j] += self.learning_rate * gradients[j]
        
        return prev_errors


class DeepNeuralNetwork:
    """
    Deep Neural Network dengan multiple hidden layers.
    Lebih powerful dari SimpleNeuralNetwork!
    """
    
    def __init__(self, layer_sizes: List[int], activation: str = 'sigmoid', 
                 learning_rate: float = 0.1):
        """
        Create deep neural network.
        
        Args:
            layer_sizes: List of layer sizes, e.g., [2, 4, 4, 1] for:
                         2 inputs, 2 hidden layers of 4, 1 output
            activation: 'sigmoid', 'relu', or 'tanh'
            learning_rate: Learning rate for gradient descent
        """
        self.layer_sizes = layer_sizes
        self.layers: List[Layer] = []
        
        # Create layers
        for i in range(len(layer_sizes) - 1):
            layer = Layer(
                input_size=layer_sizes[i],
                output_size=layer_sizes[i + 1],
                activation=activation,
                learning_rate=learning_rate
            )
            self.layers.append(layer)
        
        self.training_history: List[float] = []
    
    def forward(self, inputs: List[float]) -> List[float]:
        """Forward pass through all layers."""
        current = inputs
        for layer in self.layers:
            current = layer.forward(current)
        return current
    
    def train_single(self, inputs: List[float], targets: List[float]) -> float:
        """Train on single example, returns error."""
        # Forward pass
        outputs = self.forward(inputs)
        
        # Calculate output errors
        errors = [targets[i] - outputs[i] for i in range(len(targets))]
        
        # Backward pass through all layers (reversed)
        current_errors = errors
        for layer in reversed(self.layers):
            current_errors = layer.backward(current_errors)
        
        # Calculate MSE
        mse = sum(e * e for e in errors) / len(errors)
        return mse
    
    def train(self, X: List[List[float]], y: List[List[float]], 
              epochs: int = 1000, verbose: bool = False) -> List[float]:
        """
        Train on dataset.
        
        Args:
            X: List of input vectors
            y: List of target vectors
            epochs: Number of training epochs
            verbose: Print progress
        
        Returns:
            List of losses per epoch
        """
        losses = []
        
        for epoch in range(epochs):
            epoch_loss = 0
            
            # Shuffle training data
            indices = list(range(len(X)))
            random.shuffle(indices)
            
            for idx in indices:
                loss = self.train_single(X[idx], y[idx])
                epoch_loss += loss
            
            avg_loss = epoch_loss / len(X)
            losses.append(avg_loss)
            self.training_history.append(avg_loss)
            
            if verbose and (epoch + 1) % (epochs // 10) == 0:
                print(f"Epoch {epoch + 1}/{epochs}, Loss: {avg_loss:.6f}")
        
        return losses
    
    def predict(self, inputs: List[float]) -> List[float]:
        """Predict output for given inputs."""
        return self.forward(inputs)
    
    def predict_class(self, inputs: List[float]) -> int:
        """Predict class index (for classification)."""
        outputs = self.forward(inputs)
        return outputs.index(max(outputs))
    
    def save(self, filepath: str):
        """Save model to JSON file."""
        model_data = {
            'layer_sizes': self.layer_sizes,
            'layers': []
        }
        
        for layer in self.layers:
            layer_data = {
                'weights': layer.weights,
                'biases': layer.biases,
                'learning_rate': layer.learning_rate
            }
            model_data['layers'].append(layer_data)
        
        with open(filepath, 'w') as f:
            json.dump(model_data, f)
    
    def load(self, filepath: str):
        """Load model from JSON file."""
        with open(filepath, 'r') as f:
            model_data = json.load(f)
        
        self.layer_sizes = model_data['layer_sizes']
        
        for i, layer_data in enumerate(model_data['layers']):
            self.layers[i].weights = layer_data['weights']
            self.layers[i].biases = layer_data['biases']
            self.layers[i].learning_rate = layer_data['learning_rate']


class TextEncoder:
    """
    Encode text untuk neural network input.
    Bag of Words + TF-IDF style encoding.
    """
    
    def __init__(self, max_features: int = 100):
        self.max_features = max_features
        self.vocabulary: Dict[str, int] = {}
        self.idf: Dict[str, float] = {}
        self.fitted = False
    
    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization."""
        import re
        text = text.lower()
        words = re.findall(r'\b\w+\b', text)
        return words
    
    def fit(self, documents: List[str]):
        """Build vocabulary from documents."""
        # Count word frequencies across all documents
        word_doc_count: Counter = Counter()
        word_total_count: Counter = Counter()
        
        for doc in documents:
            words = set(self._tokenize(doc))
            word_doc_count.update(words)
            word_total_count.update(self._tokenize(doc))
        
        # Get top words by frequency
        top_words = word_total_count.most_common(self.max_features)
        
        # Create vocabulary mapping
        self.vocabulary = {word: idx for idx, (word, _) in enumerate(top_words)}
        
        # Calculate IDF
        n_docs = len(documents)
        for word, count in word_doc_count.items():
            if word in self.vocabulary:
                self.idf[word] = math.log(n_docs / (1 + count))
        
        self.fitted = True
    
    def encode(self, text: str) -> List[float]:
        """Encode single text to vector."""
        if not self.fitted:
            raise ValueError("TextEncoder not fitted. Call fit() first.")
        
        words = self._tokenize(text)
        word_count = Counter(words)
        
        vector = [0.0] * len(self.vocabulary)
        
        for word, count in word_count.items():
            if word in self.vocabulary:
                idx = self.vocabulary[word]
                # TF-IDF score
                tf = count / len(words) if words else 0
                idf = self.idf.get(word, 0)
                vector[idx] = tf * idf
        
        # Normalize
        magnitude = math.sqrt(sum(v * v for v in vector))
        if magnitude > 0:
            vector = [v / magnitude for v in vector]
        
        return vector
    
    def encode_batch(self, texts: List[str]) -> List[List[float]]:
        """Encode multiple texts."""
        return [self.encode(text) for text in texts]


class NeuralTextClassifier:
    """
    Neural Network based text classifier.
    Combines TextEncoder + DeepNeuralNetwork.
    """
    
    def __init__(self, hidden_sizes: List[int] = [64, 32], 
                 max_features: int = 100, learning_rate: float = 0.1):
        self.encoder = TextEncoder(max_features=max_features)
        self.hidden_sizes = hidden_sizes
        self.learning_rate = learning_rate
        self.network: Optional[DeepNeuralNetwork] = None
        self.label_to_idx: Dict[str, int] = {}
        self.idx_to_label: Dict[int, str] = {}
    
    def fit(self, texts: List[str], labels: List[str], epochs: int = 100, verbose: bool = False):
        """
        Train the classifier.
        
        Args:
            texts: List of training texts
            labels: List of labels
            epochs: Training epochs
            verbose: Print progress
        """
        # Fit encoder
        self.encoder.fit(texts)
        
        # Create label mappings
        unique_labels = list(set(labels))
        self.label_to_idx = {label: idx for idx, label in enumerate(unique_labels)}
        self.idx_to_label = {idx: label for label, idx in self.label_to_idx.items()}
        
        # Encode texts
        X = self.encoder.encode_batch(texts)
        
        # One-hot encode labels
        n_classes = len(unique_labels)
        y = []
        for label in labels:
            one_hot = [0.0] * n_classes
            one_hot[self.label_to_idx[label]] = 1.0
            y.append(one_hot)
        
        # Create network
        input_size = len(self.encoder.vocabulary)
        layer_sizes = [input_size] + self.hidden_sizes + [n_classes]
        self.network = DeepNeuralNetwork(
            layer_sizes=layer_sizes,
            activation='sigmoid',
            learning_rate=self.learning_rate
        )
        
        # Train
        if verbose:
            print(f"Training with {len(texts)} samples, {n_classes} classes")
            print(f"Network architecture: {layer_sizes}")
        
        self.network.train(X, y, epochs=epochs, verbose=verbose)
    
    def predict(self, text: str) -> Tuple[str, float]:
        """
        Predict label for text.
        
        Returns:
            Tuple of (predicted_label, confidence)
        """
        if self.network is None:
            raise ValueError("Model not trained. Call fit() first.")
        
        # Encode text
        x = self.encoder.encode(text)
        
        # Predict
        outputs = self.network.predict(x)
        
        # Get best class
        best_idx = outputs.index(max(outputs))
        confidence = outputs[best_idx]
        
        return self.idx_to_label[best_idx], confidence
    
    def predict_proba(self, text: str) -> Dict[str, float]:
        """Get probabilities for all classes."""
        if self.network is None:
            raise ValueError("Model not trained. Call fit() first.")
        
        x = self.encoder.encode(text)
        outputs = self.network.predict(x)
        
        # Apply softmax for proper probabilities
        probs = ActivationFunctions.softmax(outputs)
        
        return {self.idx_to_label[i]: probs[i] for i in range(len(probs))}


class SmartQueryClassifier:
    """
    Classifier khusus untuk WeaR AI - classify user queries.
    Pre-trained dengan berbagai jenis query.
    """
    
    def __init__(self):
        self.classifier = NeuralTextClassifier(
            hidden_sizes=[32, 16],
            max_features=50,
            learning_rate=0.2
        )
        self._train_default()
    
    def _train_default(self):
        """Train dengan default query patterns."""
        # Training data
        training_data = [
            # Technical questions
            ("apa itu python", "tech_question"),
            ("bagaimana cara coding", "tech_question"),
            ("what is javascript", "tech_question"),
            ("how to use docker", "tech_question"),
            ("explain machine learning", "tech_question"),
            ("apa itu database", "tech_question"),
            ("cara membuat website", "tech_question"),
            ("tutorial programming", "tech_question"),
            
            # General knowledge
            ("siapa presiden indonesia", "general_knowledge"),
            ("berapa populasi dunia", "general_knowledge"),
            ("dimana lokasi", "general_knowledge"),
            ("sejarah indonesia", "general_knowledge"),
            ("what is the capital", "general_knowledge"),
            ("who invented", "general_knowledge"),
            
            # Greeting
            ("halo", "greeting"),
            ("hai", "greeting"),
            ("hello", "greeting"),
            ("selamat pagi", "greeting"),
            ("good morning", "greeting"),
            ("hi there", "greeting"),
            
            # Help request
            ("tolong bantu", "help"),
            ("saya bingung", "help"),
            ("help me", "help"),
            ("bantuan", "help"),
            ("tidak mengerti", "help"),
            
            # Opinion/Recommendation
            ("rekomendasi", "recommendation"),
            ("saran", "recommendation"),
            ("yang terbaik", "recommendation"),
            ("recommend", "recommendation"),
            ("what should i", "recommendation"),
            
            # Comparison
            ("perbedaan", "comparison"),
            ("bedanya apa", "comparison"),
            ("vs", "comparison"),
            ("compare", "comparison"),
            ("difference between", "comparison"),
            
            # Definition
            ("definisi", "definition"),
            ("pengertian", "definition"),
            ("artinya apa", "definition"),
            ("meaning of", "definition"),
            ("define", "definition"),
            
            # How-to
            ("cara", "howto"),
            ("bagaimana", "howto"),
            ("langkah", "howto"),
            ("how to", "howto"),
            ("tutorial", "howto"),
            ("step by step", "howto"),
        ]
        
        texts = [t[0] for t in training_data]
        labels = [t[1] for t in training_data]
        
        self.classifier.fit(texts, labels, epochs=500, verbose=False)
    
    def classify(self, query: str) -> Tuple[str, float]:
        """Classify user query."""
        return self.classifier.predict(query)
    
    def get_all_probabilities(self, query: str) -> Dict[str, float]:
        """Get probabilities for all categories."""
        return self.classifier.predict_proba(query)


# Singleton instance
_smart_classifier: Optional[SmartQueryClassifier] = None

def get_smart_classifier() -> SmartQueryClassifier:
    """Get or create smart query classifier."""
    global _smart_classifier
    if _smart_classifier is None:
        _smart_classifier = SmartQueryClassifier()
    return _smart_classifier


def demo_advanced():
    """Demonstrate advanced neural network features."""
    print("=== WeaR AI Advanced Neural Network Demo ===\n")
    
    # 1. Deep Neural Network - more complex XOR with hidden layers
    print("1. Deep Neural Network (Multiple Hidden Layers):")
    dnn = DeepNeuralNetwork([2, 8, 8, 1], activation='sigmoid', learning_rate=0.5)
    
    # XOR training data
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [[0], [1], [1], [0]]
    
    print("   Training on XOR problem...")
    losses = dnn.train(X, y, epochs=5000, verbose=False)
    print(f"   Final loss: {losses[-1]:.6f}")
    
    print("   Predictions:")
    for inputs in X:
        output = dnn.predict(inputs)
        print(f"   {inputs} -> {output[0]:.4f}")
    
    print()
    
    # 2. Neural Text Classifier
    print("2. Neural Text Classifier:")
    clf = NeuralTextClassifier(hidden_sizes=[32, 16], max_features=30)
    
    # Training data
    texts = [
        "python programming language",
        "java code development",
        "javascript web frontend",
        "database sql query",
        "machine learning model",
        "selamat pagi semua",
        "halo apa kabar",
        "terima kasih banyak",
        "sampai jumpa lagi",
    ]
    labels = [
        "tech", "tech", "tech", "tech", "tech",
        "greeting", "greeting", "greeting", "goodbye"
    ]
    
    clf.fit(texts, labels, epochs=1000, verbose=False)
    
    test_texts = ["belajar python coding", "halo semuanya", "bye bye"]
    for text in test_texts:
        pred, conf = clf.predict(text)
        print(f"   '{text}' -> {pred} (confidence: {conf:.2f})")
    
    print()
    
    # 3. Smart Query Classifier
    print("3. Smart Query Classifier (Pre-trained for WeaR AI):")
    smart_clf = get_smart_classifier()
    
    test_queries = [
        "apa itu react js",
        "halo selamat malam",
        "tolong bantu saya",
        "perbedaan python dan java",
        "bagaimana cara install node"
    ]
    
    for query in test_queries:
        category, conf = smart_clf.classify(query)
        print(f"   '{query}'")
        print(f"   -> Category: {category} (confidence: {conf:.2f})")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    demo_advanced()
