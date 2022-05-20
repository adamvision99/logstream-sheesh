def bottlesLeft(bottles):
    s = str(bottles)
    if bottles == 0:
        return 'бутылок не осталось'
    mod = bottles % 10
    if mod == 1:
        return s + ' бутылка осталась'
    if mod > 1 and mod < 5:
        return s + ' бутылки осталось'
    return s + ' бутылок осталось'

def dropBottles(bottles, value):
    s = str(value)
    bottles -= value
    mod = value % 10
    if mod == 1:
        return s + ' бутылка упала, '
    if mod > 1 and mod < 5:
        return s + ' бутылки упало, '
    return s + ' бутылок упало, '

bottles_left = 100
drop = 1
while bottles_left > 0:
    if drop > bottles_left:
        drop = bottles_left
    bottles_left -= drop
    print(dropBottles(bottles_left, drop) + bottlesLeft(bottles_left))
