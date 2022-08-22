import time

from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from threading import Thread

toys = scanner.find_toys()
print('Concurrent connections:', len(toys))

def move_0B7D(toy):
  with SpheroEduAPI(toy) as api:
    time.sleep(1)
    api.spin(360, 1)
    print(toy.name, 'just spun')


def move_DC3E(toy):
  with SpheroEduAPI(toy) as api:
    time.sleep(1)
    api.spin(360, 1)
    print(toy.name, 'just spun')

def move_sphere(toy):
  balls = {
    "0B7D": move_0B7D,
    "DC3E": move_DC3E
  }
  if toy.name[3:] in balls:
    balls[toy.name[3:]](toy)  
  
for toy in toys:
    print(toy.name)
    Thread(target=lambda: move_sphere(toy), daemon=True).start()
    # time.sleep(0.5)

print('\nPress Ctrl + C to exit.')
time.sleep(2 ** 16 - 1)
