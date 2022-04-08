arr = [1, 2, 3, 4, 5, 6,7]
'''
copy siginifica que vc esta copiando uma parte do array
se n fazer copy o array anterior vai sofrer as alterações que acontecerem com o 2
'''
arr2 = arr[:5] # pegando 5 primeiros posições 

arr2[0] = 100

print(f'''
arr1: {arr}
arr2: {arr2}
''')