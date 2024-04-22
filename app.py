import re
import os
import json
import openai
import pathlib
import streamlit as st # type: ignore
from openai import OpenAI
from streamlit_lottie import st_lottie

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


st.set_page_config(
    page_title="SQL Query Generator",
    page_icon="✨",
    layout= "wide",
    initial_sidebar_state="expanded",
    menu_items={
    'Get Help': 'https://github.com/mann1105',
    'Report a bug': "mailto:patelman567@gmail.com",
    'About': "## A minimalistic application to generate SQL queries using OpenAI APIs built with Python and Streamlit"
    } )

@st.cache_data()
def lottie_local(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.cache_data()
def hide_footer():
    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Natural Language to SQL Query")
hide_footer()

col1, col2 = st.columns(2)
with col1:
    anim = lottie_local(r"./assets/animation.json")
    st_lottie(anim,
            speed=1,
            reverse=False,
            loop=True,
            height = 700,
            width = 700,
            quality="high",
            key=None)

with col2:
    st.markdown("-----------------------------")
    english_input = st.text_area("Please enter the desired question and see the sqlcoder's magic 💫", height = 250)

    prompt = f"Translate this natural language query into syntactically correct SQL:\n\n{english_input}\n\nSQL Query:"
    st.markdown("-----------------------------")
    ch = st.checkbox("Table Schema")
    if ch:
        schema = st.text_area("Enter Table Schema 📝")
        # prompt = f"Translate this natural language query into syntactically correct SQL:\n\n{query}\n\nUse this table schema:\n\n{schema}\n\n{prompt}"
        prompt = f"""
        ### Task

        Generate a SQL query to answer the following question: {english_input}

        ### PostgreSQL Database Schema

        The query will run on a database with the following schema:

        {schema}

        ### Answer

        Here is the SQL query that answers the question: {english_input}

        ```sql

        """
        st.markdown("-----------------------------")
    if st.button("Generate SQL Query ✨", use_container_width=True):
        with st.spinner("Working.. 💫"):
            try:
                completion = client.chat.completions.create(
                    model = "TheBloke/sqlcoder-7B-GGUF",
                    messages = [
                        {"role": "user", "content":prompt}
                    ]
                )

                response = completion.choices[0].message.content.split("sql")[-1].strip()
                st.balloons()
                st.markdown("### Output:")
                st.success(f"{response}")
            except Exception as e:
                st.error(f"Error: {e}")
