# Setup Instructions

## Local Development
1. Clone the repo
2. Install Python dependencies:
   ```bash
   pip install -r docker/requirements.txt
   ```
3. Train the model:
   ```bash
   python train/train.py
   ```
4. Start the API server:
   ```bash
   uvicorn api.api:app --reload
   ```
5. Run the frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Production Deployment
- Build Docker image:
  ```bash
  docker build -t wear-ai-backend -f docker/Dockerfile .
  ```
- Push to Docker Hub
- Use Helm chart in `infra/` for Kubernetes
- Provision cloud resources with Terraform
