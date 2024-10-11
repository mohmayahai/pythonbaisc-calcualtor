# sort(method = used with lists
#sort function) = used with iterable

students = ['Squiward','Sandy','Patrick','Spongebob','Mr. Kracbs']
students2=('Squiward','Sandy','Patrick','Spongebob','Mr. Kracbs')

students.sort(reverse = True)

for i in students:
    print(i)

print(students)

sorted_students = sorted(students2)
for i in sorted_students:
    print(i)
print(sorted_students)


#keyword arguemnets

student3=[ ('Squidwaard','F',60),
          ('Spongebob','A',50),
          ('Mr Krabs','B',90),
          ('Sandy','D',89),
          ('Patrick','C',60),]

grade = lambda grade:grade[1]

print(student3.sort(key=lambda grade:grade[1]))
for i in student3:
    print(i)

#map
store=[('Shirt',20.00),
       ('Pants',20.00),
       ('Jacket',50.00),
       ('Socks',10.00)]

to_euros= lambda data:(data[0], data[1]*0.82)
to_dollars = lambda data:(data[0],round(data[1]/0.82,4))

store_euros =list(map(to_euros,store))
store_dollars =list(map(to_dollars,store))

for i in store_euros:
    print(i)

for i in store_dollars:
    print(i)


#filter() =creates a collection of elements from a n iterable for whihc function returns , function, iterable
#filter(function,iterbale)

friends = [('Rachel',19),
           ('Monica',18),
           ('Chandler',24),
           ('Joey',14),
           ('Phoebe',23),
           ('Ross',19)]

drink_1=filter(lambda age:age[1]>18,friends)
for i in drink_1:
    print(i)
#reduce() = a fucntion for an iterable and reduce toa cummlative single value
import functools
factorial=[5,4,3,21,1,12,12]
result = functools.reduce(lambda x,y:x*y,factorial)
print(result)


