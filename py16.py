x = int(input())
y = int(input())
if x>=2 and x<=3 and y>= -5 and y<= -2:
    print("no yes")
elif x > 3 and x <= 6 and y >= -5 and y <= 1:
    print("no yes")
elif x == 3 and y == 1:
    print("no yes")
elif x == 3 and y ==-2:
    print("no yes")
elif x == 3 and y == -1:
    print("no yes")
elif x>= 2 and x<=3 and y>-2 and y <= 1:
    print("yes yes")
elif x>=1 and x < 2 and y>= 2 and y<=-1:
    print("yes no")
elif x==1 or x == 2 and y == -2:
    print("no no")
elif x >= -1 and x < 0 and y>= -1 and y<=2:
    print("yes no")
elif x == -1 and y == 1 or y == 2:
    print("no no")
elif x >= 0 and x<2 and y>=1 and y <= 2:
    print("yes no")
else: 
    print("no no")
