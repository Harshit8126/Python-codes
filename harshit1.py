speed=int(input('enter the speed of car:'))
if speed>80:
	print('Ticket 1')
elif speed<80 and speed>60:
	print('Ticket 2')
elif speed<60 and speed>40:
	print('Ticket 3')


