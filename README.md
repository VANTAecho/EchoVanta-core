# EchoVanta Core

This repository contains a minimal FastAPI application for registering bots.

## Running Locally

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Register a bot by sending a POST request to `http://localhost:8000/bots/` with a JSON body containing `name`, `type`, `platform`, and `config` fields.
