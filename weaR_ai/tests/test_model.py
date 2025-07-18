"""
Pytest tests for weaR AI model
"""
import torch
from model.model import WeaRAITransformer

def test_model_forward():
    model = WeaRAITransformer()
    x = torch.randint(0, 32000, (8, 128))
    logits = model(x)
    assert logits.shape == (8, 128, 32000)
