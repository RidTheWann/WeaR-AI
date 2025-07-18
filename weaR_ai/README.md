# weaR AI

A state-of-the-art AI assistant with advanced reasoning, chat, and API capabilities.

## Project Structure
- `model/` — Transformer model code (PyTorch Lightning)
- `data/` — Data loading & preprocessing
- `train/` — Training scripts
- `eval/` — Evaluation & fine-tuning
- `api/` — FastAPI backend
- `frontend/` — Next.js React web app
- `docker/` — Containerization files
- `infra/` — Terraform, Helm, deployment scripts
- `tests/` — End-to-end and unit tests
- `docs/` — Documentation

## Quickstart
1. Install Python dependencies:
   ```bash
   pip install -r docker/requirements.txt
   ```
2. Train the model:
   ```bash
   python train/train.py
   ```
3. Start the API server:
   ```bash
   uvicorn api.api:app --reload
   ```
4. Run the frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

See `docs/` for full documentation.
