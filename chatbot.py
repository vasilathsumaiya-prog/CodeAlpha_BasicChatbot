from tkinter import *
def send_message():
    user_message = entry_box.get()
    chat_box.insert(END, "You: " + user_message + "\n")
    user_message = user_message.lower()
    if user_message == "hello":
        bot_reply = "Hello! Nice to meet you."
    elif user_message == "hi":
        bot_reply = "Hi there! How can I help you?"
    elif user_message == "how are you":
        bot_reply = "I am doing great. What about you?"
    elif user_message == "what is your name":
        bot_reply = "My name is AI Chatbot."
    elif user_message == "who created you":
        bot_reply = "I was created using Python and Tkinter."
    elif user_message == "what can you do":
        bot_reply = "I can chat with you and answer simple questions."
    elif user_message == "bye":
        bot_reply = "Goodbye! Have a wonderful day."
    elif user_message == "thank you":
        bot_reply = "You are always welcome."
    elif user_message == "good morning":
        bot_reply = "Good morning! Hope you have a great day."
    elif user_message == "good night":
        bot_reply = "Good night! Sleep well."
    elif user_message == "where are you from":
        bot_reply = "I live inside your computer."
    elif user_message == "tell me a joke":
        bot_reply = "Why do programmers prefer Python? Because it is easy to understand."
    elif user_message == "what is python":
        bot_reply = "Python is a popular programming language."
    elif user_message == "i am sad":
        bot_reply = "Don't worry. Everything will be fine soon."
    elif user_message == "i am happy":
        bot_reply = "That is wonderful to hear."
    else:
        bot_reply = "Sorry, I don't understand that."
    chat_box.insert(END, "Bot: " + bot_reply + "\n\n")
    entry_box.delete(0, END)
window = Tk()
window.title("AI Chatbot")
window.geometry("500x500")
window.config(bg="lightblue")
title_label = Label(
    window,
    text="AI CHATBOT",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title_label.pack(pady=10)
chat_box = Text(
    window,
    width=55,
    height=20,
    font=("Arial", 12)
)
chat_box.pack(pady=10)
entry_box = Entry(
    window,
    width=35,
    font=("Arial", 14)
)
entry_box.pack(side=LEFT, padx=10, pady=10)
send_button = Button(
    window,
    text="Send",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    command=send_message
)
send_button.pack(side=LEFT, padx=10)
window.mainloop()