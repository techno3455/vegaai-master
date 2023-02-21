'''
Copyright (C) Tetra System Solutions, 2023. All rights reserved.
'''

# Get proper imports.
from vega_util import *

# This class allows us to create either a Custom quark or a Quark defined in the Standard Model.
class createQuarkPath:
    def __init__(self, mP1, mP2, xPos, yPos, zPos, acceleration, velocity, spin, trailType, trailPps, mode, quarkParticleMode=None, charge=None, particleColor=color.white, mass=None, name="Unnamed Quark"):
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos
        self.mP1 = mP1
        self.mP2 = mP2
        self.velocity = velocity
        self.acceleration = acceleration
        self.trailType = trailType
        self.trailPps = trailPps
        self.name = name
        self.mass = mass
        self.spin = spin
        self.mode = mode
        self.charge = charge
        self.quarkParticleMode = quarkParticleMode
        self.particleColor = particleColor
        self.massList = [1.41e-14, 1.05e-15, 2.44e-17, 5.22e-17, 1.92e-14, 4.65e-17]
        self.chargeList = [0.66, -0.66, -0.33, 0.33, 0.66, -0.66, -0.33, 0.33, 0.66, -0.66, -0.33, 0.33]
        self.spinList = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
        self.radiusList = [1, 1, 2, 5, 1, 4]
        if self.quarkParticleMode == 1:
            charmQuark = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[0], charge=self.chargeList[0], spin=self.spinList[0], velocity=velocity, color=vec(0.9,0.4,0.9), name=self.name, mass=self.convertToUseableMass(self.massList[0]), trailColor=vec(0.8,0.4,0.8), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Charm Quark has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            charmQuark.executeEulerLagrange(charmQuark, self.mP1, self.mP2, self.mode)
        elif self.quarkParticleMode == 2:
            antiCharmQuark = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[0], velocity=velocity, spin=self.spinList[0], charge=self.chargeList[1], color=vec(0.6,0.4,0.6), name=name, mass=self.convertToUseableMass(self.massList[0]), trailColor=vec(0.5,0.4,0.5), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Anti Charm Quark has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            antiCharmQuark.executeEulerLagrange(antiCharmQuark, self.mP1, self.mP2, self.mode)
        elif self.quarkParticleMode == 3:
            strangeQuark = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[1], velocity=velocity, spin=self.spinList[1], charge=self.chargeList[2], color=vec(0.2,0.2,1), name=name, mass=self.convertToUseableMass(self.massList[1]), trailColor=vec(1,1,1), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Strange Quark has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            strangeQuark.executeEulerLagrange(strangeQuark, self.mP1, self.mP2, self.mode)
        elif self.quarkParticleMode == 4:
            antiStrangeQuark = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[1], velocity=velocity, spin=self.spinList[1], charge=self.chargeList[3], color=vec(1,0.2,0.2), name=name, mass=self.convertToUseableMass(self.massList[1]), trailColor=vec(0.7,0.7,0.7), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Anti Strange Quark has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            antiStrangeQuark.executeEulerLagrange(antiStrangeQuark, self.mP1, self.mP2, self.mode)
        elif self.quarkParticleMode == 5:
            upQuark = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[2], velocity=velocity, spin=self.spinList[2], charge=self.chargeList[4], color=vec(0,0.7,0.7), name=name, mass=self.convertToUseableMass(self.massList[2]), trailColor=vec(0,0,0.7), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Up Quark has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            upQuark.executeEulerLagrange(upQuark, self.mP1, self.mP2, self.mode)
        elif self.quarkParticleMode == 6:
            antiUpQuark = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[2], velocity=velocity, spin=self.spinList[2], charge=self.chargeList[5], color=vec(0.7,0.7,0), name=name, mass=self.convertToUseableMass(self.massList[2]), trailColor=vec(0.7,0,0.3), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Anti Up Quark has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            antiUpQuark.executeEulerLagrange(antiUpQuark, self.mP1, self.mP2, self.mode)
        elif self.quarkParticleMode == 7:
            downQuark = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[3], velocity=velocity, spin=self.spinList[3], charge=self.chargeList[6], color=vec(0.4,0.4,0.1), name=name, mass=self.convertToUseableMass(self.massList[3]), trailColor=vec(0.7,0.7,0), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Down Quark has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            downQuark.executeEulerLagrange(downQuark, self.mP1, self.mP2, self.mode)
        elif self.quarkParticleMode == 8:
            antiDownQuark = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[3], velocity=velocity, spin=self.spinList[3], charge=self.chargeList[7], color=vec(0.1,0.4,0.4), name=name, mass=self.convertToUseableMass(self.massList[3]), trailColor=vec(0.7,0.7,0.3), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Anti Down Quark has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            antiDownQuark.executeEulerLagrange(antiDownQuark, self.mP1, self.mP2, self.mode)
        elif self.quarkParticleMode == 9:
            topQuark = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[4], velocity=velocity, spin=self.spinList[4], charge=self.chargeList[8], color=vec(0.6,0.6,0.3), name=name, mass=self.convertToUseableMass(self.massList[4]), trailColor=vec(0.7,0.7,0.3), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Top Quark has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            topQuark.executeEulerLagrange(topQuark, self.mP1, self.mP2, self.mode)
        elif self.quarkParticleMode == 10:
            antiTopQuark = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[4], velocity=velocity, spin=self.spinList[4], charge=self.chargeList[9], color=vec(0.3,0.6,0.6), name=name, mass=self.convertToUseableMass(self.massList[4]), trailColor=vec(0.7,0.7,0.3), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Anti Top Quark has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            antiTopQuark.executeEulerLagrange(antiTopQuark, self.mP1, self.mP2, self.mode)
        elif self.quarkParticleMode == 11:
            bottomQuark = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[5], velocity=velocity, spin=self.spinList[5], charge=self.chargeList[10], color=vec(0.8,0.8,0.3), name=name, mass=self.convertToUseableMass(self.massList[5]), trailColor=vec(0.7,0.7,0.3), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Bottom Quark has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            bottomQuark.executeEulerLagrange(bottomQuark, self.mP1, self.mP2, self.mode)
        elif self.quarkParticleMode == 12:
            antiBottomQuark = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[5], velocity=velocity, spin=self.spinList[5], charge=self.chargeList[11], color=vec(0.3,0.8,0.8), name=name, mass=self.convertToUseableMass(self.massList[5]), trailColor=vec(0.7,0.7,0.3), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Anti Bottom Quark has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg")
            antiBottomQuark.executeEulerLagrange(antiBottomQuark, self.mP1, self.mP2, self.mode)
        elif self.quarkParticleMode is None:
            particle = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=mP1, velocity=velocity, spin=spin, charge=charge, color=self.particleColor, name=name, mass=self.convertToUseableMass(self.mass), trailColor=self.particleColor, trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            particle.executeEulerLagrange(particle, self.mP1, self.mP2, self.mode)
    def convertColorToHSV(self, hsvColor):
        self.finalHsv = color.rgb_to_hsv(hsvColor)
        return self.finalHsv
    def convertToUseableMass(self, massToConvert):
        finalMass = str(massToConvert)
        finalHalf = finalMass[:len(finalMass)//2]
        print(int(float(finalHalf)))
        return int(float(finalHalf))
createQuarkPath(1, 1, 0, 0, 0, 1, 1, spin=1, mass=1.22e-27, trailType="solid", trailPps=1, quarkParticleMode=1, mode=1)