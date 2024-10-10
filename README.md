# Pygame Car Simulation

This project is a simple car simulation created using Pygame. The car navigates a predefined track based on pixel detection for road following.

## Features

- Car movement controlled by pixel detection
- Dynamic turning based on road detection
- Real-time updates at 60 frames per second

## Requirements

- Python 3.x
- Pygame

## Installation

1. Install Python 3.x from the official website: [Python.org](https://www.python.org/)
2. Install Pygame using pip:

   ```sh
   pip install pygame
    ```
## Usage
1. Clone this repository or download the car_simulation.py file.

2. Place the track image (track6.png) and car image (tesla.png) in the same directory as the script.

3. Run the script:

``` Sh
python car_simulation.py
```
## Code Explanation
The main script car_simulation.py includes:

``` python
import pygame
pygame.init()

# Taking Variables
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

```

## Contributing
Feel free to fork this repository and contribute by submitting a pull request. Any improvements or new features are welcome!

## License
This project is licensed under the MIT License.
