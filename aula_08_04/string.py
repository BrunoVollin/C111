import numpy as np

txt = "Nao custa nada se inscreva no mau canal"

print(f'''
fez: {np.char.find(txt, "custa")}
canal: {np.char.find(txt, "canal")}
''')