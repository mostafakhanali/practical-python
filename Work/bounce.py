# bounce.py
#
# Exercise 1.5
height = 100 # Initial height(meters)

for _ in range(10):
    height = (3/5) * height
    print(round(height,5))