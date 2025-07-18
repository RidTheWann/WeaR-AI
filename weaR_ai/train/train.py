"""
WeaR AI Training Script
- Distributed (multi-GPU/TPU)
- TensorBoard & W&B logging
"""
import pytorch_lightning as pl
from pytorch_lightning.loggers import TensorBoardLogger, WandbLogger
from model.model import WeaRAITransformer
from data.data_module import WeaRAIDataModule

if __name__ == "__main__":
    model = WeaRAITransformer()
    data_module = WeaRAIDataModule(
        dataset_name="webtext", tokenizer_name="gpt2", batch_size=8, max_seq_len=4096
    )
    import os
    from datasets import load_dataset
    from torch.utils.data import DataLoader
    from model.model import WeaRTransformer

    # Load dataset (WebText or custom)
    dataset = load_dataset('openwebtext', split='train[:1%]')
    def tokenize(batch):
        # Tokenizer placeholder
        return {'input_ids': batch['text'], 'labels': batch['text']}
    dataset = dataset.map(tokenize, batched=True)
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

    # Model
    model = WeaRTransformer(vocab_size=50257)

    # Logger
    logger = TensorBoardLogger('tb_logs', name='wear_ai')
    # logger = WandbLogger(project='wear_ai')  # Uncomment for W&B

    # Trainer with DDP (multi-GPU)
    trainer = pl.Trainer(
        max_epochs=1,
        accelerator='gpu',
        devices='auto',
        strategy='ddp',
        logger=logger
    )
    trainer.fit(model, dataloader)
    # Run test after training
    trainer.test(model, datamodule=data_module)
