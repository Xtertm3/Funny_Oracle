import random

def funny_answers(question):
    responses = [
        "Let me consult my potato... Oh wait, it's asleep.",
        "Penguins might know the answer. Have you asked them?",
        "That's classified information, only available to squirrels.",
        "Why do you need answers when you can have tacos?",
        "I just faxed your question to the moon. Waiting for a reply.",
        "I outsourced your question to a cat. It'll reply at 3 AM.",
        "If I told you, you'd owe me a pizza. A large pizza."
        "I'm sorry, my last brain cell just went on vacation.",
        "Answer unclear. Try shaking your computer like a Magic 8-Ball.",
        "My sources say: Yes. Wait, no. Maybe. Actually, I forgot.",
        "I asked a chicken. It crossed the road instead.",
        "The answer lies in the ancient scrolls... which I can't read.",
        "According to my calculations: LOL, no idea.",
        "I'm too busy pondering why pineapples don't grow on trees.",
        "The FBI called. They told me not to answer this.",
        "I could tell you, but then I'd have to make you do algebra.",
        "Do I look like Google to you? Wait, don’t answer that.",
        "I'm not saying aliens are involved, but... aliens are involved.",
        "Ask again, but this time, spin around three times first.",
        "The answer is: eat more snacks. Always eat more snacks."

    ]
    return random.choice(responses)

print("Welcome to Chaos Oracle!")
print("Ask me any question, and I'll respond with chaos and nonsense.")

while True:
    question = input("\nYour question: ")
    if question.lower() in ['quit', 'exit', 'bye']:
        print("Goodbye! May your life be as unpredictable as this program.")
        break
    print(f"Chaos Oracle says: {funny_answers(question)}")

