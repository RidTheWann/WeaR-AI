"""
WeaR AI - Audio Processing & Speech Module
Pemrosesan audio tanpa external libraries - Pure Python!
Created by RidTheWann

Fitur:
- Audio signal representation
- Basic signal processing (FFT, filters)
- Feature extraction (MFCC-like, spectral)
- Voice Activity Detection
- Simple audio classification
"""

import math
from typing import List, Tuple, Optional, Dict
from collections import deque


class AudioSignal:
    """
    Represents an audio signal.
    Stores samples as list of floats (-1.0 to 1.0).
    """
    
    def __init__(self, samples: List[float], sample_rate: int = 16000):
        self.samples = samples
        self.sample_rate = sample_rate
    
    @property
    def duration(self) -> float:
        """Duration in seconds."""
        return len(self.samples) / self.sample_rate
    
    @property
    def num_samples(self) -> int:
        return len(self.samples)
    
    def get_segment(self, start_sec: float, end_sec: float) -> 'AudioSignal':
        """Extract a segment of the audio."""
        start_idx = int(start_sec * self.sample_rate)
        end_idx = int(end_sec * self.sample_rate)
        return AudioSignal(self.samples[start_idx:end_idx], self.sample_rate)
    
    def normalize(self) -> 'AudioSignal':
        """Normalize signal to -1 to 1 range."""
        max_val = max(abs(s) for s in self.samples) if self.samples else 1
        if max_val == 0:
            return AudioSignal(self.samples[:], self.sample_rate)
        normalized = [s / max_val for s in self.samples]
        return AudioSignal(normalized, self.sample_rate)
    
    def apply_window(self, window_type: str = 'hamming') -> 'AudioSignal':
        """Apply window function to signal."""
        n = len(self.samples)
        if window_type == 'hamming':
            window = [0.54 - 0.46 * math.cos(2 * math.pi * i / (n - 1)) 
                      for i in range(n)]
        elif window_type == 'hann':
            window = [0.5 * (1 - math.cos(2 * math.pi * i / (n - 1))) 
                      for i in range(n)]
        else:
            window = [1.0] * n
        
        windowed = [s * w for s, w in zip(self.samples, window)]
        return AudioSignal(windowed, self.sample_rate)


class FFT:
    """
    Fast Fourier Transform implementation.
    Cooley-Tukey algorithm.
    """
    
    @staticmethod
    def fft(x: List[complex]) -> List[complex]:
        """Compute FFT of x."""
        n = len(x)
        
        if n <= 1:
            return x
        
        # Pad to power of 2
        if n & (n - 1) != 0:
            next_pow2 = 1 << (n - 1).bit_length()
            x = x + [0j] * (next_pow2 - n)
            n = next_pow2
        
        # Cooley-Tukey
        if n <= 1:
            return x
        
        even = FFT.fft(x[0::2])
        odd = FFT.fft(x[1::2])
        
        result = [0j] * n
        for k in range(n // 2):
            t = math.e ** (-2j * math.pi * k / n) * odd[k]
            result[k] = even[k] + t
            result[k + n // 2] = even[k] - t
        
        return result
    
    @staticmethod
    def magnitude_spectrum(x: List[float]) -> List[float]:
        """Compute magnitude spectrum."""
        # Convert to complex
        x_complex = [complex(s, 0) for s in x]
        
        # Compute FFT
        spectrum = FFT.fft(x_complex)
        
        # Get magnitude (only first half - symmetric)
        n = len(spectrum)
        magnitude = [abs(s) for s in spectrum[:n // 2]]
        
        return magnitude
    
    @staticmethod
    def power_spectrum(x: List[float]) -> List[float]:
        """Compute power spectrum."""
        mag = FFT.magnitude_spectrum(x)
        return [m * m for m in mag]


class AudioFilter:
    """
    Audio filters for signal processing.
    """
    
    @staticmethod
    def low_pass(signal: AudioSignal, cutoff_hz: float) -> AudioSignal:
        """Simple low-pass filter using moving average."""
        # Calculate window size based on cutoff
        window_size = max(1, int(signal.sample_rate / cutoff_hz))
        
        filtered = []
        buffer = deque(maxlen=window_size)
        
        for sample in signal.samples:
            buffer.append(sample)
            filtered.append(sum(buffer) / len(buffer))
        
        return AudioSignal(filtered, signal.sample_rate)
    
    @staticmethod
    def high_pass(signal: AudioSignal, cutoff_hz: float) -> AudioSignal:
        """Simple high-pass filter (original - low-passed)."""
        low_passed = AudioFilter.low_pass(signal, cutoff_hz)
        high_passed = [s1 - s2 for s1, s2 in zip(signal.samples, low_passed.samples)]
        return AudioSignal(high_passed, signal.sample_rate)
    
    @staticmethod
    def pre_emphasis(signal: AudioSignal, coef: float = 0.97) -> AudioSignal:
        """Apply pre-emphasis filter (boost high frequencies)."""
        emphasized = [signal.samples[0]]
        for i in range(1, len(signal.samples)):
            emphasized.append(signal.samples[i] - coef * signal.samples[i - 1])
        return AudioSignal(emphasized, signal.sample_rate)


class AudioFeatures:
    """
    Extract features from audio for ML/classification.
    """
    
    @staticmethod
    def energy(signal: AudioSignal) -> float:
        """Calculate signal energy."""
        return sum(s * s for s in signal.samples) / len(signal.samples) if signal.samples else 0
    
    @staticmethod
    def zero_crossing_rate(signal: AudioSignal) -> float:
        """Calculate zero-crossing rate."""
        if len(signal.samples) < 2:
            return 0
        
        crossings = sum(
            1 for i in range(1, len(signal.samples))
            if (signal.samples[i] >= 0) != (signal.samples[i - 1] >= 0)
        )
        return crossings / len(signal.samples)
    
    @staticmethod
    def spectral_centroid(signal: AudioSignal) -> float:
        """Calculate spectral centroid (brightness)."""
        spectrum = FFT.magnitude_spectrum(signal.samples)
        if not spectrum or sum(spectrum) == 0:
            return 0
        
        freqs = [i * signal.sample_rate / (2 * len(spectrum)) for i in range(len(spectrum))]
        weighted_sum = sum(f * m for f, m in zip(freqs, spectrum))
        total_magnitude = sum(spectrum)
        
        return weighted_sum / total_magnitude if total_magnitude > 0 else 0
    
    @staticmethod
    def spectral_rolloff(signal: AudioSignal, threshold: float = 0.85) -> float:
        """Calculate spectral rolloff frequency."""
        spectrum = FFT.magnitude_spectrum(signal.samples)
        if not spectrum:
            return 0
        
        total_energy = sum(s * s for s in spectrum)
        target_energy = threshold * total_energy
        
        cumulative = 0
        for i, s in enumerate(spectrum):
            cumulative += s * s
            if cumulative >= target_energy:
                return i * signal.sample_rate / (2 * len(spectrum))
        
        return signal.sample_rate / 2
    
    @staticmethod
    def spectral_bandwidth(signal: AudioSignal) -> float:
        """Calculate spectral bandwidth."""
        spectrum = FFT.magnitude_spectrum(signal.samples)
        if not spectrum:
            return 0
        
        centroid = AudioFeatures.spectral_centroid(signal)
        freqs = [i * signal.sample_rate / (2 * len(spectrum)) for i in range(len(spectrum))]
        
        total_magnitude = sum(spectrum)
        if total_magnitude == 0:
            return 0
        
        weighted_variance = sum(
            m * (f - centroid) ** 2 
            for f, m in zip(freqs, spectrum)
        )
        
        return math.sqrt(weighted_variance / total_magnitude)
    
    @staticmethod
    def frame_features(signal: AudioSignal, frame_size: int = 512, 
                       hop_size: int = 256) -> List[List[float]]:
        """Extract features for each frame."""
        frames = []
        
        for start in range(0, len(signal.samples) - frame_size, hop_size):
            frame_samples = signal.samples[start:start + frame_size]
            frame_signal = AudioSignal(frame_samples, signal.sample_rate)
            
            features = [
                AudioFeatures.energy(frame_signal),
                AudioFeatures.zero_crossing_rate(frame_signal),
                AudioFeatures.spectral_centroid(frame_signal),
                AudioFeatures.spectral_rolloff(frame_signal),
                AudioFeatures.spectral_bandwidth(frame_signal)
            ]
            frames.append(features)
        
        return frames
    
    @staticmethod
    def mel_filterbank(num_filters: int, fft_size: int, 
                       sample_rate: int) -> List[List[float]]:
        """Create mel filterbank."""
        def hz_to_mel(hz):
            return 2595 * math.log10(1 + hz / 700)
        
        def mel_to_hz(mel):
            return 700 * (10 ** (mel / 2595) - 1)
        
        low_mel = hz_to_mel(0)
        high_mel = hz_to_mel(sample_rate / 2)
        
        mel_points = [
            low_mel + i * (high_mel - low_mel) / (num_filters + 1)
            for i in range(num_filters + 2)
        ]
        
        hz_points = [mel_to_hz(m) for m in mel_points]
        bin_points = [int((fft_size + 1) * h / sample_rate) for h in hz_points]
        
        filterbank = []
        for i in range(1, num_filters + 1):
            filt = [0.0] * (fft_size // 2)
            
            for j in range(bin_points[i - 1], min(bin_points[i], fft_size // 2)):
                filt[j] = (j - bin_points[i - 1]) / (bin_points[i] - bin_points[i - 1])
            
            for j in range(bin_points[i], min(bin_points[i + 1], fft_size // 2)):
                filt[j] = (bin_points[i + 1] - j) / (bin_points[i + 1] - bin_points[i])
            
            filterbank.append(filt)
        
        return filterbank
    
    @staticmethod
    def mfcc_like(signal: AudioSignal, num_coeffs: int = 13) -> List[float]:
        """
        Compute MFCC-like features.
        Simplified version without DCT.
        """
        # Pre-emphasis
        emphasized = AudioFilter.pre_emphasis(signal)
        
        # Power spectrum
        spectrum = FFT.power_spectrum(emphasized.samples)
        
        # Apply mel filterbank
        num_filters = num_coeffs * 2
        filterbank = AudioFeatures.mel_filterbank(
            num_filters, len(spectrum) * 2, signal.sample_rate
        )
        
        # Filter energies
        filter_energies = []
        for filt in filterbank:
            energy = sum(
                f * s for f, s in zip(filt, spectrum[:len(filt)])
            )
            filter_energies.append(max(energy, 1e-10))
        
        # Log compression
        log_energies = [math.log(e) for e in filter_energies]
        
        # Return first num_coeffs (simplified - normally would apply DCT)
        return log_energies[:num_coeffs]


class VoiceActivityDetector:
    """
    Simple Voice Activity Detection (VAD).
    Detects speech vs silence.
    """
    
    def __init__(self, energy_threshold: float = 0.01, 
                 zcr_threshold: float = 0.1):
        self.energy_threshold = energy_threshold
        self.zcr_threshold = zcr_threshold
    
    def detect(self, signal: AudioSignal, frame_size: int = 512,
               hop_size: int = 256) -> List[bool]:
        """
        Detect voice activity in frames.
        Returns list of booleans (True = speech, False = silence).
        """
        activity = []
        
        for start in range(0, len(signal.samples) - frame_size, hop_size):
            frame = AudioSignal(
                signal.samples[start:start + frame_size],
                signal.sample_rate
            )
            
            energy = AudioFeatures.energy(frame)
            zcr = AudioFeatures.zero_crossing_rate(frame)
            
            # Speech typically has high energy and moderate ZCR
            # Silence has low energy
            # Noise might have high ZCR but low energy
            is_speech = energy > self.energy_threshold and zcr < self.zcr_threshold
            activity.append(is_speech)
        
        return activity
    
    def get_speech_segments(self, signal: AudioSignal, 
                            min_duration: float = 0.1) -> List[Tuple[float, float]]:
        """
        Get start and end times of speech segments.
        """
        frame_size = 512
        hop_size = 256
        
        activity = self.detect(signal, frame_size, hop_size)
        
        segments = []
        in_speech = False
        start_time = 0
        
        for i, is_speech in enumerate(activity):
            time = i * hop_size / signal.sample_rate
            
            if is_speech and not in_speech:
                start_time = time
                in_speech = True
            elif not is_speech and in_speech:
                if time - start_time >= min_duration:
                    segments.append((start_time, time))
                in_speech = False
        
        # Handle case where speech continues to end
        if in_speech:
            end_time = len(activity) * hop_size / signal.sample_rate
            if end_time - start_time >= min_duration:
                segments.append((start_time, end_time))
        
        return segments


class AudioClassifier:
    """
    Simple audio classifier using extracted features.
    """
    
    def __init__(self, k: int = 3):
        self.k = k
        self.training_data: List[Tuple[List[float], str]] = []
    
    def train(self, signals: List[AudioSignal], labels: List[str]):
        """Train on labeled audio signals."""
        for signal, label in zip(signals, labels):
            features = AudioFeatures.mfcc_like(signal)
            
            # Add more features
            features.extend([
                AudioFeatures.energy(signal),
                AudioFeatures.zero_crossing_rate(signal),
                AudioFeatures.spectral_centroid(signal),
                AudioFeatures.spectral_rolloff(signal)
            ])
            
            self.training_data.append((features, label))
    
    def _euclidean_distance(self, a: List[float], b: List[float]) -> float:
        """Calculate Euclidean distance."""
        min_len = min(len(a), len(b))
        return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(min_len)))
    
    def predict(self, signal: AudioSignal) -> Tuple[str, float]:
        """Predict class for audio signal."""
        if not self.training_data:
            return "unknown", 0.0
        
        features = AudioFeatures.mfcc_like(signal)
        features.extend([
            AudioFeatures.energy(signal),
            AudioFeatures.zero_crossing_rate(signal),
            AudioFeatures.spectral_centroid(signal),
            AudioFeatures.spectral_rolloff(signal)
        ])
        
        # Find k nearest neighbors
        distances = []
        for train_features, label in self.training_data:
            dist = self._euclidean_distance(features, train_features)
            distances.append((dist, label))
        
        distances.sort(key=lambda x: x[0])
        k_nearest = distances[:self.k]
        
        # Vote
        votes: Dict[str, int] = {}
        for _, label in k_nearest:
            votes[label] = votes.get(label, 0) + 1
        
        winner = max(votes.items(), key=lambda x: x[1])
        return winner[0], winner[1] / self.k


def create_test_signal(signal_type: str, duration: float = 1.0, 
                       sample_rate: int = 16000) -> AudioSignal:
    """Create test audio signals."""
    num_samples = int(duration * sample_rate)
    samples = []
    
    if signal_type == "sine":
        freq = 440  # A4 note
        for i in range(num_samples):
            t = i / sample_rate
            samples.append(math.sin(2 * math.pi * freq * t))
    
    elif signal_type == "square":
        freq = 440
        for i in range(num_samples):
            t = i / sample_rate
            val = math.sin(2 * math.pi * freq * t)
            samples.append(1.0 if val > 0 else -1.0)
    
    elif signal_type == "noise":
        import random
        samples = [random.uniform(-1, 1) for _ in range(num_samples)]
    
    elif signal_type == "silence":
        samples = [0.0] * num_samples
    
    elif signal_type == "chirp":
        # Frequency sweep
        start_freq = 200
        end_freq = 2000
        for i in range(num_samples):
            t = i / sample_rate
            freq = start_freq + (end_freq - start_freq) * t / duration
            samples.append(math.sin(2 * math.pi * freq * t))
    
    return AudioSignal(samples, sample_rate)


def demo_audio_processing():
    """Demo audio processing capabilities."""
    print("=== WeaR AI Audio Processing Demo ===\n")
    
    # 1. Create test signals
    print("1. Creating test audio signals...")
    signals = {
        "sine": create_test_signal("sine"),
        "square": create_test_signal("square"),
        "noise": create_test_signal("noise"),
        "chirp": create_test_signal("chirp")
    }
    for name, sig in signals.items():
        print(f"   {name}: {sig.num_samples} samples, {sig.duration:.2f}s")
    
    # 2. Feature extraction
    print("\n2. Feature Extraction (Sine wave):")
    sig = signals["sine"]
    print(f"   Energy: {AudioFeatures.energy(sig):.4f}")
    print(f"   ZCR: {AudioFeatures.zero_crossing_rate(sig):.4f}")
    print(f"   Spectral Centroid: {AudioFeatures.spectral_centroid(sig):.1f} Hz")
    print(f"   Spectral Rolloff: {AudioFeatures.spectral_rolloff(sig):.1f} Hz")
    
    # 3. MFCC-like features
    print("\n3. MFCC-like Features:")
    mfcc = AudioFeatures.mfcc_like(sig, num_coeffs=5)
    print(f"   Coefficients: {[round(c, 2) for c in mfcc]}")
    
    # 4. Voice Activity Detection
    print("\n4. Voice Activity Detection:")
    # Create signal with speech-like and silence sections
    mixed_samples = (
        [0.0] * 4000 +  # Silence
        [math.sin(2 * math.pi * 300 * i / 16000) * 0.5 for i in range(8000)] +  # Speech-like
        [0.0] * 4000  # Silence
    )
    mixed_signal = AudioSignal(mixed_samples, 16000)
    
    vad = VoiceActivityDetector(energy_threshold=0.01)
    segments = vad.get_speech_segments(mixed_signal, min_duration=0.1)
    print(f"   Signal duration: {mixed_signal.duration:.2f}s")
    print(f"   Speech segments: {len(segments)}")
    for start, end in segments:
        print(f"   - {start:.2f}s to {end:.2f}s")
    
    # 5. Audio Classification
    print("\n5. Audio Classification (k-NN):")
    classifier = AudioClassifier(k=3)
    
    # Create training data
    train_signals = [
        create_test_signal("sine"),
        create_test_signal("sine"),
        create_test_signal("square"),
        create_test_signal("square"),
        create_test_signal("noise"),
        create_test_signal("noise"),
    ]
    train_labels = ["tone", "tone", "harsh", "harsh", "noise", "noise"]
    
    classifier.train(train_signals, train_labels)
    print(f"   Trained with {len(train_signals)} samples")
    
    # Test
    test_signal = create_test_signal("sine")
    pred, conf = classifier.predict(test_signal)
    print(f"   Test: sine wave")
    print(f"   Predicted: {pred} (confidence: {conf:.2f})")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    demo_audio_processing()
