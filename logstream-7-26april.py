#1
try:
    keys_list = read_list() # Keys
    len_kl = len(keys_list)

    values_list = read_list() # Values
    len_vl = len(values_list)

    if len_vl != len_kl:
        raise Exception(f'Error: {len_vl} != {len_kl}')

    print(dict(zip(keys_list, values_list)))
except Exception as e:
    print(e)

#2

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
print(sorted(my_dict.values())[-3:])

#3

def is_year_leap(year: int):
    return year % 4 == 0 or (year % 100 != 0 and year % 400 == 0)

for year in range(2000, 2023):
    print(f'{year} : {is_year_leap(year)}')
