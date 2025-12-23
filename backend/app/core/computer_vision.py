"""
WeaR AI - Computer Vision & Image Processing Module
Pemrosesan gambar tanpa OpenCV - Pure Python!
Created by RidTheWann

Fitur:
- Image loading dan basic operations
- Edge detection (Sobel, simple)
- Image filters (blur, sharpen)
- Feature extraction untuk neural networks
- Simple pattern recognition
"""

import math
import struct
from typing import List, Tuple, Optional, Dict, Any


class Image:
    """
    Simple image representation.
    Stores pixels as 2D array of grayscale values (0-255).
    """
    
    def __init__(self, width: int, height: int, pixels: Optional[List[List[int]]] = None):
        self.width = width
        self.height = height
        
        if pixels is not None:
            self.pixels = pixels
        else:
            # Initialize with zeros (black image)
            self.pixels = [[0 for _ in range(width)] for _ in range(height)]
    
    @classmethod
    def from_flat(cls, width: int, height: int, flat_data: List[int]) -> 'Image':
        """Create image from flat array of pixels."""
        pixels = []
        for y in range(height):
            row = []
            for x in range(width):
                idx = y * width + x
                row.append(flat_data[idx] if idx < len(flat_data) else 0)
            pixels.append(row)
        return cls(width, height, pixels)
    
    def get_pixel(self, x: int, y: int) -> int:
        """Get pixel value at (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.pixels[y][x]
        return 0
    
    def set_pixel(self, x: int, y: int, value: int):
        """Set pixel value at (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = max(0, min(255, value))
    
    def to_flat(self) -> List[float]:
        """Convert to flat normalized array (0-1) for neural network."""
        flat = []
        for row in self.pixels:
            for pixel in row:
                flat.append(pixel / 255.0)
        return flat
    
    def copy(self) -> 'Image':
        """Create a copy of the image."""
        new_pixels = [row[:] for row in self.pixels]
        return Image(self.width, self.height, new_pixels)
    
    def resize(self, new_width: int, new_height: int) -> 'Image':
        """Simple nearest-neighbor resize."""
        new_pixels = []
        for y in range(new_height):
            row = []
            for x in range(new_width):
                # Map to original coordinates
                orig_x = int(x * self.width / new_width)
                orig_y = int(y * self.height / new_height)
                row.append(self.get_pixel(orig_x, orig_y))
            new_pixels.append(row)
        return Image(new_width, new_height, new_pixels)
    
    def __str__(self) -> str:
        return f"Image({self.width}x{self.height})"


class ImageFilter:
    """
    Collection of image filters/kernels.
    """
    
    # Predefined kernels
    BLUR_3x3 = [
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ]
    
    GAUSSIAN_3x3 = [
        [1/16, 2/16, 1/16],
        [2/16, 4/16, 2/16],
        [1/16, 2/16, 1/16]
    ]
    
    SHARPEN = [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]
    
    EDGE_DETECT = [
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ]
    
    SOBEL_X = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]
    
    SOBEL_Y = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]
    
    EMBOSS = [
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ]
    
    @staticmethod
    def apply_kernel(image: Image, kernel: List[List[float]]) -> Image:
        """Apply convolution kernel to image."""
        k_size = len(kernel)
        k_half = k_size // 2
        
        result = Image(image.width, image.height)
        
        for y in range(image.height):
            for x in range(image.width):
                total = 0.0
                
                for ky in range(k_size):
                    for kx in range(k_size):
                        px = x + kx - k_half
                        py = y + ky - k_half
                        pixel = image.get_pixel(px, py)
                        total += pixel * kernel[ky][kx]
                
                result.set_pixel(x, y, int(total))
        
        return result
    
    @classmethod
    def blur(cls, image: Image) -> Image:
        """Apply blur filter."""
        return cls.apply_kernel(image, cls.GAUSSIAN_3x3)
    
    @classmethod
    def sharpen(cls, image: Image) -> Image:
        """Apply sharpen filter."""
        return cls.apply_kernel(image, cls.SHARPEN)
    
    @classmethod
    def edge_detect(cls, image: Image) -> Image:
        """Detect edges using simple kernel."""
        return cls.apply_kernel(image, cls.EDGE_DETECT)
    
    @classmethod
    def sobel(cls, image: Image) -> Tuple[Image, Image, Image]:
        """
        Apply Sobel edge detection.
        Returns (gradient_x, gradient_y, gradient_magnitude).
        """
        grad_x = cls.apply_kernel(image, cls.SOBEL_X)
        grad_y = cls.apply_kernel(image, cls.SOBEL_Y)
        
        # Calculate magnitude
        magnitude = Image(image.width, image.height)
        for y in range(image.height):
            for x in range(image.width):
                gx = grad_x.get_pixel(x, y)
                gy = grad_y.get_pixel(x, y)
                mag = int(math.sqrt(gx * gx + gy * gy))
                magnitude.set_pixel(x, y, mag)
        
        return grad_x, grad_y, magnitude


class ImageFeatures:
    """
    Extract features from images for ML/classification.
    """
    
    @staticmethod
    def histogram(image: Image, bins: int = 16) -> List[float]:
        """Calculate histogram of pixel intensities."""
        hist = [0] * bins
        bin_size = 256 / bins
        
        for row in image.pixels:
            for pixel in row:
                bin_idx = min(int(pixel / bin_size), bins - 1)
                hist[bin_idx] += 1
        
        # Normalize
        total = image.width * image.height
        return [h / total for h in hist]
    
    @staticmethod
    def mean_intensity(image: Image) -> float:
        """Calculate mean pixel intensity."""
        total = sum(sum(row) for row in image.pixels)
        return total / (image.width * image.height)
    
    @staticmethod
    def std_intensity(image: Image) -> float:
        """Calculate standard deviation of pixel intensity."""
        mean = ImageFeatures.mean_intensity(image)
        variance = sum(
            sum((p - mean) ** 2 for p in row) 
            for row in image.pixels
        ) / (image.width * image.height)
        return math.sqrt(variance)
    
    @staticmethod
    def contrast(image: Image) -> float:
        """Calculate image contrast (max - min)."""
        min_val = min(min(row) for row in image.pixels)
        max_val = max(max(row) for row in image.pixels)
        return (max_val - min_val) / 255.0
    
    @staticmethod
    def edge_density(image: Image) -> float:
        """Calculate density of edges in image."""
        edges = ImageFilter.edge_detect(image)
        edge_count = sum(
            sum(1 for p in row if p > 50) 
            for row in edges.pixels
        )
        return edge_count / (image.width * image.height)
    
    @staticmethod
    def quadrant_means(image: Image) -> List[float]:
        """Calculate mean intensity for each quadrant."""
        mid_x = image.width // 2
        mid_y = image.height // 2
        
        quadrants = [
            (0, 0, mid_x, mid_y),           # Top-left
            (mid_x, 0, image.width, mid_y), # Top-right
            (0, mid_y, mid_x, image.height), # Bottom-left
            (mid_x, mid_y, image.width, image.height)  # Bottom-right
        ]
        
        means = []
        for x1, y1, x2, y2 in quadrants:
            total = 0
            count = 0
            for y in range(y1, y2):
                for x in range(x1, x2):
                    total += image.get_pixel(x, y)
                    count += 1
            means.append(total / count if count > 0 else 0)
        
        return [m / 255.0 for m in means]
    
    @classmethod
    def extract_all(cls, image: Image) -> List[float]:
        """Extract comprehensive feature vector from image."""
        features = []
        
        # Histogram (16 bins)
        features.extend(cls.histogram(image, 16))
        
        # Basic stats
        features.append(cls.mean_intensity(image) / 255.0)
        features.append(cls.std_intensity(image) / 128.0)
        features.append(cls.contrast(image))
        features.append(cls.edge_density(image))
        
        # Quadrant analysis
        features.extend(cls.quadrant_means(image))
        
        return features


class SimplePatternMatcher:
    """
    Simple pattern matching for shapes/objects.
    Template-based matching.
    """
    
    def __init__(self):
        self.templates: Dict[str, Image] = {}
    
    def add_template(self, name: str, template: Image):
        """Add a template for matching."""
        self.templates[name] = template
    
    def match(self, image: Image, template_name: str) -> Tuple[float, Tuple[int, int]]:
        """
        Find best match location for template.
        Returns (score, (x, y)) where score is 0-1 similarity.
        """
        if template_name not in self.templates:
            return 0.0, (0, 0)
        
        template = self.templates[template_name]
        best_score = 0.0
        best_loc = (0, 0)
        
        for y in range(image.height - template.height + 1):
            for x in range(image.width - template.width + 1):
                score = self._calculate_match_score(image, template, x, y)
                if score > best_score:
                    best_score = score
                    best_loc = (x, y)
        
        return best_score, best_loc
    
    def _calculate_match_score(self, image: Image, template: Image, 
                               offset_x: int, offset_y: int) -> float:
        """Calculate normalized cross-correlation score."""
        sum_product = 0.0
        sum_img_sq = 0.0
        sum_tmpl_sq = 0.0
        
        for ty in range(template.height):
            for tx in range(template.width):
                img_val = image.get_pixel(offset_x + tx, offset_y + ty)
                tmpl_val = template.get_pixel(tx, ty)
                
                sum_product += img_val * tmpl_val
                sum_img_sq += img_val * img_val
                sum_tmpl_sq += tmpl_val * tmpl_val
        
        denominator = math.sqrt(sum_img_sq * sum_tmpl_sq)
        if denominator == 0:
            return 0.0
        
        return sum_product / denominator


class ImageClassifier:
    """
    Simple image classifier using extracted features.
    Uses k-NN algorithm for classification.
    """
    
    def __init__(self, k: int = 3):
        self.k = k
        self.training_data: List[Tuple[List[float], str]] = []
    
    def train(self, images: List[Image], labels: List[str]):
        """Train classifier on labeled images."""
        for image, label in zip(images, labels):
            features = ImageFeatures.extract_all(image)
            self.training_data.append((features, label))
    
    def _euclidean_distance(self, a: List[float], b: List[float]) -> float:
        """Calculate Euclidean distance between feature vectors."""
        return math.sqrt(sum((ai - bi) ** 2 for ai, bi in zip(a, b)))
    
    def predict(self, image: Image) -> Tuple[str, float]:
        """
        Predict class for new image.
        Returns (predicted_label, confidence).
        """
        if not self.training_data:
            return "unknown", 0.0
        
        features = ImageFeatures.extract_all(image)
        
        # Calculate distances to all training samples
        distances = []
        for train_features, label in self.training_data:
            dist = self._euclidean_distance(features, train_features)
            distances.append((dist, label))
        
        # Sort by distance
        distances.sort(key=lambda x: x[0])
        
        # Get k nearest neighbors
        k_nearest = distances[:self.k]
        
        # Vote
        votes: Dict[str, int] = {}
        for _, label in k_nearest:
            votes[label] = votes.get(label, 0) + 1
        
        # Get winner
        winner = max(votes.items(), key=lambda x: x[1])
        confidence = winner[1] / self.k
        
        return winner[0], confidence


def create_test_image(pattern: str, size: int = 16) -> Image:
    """Create test images with simple patterns."""
    image = Image(size, size)
    
    if pattern == "horizontal_lines":
        for y in range(size):
            if y % 3 == 0:
                for x in range(size):
                    image.set_pixel(x, y, 255)
    
    elif pattern == "vertical_lines":
        for x in range(size):
            if x % 3 == 0:
                for y in range(size):
                    image.set_pixel(x, y, 255)
    
    elif pattern == "diagonal":
        for i in range(size):
            image.set_pixel(i, i, 255)
            if i > 0:
                image.set_pixel(i-1, i, 200)
            if i < size - 1:
                image.set_pixel(i+1, i, 200)
    
    elif pattern == "square":
        # Draw a square in the center
        margin = size // 4
        for y in range(margin, size - margin):
            for x in range(margin, size - margin):
                if y == margin or y == size - margin - 1 or x == margin or x == size - margin - 1:
                    image.set_pixel(x, y, 255)
    
    elif pattern == "circle":
        # Draw a circle
        center = size // 2
        radius = size // 3
        for y in range(size):
            for x in range(size):
                dist = math.sqrt((x - center) ** 2 + (y - center) ** 2)
                if abs(dist - radius) < 1.5:
                    image.set_pixel(x, y, 255)
    
    elif pattern == "noise":
        import random
        for y in range(size):
            for x in range(size):
                image.set_pixel(x, y, random.randint(0, 255))
    
    return image


def demo_computer_vision():
    """Demo computer vision capabilities."""
    print("=== WeaR AI Computer Vision Demo ===\n")
    
    # 1. Create test images
    print("1. Creating test images...")
    images = {
        "horizontal": create_test_image("horizontal_lines"),
        "vertical": create_test_image("vertical_lines"),
        "diagonal": create_test_image("diagonal"),
        "square": create_test_image("square"),
        "circle": create_test_image("circle")
    }
    print(f"   Created {len(images)} test images (16x16)")
    
    # 2. Feature extraction
    print("\n2. Feature Extraction:")
    img = images["circle"]
    features = ImageFeatures.extract_all(img)
    print(f"   Image: circle (16x16)")
    print(f"   Features extracted: {len(features)}")
    print(f"   Mean intensity: {ImageFeatures.mean_intensity(img):.2f}")
    print(f"   Edge density: {ImageFeatures.edge_density(img):.3f}")
    
    # 3. Edge detection
    print("\n3. Edge Detection (Sobel):")
    _, _, magnitude = ImageFilter.sobel(img)
    edge_count = sum(1 for row in magnitude.pixels for p in row if p > 50)
    print(f"   Edges detected: {edge_count} pixels")
    
    # 4. Image classification
    print("\n4. Image Classification (k-NN):")
    classifier = ImageClassifier(k=3)
    
    # Create training data
    train_images = [
        create_test_image("horizontal_lines"),
        create_test_image("horizontal_lines"),
        create_test_image("vertical_lines"),
        create_test_image("vertical_lines"),
        create_test_image("circle"),
        create_test_image("circle"),
        create_test_image("square"),
        create_test_image("square"),
    ]
    train_labels = ["horizontal", "horizontal", "vertical", "vertical",
                    "circle", "circle", "square", "square"]
    
    classifier.train(train_images, train_labels)
    print(f"   Trained with {len(train_images)} images")
    
    # Test
    test_img = create_test_image("circle")
    pred, conf = classifier.predict(test_img)
    print(f"   Test: circle pattern")
    print(f"   Predicted: {pred} (confidence: {conf:.2f})")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    demo_computer_vision()
