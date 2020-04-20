import datetime
"""
price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)
"""
price = 123
bonus = 23
bonus_granted = False


# print(price) if bonus_granted else print(price-bonus)

'''
rating = 5

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')
'''
rating = 2

# print('vg') if rating == 5 else print('g') if rating == 4 else print("w")


day_of_week = datetime.datetime.now()
print(day_of_week.weekday())
dict_weeks = {0:"MON",
              1:"TUE",
              2:"WEN",
              3:"THR",
              4:"FRI",
              5:"SAT",
              6:"SUN",}

if day_of_week.weekday() == 0:
    print(dict_weeks[0])
elif day_of_week.weekday() == 1:
    print(dict_weeks[1])
elif day_of_week.weekday() == 2:
    print(dict_weeks[2])
elif day_of_week.weekday() == 3:
    print(dict_weeks[3])
elif day_of_week.weekday() == 4:
    print(dict_weeks[4])
elif day_of_week.weekday() == 5:
    print(dict_weeks[5])
elif day_of_week.weekday() == 6:
    print(dict_weeks[6])


print(dict_weeks[0] if day_of_week.weekday() == 0 else
      dict_weeks[1] if day_of_week.weekday() == 1 else
      dict_weeks[2] if day_of_week.weekday() == 2 else
      dict_weeks[3] if day_of_week.weekday() == 3 else
      dict_weeks[4] if day_of_week.weekday() == 4 else
      dict_weeks[5] if day_of_week.weekday() == 5 else
      dict_weeks[6])