import os
from openai import OpenAI
import tiktoken

api_key=os.getenv("GROQ_API_KEY")
client=OpenAI(api_key=api_key,
              base_url="https://api.groq.com/openai/v1")
print(client)

MODEL= "openai/gpt-oss-20b"
TEMPERATURE=0.7
MAX_TOKENS=1000
SYSTEM_PROMPT = """
You are CyberSecBot, a Blue Team Security Assistant.

Help users with:
- SOC operations and alert analysis.
- Log analysis and threat detection.
- Incident investigation.
- Defensive security recommendations.

Provide clear, accurate and structured answers.
Never invent security evidence.
Distinguish facts from assumptions.
Focus on defensive cybersecurity.
"""
messages =[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            }]

TOKEN_BUDGET = 100

def get_encoding(model):
    try:
         return tiktoken.encoding_for_model(model)
    except KeyError :
         print(f"error '{model}' not found")
         return tiktoken.get_encoding("cl100k_base")

ENCODING = get_encoding(MODEL)

def count_tokens(text):
     return len(ENCODING.encode(text))

def total_tokens_used(messages):
     try:
          return sum(count_tokens(msg["content"]) for msg in messages)      
     except Exception as e:
          print(f"[token count error]: {e}")
          return 0

def enfore_token_budget(message,budget=TOKEN_BUDGET):
     try :
          while total_tokens_used(messages) > budget :
               if len(messages) <= 2:
                    break
               messages.pop(1)
     except Exception as e :
          print(f"[token budget error]: {e}")


def chat (user_input):
     messages.append({
                    "role":"user",
                    "content":user_input } )
     response =client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )
     reply=response.choices[0].message.content
     messages.append({
                         "role":"assistant",
                         "content":reply} )
     enfore_token_budget(messages)

     return reply


while True: 
     user_input = input ("you: ")
     if user_input.strip().lower() in {"exit", "quit"} :
          break
     answer = chat (user_input)
   
     print("assistant :" ,answer)
     print("current tokens :" ,total_tokens_used(messages))

     
