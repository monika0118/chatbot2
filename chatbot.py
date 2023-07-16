import random

# Define a dictionary of responses
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm good, thanks!", "I'm doing great!", "All is well!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm sorry, I didn't understand that.", "Could you please rephrase that?"]
}

# Function to generate a response
def generate_response(message):
    message = message.lower()
    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(responses["default"])

# Main chat loop
while True:
    user_input = input("User: ")
    response = generate_response(user_input)
    print("ChatBot:", response)
