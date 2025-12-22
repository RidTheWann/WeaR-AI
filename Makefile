.PHONY: help dev backend frontend docker clean install

help:
	@echo "WeaR Ai - Development Commands"
	@echo ""
	@echo "  make install    - Install all dependencies"
	@echo "  make dev        - Start development servers"
	@echo "  make backend    - Start backend only"
	@echo "  make frontend   - Start frontend only"
	@echo "  make docker     - Start with Docker Compose"
	@echo "  make test       - Run tests"
	@echo "  make clean      - Clean build artifacts"

install:
	cd backend && pip install -e ".[dev]"
	cd frontend && npm install

dev:
	@echo "Starting WeaR Ai development servers..."
	@make backend & make frontend

backend:
	cd backend && uvicorn app.main:app --reload --port 8000

frontend:
	cd frontend && npm run dev

docker:
	docker-compose up -d

docker-down:
	docker-compose down

test:
	cd backend && pytest tests/ -v

lint:
	cd backend && ruff check app/
	cd frontend && npm run lint

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "node_modules" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".next" -exec rm -rf {} + 2>/dev/null || true
