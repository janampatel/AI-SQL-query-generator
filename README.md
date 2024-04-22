# AI-SQL-query-generator
This repository contains the project for AI based SQL query generator based on natural language based input of user. This repository was originally developed for our submissions at CSI HackNUthon, Nirma University

This is a minimalistic web application built with Streamlit that allows users to generate SQL queries based on their inputs locally using LM studio.

## Pre requisites
Libraries:
flask, openai, pathlib, streamlit, streamlit_lottie 
Others:
LM studio, VS code, SQL Lite, Browser(for user interaction)

## How to Use
1. Input your ddl, such as table names, columns, conditions, etc.
2. Input Natural language query from user to retrieve data.
3. Click on the "Generate Query" button to generate the SQL query based on your inputs.
4. Copy the generated SQL query and use it in your database operations.
5. To avoid step 4, we tried to implement the 'sql.py' file so that the extracted query can directly can be used on input database.
6. We also tried to implement a chatbot like structure for making a full fledged AI-SQL chatbot in 'text.py'.

Contributions are welcome for this project.
