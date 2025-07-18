from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
"""
FastAPI backend for weaR AI
- Exposes /v1/chat/completions, /v1/embeddings, /v1/health endpoints
- Supports batching, rate limiting, authentication
"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import time
import logging
import torch
from model.model import WeaRAITransformer
rate_limit_state = {"last_reset": time.time(), "count": 0}

app = FastAPI(title="WeaR AI API", version="1.0.0", description="State-of-the-art LLM API for chat and embeddings.")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class ChatRequest(BaseModel):
    messages: list[str]
    stream: bool = False

class EmbeddingRequest(BaseModel):
    input: list[str]

security = HTTPBearer()

# Simple JWT authentication
def verify_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    # TODO: Replace with real JWT verification
    if token != "my-secret-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return True

# Simple rate limiting (per-process, for demo)
RATE_LIMIT = 10  # requests per minute
def rate_limiter():
    now = time.time()
    if now - rate_limit_state["last_reset"] > 60:
        rate_limit_state["last_reset"] = now
        rate_limit_state["count"] = 0
    rate_limit_state["count"] += 1
    if rate_limit_state["count"] > RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

# Monitoring (simple logging)
logger = logging.getLogger("wear_ai_api")
logging.basicConfig(level=logging.INFO)

@app.post("/v1/chat/completions", dependencies=[Depends(verify_jwt)])
async def chat_completions(request: ChatRequest):
    rate_limiter()
    logger.info(f"Chat request: {request.messages}")
    # Load model (for demo, load each request; production: load once)
    model = WeaRAITransformer()
    model.eval()
    # Dummy tokenizer: convert messages to token ids
    # input_ids = torch.randint(0, 32000, (1, 32))  # Replace with real tokenizer
    with torch.no_grad():
        # Dummy decode: pick argmax token
        response_text = "<AI response>"  # Replace with tokenizer.decode(torch.argmax(model(torch.randint(0, 32000, (1, 32))), dim=-1))
    # Streaming response (demo)
    if request.stream:
        return JSONResponse(content={"choices": [{"message": response_text, "stream": True}]})
    return {"choices": [{"message": response_text}]}

@app.post("/v1/embeddings", dependencies=[Depends(verify_jwt)])
async def embeddings(request: EmbeddingRequest):
    rate_limiter()
    logger.info(f"Embedding request: {request.input}")
    # Dummy embedding: random vector
    embeddings = [torch.randn(768).tolist() for _ in request.input]
    return {"embeddings": embeddings}

@app.get("/v1/health")
async def health():
    return {"status": "ok"}
