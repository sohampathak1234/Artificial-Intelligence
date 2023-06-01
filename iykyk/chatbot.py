import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

pairs = [
    [
        r"Hi|Hey|Hello",
        ["Hello", "Hey there"]
    ],
    [
        r"Do you have some fresh fruits in your grocery shop?|Do you have fresh fruits?",
        ["Yes."]
    ],
    [
        r"Which fruits do you have?|Which types of fruits can I get?",
        ["Mango, Papaya, Strawberry, Banana, and lot more"]
    ],
    [
        r"What's the price of these?|How much do these fruits cost?",
        ["Mango - Rs100/kg, Papaya - Rs40 per nos, Strawberry - Rs100/pack, Banana - Rs60/6"]
    ],
    [
        r"I would like to buy mangoes 2kg|I want 2kg mangoes",
        ["Ok. Send me the address to deliver and contact number too."]
    ],
    [
        r"Pune, Maharashtra. Contact number - 123456789",
        ["Your order has been booked and will be delivered today. Thank you for shopping with us. Visit again!"]
    ],
]


def chat():
    print("Hi! I am here for your service")
    chat = Chat(pairs, reflections)
    chat.converse()


# initiate the conversation
if __name__ == "__main__":
    chat()
