import numpy as np

arr = np.random.seed(10)

arr = np.random.randint(1, 11, 11)
'''
copy siginifica que vc esta copiando uma parte do array
se n fazer copy o array anterior vai sofrer as alterações que acontecerem com o 2
'''
arr2 = arr[:5].copy() # pegando 5 primeiros posições 

arr2[0] = 100

print(f'''
arr1: {arr};
arr2: {arr2};
''')