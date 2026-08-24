# Copilot Instructions - Fund & ETF Reaserch Agent

## Goal
The goal of this app is to provide a Fund & ETF Research Agent that can answer questions about funds and ETFs. The agent will be able to provide information about the fund's performance, holdings, and other relevant data, using natural language processing. There wil be chat based interface for users to interact with the agent and ask questions about funds and ETFs. The agent will be able to provide answers in a conversational manner, making it easy for users to understand the information provided.

## Technology Stack:
- UI: Streamlit
- Backend: Python
- Agent: LangChain
- Data: Yahoo Finance API

## Architecture:
UI Layer (Streamlit) <-> Agent Layer (LangChain) <-> Data Layer (Yahoo Finance API)

## Agent: 
- Use tools to retrive Fund & ETF data from Yahoo Finance API
- For Fund comparison do not use LLM , it need to be diterministic logic using python code to compare the funds and ETFs based on their performance, holdings, and other relevant data. The agent will be able to provide a comparison of the funds and ETFs in a tabular format, making it easy for users to understand the differences between them.
- if the data is not available say "Data not available for the requested fund or ETF."

## Code Style
- Keep the implementation simple as this for demo purpose only and to be executed from local machine. Do not use any complex architecture or design patterns.
- 

## Project Structure
VGDemoAgent
    ├───.github
    ├───app
    ├───data
    └───src
        ├───agent
        └───tools

