import time

from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from threading import Thread

toysUsed = 8
toys = []
while len(toys) < toysUsed:
  toys = scanner.find_toys()

print('Concurrent connections:', len(toys))

def move_0B7D(toy):
  done = False

  while not done:
    try:
      with SpheroEduAPI(toy) as api:
        done = True
        sync.append(toy.name)

        while len(sync) != toysUsed:
          time.sleep(0.005)

        # time.sleep(1)
        api.spin(360, 1)
        print(toy.name, 'just spun')
    except Exception:
      pass
    time.sleep(0.5)

def move_093B(toy):
  done = False

  while not done:
    try:
      with SpheroEduAPI(toy) as api:
        done = True
        sync.append(toy.name)

        while len(sync) != toysUsed:
          time.sleep(0.005)

        # time.sleep(1)
        api.spin(360, 1)
        print(toy.name, 'just spun')
    except Exception:
      pass
    time.sleep(0.5)

def move_DC3E(toy):
  done = False

  while not done:
    try:
      with SpheroEduAPI(toy) as api:
        done = True
        sync.append(toy.name)

        while len(sync) != toysUsed:
          time.sleep(0.005)

        # time.sleep(1)
        api.spin(360, 1)
        print(toy.name, 'just spun')
    except Exception:
      pass
    time.sleep(0.5)

def move_AA84(toy):
  done = False

  while not done:
    try:
      with SpheroEduAPI(toy) as api:
        done = True
        sync.append(toy.name)

        while len(sync) != toysUsed:
          time.sleep(0.005)

        # time.sleep(1)
        api.spin(360, 1)
        print(toy.name, 'just spun')
    except Exception:
      pass
    time.sleep(0.5)

def move_166E(toy):
  done = False

  while not done:
    try:
      with SpheroEduAPI(toy) as api:
        done = True
        sync.append(toy.name)

        while len(sync) != toysUsed:
          time.sleep(0.005)

        # time.sleep(1)
        api.spin(360, 1)
        print(toy.name, 'just spun')
    except Exception:
      pass
    time.sleep(0.5)

def move_7FC9(toy):
  done = False

  while not done:
    try:
      with SpheroEduAPI(toy) as api:
        done = True
        sync.append(toy.name)

        while len(sync) != toysUsed:
          time.sleep(0.005)

        # time.sleep(1)
        api.spin(360, 1)
        print(toy.name, 'just spun')
    except Exception:
      pass
    time.sleep(0.5)

def move_17E9(toy):
  done = False

  while not done:
    try:
      with SpheroEduAPI(toy) as api:
        done = True
        sync.append(toy.name)

        while len(sync) != toysUsed:
          time.sleep(0.005)

        # time.sleep(1)
        api.spin(360, 1)
        print(toy.name, 'just spun')
    except Exception:
      pass
    time.sleep(0.5)

def move_98D2(toy):
  done = False

  while not done:
    try:
      with SpheroEduAPI(toy) as api:
        done = True
        sync.append(toy.name)

        while len(sync) != toysUsed:
          time.sleep(0.005)

        # time.sleep(1)
        api.spin(360, 1)
        print(toy.name, 'just spun')
    except Exception:
      pass
    time.sleep(0.5)

def move_sphere(toy):
  balls = {
    "0B7D": move_0B7D,
    "DC3E": move_DC3E,
    "093B": move_093B,
    "AA84": move_AA84,
    "166E": move_166E,
    "7FC9": move_7FC9,
    "17E9": move_17E9,
    "98D2": move_98D2,
  }

  if toy.name[3:] in balls:
    balls[toy.name[3:]](toy)


sync = []

for toy in toys:
  print(toy.name)
  Thread(target=lambda: move_sphere(toy), daemon=True).start()
  # time.sleep(0.5)

print('\nPress Ctrl + C to exit.')
time.sleep(2 ** 16 - 1)
