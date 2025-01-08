import nltk
from nltk.chat.util import Chat, reflections


reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by Codingal Edu. Pvt. Lim. You can call me Jarvis!"]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind"]
    ],
    [
        r"I am fine",
        ["Great to hear that. How can I help you?"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that. How can I help you? :)"]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude. Seriously, you are asking me this?"]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse"]
    ],
    [
        r"(.*) created ?",
        ["Shravan created me using Python's NLTK library", "Top secret ;)"]
    ],
    [
        r"(.*) (location|city) ?",
        ["Bangalore, Karnataka"]
    ],
    [
        r"how is the weather in (.*)?",
        ["The weather in %1 is awesome like always", "Too hot here in %1", "Too cold here in %1", "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an amazing company, though I've heard they are facing some challenges lately."]
    ],
    [
        r"(.*) raining in (.*)",
        ["No rain since last week here in %2", "Damn, it's raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy"]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of football and cricket."]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messi", "Ronaldo", "Rooney", "Virat Kohli", "M.S. Dhoni", "Rohit Sharma"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Benedict Cumberbatch"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Jarvis_Tech has many great articles with detailed step-by-step explanations and code. You should definitely check it out."]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
]



def mychat():
    print("Hi! I am a chatbot created by Codingal Edu. Pvt. Lim. for your service.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

# Initiate the conversation
if __name__ == "__main__":
    mychat()