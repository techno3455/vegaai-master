from vpython import *

def basicFollow(particle, distance):
    scene.camera.follow(particle)
    if scene.camera.pos != distance:
        if distance >= 0:
            scene.camera.pos = vector(distance,distance,distance)
        else:
            print("Please enter a value that is more or less than one, thank you")
    else:
        print("The scene is not working, please start it over and try again, make sure the Vpython package is downloaded")
def followMode1(particle, distance):
    scene.camera.follow(particle)
    if scene.camera.pos != distance:
        if distance <= 0:
            scene.camera.pos = vector(distance-20,distance,distance-20)
        else:
            print("Please enter a value that is less than one or zero, thank you.")
    else:
        print("The scene is not working, please start it over and try again, make sure the Vpython package is downloaded")
def followMode2(particle, distance):
    scene.camera.follow(particle)
    if scene.camera.pos != distance:
        if distance <= -2:
            scene.camera.pos = vector(distance-20,distance,distance-20)
        else:
            print("Please enter a value that is less than one or zero, thank you.")
    else:
        print("The scene is not working, please start it over and try again, make sure the Vpython package is downloaded")
def followMode3(particle, distance):
    scene.camera.follow(particle)
    if scene.camera.pos != distance:
        if distance <= -4:
            scene.camera.pos = vector(distance-20,distance,distance-20)
        else:
            print("Please enter a value that is less than one or zero, thank you.")
    else:
        print("The scene is not working, please start it over and try again, make sure the Vpython package is downloaded")

class changeFollowMode():
    def __init__(self, mode, particle, distance):
        self.mode = mode
        self.particle = particle
        self.distance = distance
        self.listenForEventClick()
        if mode is not None:
            if mode == 0:
                basicFollow(particle=self.particle, distance=self.distance)
            elif mode == 1:
                followMode1(particle=self.particle, distance=self.distance)
            elif mode == 2:
                followMode2(particle=self.particle, distance=self.distance)
            elif mode == 3:
                followMode3(particle=self.particle, distance=self.distance)
        else:
            print("Please enter a proper mode into the class, thank you.")

