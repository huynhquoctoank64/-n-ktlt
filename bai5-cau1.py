print("Huynh Quoc Toan MSV:235752021610081")

import mymath

values = [2, 4, 6, 8, 10]

print('Squares:')
for v in values:
    print(mymath.square(v))

print('Cubes:')
for v in values:
    print(mymath.cube(v))

print('Average:', mymath.average(values))