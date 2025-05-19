* Pre-Req:
1. Install uv: [Getting Started](https://docs.astral.sh/uv/getting-started/installation)  
`curl -LsSf https://astral.sh/uv/install.sh | sh`

* Running the code
1. `cd sandbox` (if not already)
2. Populate .env file  
```
GROQ_API_KEY=<API_KEY>
```
3. `uv sync`
4. `uv run simple-groq-openapi.py`
5. `uv run agent-groq-openapi.py`
6. `uv run server.py`
7. `uv run main.py`