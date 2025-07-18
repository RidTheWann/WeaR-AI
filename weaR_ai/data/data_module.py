"""
WeaR AI Data Pipeline
- Hugging Face Datasets
- Tokenization, padding, truncation
- Supports WebText & custom corpora
"""
import pytorch_lightning as pl
from torch.utils.data import DataLoader
from datasets import load_dataset
from transformers import AutoTokenizer

class WeaRAIDataModule(pl.LightningDataModule):
    def __init__(self, dataset_name="webtext", tokenizer_name="gpt2", batch_size=8, max_seq_len=4096):
        super().__init__()
        self.dataset_name = dataset_name
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        self.batch_size = batch_size
        self.max_seq_len = max_seq_len

    def setup(self, stage=None):
        self.dataset = load_dataset(self.dataset_name)
        def preprocess(example):
            # Data augmentation: random masking (optional)
            tokens = self.tokenizer(
                example["text"],
                truncation=True,
                padding="max_length",
                max_length=self.max_seq_len,
                return_tensors="pt"
            )
            input_ids = tokens["input_ids"].squeeze()
            # Random masking augmentation (for pretraining)
            if torch.rand(1).item() < 0.1:
                mask_idx = torch.randint(0, input_ids.size(0), (1,)).item()
                input_ids[mask_idx] = self.tokenizer.mask_token_id if hasattr(self.tokenizer, 'mask_token_id') else input_ids[mask_idx]
            return {"input_ids": input_ids, "labels": input_ids}
        self.dataset = self.dataset.map(preprocess, batched=True)
        self.train_data = self.dataset["train"]
        self.val_data = self.dataset["validation"] if "validation" in self.dataset else None
        self.test_data = self.dataset["test"] if "test" in self.dataset else None

    def train_dataloader(self):
        return DataLoader(self.train_data, batch_size=self.batch_size, shuffle=True)

    def val_dataloader(self):
        if self.val_data:
            return DataLoader(self.val_data, batch_size=self.batch_size)
        return None

    def test_dataloader(self):
        if self.test_data:
            return DataLoader(self.test_data, batch_size=self.batch_size)
        return None
