import openai

openai.api_key = "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"

def chat_with_gpt(prompt, max_tokens= 30):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages =[
            # Change the role and content ticket booking assistant, Language translator...etc
            {"role": "system", "content": "ticket booking assistant"}, 
            {"role":"user", "content": prompt}
            ],
        max_tokens= max_tokens
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("Bot: Hi! I'm a ticket booking assistant. You can ask me about available flights, prices, and booking details.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit", "stop"]:
            print("Goodbye! If you have more questions, feel free to ask.")
            break

        response = chat_with_gpt(user_input)
        print("Vika: ",response)

