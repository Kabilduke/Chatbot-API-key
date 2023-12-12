import openai
import streamlit as st

openai.api_key = "Enter your openai API key"

def chat_with_gpt(prompt, max_tokens=30):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Language translator "},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    st.title("Language Translator")
    st.write("Bot: Hi! I'm a language translator assistant. You can ask me about language")

    user_input = st.text_input("You:")
    
    if user_input.lower() in ["quit", "bye", "exit", "stop"]:
        st.write("Goodbye! If you have more questions, feel free to ask.")
    else:
        response = chat_with_gpt(user_input)
        st.write("Vika:", response)
