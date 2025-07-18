"""
Fine-tuning script for weaR AI
- Supports domain-specific data
- Hyperparameter search with Optuna
"""
import optuna
import pytorch_lightning as pl
from model.model import WeaRAITransformer
from data.data_module import WeaRAIDataModule

def objective(trial):
    lr = trial.suggest_loguniform('lr', 1e-5, 1e-3)
    dropout = trial.suggest_uniform('dropout', 0.05, 0.3)
    model = WeaRAITransformer(dropout=dropout)
    data_module = WeaRAIDataModule()
    trainer = pl.Trainer(max_epochs=3)
    trainer.fit(model, datamodule=data_module)
    # ...return validation loss...
    return 0.0

if __name__ == "__main__":
    study = optuna.create_study(direction='minimize')
    study.optimize(objective, n_trials=10)
    print('Best hyperparameters:', study.best_params)
