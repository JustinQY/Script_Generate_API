#!/bin/zsh

uvicorn app:app --host 0.0.0.0 --port 8000 &

streamlit run ./streamlit_app.py --server.port 7860 --server.enableCORS false