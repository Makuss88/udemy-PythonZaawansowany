text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']

f = lambda x: len(x)
word = "makuss"

print(f(word))
print("-"*30)
print(list(map(f, text_list)))
print("-"*30)
print(list(map(lambda string: len(string), text_list)))