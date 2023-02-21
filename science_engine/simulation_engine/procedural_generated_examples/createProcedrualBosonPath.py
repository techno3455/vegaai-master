'''
Copyright (C) Tetra System Solutions, 2023. All rights reserved.
'''

# Get proper imports.
from . import vega_util

# This class allows us to create custom Bosons or create Bosons that have been declared, the bosons included are all included in the Standard Model.
class createBosonPath:
    def __init__(self, mP1, mP2, xPos, yPos, zPos, acceleration, velocity, spin, arrayNumber, mode, x2, y2, z2, bosonParticleMode=None, charge=None, particleColor=vega_util.color.white, mass=None, name="Unnamed Boson"):
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos
        self.mP1 = mP1
        self.mP2 = mP2
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.velocity = velocity
        self.acceleration = acceleration
        self.name = name
        self.mass = mass
        self.spin = spin
        self.charge = charge
        self.mode = mode
        self.arrayNumber = arrayNumber
        self.bosonParticleMode = bosonParticleMode
        self.particleColor = particleColor
        self.massList = [0]
        self.spinList = [1, 1, 1, 1, 0]
        self.chargeList = [0, 0, -1, 0, 0]
        self.thicknessList = [0.1]
        if self.bosonParticleMode == 1:
            gluon = vega_util.createStandardModelBoson(pos=vega_util.vec(self.xPos, self.yPos, self.zPos), charge=self.chargeList[0], arrayNumber=self.arrayNumber, spin=self.spinList[0], width=100, height=100, radius=1, thickness=self.thicknessList[0], color=vega_util.vector(0.2,0.9,0.2), velocity=velocity, name=self.name, type=1, mass=0)
            print ("A new Gluon has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            gluon.executeEulerLagrange(gluon, self.mP1, self.mP2, 0, 1)
        elif self.bosonParticleMode == 2:
            photon = vega_util.createStandardModelBoson(pos=vega_util.vec(self.xPos, self.yPos, self.zPos), charge=self.chargeList[0], arrayNumber=self.arrayNumber, spin=self.spinList[0], width=100, height=100, radius=1, color=None, thickness=self.thicknessList[1], velocity=velocity, name=self.name, type=2, mass=0)
            print ("A new Photon has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            photon.executeEulerLagrange(self.mP1, self.mP2, 1, self.mode)
        elif self.bosonParticleMode == 3:
            zBoson = vega_util.createStandardModelBoson(pos=vega_util.vec(self.xPos, self.yPos, self.zPos), charge=self.chargeList[0], arrayNumber=self.arrayNumber, spin=self.spinList[0], width=100, height=100, radius=1, color=None, thickness=self.thicknessList[2], velocity=velocity, name=self.name, type=3, mass=0)
            print ("A new zBoson has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            zBoson.executeEulerLagrange(self.mP1, self.mP2, 2, self.mode)
        elif self.bosonParticleMode == 4:
            wBoson = vega_util.createStandardModelBoson(pos=vega_util.vec(self.xPos, self.yPos, self.zPos), charge=self.chargeList[0], arrayNumber=self.arrayNumber, spin=self.spinList[0], width=100, height=100, radius=1, color=None, thickness=self.thicknessList[3], velocity=velocity, name=self.name, type=4, mass=0)
            print ("A new wBoson has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            wBoson.executeEulerLagrange(self.mP1, self.mP2, 3, self.mode)
        elif self.bosonParticleMode == 5:
            higgsBoson = vega_util.createStandardModelBoson(pos=vega_util.vec(self.xPos, self.yPos, self.zPos), charge=self.chargeList[0], arrayNumber=self.arrayNumber, spin=self.spinList[0], width=100, height=100, radius=1, color=None, thickness=self.thicknessList[4], velocity=velocity, name=self.name, type=5, mass=0)
            print ("A new Higgs Boson has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            #higgsBoson.executeEulerLagrange(self.mP1, self.mP2, 4, self.mode)
        elif self.bosonParticleMode is None:
            particle = vega_util.createStandardModelParticle(pos=vega_util.vec(self.xPos, self.yPos, self.zPos), radius=mP1, velocity=velocity, arrayNumber=self.arrayNumber, spin=spin, charge=charge, color=self.particleColor, name=name, mass=self.convertToUseableMass(self.mass), trailColor=self.particleColor, trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            particle.executeEulerLagrange(particle, self.mP1, self.mP2, self.arrayNumber)
    def convertColorToHSV(self, hsvColor):
        self.finalHsv = vega_util.color.rgb_to_hsv(hsvColor)
        return self.finalHsv
    def convertToUseableMass(self, massToConvert):
        finalMass = str(massToConvert)
        finalHalf = finalMass[:len(finalMass)//2]
        print(int(float(finalHalf)))
        return int(float(finalHalf))
    
createBosonPath(1, 1, 0, 0, 0, 1, 1, spin=1, mass=1.22e-27, bosonParticleMode=1, arrayNumber=0, mode=1, x2=4, y2=4, z2=4)