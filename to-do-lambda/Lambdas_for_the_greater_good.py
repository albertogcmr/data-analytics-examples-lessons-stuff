import random


def is_even(num):
    return num % 2 == 0


variable = lambda num: num % 2 == 0

what_is_two = "Even Steven" if is_even(2) else "Odd as Todd"

if is_even(2):
    what_is_two = "Even Steven"
else:
    what_is_two = "Odd as Todd"

print(is_even(1))
print(is_even(2))

print(variable(1))
print(variable(2))

thing_to_sort = "iodsjfoiSADFasmfoie"
print(sorted(thing_to_sort, reverse=True))

thing_to_sort_2 = [(word, i) for i, word in enumerate("Hola qué tal andamos".split(' '))]
random.shuffle(thing_to_sort_2)

def nazi_message_key(nazi_message):
    return nazi_message[1]


def holis():
    print("Holis!!")

variable = holis()
print(variable)

print(sorted(thing_to_sort_2, key=lambda mensaje_nazi: mensaje_nazi[0][1]))