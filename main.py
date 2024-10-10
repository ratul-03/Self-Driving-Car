import pygame
pygame.init()

# Taking Varriables
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 155
car_y = 300
car_x_offest = 0
car_y_offest = 0
focal_dist = 25
direction = 'up'
drive = True
clock = pygame.time.Clock()

while drive:
    clock.tick(60)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            drive = False
    # Detect Road
    camera_x = car_x + car_x_offest + 15
    camera_y = car_y + car_y_offest + 15
    up_px = window.get_at((camera_x, camera_y - focal_dist))[0]
    down_px = window.get_at((camera_x, camera_y + focal_dist))[0]
    right_px = window.get_at((camera_x + focal_dist, camera_y))[0]
    print(up_px, right_px, down_px)

    # Take Turn 
    if (up_px != 255 and right_px == 255 and direction == 'up'):
        direction = 'right'
        car_x_offest = 30
        car = pygame.transform.rotate(car, - 90)
    elif (direction == 'right' and right_px != 255 and down_px == 255):
        direction = 'down'
        car_x = car_x + 30
        car_x_offest = 0
        car_y_offest = 30
        car = pygame.transform.rotate(car, -90)
    elif (direction == 'down' and down_px != 255 and right_px == 255):
        direction = 'right'
        car_y = car_y + 30
        car_y_offest = 0
        car_x_offest = 30
        car = pygame.transform.rotate(car, 90)
    elif (direction == 'right' and right_px != 255 and up_px == 255):
        direction =  'up'
        car_x = car_x + 30
        car_x_offest = 0
        car = pygame.transform.rotate(car, 90)

    # Drive
    if (up_px == 255 and direction == 'up'):
        car_y = car_y - 2
    elif (direction == 'right' and right_px == 255):
        car_x = car_x + 2
    elif (direction == 'down' and down_px == 255):
        car_y = car_y + 2

    
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (camera_x, camera_y), 5, 5)
    pygame.display.update()