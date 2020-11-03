from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init ()

int
number = 24 

str
name = "Влад" 

print (Back.GREEN)
print (Fore.BLACK)

print ('Привет')

print("Меня зовут " + name + "\nМне " + str(number) + " года. \nКак тебя зовут?")

print (Back.CYAN)
print (Fore.BLACK)

name1 = input( "Меня зовут ")

print (Back.GREEN)
print (Fore.BLACK)

print ("Отлчино, приятно познакомиться, " + name1 + "!" + "\nСколько тебе лет?")

print (Back.CYAN)
print (Fore.BLACK)

age = input ("Мне ")

print (Back.GREEN)
print (Fore.BLACK)

print ( str(age) + " это круто! Ты заметил, погода что-то часто меняется. \nЯ кстати знаю погоду по всему миру. \nВ каком городе ты живешь?")

print (Back.CYAN)
print (Fore.BLACK)

import pyowm

owm = pyowm.OWM('bb4a1cf498eaea7d00754f57fed8c2e9')
mgr = owm.weather_manager()

place = input ()

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius') ["temp"]

print (Back.GREEN)
print (Fore.BLACK)

from translate import Translator

translator= Translator(from_lang="english",to_lang="russian")
translation = translator.translate(w.detailed_status)

print ("В городе " + place + " сейчас " + translation)


print ("Температура сейчас в районе " + str(temp) + " градусов")
if temp < 15:
	print ("Прохладно уже, одевайся теплее ;)")
elif temp > 14:
	print ("Снова тепленько, но возьми с собой кофточку")
print ('Надеюсь тебе было полезно, мне достаточно просто "спасибо"')

print (Back.CYAN)
print (Fore.BLACK)

input ()
 	
print (Back.GREEN)
print (Fore.BLACK)

print("Не за что, а еще я умею считать, хочешь посчитаем?")

print (Back.CYAN)
print (Fore.BLACK)

input()


print (Back.WHITE)
print (Fore.BLACK)

what = input ("Что делаем? +, -, /, *: ")


a = float (input("Введите первое число:"))
b = float (input("Введите второе число:"))

if what == "+":
	c = a + b
	print ("Результат " + str (c))
elif what == "-": 
	c = a - b
	print ("Результат " + str (c))
elif what == "/": 
	c = a / b
	print ("Результат " + str (c))
elif what == "*":
	c = a * b
	print ("Результат " + str(c))
else: 
	print ("Выбрана неверная команда")

print (Back.GREEN)
print (Fore.BLACK)
print ("Хотите повторить? (+ или -)")

print (Back.WHITE)
print (Fore.BLACK)
y = input ()

while y == "+":

	what = input ("Что делаем? +, -, /, *: ")
	a = float (input("Введите первое число:"))
	b = float (input("Введите второе число:"))

	if what == "+":
		c = a + b
		print ("Результат " + str (c))
	elif what == "-": 
		c = a - b
		print ("Результат " + str (c))
	elif what == "/": 
		c = a / b
		print ("Результат " + str (c))
	elif what == "*":
		c = a * b
		print ("Результат " + str(c))
	else: 
		print ("Выбрана неверная команда")

	print (Back.GREEN)
	print (Fore.BLACK)
	print ("Хотите повторить? (+ или -)")

	print (Back.CYAN)
	print (Fore.BLACK)
	y = input ()

	if y == "-":
		print (Back.GREEN)
		print (Fore.BLACK)
		print ("Спасибо за внимание, пока!")
		
		print (Back.CYAN)
		print (Fore.BLACK)
		input ()
