from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from threading import Thread

toys = scanner.find_toys()
print('Concurrent Connections:', len(toys))

def move_sphere(toy):
    print(toy, 'just spun')
    with SpheroEduAPI(toy) as api:
        api.spin(360, 1)

for toy in toys[:4]:
    Thread(target=lambda: move_sphere(toy)).start()