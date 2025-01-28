# Setup

### Frontend: 
`npm install`

### Backend: 
1. Create new Python virtual environment called "env" `python -m venv env`
2. Activate environment `source env/bin/activate` (Mac) 
3. `pip install -r requirements.txt`
4. Create and fill in `.env` file with `OPENAI_API_KEY` and `MONGODB_URI`

## How to Run

### Frontend: 
`npm start`

### Gradio: 
ex. `python3 badwords.py`

### Backend:
`uvicorn app.main:app --reload`
