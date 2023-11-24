def create_phone_number(n):
    phone = []
    for elem in n:
        phone.append(elem)
    phone.insert(0, '(')
    phone.insert(4, ')')
    phone.insert(5, ' ')
    phone.insert(10, '-')
    phone_number = ''
    for elem in phone:
        phone_number += str(elem)
    return phone_number



print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
