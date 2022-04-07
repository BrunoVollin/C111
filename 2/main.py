import numpy as np

#1
np.random.seed(5)

a = np.random.rand(10) * 100
b = a.astype(int)

print(f'''
Question 1:
    a : {a}
    b : {b}
''')

#2
np.random.seed(10)

a = np.random.randint(1, 50, size=(5, 5))
print(f'''
Question 2:
    a :
{a}
''')

#3
x = np.median(a, axis=0)
y = np.median(a, axis=1)
larger_x = np.max(x)
larger_y = np.max(y)


print(f'''
Question 3:
a :
{a}

median {{
    axis 0 : {x},
    axis 1 : {y},
    larger_x : {larger_x},
    larger_y : {larger_y},
}}
''')

#4
count = np.bincount(a.flatten())
twice = np.where(count == 2)[0]


print(f'''
Question 4:
count :{count}
twice:{twice}
''')




