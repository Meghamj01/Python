even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)

words = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
answers = [[w.upper(), w.lower(), len(w)] for w in words]
print(answers)
