"""
WeaR AI - Deep Learning Training Script
Latih semua model deep learning untuk performa yang lebih baik.
Created by RidTheWann
"""

import sys
import time

def train_all_models():
    """Train all deep learning models."""
    print("=" * 60)
    print("🧠 WeaR AI Deep Learning Training")
    print("=" * 60)
    print()
    
    # 1. Train Neural Text Classifier
    print("📚 1. Training Neural Text Classifier...")
    print("-" * 40)
    
    from app.core.neural_network import NeuralTextClassifier
    
    text_clf = NeuralTextClassifier(hidden_sizes=[64, 32], max_features=50, learning_rate=0.1)
    
    # Extended training data
    training_texts = [
        # Tech
        "python programming language code",
        "javascript web development frontend",
        "java backend server application",
        "html css website design",
        "database sql query optimization",
        "machine learning artificial intelligence",
        "docker kubernetes container",
        "git version control",
        "api rest endpoint",
        "react angular vue framework",
        
        # Greeting
        "halo selamat pagi",
        "hello good morning",
        "hai apa kabar",
        "hi there how are you",
        "selamat siang semua",
        "good afternoon everyone",
        
        # Question
        "apa itu programming",
        "bagaimana cara coding",
        "what is machine learning",
        "how to build website",
        "mengapa error terjadi",
        
        # Help
        "tolong bantu saya",
        "saya butuh bantuan",
        "help me please",
        "i need assistance",
        "bingung tidak mengerti",
    ]
    
    training_labels = [
        "tech", "tech", "tech", "tech", "tech", "tech", "tech", "tech", "tech", "tech",
        "greeting", "greeting", "greeting", "greeting", "greeting", "greeting",
        "question", "question", "question", "question", "question",
        "help", "help", "help", "help", "help",
    ]
    
    text_clf.fit(training_texts, training_labels, epochs=500, verbose=True)
    
    # Test
    test_cases = [
        "apa itu react js",
        "halo semuanya",
        "tolong saya bingung"
    ]
    print("\n🧪 Testing Neural Text Classifier:")
    for text in test_cases:
        pred, conf = text_clf.predict(text)
        print(f"   '{text}' -> {pred} ({conf:.2%})")
    
    print()
    
    # 2. Train Deep Neural Network
    print("🔮 2. Training Deep Neural Network...")
    print("-" * 40)
    
    from app.core.deep_learning import DeepNeuralNetwork
    
    # Train on XOR problem with deeper network
    dnn = DeepNeuralNetwork([2, 16, 16, 8, 1], activation='sigmoid', learning_rate=0.5)
    
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [[0], [1], [1], [0]]
    
    losses = dnn.train(X, y, epochs=5000, verbose=True)
    
    print("\n🧪 Testing Deep Neural Network (XOR):")
    for inputs in X:
        output = dnn.predict(inputs)
        expected = 0 if inputs[0] == inputs[1] else 1
        correct = "✅" if round(output[0]) == expected else "❌"
        print(f"   {inputs} -> {output[0]:.4f} (expected: {expected}) {correct}")
    
    print()
    
    # 3. Train CNN for pattern recognition
    print("🖼️ 3. Training CNN for Pattern Recognition...")
    print("-" * 40)
    
    from app.core.computer_vision import create_test_image, ImageClassifier
    
    # Create more training data
    train_images = []
    train_labels = []
    
    patterns = ["horizontal_lines", "vertical_lines", "circle", "square", "diagonal"]
    for pattern in patterns:
        for _ in range(5):  # 5 samples each
            train_images.append(create_test_image(pattern))
            train_labels.append(pattern)
    
    img_clf = ImageClassifier(k=5)
    img_clf.train(train_images, train_labels)
    
    print(f"   Trained with {len(train_images)} images, {len(set(train_labels))} classes")
    
    print("\n🧪 Testing Image Classifier:")
    for pattern in patterns:
        test_img = create_test_image(pattern)
        pred, conf = img_clf.predict(test_img)
        correct = "✅" if pred == pattern else "❌"
        print(f"   {pattern} -> {pred} ({conf:.2%}) {correct}")
    
    print()
    
    # 4. Train Audio Classifier
    print("🎵 4. Training Audio Classifier...")
    print("-" * 40)
    
    from app.core.audio_processing import create_test_signal, AudioClassifier
    
    train_signals = []
    audio_labels = []
    
    audio_types = [("sine", "tone"), ("square", "harsh"), ("noise", "noise"), ("chirp", "sweep")]
    for sig_type, label in audio_types:
        for _ in range(5):
            train_signals.append(create_test_signal(sig_type))
            audio_labels.append(label)
    
    audio_clf = AudioClassifier(k=5)
    audio_clf.train(train_signals, audio_labels)
    
    print(f"   Trained with {len(train_signals)} audio samples")
    
    print("\n🧪 Testing Audio Classifier:")
    for sig_type, expected_label in audio_types:
        test_sig = create_test_signal(sig_type)
        pred, conf = audio_clf.predict(test_sig)
        correct = "✅" if pred == expected_label else "❌"
        print(f"   {sig_type} -> {pred} ({conf:.2%}) {correct}")
    
    print()
    
    # 5. Train Smart Query Classifier
    print("💡 5. Training Smart Query Classifier...")
    print("-" * 40)
    
    from app.core.neural_network import get_smart_classifier
    smart_clf = get_smart_classifier()
    
    test_queries = [
        ("apa itu javascript", "tech_question"),
        ("halo selamat malam", "greeting"),
        ("bagaimana cara install", "howto"),
        ("perbedaan react dan vue", "comparison"),
        ("tolong bantu saya", "help"),
    ]
    
    print("🧪 Testing Smart Query Classifier:")
    correct_count = 0
    for query, expected in test_queries:
        pred, conf = smart_clf.classify(query)
        correct = "✅" if pred == expected else "❌"
        if pred == expected:
            correct_count += 1
        print(f"   '{query}' -> {pred} ({conf:.2%}) {correct}")
    
    accuracy = correct_count / len(test_queries)
    print(f"\n   Accuracy: {accuracy:.2%}")
    
    print()
    print("=" * 60)
    print("🎉 ALL DEEP LEARNING TRAINING COMPLETED!")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    try:
        train_all_models()
    except KeyboardInterrupt:
        print("\n\n⚠️ Training interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error during training: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
