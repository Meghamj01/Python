



def about(name,age,likes):
    sentence = "Meet {}! They are {} years old and They likes {}".format(name,age,likes)
    return sentence

answer = about("jack",23,"python")

print(answer)



dictionary = {"name":"ziyad", "age":23 , "likes":"python"}
y = about(**dictionary)   #unpacking
print(y)
