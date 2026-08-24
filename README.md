# VGDemoAgent

Simple local Fund and ETF research agent demo.

## Run locally

1. Install dependencies: `pip install -r requirements.txt`
2. Set `ANTHROPIC_API_KEY` in `.env`.
3. Start the UI: `streamlit run app/streamlit_app.py`

The agent uses Yahoo Finance for fund data and deterministic Python logic for comparisons. It reports ticker, fund name, AUM, expense ratio, and the average annual adjusted-close return across the available five-year history. Missing data is reported as unavailable; no investment recommendations are generated.