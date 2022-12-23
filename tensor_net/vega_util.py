import wolfram_util as wfu
import neuralnet_util as neu
from vpython import *
import numpy as np

defaultPos = vector(0,0,0)
defaultVel = vector(0,0,0)
defaultAcc = vector(0,-10,0)
defaultMass = 0
defaultCharge = 0
defaultColor = color.white
class createUniversalParticle(sphere):
    def __init__(self, number1, number2, particle=None, pos=defaultPos, velocity=defaultVel, acceleration=defaultAcc, name='Unnamed Particle', mass=defaultMass, charge=defaultCharge, color=defaultColor):
        self.position = pos
        self.velocity = velocity
        self.acceleration = acceleration
        self.name = name
        self.mass = mass
        self.number1 = number1
        self.number2 = number2
        self.charge = charge
        self.color = color
    def returnAtrribs(self):
        print("Particle: "+str(self.name)+", Mass: "+str(self.mass)+", Position: "+str(self.position)+", Velocity: "+str(self.velocity)+", Acceleration: "+str(self.acceleration))
    def acc(self, electron, nucleus):
        dr = electron.pos - nucleus.pos
        Force = 1./(4.*self.pi*self.epsilon)*nucleus.charge*electron.charge/(mag(dr)**2) * norm(dr)
        m1 = electron.mass
        return Force/m1
    def accUpdate(self, Particle1, Particle2, method):
        if method == 'Euler':
            Particle1.pos = Particle1.pos + Particle1.velocity*self.dt
            Particle1.velocity = Particle1.velocity + self.acc(Particle1, Particle2)*self.dt
        elif method == "Euler Chromer":
            Particle1.velocity = Particle1.velocity + self.acc(Particle1, Particle2)*self.dt
            Particle1.pos = Particle1.pos + Particle1.velocity*self.dt
        elif method == "":
            Particle1.pos = None
            Particle1.velocity = None
    def update(self, t, method):
        if method == 'Euler':
            self.position = self.position + self.velocity*t
            self.velocity = self.velocity + self.acceleration*t
        elif method == 'Euler Chromer':
            self.velocity = self.velocity + self.acceleration*t
            self.position = self.position + self.velocity*t
        elif method == 'None':
            self.velocity = defaultVel
            self.position = defaultPos
    
class createExpandedAtom:
    def __init__(self, x, y, z, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.atomCreate()
    def atomCreate(self):
        atom = sphere(pos=vector(self.x,self.y,self.z), radius=self.radius, color=color.red)    


