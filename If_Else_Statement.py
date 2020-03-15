#If Else Statements


#Boolean Expression

print (20 > 10)
print (20 == 10)
print (20 < 10)
print (bool("Hello World"))
print (bool(20))


Python Conditions

Equals						-> x == y
Not Equals					-> x != y
Less Than					-> x <  y
Less Than or Equals 		-> x <= y
Greater Than 				-> x >  y
Greater Than or Equals 		-> x >= y
Boolean OR 					-> x or y , x | y
Boolean AND 				-> x and y, x & y
Boolean NOT 				-> not x


if -
else 


#If statement

x = 60
y = 7

if x > y:
	print ("x is greater than y")

#Elif

x = 70
y = 70

if x > y :
	print ("x is greater than y")
else
	print ("x and y are equal")


#Else

x = 50
y = 150
if x > y:
	print ("x is greater than")
if x == y:
	print ("x and y are equal")
else:
	print ("x is less than y")

#Short Hand If

if x > y: print("x is greater than y")

#Short hand if ... else

x = 50
y = 150
print (x) if x > y else print (y)


#And is logical operator

x = 50
y = 40
z = 100
if x > y and z > x:
	print("All Conditions are true")

#Or is logical operator

x = 50
y = 40
z = 100

if x > y or z < y:
	print ("One of the condition is true")
elif x > y and z > y:
	print ("All Conditions are True")
else:
	print ("Nothing else")


x = 50

if x >10:
    print("x is ten")
    if x > 20
        print("x is greater than 20")
    else:
        print("No, x is not greater than 20")
        
if x > 10 and x != 10 or x > 20:
    print("x is greater than 10 and 20")
else:
    print("x is not greater than 10 & 20")



