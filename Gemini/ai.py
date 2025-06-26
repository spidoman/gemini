# pip install google-generativeai

import google.generativeai as gemini

# find api key at https://aistudio.google.com/apikey

API_KEY = "YOUR_API_KEY"
gemini.configure(api_key=API_KEY)

model = gemini.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

print("Chat with Gemini! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
