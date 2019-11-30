"""
def outer():
	
	counter=0
	def inner():
		nonlocal counter
		print("hello world")
		counter+= 1
		print(counter)
	inner()
	inner()
	inner()	
outer()	
"""

def outer():
	
	counter=0
	def inner():
		nonlocal counter
		counter+= 1
		print(counter)
	return inner	

hello=outer()	
hello()
hello()
hi=outer()
hello()
hello()
hi()
hi()
