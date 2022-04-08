import numpy as np

spaceDS = np.loadtxt("space.csv", 
                        delimiter=";",
                        dtype=str, 
                        encoding="utf-8")

print(spaceDS[2][7])
print(spaceDS[(spaceDS == 'Success').size/spaceDS.size])