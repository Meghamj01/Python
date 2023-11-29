
from random import choice

questions = ["why is the sky blue?: ", "why is there a face on the moon?: ", "where are these all dinasourous?: "]
question = choice(questions)
answer = input(question).lower().strip()

while answer != "just because":
    answer = input("why..?").strip().lower()
    print("ohhh alas Okay")
    
    
