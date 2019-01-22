rollno=int(input('enter your roll no:'))
a=rollno%10
b=rollno//10
if (a+b==6) or (a-b==6) or (a*b==6) or (a/b==6):	
	print('you have lucky roll no.')
else:
	print('you did not have a lucky roll no because u are GENIUS.')
 
