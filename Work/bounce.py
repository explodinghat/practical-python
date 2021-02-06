# bounce.py
#
# Exercise 1.5
bounce_height = 100
bounce_number = 1

for bounce_number in range(0,10):
    bounce_height = bounce_height
    bounce_height = bounce_height * 0.6
    bounce_number = bounce_number + 1
    print(bounce_number, (round(bounce_height,4)))
    
