a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))
d = int(input('Enter fourth number  : '))
e = int(input('Enter fifth number : '))

list=[a,b,c,d,e]

if a>b and a>c and a>d and a>e:
   print("the largest number is",a)
elif b>a and b>c and b>d and b>e:
   print("the largest number is",b)
elif c>a and c>b and c>d and c>e:
   print("the largest number is",c)
elif d>a and d>b and d>c and d>e:
   print("the largest number is",d)
else:
   print("the largest number is",e)

if a<b and a<c and a<d and a<e:
   print("the smallest number is",a)
elif b<a and b<c and b<d and b<e:
   print("the smallest number is",b)
elif c<a and c<b and c<d and c<e:
   print("the smallest number is",c)
elif d<a and d<b and d<c and d<e:
   print("the smallest number is",d)
else:
   print("the smallest number is",e)








