import random
import re

# Define responses for the chatbot
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey, how can I help you?"],
    "project_idea": [
        "How about working on a sentiment analysis project using natural language processing?",
        "You could try building a recommendation system using collaborative filtering.",
        "Anomaly detection in time series data could be an interesting project to tackle.",
        "Why not explore deep learning techniques for image classification?"
    ],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!"]
}

# Function to generate response
def get_response(message):
    message = message.lower()
    if re.search(r'\b(hello|hi|hey)\b', message):
        return random.choice(responses["greeting"])
    elif re.search(r'\b(project|idea|work)\b', message):
        return random.choice(responses["project_idea"])
    elif re.search(r'\b(thanks|thank you)\b', message):
        return random.choice(responses["thanks"])
    else:
        return "I'm sorry, I'm not sure how to respond to that."

def chat():
    print("Welcome to the Chatbot!")
    user_message = ""
    while user_message != 'exit':
        try:
            user_message = input("You: ").strip().lower()
            if user_message == '':
                print("Chatbot: Please say something.")
                continue
            if user_message == 'exit':
                print("Chatbot: Goodbye!")
            else:
                bot_response = get_response(user_message)
                print("Chatbot:", bot_response)
        except KeyboardInterrupt:
            print("\nChatbot: Goodbye!")
            break

def main():
    chat()

if __name__ == '__main__':
    main()
