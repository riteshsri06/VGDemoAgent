import sys
from pathlib import Path

import streamlit as st


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from agent.fund_agent import ask_fund_agent


st.set_page_config(page_title="Fund Research Demo", page_icon="📊")
st.title("Fund Research Agent")
st.caption("Facts from Yahoo Finance. No investment recommendations.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask about a fund or ETF, such as VTI or compare VTI and SPY")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        try:
            answer = ask_fund_agent(question)
        except Exception as error:
            answer = f"The request could not be completed: {error}"
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})