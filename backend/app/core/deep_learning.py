"""
WeaR AI - Advanced Deep Learning Module
Deep Learning dengan arsitektur canggih tanpa TensorFlow/PyTorch!
Created by RidTheWann

Fitur:
- Convolutional Neural Network (CNN) untuk image-like data
- Recurrent Neural Network (RNN) untuk sequential data
- Long Short-Term Memory (LSTM) untuk time series
- Autoencoder untuk feature learning
- Batch Normalization
- Dropout Regularization
- Adam Optimizer
"""

import math
import random
from typing import List, Dict, Tuple, Any, Optional, Callable
from collections import deque
import json


class AdamOptimizer:
    """
    Adam Optimizer - lebih baik dari SGD biasa.
    Adaptive learning rate berdasarkan first dan second moments.
    """
    
    def __init__(self, learning_rate: float = 0.001, beta1: float = 0.9, 
                 beta2: float = 0.999, epsilon: float = 1e-8):
        self.lr = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.t = 0
        
        # First and second moment estimates
        self.m: Dict[str, List] = {}
        self.v: Dict[str, List] = {}
    
    def step(self, param_id: str, gradients: List[float], params: List[float]) -> List[float]:
        """Update parameters using Adam."""
        self.t += 1
        
        # Initialize moments if first time
        if param_id not in self.m:
            self.m[param_id] = [0.0] * len(gradients)
            self.v[param_id] = [0.0] * len(gradients)
        
        updated = []
        for i, (g, p) in enumerate(zip(gradients, params)):
            # Update biased first moment estimate
            self.m[param_id][i] = self.beta1 * self.m[param_id][i] + (1 - self.beta1) * g
            
            # Update biased second moment estimate
            self.v[param_id][i] = self.beta2 * self.v[param_id][i] + (1 - self.beta2) * g * g
            
            # Bias correction
            m_hat = self.m[param_id][i] / (1 - self.beta1 ** self.t)
            v_hat = self.v[param_id][i] / (1 - self.beta2 ** self.t)
            
            # Update parameter
            new_p = p + self.lr * m_hat / (math.sqrt(v_hat) + self.epsilon)
            updated.append(new_p)
        
        return updated


class BatchNorm:
    """
    Batch Normalization untuk stabilisasi training.
    """
    
    def __init__(self, size: int, momentum: float = 0.1, epsilon: float = 1e-5):
        self.size = size
        self.momentum = momentum
        self.epsilon = epsilon
        
        # Learnable parameters
        self.gamma = [1.0] * size  # Scale
        self.beta = [0.0] * size   # Shift
        
        # Running statistics for inference
        self.running_mean = [0.0] * size
        self.running_var = [1.0] * size
        
        # Cache for backward pass
        self.cache: Dict = {}
    
    def forward(self, x: List[float], training: bool = True) -> List[float]:
        """Forward pass."""
        if training:
            # Calculate batch statistics (for single sample, use sample stats)
            mean = sum(x) / len(x) if x else 0
            var = sum((xi - mean) ** 2 for xi in x) / len(x) if x else 1
            
            # Normalize
            x_norm = [(xi - mean) / math.sqrt(var + self.epsilon) for xi in x]
            
            # Scale and shift
            out = [self.gamma[i % self.size] * x_norm[i] + self.beta[i % self.size] 
                   for i in range(len(x))]
            
            # Update running stats
            for i in range(min(len(x), self.size)):
                self.running_mean[i] = (1 - self.momentum) * self.running_mean[i] + self.momentum * mean
                self.running_var[i] = (1 - self.momentum) * self.running_var[i] + self.momentum * var
            
            # Cache for backward
            self.cache = {'x': x, 'x_norm': x_norm, 'mean': mean, 'var': var}
            
            return out
        else:
            # Use running statistics for inference
            mean = sum(self.running_mean) / len(self.running_mean)
            var = sum(self.running_var) / len(self.running_var)
            x_norm = [(xi - mean) / math.sqrt(var + self.epsilon) for xi in x]
            return [self.gamma[i % self.size] * x_norm[i] + self.beta[i % self.size] 
                    for i in range(len(x))]


class Dropout:
    """
    Dropout untuk regularization - mencegah overfitting.
    """
    
    def __init__(self, rate: float = 0.5):
        self.rate = rate
        self.mask: List[float] = []
    
    def forward(self, x: List[float], training: bool = True) -> List[float]:
        """Forward pass."""
        if training and self.rate > 0:
            # Create dropout mask
            self.mask = [1.0 if random.random() > self.rate else 0.0 for _ in x]
            # Scale to maintain expected value
            scale = 1.0 / (1.0 - self.rate)
            return [xi * m * scale for xi, m in zip(x, self.mask)]
        return x
    
    def backward(self, grad: List[float]) -> List[float]:
        """Backward pass - apply same mask."""
        scale = 1.0 / (1.0 - self.rate) if self.rate < 1 else 0
        return [g * m * scale for g, m in zip(grad, self.mask)]


class ConvLayer:
    """
    Convolutional Layer untuk feature extraction dari data 2D (images).
    Simplified 1D convolution untuk demo.
    """
    
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int = 3,
                 stride: int = 1, padding: int = 0):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        
        # Initialize kernels (filters)
        limit = math.sqrt(6 / (in_channels * kernel_size))
        self.kernels = [
            [[random.uniform(-limit, limit) for _ in range(kernel_size)]
             for _ in range(in_channels)]
            for _ in range(out_channels)
        ]
        self.biases = [random.uniform(-0.1, 0.1) for _ in range(out_channels)]
        
        self.cache: Dict = {}
    
    def forward(self, x: List[List[float]]) -> List[List[float]]:
        """
        Forward pass.
        x: [in_channels][width]
        returns: [out_channels][output_width]
        """
        # Add padding
        if self.padding > 0:
            x = [[0.0] * self.padding + channel + [0.0] * self.padding for channel in x]
        
        self.cache['input'] = x
        
        # Calculate output size
        input_width = len(x[0]) if x else 0
        output_width = (input_width - self.kernel_size) // self.stride + 1
        
        # Perform convolution
        output = []
        for k in range(self.out_channels):
            channel_output = []
            for i in range(0, input_width - self.kernel_size + 1, self.stride):
                # Convolution at position i
                conv_sum = self.biases[k]
                for c in range(self.in_channels):
                    for j in range(self.kernel_size):
                        conv_sum += x[c][i + j] * self.kernels[k][c][j]
                channel_output.append(conv_sum)
            output.append(channel_output)
        
        return output
    
    def relu(self, x: List[List[float]]) -> List[List[float]]:
        """Apply ReLU activation."""
        return [[max(0, val) for val in channel] for channel in x]


class MaxPool:
    """
    Max Pooling layer untuk downsampling.
    """
    
    def __init__(self, pool_size: int = 2, stride: int = 2):
        self.pool_size = pool_size
        self.stride = stride
        self.cache: Dict = {}
    
    def forward(self, x: List[List[float]]) -> List[List[float]]:
        """Forward pass."""
        self.cache['input'] = x
        output = []
        
        for channel in x:
            channel_output = []
            i = 0
            while i + self.pool_size <= len(channel):
                pool_region = channel[i:i + self.pool_size]
                channel_output.append(max(pool_region))
                i += self.stride
            output.append(channel_output)
        
        return output


class RNNCell:
    """
    Basic RNN Cell untuk sequential data.
    h_t = tanh(W_hh * h_{t-1} + W_xh * x_t + b)
    """
    
    def __init__(self, input_size: int, hidden_size: int):
        self.input_size = input_size
        self.hidden_size = hidden_size
        
        # Weight initialization
        limit_h = math.sqrt(6 / (hidden_size + hidden_size))
        limit_x = math.sqrt(6 / (input_size + hidden_size))
        
        # Hidden-to-hidden weights
        self.W_hh = [[random.uniform(-limit_h, limit_h) for _ in range(hidden_size)]
                     for _ in range(hidden_size)]
        
        # Input-to-hidden weights
        self.W_xh = [[random.uniform(-limit_x, limit_x) for _ in range(hidden_size)]
                     for _ in range(input_size)]
        
        # Bias
        self.b_h = [0.0] * hidden_size
    
    def forward(self, x: List[float], h_prev: List[float]) -> List[float]:
        """
        Forward pass for one timestep.
        x: [input_size]
        h_prev: [hidden_size]
        returns: h_new [hidden_size]
        """
        h_new = []
        for i in range(self.hidden_size):
            # W_hh * h_prev
            hh_sum = sum(self.W_hh[j][i] * h_prev[j] for j in range(self.hidden_size))
            
            # W_xh * x
            xh_sum = sum(self.W_xh[j][i] * x[j] for j in range(self.input_size))
            
            # Tanh activation
            val = hh_sum + xh_sum + self.b_h[i]
            h_new.append(math.tanh(max(-500, min(500, val))))
        
        return h_new


class LSTMCell:
    """
    LSTM Cell - better than RNN untuk long-term dependencies.
    Includes forget gate, input gate, output gate.
    """
    
    def __init__(self, input_size: int, hidden_size: int):
        self.input_size = input_size
        self.hidden_size = hidden_size
        
        # Combined input size (x + h concatenated)
        combined_size = input_size + hidden_size
        
        # Initialize weights for all gates
        limit = math.sqrt(6 / (combined_size + hidden_size))
        
        def init_weights():
            return [[random.uniform(-limit, limit) for _ in range(hidden_size)]
                    for _ in range(combined_size)]
        
        # Forget gate
        self.W_f = init_weights()
        self.b_f = [1.0] * hidden_size  # Bias towards remembering
        
        # Input gate
        self.W_i = init_weights()
        self.b_i = [0.0] * hidden_size
        
        # Candidate values
        self.W_c = init_weights()
        self.b_c = [0.0] * hidden_size
        
        # Output gate
        self.W_o = init_weights()
        self.b_o = [0.0] * hidden_size
    
    @staticmethod
    def sigmoid(x: float) -> float:
        try:
            return 1 / (1 + math.exp(-max(-500, min(500, x))))
        except OverflowError:
            return 0.0 if x < 0 else 1.0
    
    def forward(self, x: List[float], h_prev: List[float], 
                c_prev: List[float]) -> Tuple[List[float], List[float]]:
        """
        Forward pass for one timestep.
        Returns: (h_new, c_new)
        """
        # Concatenate x and h_prev
        combined = x + h_prev
        
        h_new = []
        c_new = []
        
        for i in range(self.hidden_size):
            # Forget gate
            f_sum = sum(self.W_f[j][i] * combined[j] for j in range(len(combined))) + self.b_f[i]
            f = self.sigmoid(f_sum)
            
            # Input gate
            i_sum = sum(self.W_i[j][i] * combined[j] for j in range(len(combined))) + self.b_i[i]
            i_gate = self.sigmoid(i_sum)
            
            # Candidate value
            c_sum = sum(self.W_c[j][i] * combined[j] for j in range(len(combined))) + self.b_c[i]
            c_tilde = math.tanh(max(-500, min(500, c_sum)))
            
            # New cell state
            new_c = f * c_prev[i] + i_gate * c_tilde
            c_new.append(new_c)
            
            # Output gate
            o_sum = sum(self.W_o[j][i] * combined[j] for j in range(len(combined))) + self.b_o[i]
            o = self.sigmoid(o_sum)
            
            # New hidden state
            new_h = o * math.tanh(max(-500, min(500, new_c)))
            h_new.append(new_h)
        
        return h_new, c_new


class Autoencoder:
    """
    Autoencoder untuk unsupervised feature learning.
    Learns compressed representation of input data.
    """
    
    def __init__(self, input_size: int, encoding_size: int, hidden_sizes: List[int] = None):
        self.input_size = input_size
        self.encoding_size = encoding_size
        
        # Build encoder layers
        if hidden_sizes is None:
            hidden_sizes = []
        
        encoder_sizes = [input_size] + hidden_sizes + [encoding_size]
        decoder_sizes = [encoding_size] + list(reversed(hidden_sizes)) + [input_size]
        
        self.encoder_weights = []
        self.encoder_biases = []
        self.decoder_weights = []
        self.decoder_biases = []
        
        # Initialize encoder
        for i in range(len(encoder_sizes) - 1):
            limit = math.sqrt(6 / (encoder_sizes[i] + encoder_sizes[i + 1]))
            weights = [[random.uniform(-limit, limit) for _ in range(encoder_sizes[i + 1])]
                       for _ in range(encoder_sizes[i])]
            biases = [0.0] * encoder_sizes[i + 1]
            self.encoder_weights.append(weights)
            self.encoder_biases.append(biases)
        
        # Initialize decoder
        for i in range(len(decoder_sizes) - 1):
            limit = math.sqrt(6 / (decoder_sizes[i] + decoder_sizes[i + 1]))
            weights = [[random.uniform(-limit, limit) for _ in range(decoder_sizes[i + 1])]
                       for _ in range(decoder_sizes[i])]
            biases = [0.0] * decoder_sizes[i + 1]
            self.decoder_weights.append(weights)
            self.decoder_biases.append(biases)
        
        self.learning_rate = 0.01
    
    @staticmethod
    def relu(x: List[float]) -> List[float]:
        return [max(0, val) for val in x]
    
    @staticmethod
    def sigmoid(values: List[float]) -> List[float]:
        result = []
        for x in values:
            try:
                result.append(1 / (1 + math.exp(-max(-500, min(500, x)))))
            except OverflowError:
                result.append(0.0 if x < 0 else 1.0)
        return result
    
    def _forward_layer(self, x: List[float], weights: List[List[float]], 
                       biases: List[float], activation: str = 'relu') -> List[float]:
        """Forward through single layer."""
        output_size = len(biases)
        output = []
        
        for j in range(output_size):
            val = biases[j] + sum(x[i] * weights[i][j] for i in range(len(x)))
            output.append(val)
        
        if activation == 'relu':
            return self.relu(output)
        elif activation == 'sigmoid':
            return self.sigmoid(output)
        return output
    
    def encode(self, x: List[float]) -> List[float]:
        """Encode input to compressed representation."""
        current = x
        for weights, biases in zip(self.encoder_weights[:-1], self.encoder_biases[:-1]):
            current = self._forward_layer(current, weights, biases, 'relu')
        # Last encoder layer
        current = self._forward_layer(current, self.encoder_weights[-1], 
                                       self.encoder_biases[-1], 'relu')
        return current
    
    def decode(self, z: List[float]) -> List[float]:
        """Decode from compressed representation."""
        current = z
        for weights, biases in zip(self.decoder_weights[:-1], self.decoder_biases[:-1]):
            current = self._forward_layer(current, weights, biases, 'relu')
        # Last decoder layer (sigmoid for 0-1 output)
        current = self._forward_layer(current, self.decoder_weights[-1], 
                                       self.decoder_biases[-1], 'sigmoid')
        return current
    
    def forward(self, x: List[float]) -> Tuple[List[float], List[float]]:
        """Full forward pass."""
        z = self.encode(x)
        x_reconstructed = self.decode(z)
        return z, x_reconstructed
    
    def train_step(self, x: List[float]) -> float:
        """Single training step, returns reconstruction loss."""
        z, x_recon = self.forward(x)
        
        # Mean Squared Error
        loss = sum((x[i] - x_recon[i]) ** 2 for i in range(len(x))) / len(x)
        
        # Simple gradient descent (simplified - real implementation would do backprop)
        # For demo purposes, we use numerical gradient approximation
        epsilon = 1e-5
        
        # Update decoder weights
        for layer_idx in range(len(self.decoder_weights)):
            for i in range(len(self.decoder_weights[layer_idx])):
                for j in range(len(self.decoder_weights[layer_idx][i])):
                    # Numerical gradient
                    self.decoder_weights[layer_idx][i][j] += epsilon
                    _, x_new = self.forward(x)
                    loss_new = sum((x[k] - x_new[k]) ** 2 for k in range(len(x))) / len(x)
                    grad = (loss_new - loss) / epsilon
                    self.decoder_weights[layer_idx][i][j] -= epsilon
                    
                    # Update
                    self.decoder_weights[layer_idx][i][j] -= self.learning_rate * grad
        
        return loss


class CNN:
    """
    Simplified Convolutional Neural Network.
    Can process 1D sequences (like time series or flattened images).
    """
    
    def __init__(self, input_channels: int, input_length: int, num_classes: int):
        self.input_channels = input_channels
        self.input_length = input_length
        self.num_classes = num_classes
        
        # Layer 1: Conv + ReLU + Pool
        self.conv1 = ConvLayer(input_channels, 8, kernel_size=3, padding=1)
        self.pool1 = MaxPool(pool_size=2)
        self.bn1 = BatchNorm(8)
        
        # Layer 2: Conv + ReLU + Pool
        self.conv2 = ConvLayer(8, 16, kernel_size=3, padding=1)
        self.pool2 = MaxPool(pool_size=2)
        self.bn2 = BatchNorm(16)
        
        # Calculate flattened size
        length_after_conv = input_length // 4  # After 2 pooling layers
        self.flat_size = 16 * max(1, length_after_conv)
        
        # Fully connected layer
        limit = math.sqrt(6 / (self.flat_size + num_classes))
        self.fc_weights = [[random.uniform(-limit, limit) for _ in range(num_classes)]
                           for _ in range(self.flat_size)]
        self.fc_bias = [0.0] * num_classes
        
        self.dropout = Dropout(0.5)
    
    def forward(self, x: List[List[float]], training: bool = True) -> List[float]:
        """
        Forward pass.
        x: [input_channels][input_length]
        """
        # Conv block 1
        x = self.conv1.forward(x)
        x = self.conv1.relu(x)
        x = self.pool1.forward(x)
        
        # Conv block 2
        x = self.conv2.forward(x)
        x = self.conv2.relu(x)
        x = self.pool2.forward(x)
        
        # Flatten
        flat = []
        for channel in x:
            flat.extend(channel)
        
        # Pad or truncate to expected size
        if len(flat) < self.flat_size:
            flat.extend([0.0] * (self.flat_size - len(flat)))
        elif len(flat) > self.flat_size:
            flat = flat[:self.flat_size]
        
        # Dropout
        if training:
            flat = self.dropout.forward(flat, training)
        
        # Fully connected
        output = []
        for j in range(self.num_classes):
            val = self.fc_bias[j] + sum(flat[i] * self.fc_weights[i][j] 
                                         for i in range(len(flat)))
            output.append(val)
        
        # Softmax
        max_val = max(output)
        exp_vals = [math.exp(v - max_val) for v in output]
        sum_exp = sum(exp_vals)
        return [v / sum_exp for v in exp_vals]


class SequenceModel:
    """
    Sequence Model using LSTM for sequential data processing.
    Good for text, time series, audio-like data.
    """
    
    def __init__(self, input_size: int, hidden_size: int, output_size: int, 
                 num_layers: int = 1):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.num_layers = num_layers
        
        # LSTM layers
        self.lstm_cells = []
        for i in range(num_layers):
            in_size = input_size if i == 0 else hidden_size
            self.lstm_cells.append(LSTMCell(in_size, hidden_size))
        
        # Output layer
        limit = math.sqrt(6 / (hidden_size + output_size))
        self.output_weights = [[random.uniform(-limit, limit) for _ in range(output_size)]
                                for _ in range(hidden_size)]
        self.output_bias = [0.0] * output_size
    
    def forward(self, sequence: List[List[float]]) -> List[float]:
        """
        Process a sequence and return output.
        sequence: [seq_length][input_size]
        """
        # Initialize hidden states
        h = [[0.0] * self.hidden_size for _ in range(self.num_layers)]
        c = [[0.0] * self.hidden_size for _ in range(self.num_layers)]
        
        # Process sequence
        for x_t in sequence:
            current_input = x_t
            
            for layer_idx, lstm in enumerate(self.lstm_cells):
                h[layer_idx], c[layer_idx] = lstm.forward(
                    current_input, h[layer_idx], c[layer_idx]
                )
                current_input = h[layer_idx]
        
        # Output from last hidden state
        final_h = h[-1]
        output = []
        for j in range(self.output_size):
            val = self.output_bias[j] + sum(final_h[i] * self.output_weights[i][j] 
                                             for i in range(self.hidden_size))
            output.append(val)
        
        # Softmax
        max_val = max(output)
        exp_vals = [math.exp(v - max_val) for v in output]
        sum_exp = sum(exp_vals)
        return [v / sum_exp for v in exp_vals]


class FeatureExtractor:
    """
    Automatic Feature Extraction dari raw data.
    Mengekstrak fitur tanpa manual engineering.
    """
    
    def __init__(self):
        self.autoencoder: Optional[Autoencoder] = None
        self.fitted = False
    
    def fit(self, data: List[List[float]], encoding_size: int = 32, epochs: int = 100):
        """
        Train feature extractor on data.
        """
        if not data:
            return
        
        input_size = len(data[0])
        hidden_sizes = [max(encoding_size * 2, input_size // 2)]
        
        self.autoencoder = Autoencoder(input_size, encoding_size, hidden_sizes)
        
        # Train
        for epoch in range(epochs):
            total_loss = 0
            for sample in data:
                loss = self.autoencoder.train_step(sample)
                total_loss += loss
            
            if (epoch + 1) % 10 == 0:
                avg_loss = total_loss / len(data)
                # print(f"Epoch {epoch + 1}, Loss: {avg_loss:.6f}")
        
        self.fitted = True
    
    def extract(self, data: List[float]) -> List[float]:
        """Extract features from single sample."""
        if not self.fitted or self.autoencoder is None:
            return data
        return self.autoencoder.encode(data)
    
    def extract_batch(self, data: List[List[float]]) -> List[List[float]]:
        """Extract features from batch."""
        return [self.extract(sample) for sample in data]


def demo_deep_learning():
    """Demo Deep Learning capabilities."""
    print("=== WeaR AI Deep Learning Demo ===\n")
    
    # 1. CNN Demo
    print("1. Convolutional Neural Network (CNN):")
    cnn = CNN(input_channels=1, input_length=16, num_classes=3)
    
    # Create fake image-like data (1 channel, 16 pixels)
    sample = [[random.random() for _ in range(16)]]
    output = cnn.forward(sample)
    print(f"   Input shape: [1][16]")
    print(f"   Output probabilities: {[round(p, 3) for p in output]}")
    print(f"   Predicted class: {output.index(max(output))}")
    
    print()
    
    # 2. LSTM Demo
    print("2. LSTM Sequence Model:")
    lstm_model = SequenceModel(input_size=4, hidden_size=8, output_size=2, num_layers=2)
    
    # Create sequence data (10 timesteps, 4 features each)
    sequence = [[random.random() for _ in range(4)] for _ in range(10)]
    output = lstm_model.forward(sequence)
    print(f"   Sequence length: 10, Features per step: 4")
    print(f"   Output probabilities: {[round(p, 3) for p in output]}")
    
    print()
    
    # 3. Autoencoder Demo
    print("3. Autoencoder (Unsupervised Feature Learning):")
    ae = Autoencoder(input_size=10, encoding_size=3, hidden_sizes=[6])
    
    # Sample data
    sample = [random.random() for _ in range(10)]
    encoding, reconstruction = ae.forward(sample)
    
    print(f"   Original size: 10")
    print(f"   Encoded size: {len(encoding)} (compression!)")
    print(f"   Reconstructed size: {len(reconstruction)}")
    
    # Calculate reconstruction error
    error = sum((sample[i] - reconstruction[i]) ** 2 for i in range(len(sample))) / len(sample)
    print(f"   Reconstruction MSE: {error:.4f}")
    
    print()
    
    # 4. Feature Extractor Demo
    print("4. Automatic Feature Extraction:")
    fe = FeatureExtractor()
    
    # Create training data
    training_data = [[random.random() for _ in range(20)] for _ in range(50)]
    
    print("   Training feature extractor...")
    fe.fit(training_data, encoding_size=5, epochs=20)
    
    # Extract features
    test_sample = [random.random() for _ in range(20)]
    features = fe.extract(test_sample)
    
    print(f"   Original dimensions: 20")
    print(f"   Extracted features: {len(features)}")
    print(f"   Features: {[round(f, 3) for f in features]}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    demo_deep_learning()
