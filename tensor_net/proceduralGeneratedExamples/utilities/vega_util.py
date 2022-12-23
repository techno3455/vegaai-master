#import utilities.wolfram_util as wfu
#import utilities.neuralnet_util as neu
import numpy as np
from sympy import *
from scipy import *
from utilities.camera_utils import *
defaultPos = vector(0,0,0)
defaultVel = vector(0,0,0)
defaultAcc = vector(0,0,0)

defaultMass = 0
defaultCharge = 0
defaultColor = color.white

class createUniversalParticle(sphere):
    def __init__(self, pos, radius, velocity, mass, charge, color, name="Unamed Particle"):
        super().__init__()
        self.pos = pos
        self.velocity = velocity
        self.name = name
        self.mass = mass
        self.color = color
        self.radius = radius
        self.charge = charge
    def returnAtrribs(self):
        print("Particle: "+str(self.name)+", Mass: "+str(self.mass)+", Position: "+str(self.position)+", Velocity: "+str(self.velocity)+", Acceleration: "+str(self.acceleration))
    def getevent(self):
        lasthit = None
        lastpick = None
        lastcolor = None
        if lasthit != None:
            if lastpick != None: lasthit.modify(lastpick, color=lastcolor)
            else: lasthit.color = vector(lastcolor)
            lasthit = lastpick = None
        hit = scene.mouse.pick
        if hit != None:
            lasthit = hit
            lastpick = None
            if isinstance(hit, createUniversalParticle):
                lasthit = hit.pos
                followMode1(hit, 1)
    def listenForEventClick(self):
        scene.bind('mousedown', self.getevent)

class createStandardModelParticle(sphere):
    def __init__(self, radius, velocity, mass, charge, color, pos, trailType, trailPps, type=None, trailRadius=None, trailColor=None, trailRetain=None, arrowAxis=None, arrowScale=None, arrowShaftWidth=None, arrowColor=None, name="Unamed Particle"):
        super().__init__()
        self.pos = pos
        self.velocity = velocity
        self.name = name
        self.mass = mass
        self.trailType = trailType
        self.trailPps = trailPps
        self.color = color
        self.radius = radius
        self.charge = charge
        self.createTrail(type=type, trailRadius=trailRadius, trailColor=trailColor, trailType=self.trailType, trailRetain=trailRetain, trailPps=self.trailPps, arrowAxis=arrowAxis, arrowScale=arrowScale, arrowShaftWidth=arrowShaftWidth, arrowColor=arrowColor)
    def returnAtrribs(self):
        print("Particle: "+str(self.name)+", Mass: "+str(self.mass)+", Position: "+str(self.position)+", Velocity: "+str(self.velocity)+", Acceleration: "+str(self.acceleration))
    def getevent(self):
        lasthit = None
        lastpick = None
        lastcolor = None
        if lasthit != None:
            if lastpick != None: lasthit.modify(lastpick, color=lastcolor)
            else: lasthit.color = vector(lastcolor)
            lasthit = lastpick = None
        hit = scene.mouse.pick
        if hit != None:
            lasthit = hit
            lastpick = None
            if isinstance(hit, createStandardModelParticle):
                lasthit = hit.pos
                followMode1(hit, 1)
    def createTrail(self, type=None, trailRadius=None, trailColor=None, trailType=None, trailRetain=None, trailPps=None, arrowAxis=None, arrowScale=None, arrowShaftWidth=None, arrowColor=None):
        if type is None or trailRadius is None:
            if trailColor or str(trailType) or trailPps is not None:
                type = attach_trail(self, color=trailColor, radius=trailRadius, type=trailType, pps=trailPps, retain=10)
            else:
                print("Please enter a proper Color and Trail Type, thank you.")
        elif type is not None and arrowAxis is not None and arrowScale is not None and arrowShaftWidth is not None and arrowColor is not None:
            if type == "ball":
                type = self.trail_type(type)
                typeObject = attach_trail(self, color=trailColor, radius=trailRadius, type=trailType, pps=trailPps, retain=trailRetain)
            elif type == "point":
                type = self.trail_type(type)
                typeObject = attach_trail(self, color=trailColor, radius=trailRadius, type=trailType, pps=trailPps, retain=trailRetain)
            elif type == "arrow":
                type = self.trail_type(type)
                typeObject = attach_arrow(self, axis=arrowAxis, scale=arrowScale, shaftwidth=arrowShaftWidth, color=arrowColor)
        else:
            print (str(type) + " is not a proper type, please try again, thank you.")
        return type
    def clearTrail(self, type):
        self.clear_trail()
    def returnPathLagrangian(self, m1, m2, v1, v2):
        return self.calculateKineticEnergy(m1, v1) - self.calculatePotentialEnergy(m2, v2) 
    def listenForEventClick(self):
        scene.bind('mousedown', self.getevent)
    def calculatePotentialEnergy(self, m, v):
        self.totalPotentialEnergy = m*9.8*v
        return self.totalPotentialEnergy
    def calculateKineticEnergy(self, m, v):
        self.totalKineticEnergy = (m*v**2)/2
        return self.totalKineticEnergy
    def executeEulerLagrange(self, lepton, v1, v2):
        m1 = self.mass
        m2 = self.mass
        t = 0
        dt = 0.001
        self.m = m1
        self.p = self.m*vector(self.returnPathLagrangian(m1, m2, v1, v2), self.returnPathLagrangian(m1, m2, v1, v2), self.returnPathLagrangian(m1, m2, v1, v2))
        finalForce = vector(0,0,0)
        while t<1.3:
            rate(1000)
            finalForce = vector(0,0,0)
            self.p = self.p + finalForce*dt
            self.pos = self.pos+self.p*dt/self.m
            t = t + dt

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