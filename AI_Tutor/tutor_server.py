"""
Build an AI Tutor Chatbot
    Problem Statement
    Build an AI tutor chatbot that helps students understand programming concepts.

    Requirements
         Backend API using FastAPI.
         Frontend chat interface using Gradio.
         Use Gemini SDK for generating answers.
         The chatbot must:
    o Explain concepts step-by-step using Chain-of-Thought prompting.
    o Provide examples and exercises.
    o Use few-shot examples to teach Python topics.

Expected Features
     Step-by-step explanations
     Code snippets
     Follow-up questions from students

"""

import gradio as gr
from fastapi import FastAPI
from pydantic import BaseModel
import google.genai as genai


app= FastAPI()

class RequestData(BaseModel):
    prompt:str
    max_tokens: int = 5


@app.post("/tutor")
def generate_ans(data: RequestData):
    client = genai.Client(api_key="AIzaSyApZXmQxTPhsIAUlunhMWVckUbJtyhyyc4")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=data.prompt,
    )
    return {"generated_answer": response.text}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


