students = {
    "male":["Tom","Charlie","Harry","frank"],
    "female":["sarah","huda","Samantha","Emily", "Elizabeth"]
    }
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
