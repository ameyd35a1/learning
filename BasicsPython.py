name="John"
age= 54
balance= 53.44
hobbies=["cricket","football","chess","netflix"];

#string Concatenation
print ("%s's age is %d" % (name,age))
print ("Hobbies are: %s" % hobbies)
print ("Your current balance is %.2f$" % balance)

#Conditions
if name.lower()=="john" and age == 54:
	print ("You are right!")

if "cricket" in hobbies:
	print ("cricket is a good sport!")

#Functions
def print_hobbies(hobbies):
	len = len(hobbies);
	print ("length is %d" % len)
	while len > 0:
		print (hobbies[len-1])
		len -= 1
	else:
		print ("Get some more hobbies")

#Class
class vehicle:
	value=0
	color=""

	def __init__(self,color,value):
		self.value = value
		self.color = color

	def display_details(self):
		print ("Vehicle is of color %s of value $%d" % (self.color, self.value))

v1 = vehicle("red",60000)
v2 = vehicle("blue",10000)

v1.display_details()
v2.display_details()

#Dictionary
phonebook = {
	"John": 938477566,
	"Jack": 938077456,
	"Jill": 945871237
}

phonebook.pop("Jack")
phonebook["Jake"] = 987456321

for name,number in phonebook.items():
	print ("Phone number of %s is %d" % (name, number))


#Generators
def fib():
	a,b = 0,1
	while True:
		yield a
		a,b = b, a+b


import itertools
print (list(itertools.islice(fib(),10)))

#List Comphrension
sentence = "the quick brown fox jumos over the lazy dog"
words = sentence.split()
words_length = [len(word) for word in words if word != "the"]
print (words_length)

#Multiple function arguments
def foo(first,second,*therest):
	print ("First argument is %s" % first)
	print ("Second argument is %s" % second)
	print ("Remaining arguments are %s" % list(therest))

foo(1,2,3,4,5)

def bar(first,second,**options):
	print ("First argument is %s" % first)
	print ("Second argument is %s" % second)
	if options.get("action") == "post":
		print ("Value posted is %s" % options.get("value"))

bar(1,2, action="post", value=5000)

#Exception handling
def error_func():
	try:
		the_list=(1,2,3,4,5,6)
		the_list[6]
	except IndexError:
		print ("Error handled successfully!")

error_func()

#Sets
a = set(["A","B","C","D"])
b = set(["B","E","F","C","G"])

print ("Common elements: %s" % a.intersection(b))
print ("Unique elements in 'a': %s" % a.difference(b))
print ("Unique elements in 'b': %s" % b.difference(a))
print ("All elements: %s" % a.union(b))
print ("Unique elements in a and b: %s" % a.symmetric_difference(b))

#Serialization
import json
str = json.dumps([1,2,"a","b"])
print (json.loads(str))

def add_details(obj, name, salary):
	salaries = json.loads(obj)
	salaries[name] = salary
	return json.dumps(salaries)
salaries = '{"A": 720, "B": 500, "C": 600}'
salaries = add_details(salaries, "D", 200)
print (json.dumps(salaries))

#Partial functions
from functools import partial
def funcTools(u,v,w,x):
	return u*5+v*2+w*3+x*6

p1 = partial(funcTools,2,3)
p2 = partial(funcTools,2,3,4)
print (p1(4,5))
print (p2(5))

#Closures : Embedded functions
def multiplier_of(n):
	def multiplier(number):
		return number*n
	return multiplier

multiplywith5 = multiplier_of(5)
print (multiplywith5(9))

#Decorator : Rename existing functions, methods and classes
def formatter(fn):
	def string_format(*args,**options):
		return "<p>Text is %s</p>" % fn(args[0])
	return string_format

@formatter
def string_display(text):
	return text

print (string_display("Confidential"))

def p_decorate(func):
	def func_wrapper(*args, **kwargs):
		return "<p>%s</p>" % func(*args, **kwargs)
	return func_wrapper

class Person(object):
	def __init__(self, name, lastname):
		self.name = name
		self.family = lastname

	@p_decorate
	def get_fullname(self):
		return self.name+" "+self.family


my_person = Person("Joe","Don")
print (my_person.get_fullname())

def tags(tag_name):
	def tags_decorator(func):
		def func_wrapper(*args,**kwargs):
			return "<{0}>{1}</{0}>".format(tag_name, func(*args,**kwargs))
		return func_wrapper
	return tags_decorator

@tags('p')
@tags('strong')
def get_text(name):
	return "Hello %s" % name

print (get_text("Phil"))
