def chatbot():
    print("Hi there! I am a simple shopping chatbot. Type 'bye' to exit.")
    
    responses = {
        "hi": "Hello there! How can I assist you today?",
        "hello": "Hello there! How can I assist you today?",
        "hey": "Hello there! How can I assist you today?",
        "bye": "Goodbye! Have a great day!",
        "i need": "What kind of item do you need?",
        "what products do you have?": "We have laptops, smartphones, and headphones. What are you interested in?",
        "can you recommend": "Sure! What kind of recommendation are you looking for?",
        "i am": "Hello! How are you feeling today?",
        "feeling": "Good to hear that!",
    }

    while True:
        user_input = input("> ").strip().lower()  
        if user_input in responses:  
            print(responses[user_input]) 
            if user_input == "bye": 
                break
        else:
            print("I'm sorry, I didn't understand that. Can you rephrase?")

if __name__ == "__main__":
    chatbot()
