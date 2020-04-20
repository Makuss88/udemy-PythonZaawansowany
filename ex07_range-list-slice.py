colors = ["red", "orange", "green", "violet", "blue", "yellow"]


def get_list_of_colors(colors, n):
    return colors[:n]


for i in range(1, len(colors) + 1):
    print(get_list_of_colors(colors, i))

definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja...'

bracket_left = definition.index('(') + 1
bracket_right = definition.index(')')

print(definition[bracket_left:bracket_right])
