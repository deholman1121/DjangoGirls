print('Hello, Django girls!')

if 5 > 2:
    print("5 is indeed greater than 2!")
else:
    print("5 is not greater than 2")

name = "Dan"
if name == "Ola":
    print("Hello Ola!")
elif name == "Dan":
    print("Hello " + name)
else:
    print("Hello Anonymous!")

volume = 101
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect! I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

if volume < 20 or volume > 80:
    volume = 50
    print("That's better")


def hi(name):
    print('Hi, ' + name + '!')

hi("Dan")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Kris', 'Charli', 'Lilly']

for name in girls:
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print(i)