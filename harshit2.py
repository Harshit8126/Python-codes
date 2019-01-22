#Program to calculate area and perimeter of ractangle using a single function:--
def rectangle(l,b):
	return l*b,2*(l+b)
l=int(input('enter the value of length:'))
b=int(input('enter the value of breadth:'))

area,perimeter=rectangle(l,b)
print(area)
print(perimeter)

