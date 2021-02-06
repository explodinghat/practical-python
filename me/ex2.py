lego_brick_height = 9.6 * 0.001
everest_height = 8889
num_bricks = 1
day = 1

while num_bricks * lego_brick_height < everest_height:
    print(day, num_bricks, num_bricks * lego_brick_height)
    day = day + 1
    num_bricks = num_bricks + 1

number_of_years = day / 365

print('Number of days', day)
print('Number of bricks', num_bricks)
print('Final height', num_bricks * lego_brick_height)
print('Years taken:', number_of_years)
