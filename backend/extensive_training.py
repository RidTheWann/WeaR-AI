"""
WeaR AI - Extensive Brain Training
Latih semua neural network dengan data lebih banyak dan epochs lebih tinggi!
"""

import time
start = time.time()

print('=' * 60)
print('🧠 WeaR AI EXTENSIVE BRAIN TRAINING')
print('=' * 60)
print()

# ============================================
# 1. DEEP NEURAL NETWORK - XOR (More epochs)
# ============================================
print('🔮 1. Deep Neural Network Training (10,000 epochs)')
print('-' * 50)

from app.core.neural_network import DeepNeuralNetwork

# Deeper network with more layers
dnn = DeepNeuralNetwork([2, 32, 32, 16, 1], activation='sigmoid', learning_rate=0.8)
X = [[0,0], [0,1], [1,0], [1,1]]
y = [[0], [1], [1], [0]]

losses = dnn.train(X, y, epochs=10000, verbose=True)

print()
print('XOR Test Results:')
correct = 0
for inputs in X:
    out = dnn.predict(inputs)
    expected = 0 if inputs[0] == inputs[1] else 1
    is_correct = abs(out[0] - expected) < 0.5
    correct += 1 if is_correct else 0
    mark = '✅' if is_correct else '❌'
    print(f'  {inputs} -> {out[0]:.4f} (expected {expected}) {mark}')
print(f'  Accuracy: {correct}/4 = {correct*25}%')

# ============================================
# 2. NEURAL TEXT CLASSIFIER (More data)
# ============================================
print()
print('📚 2. Neural Text Classifier Training (Extended Data)')
print('-' * 50)

from app.core.neural_network import NeuralTextClassifier

clf = NeuralTextClassifier(hidden_sizes=[128, 64, 32], max_features=100, learning_rate=0.15)

# Extended training data - 60+ samples
texts = [
    # Tech (20)
    'python programming language', 'javascript web development',
    'java backend server', 'react frontend framework',
    'nodejs runtime environment', 'docker container virtualization',
    'kubernetes orchestration', 'machine learning ai',
    'deep learning neural network', 'database sql query',
    'api rest endpoint', 'git version control',
    'linux operating system', 'cloud computing aws',
    'html css styling', 'typescript static typing',
    'golang concurrent programming', 'rust memory safety',
    'devops cicd pipeline', 'microservices architecture',
    
    # Greeting (15)
    'halo selamat pagi', 'hello good morning',
    'hai apa kabar', 'hi there friend',
    'selamat siang', 'good afternoon',
    'selamat malam', 'good evening',
    'hey whats up', 'yo wassup',
    'halo semua', 'hello everyone',
    'salam sejahtera', 'greetings friend',
    'assalamualaikum',
    
    # Question (15)
    'apa itu python', 'what is programming',
    'bagaimana cara coding', 'how to learn',
    'mengapa error terjadi', 'why this happens',
    'kapan mulai belajar', 'when to start',
    'dimana bisa belajar', 'where to learn',
    'siapa yang membuat', 'who created this',
    'berapa biaya', 'how much cost',
    'yang mana terbaik',
    
    # Help (10)
    'tolong bantu saya', 'please help me',
    'saya butuh bantuan', 'i need assistance',
    'bingung tidak mengerti', 'confused help',
    'ada masalah', 'having problem',
    'error tidak bisa', 'stuck need help',
]

labels = (
    ['tech'] * 20 +
    ['greeting'] * 15 +
    ['question'] * 15 +
    ['help'] * 10
)

print(f'Training with {len(texts)} samples, 4 classes')
clf.fit(texts, labels, epochs=1000, verbose=True)

print()
print('Testing:')
test_cases = [
    ('belajar react typescript', 'tech'),
    ('halo selamat pagi semua', 'greeting'),
    ('apa itu machine learning', 'question'),
    ('tolong saya bingung sekali', 'help'),
]
correct = 0
for text, expected in test_cases:
    pred, conf = clf.predict(text)
    is_correct = pred == expected
    correct += 1 if is_correct else 0
    mark = '✅' if is_correct else '❌'
    print(f'  "{text}" -> {pred} ({conf:.0%}) {mark}')
print(f'  Accuracy: {correct}/{len(test_cases)} = {correct*25}%')

# ============================================
# 3. SMART QUERY CLASSIFIER
# ============================================
print()
print('💡 3. Smart Query Classifier')
print('-' * 50)

from app.core.neural_network import SmartQueryClassifier

smart = SmartQueryClassifier()  # Pre-trained

test_queries = [
    ('apa itu javascript framework', 'tech_question'),
    ('halo selamat sore', 'greeting'),
    ('bagaimana cara install docker', 'howto'),
    ('perbedaan react dan angular', 'comparison'),
    ('tolong bantu install', 'help'),
    ('rekomendasi laptop programming', 'recommendation'),
]

print('Testing pre-trained classifier:')
correct = 0
for query, expected in test_queries:
    pred, conf = smart.classify(query)
    is_correct = pred == expected
    correct += 1 if is_correct else 0
    mark = '✅' if is_correct else '❌'
    print(f'  "{query}" -> {pred} ({conf:.0%}) {mark}')
accuracy = correct / len(test_queries)
print(f'  Accuracy: {correct}/{len(test_queries)} = {accuracy:.0%}')

# ============================================
# 4. IMAGE CLASSIFIER (Extended)
# ============================================
print()
print('🖼️ 4. Image Pattern Classifier (Extended Training)')
print('-' * 50)

from app.core.computer_vision import create_test_image, ImageClassifier

patterns = ['horizontal_lines', 'vertical_lines', 'circle', 'square', 'diagonal']
train_images = []
train_labels = []

for pattern in patterns:
    for _ in range(10):  # 10 samples each
        train_images.append(create_test_image(pattern))
        train_labels.append(pattern)

img_clf = ImageClassifier(k=5)
img_clf.train(train_images, train_labels)

print(f'Trained with {len(train_images)} images')
print('Testing:')
correct = 0
for pattern in patterns:
    test_img = create_test_image(pattern)
    pred, conf = img_clf.predict(test_img)
    is_correct = pred == pattern
    correct += 1 if is_correct else 0
    mark = '✅' if is_correct else '❌'
    print(f'  {pattern} -> {pred} ({conf:.0%}) {mark}')
accuracy = correct / len(patterns)
print(f'  Accuracy: {correct}/{len(patterns)} = {accuracy:.0%}')

# ============================================
# 5. AUDIO CLASSIFIER (Extended)
# ============================================
print()
print('🎵 5. Audio Pattern Classifier (Extended Training)')
print('-' * 50)

from app.core.audio_processing import create_test_signal, AudioClassifier

audio_types = [('sine', 'tone'), ('square', 'harsh'), ('noise', 'noise'), ('chirp', 'sweep')]
train_signals = []
audio_labels = []

for sig_type, label in audio_types:
    for _ in range(10):  # 10 samples each
        train_signals.append(create_test_signal(sig_type))
        audio_labels.append(label)

audio_clf = AudioClassifier(k=5)
audio_clf.train(train_signals, audio_labels)

print(f'Trained with {len(train_signals)} audio samples')
print('Testing:')
correct = 0
for sig_type, expected in audio_types:
    test_sig = create_test_signal(sig_type)
    pred, conf = audio_clf.predict(test_sig)
    is_correct = pred == expected
    correct += 1 if is_correct else 0
    mark = '✅' if is_correct else '❌'
    print(f'  {sig_type} -> {pred} ({conf:.0%}) {mark}')
accuracy = correct / len(audio_types)
print(f'  Accuracy: {correct}/{len(audio_types)} = {accuracy:.0%}')

# ============================================
# SUMMARY
# ============================================
print()
print('=' * 60)
elapsed = time.time() - start
print(f'🎉 TRAINING COMPLETE! (Total time: {elapsed:.1f}s)')
print('=' * 60)
