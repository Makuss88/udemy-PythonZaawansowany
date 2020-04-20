projects = ['Brexit', 'Nord Stream', 'US Mexico Border', 'Makuss888']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton', 'Grzes']
dates = ['2016-06-23', '2016-08-29', '1994-01-01', '2001-05-05']

for p, l in zip(projects, leaders):
    print('The leader of', p, 'started', 'is', l)

print('-' * 80)

for p, l, d in zip(projects, leaders, dates):
    print('The leader of', p, 'started', d, 'is', l)

print('-' * 80)

for count, (p, l, d) in enumerate(zip(projects, leaders, dates), 1):
    print(count, '- The leader of', p, 'started', d, 'is', l)
