# weaR AI API Documentation

## Endpoints
### POST /v1/chat/completions
- Request: `{ "messages": [ ... ], "stream": false }`
- Response: `{ "choices": [ { "message": "..." } ] }`

### POST /v1/embeddings
- Request: `{ ... }`
- Response: `{ "embeddings": [ ... ] }`

### GET /v1/health
- Response: `{ "status": "ok" }`

## Authentication
- API keys, JWT supported

## Monitoring
- Prometheus metrics
