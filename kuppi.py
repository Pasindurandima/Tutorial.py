

print ("mora")
print ("pasindu randima")
print('pasindu randima')

print ("ITUM \n Diyagama")

print ('hello "world" Ndt')

print ("ITUM \t Diyagama")

Name = "Randima"
print (Name)

Name = 'pasindu'
print (Name)

txt = str ("hello")
print(txt)

age = int ("22")
print(age)

x = 5>2
print  (x)

y = 10 == 5
print (y)

z = float (0.02)
print(z)

txt ="pasindu"
print(type (txt))

age = 22
print(type (age))

z = 0.05
print(type (z))

a = True
print(type (a))

c = 5.7
d = int(c)
print (d)

x = "6.45"
y = float (x)
print (y)

x = 10
y = float (x)
print (y)

x = 10
y = 5

print(x+y)
print(x-y)
print (x /y)
print (x % y )
print (x//y)
print (x**y)

x = 2 ** 2 ** 3
print(x)

x = 5
print (x +3)

x = True
y = False

print ( x and y)
print (x or Y)

list1 = [ 'A','B','C']
list2 = [ 1,2,3,4,5]

print(list1)
print(list2)

print(type(list1))
print(type(list2))

list1.append('D')
print(list1)

name = [ 'A','B','C']
name.insert ( 1, 'F')
print (name)

list2.insert(2,'10')
print (list2)

list1.remove ('B')
print(list1)

name = [ 'A','B','C']

name.pop ()
print(name)

name = [ 'A','B','C']

name.pop (1)
print(name)

y = [1,2,2,1]
y.remove (1)
print(y)

x = ['A','B','A','C']
x.remove('A')
print(x)

age = [1,2,3,4,5]
x = age [1: ]
print(x)

age = [1,2,3,4,5]
y = age [1:4]
print(y)

age = [1,2,3,4,5]
z = age [:4]
print(z)

age = [50,16,60,90]
age.sort ()
print (age)

age = [50,16,60,90]
age.sort (reverse = True)
print (age)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = {'name' : 'randima' }
y = x.keys()
print(y)

z = x.values()
print(z)

x ['age'] = 23
print (x)

x = {'a','b','c','a','d','c'}
print (x)

y = {'a','a'}
print (y)

x = 5
y = 3

if x > y :
    print("hiii")
else:
    print("wrong")

x = 15
y = 20

if x != y :
    print("true")
else:
    print("wrong")

x = 5
y = 3

if x < y :
    print("hiii")
else:
    print("wrong")




marks =25
if marks < 0 or marks > 100:
    print ("wrong")

elif marks > 75:
    print ("your result : A")    

elif marks > 65:
    print ("your result :B")

elif marks > 55:
    print ("your result :c")
    
elif marks > 35:
    print ("your result :s")

else:
    print ("your result :W")

    

def marks():
    print("Hello")
marks()

def student(marks):
    print(f"student mark is {marks}")
student(60)

def student(age):
    print(f"student mark is {age}")
student(60)
student(20)
student(10)

x = [1,2,3,4,5]
for i in x :
    print(i)

#sum of 1-100

total = 0
for i in range(101):
    total = total + i
    print(total)
print(total)

#1-100 sum of odd & even

odd = 0
even = 0

for i in range (101):
    if i%2 == 0 :
        even = even + i

    else :
        odd = odd + i
print ("sum of odd numbers",odd)
print ("sum of even numbers",even)

x = 7
y = 5

count = 0
x = 5
while  x > count:
    print("hiii")
    count +=1

for i in range (11):
    if i == 5 :
        break
    else:
        print(i)




count = 0
number= 10

while count < 10:
 
  if count == 5:
    break

  else:
    count += 1
    print(count)

    

count = 0
number= 10

while count < 10:
 
  if count == 5:
    continue

  else:
    count += 1
    print(count)   
    










