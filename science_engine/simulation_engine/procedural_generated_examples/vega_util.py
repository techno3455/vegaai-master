#import utilities.wolfram_util as wfu
#import utilities.neuralnet_util as neu
import numpy as np
from sympy import *
from scipy import *
from . import camera_utils
defaultPos = camera_utils.vector(0,0,0)
defaultVel = camera_utils.vector(0,0,0)
defaultAcc = camera_utils.vector(0,0,0)

defaultMass = 0
defaultCharge = 0
defaultColor = camera_utils.color.white
operationDict = {1:"+", 2:"-", 3:"/", 4:"*", 5:"**", 6:"//"}
class createUniversalParticle(camera_utils.sphere):
    def __init__(self, pos, radius, velocity, mass, charge, color=None, name="Unamed Particle"):
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
            else: lasthit.color = camera_utils.vector(lastcolor)
            lasthit = lastpick = None
        hit = camera_utils.scene.mouse.pick
        if hit != None:
            lasthit = hit
            lastpick = None
            if isinstance(hit, createUniversalParticle):
                lasthit = hit.pos
                camera_utils.followMode1(hit, 1)
    def listenForEventClick(self):
        camera_utils.scene.bind('mousedown', self.getevent)

class createStandardModelParticle(camera_utils.sphere):
    def __init__(self, radius, velocity, mass, spin, charge, color, pos, trailType, trailPps, type=None, trailRadius=None, trailColor=None, trailRetain=None, arrowAxis=None, arrowScale=None, arrowShaftWidth=None, arrowColor=None, name="Unamed Particle"):
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
        self.spin = spin
        print(self.mass)
        self.createTrail(type=type, trailRadius=trailRadius, trailColor=trailColor, trailType=self.trailType, trailRetain=trailRetain, trailPps=self.trailPps, arrowAxis=arrowAxis, arrowScale=arrowScale, arrowShaftWidth=arrowShaftWidth, arrowColor=arrowColor)
    def returnAtrribs(self):
        print("Particle: "+str(self.name)+", Mass: "+str(self.mass)+", Position: "+str(self.position)+", Velocity: "+str(self.velocity)+", Acceleration: "+str(self.acceleration)+", and a Spin of: "+str(self.spin))
    def getevent(self):
        lasthit = None
        lastpick = None
        lastcolor = None
        if lasthit != None:
            if lastpick != None: lasthit.modify(lastpick, color=lastcolor)
            else: lasthit.color = camera_utils.vector(lastcolor)
            lasthit = lastpick = None
        hit = camera_utils.scene.mouse.pick
        if hit != None:
            lasthit = hit
            lastpick = None
            if isinstance(hit, createStandardModelParticle):
                lasthit = hit.pos
                camera_utils.followMode1(hit, 1)
    def createTrail(self, type=None, trailRadius=None, trailColor=None, trailType=None, trailRetain=None, trailPps=None, arrowAxis=None, arrowScale=None, arrowShaftWidth=None, arrowColor=None):
        if type is None or trailRadius is None:
            if trailColor or str(trailType) or trailPps is not None:
                type = camera_utils.attach_trail(self, color=trailColor, radius=trailRadius, type=trailType, pps=trailPps, retain=10)
            else:
                print("Please enter a proper Color and Trail Type, thank you.")
        elif type is not None and arrowAxis is not None and arrowScale is not None and arrowShaftWidth is not None and arrowColor is not None:
            if type == "ball":
                type = self.trail_type(type)
                typeObject = camera_utils.attach_trail(self, color=trailColor, radius=trailRadius, type=trailType, pps=trailPps, retain=trailRetain)
            elif type == "point":
                type = self.trail_type(type)
                typeObject = camera_utils.attach_trail(self, color=trailColor, radius=trailRadius, type=trailType, pps=trailPps, retain=trailRetain)
            elif type == "arrow":
                type = self.trail_type(type)
                typeObject = camera_utils.attach_arrow(self, axis=arrowAxis, scale=arrowScale, shaftwidth=arrowShaftWidth, color=arrowColor)
        else:
            print (str(type) + " is not a proper type, please try again, thank you.")
        return type
    def clearTrail(self, type):
        self.clear_trail()
    def returnPathLagrangian(self, m1, m2, v1, v2):
        return self.calculateKineticEnergy(m1, v1, 1, None, None, None, None) - self.calculatePotentialEnergy(m2, v2, 1, None, None, None, None) 
    def listenForEventClick(self):
        camera_utils.scene.bind('mousedown', self.getevent)
    def calculatePotentialEnergy(self, m, v, mode, requiredOperation, operationToApply, extraVar):
        if mode == 1:
            self.totalPotentialEnergy = float(m)*9.8*v
        elif mode == 2:
            for key in operationDict.keys():
                if key is requiredOperation:
                    self.totalPotentialEnergy = int(operationToApply+requiredOperation.append(extraVar))
                if key is None:
                    pass
        return self.totalPotentialEnergy
    def calculateKineticEnergy(self, m, v, mode, requiredOperation, operationToApply, extraVar):
        if mode == 1:
            self.totalKineticEnergy = (float(m)*v**2)/2
        elif mode == 2:
            for key in operationDict.keys():
                if key is requiredOperation:
                    self.totalKineticEnergy = int(operationToApply+requiredOperation.append(extraVar))
                if key is None:
                    pass
        return self.totalKineticEnergy
    def returnPathHamiltonian(self, m1, m2, v1, v2, requiredOperation, operationToApply, extraVar):
        return self.calculateKineticEnergy(m1, v1, 2, requiredOperation, operationToApply, extraVar) + self.calculatePotentialEnergy(m2, v2, 2, requiredOperation, operationToApply, extraVar)
    def executeEulerLagrange(self, lepton, v1, v2, mode):
        m1 = self.mass
        m2 = self.mass
        t = 0
        dt = 0.001
        self.m = m1
        print(int(float(self.m)))
        self.p1 = int(float(self.m))*camera_utils.vector(int(abs(self.returnPathLagrangian(m1, m2, v1, v2))), int(abs(self.returnPathLagrangian(m1, m2, v1, v2))), int(abs(self.returnPathLagrangian(m1, m2, v1, v2))))
        finalForce = camera_utils.vector(0,0,0)
        if mode == 1:
            while (t<1.3):
                camera_utils.rate(1000)
                finalForce = camera_utils.vector(0,0,0)
                self.p1 = self.p1 + finalForce*dt
                self.pos = self.pos+self.p1*dt/int(float(self.m))
                t = t + dt
        elif mode == 2:
            return
    def executeEulerHamiltonian(self, lepton, v1, v2, mode, extraVar):
        m1 = self.mass
        m2 = self.mass
        t = 0
        dt = 0.001
        self.m = m1
        print(int(float(self.m)))
        self.p1 = int(float(self.m))*camera_utils.vector(int(abs(self.returnPathHamiltonian(m1, m2, v1, v2))), int(abs(self.returnPathHamiltonian(m1, m2, v1, v2))), int(abs(self.returnPathHamiltonian(m1, m2, v1, v2))))
        finalForce = camera_utils.vector(0,0,0)
        if mode == 1:
            while (t<1.3):
                camera_utils.rate(1000)
                finalForce = camera_utils.vector(0,0,0)
                self.p1 = self.p1 + finalForce*dt
                self.pos = self.pos+self.p1*dt/int(float(self.m))
                t = t + dt
        elif mode == 2:
            return
class createStandardModelBoson:
    def __init__(self, radius, velocity, mass, spin, charge, pos, thickness, width, height, color, type, arrayNumber, name="Unamed Boson"):
        self.radius = radius
        self.velocity = velocity
        self.mass = mass
        self.spin = spin
        self.charge = charge
        self.thickness = thickness
        self.arrayNumber = arrayNumber
        self.color = color
        self.type = type
        self.name = name
        self.massList = [1.6e-36, 1.6e-36, 1.6e-36, 1.6e-36, 1.6e-36]
        if type == 1:
            gluon = self.createBosonShape(0,0,0,0.1,eColor=camera_utils.vec(0.3,0.9,0.3))
        if type == 2:
            photon = self.createBosonShape(0,0,0,0.1,eColor=camera_utils.vec(0.9,0.9,0.9))
        if type == 3:
            zBoson = self.createBosonShape(0,0,0,0.1,eColor=camera_utils.vec(0.5,0.5,0.1))
        if type == 4:
            wBoson = self.createBosonShape(0,0,0,0.1,eColor=camera_utils.vec(0.5,0.1,0.5))
        if type == 5:
            hBoson = self.createBosonShape(0,0,0,0.1,eColor=camera_utils.vec(0.9,0.5,0))
        if type is None:
            boson = self.createBosonShape(0,0,0,0.1,eColor=self.color)
    def createBosonShape(self, xVec, yVec, zVec, yLength, eColor):
        bosonObj = camera_utils.shapes.circle(thickness=0.3)
        objPath = [camera_utils.vector(xVec,yVec,zVec), camera_utils.vector(xVec,yLength,zVec)]
        self.boson = camera_utils.extrusion(path=objPath, shape=bosonObj, color=eColor, scale=[1,1])
    def returnPathLagrangian(self, m1, m2, v1, v2):
        return self.calculateKineticEnergy(m1, v1) - self.calculatePotentialEnergy(m2, v2) 
    def calculatePotentialEnergy(self, m, v):
        self.totalPotentialEnergy = float(m)*9.8*v
        return self.totalPotentialEnergy
    def calculateKineticEnergy(self, m, v):
        self.totalKineticEnergy = (float(m)*v**2)/2
        return self.totalKineticEnergy
    def returnPathHamiltonian(self, m1, m2, v1, v2):
        return self.calculateKineticEnergy(m1, v1) + self.calculatePotentialEnergy(m2, v2)
    def convertToUseableMass(self, massToConvert):
        finalMass = str(massToConvert)
        finalHalf = finalMass[:len(finalMass)//2]
        print(finalHalf)
        return finalHalf
    def executeEulerLagrange(self, boson, v1, v2, numArray, mode):
        m1 = self.convertToUseableMass(self.massList[numArray])
        m2 = self.convertToUseableMass(self.massList[numArray])
        t = 0
        dt = 0.001
        self.m = m1
        print(int(float(self.m)))
        print(float(self.m))
        self.convertToUseableMass(self.m)
        self.p = int(float(self.m))*camera_utils.vector(int(abs(self.returnPathLagrangian(m1, m2, v1, v2))), int(abs(self.returnPathLagrangian(m1, m2, v1, v2))), int(abs(self.returnPathLagrangian(m1, m2, v1, v2))))
        finalForce = camera_utils.vector(0,0,0)
        while (t<1.3):
            camera_utils.rate(1000)
            finalForce = camera_utils.vector(0,0,0)
            self.p = self.p + finalForce*dt 
            self.boson.pos = self.boson.pos+self.p*dt/int(float(self.m))/60
            t = t + dt
    def executeEulerHamiltonian(self, lepton, v1, v2, mode, extraVar):
        m1 = self.mass
        m2 = self.mass
        t = 0
        dt = 0.001
        self.m = m1
        print(int(float(self.m)))
        self.p1 = int(float(self.m))*camera_utils.vector(int(abs(self.returnPathHamiltonian(m1, m2, v1, v2))), int(abs(self.returnPathHamiltonian(m1, m2, v1, v2))), int(abs(self.returnPathHamiltonian(m1, m2, v1, v2))))
        finalForce = camera_utils.vector(0,0,0)
        if mode == 1:
            while (t<1.3):
                camera_utils.rate(1000)
                finalForce = camera_utils.vector(0,0,0)
                self.p1 = self.p1 + finalForce*dt
                self.pos = self.pos+self.p1*dt/int(float(self.m))
                t = t + dt
        elif mode == 2:
            return
class createExpandedAtom:
    def __init__(self, x, y, z, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.atomCreate()
    def atomCreate(self):
        atom = camera_utils.sphere(pos=camera_utils.vector(self.x,self.y,self.z), radius=self.radius, color=camera_utils.color.red)