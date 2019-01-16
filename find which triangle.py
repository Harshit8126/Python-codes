a=int(input('enter the first side:'))
b=int(input('enter the second side:'))
c=int(input('enter the third side:'))
if a+b>c or b+c>a or c+a>b:
    print('triangle is valid')
    if a==b or b==c or c==a:
        print('given triangle is isosceles triangle')
    elif a*a + b*b ==c*c or c*c +b*b ==a*a or a*a +c*c ==b*b :
         print('given triangle is right angled triangle')
    else :
        print('given triangle is scalene triangle')
else:
    print('invalid side')
    
        
            
