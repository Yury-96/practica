def plural_form(quantity, form1, form2, form3):
    t = quantity % 10
    h = quantity % 100
    result = str(quantity) + ' ' + form3
    if t==1 and h!=11:
        result = str(quantity) + ' ' + form1
    if (t>1 and t<5) and (h!=12 and h!=13 and h!=14):
        result = str(quantity) + ' ' + form2 
    return result


print(plural_form(1, 'яблоко', 'яблока', 'яблок')) #- 1 яблоко
print(plural_form(2, 'яблоко', 'яблока', 'яблок')) #- 2 яблока
print(plural_form(11, 'студент', 'студента', 'студентов')) #- 11 студентов
print(plural_form(15, 'студент', 'студента', 'студентов')) #- 15 студентов
print(plural_form(3, 'студент', 'студента', 'студентов')) #- 3 студента
print(plural_form(3, 'жена', 'жены', 'жён'))
print(plural_form(21, 'музей', 'музея', 'музеев'))
print(plural_form(102, 'премия', 'премии', 'премий'))
print(plural_form(0,'окно', 'окна', 'окон'))
print(plural_form(7,'гараж', 'гаража', 'гаражей'))

