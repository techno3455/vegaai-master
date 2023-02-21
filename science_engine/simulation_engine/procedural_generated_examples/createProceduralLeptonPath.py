'''
Copyright (C) Tetra System Solutions, 2023. All rights reserved.
'''

# Get proper imports.
from vega_util import *

# This class allows us to either create a custom Lepton or create one from the Standard Model.
class createLeptonPath:
    def __init__(self, mP1, mP2, xPos, yPos, zPos, acceleration, spin, velocity, trailType, trailPps, mode, leptonParticleMode=None, charge=None, particleColor=color.white, mass=None, name="Unnamed Lepton"):
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos
        self.mP1 = mP1
        self.mP2 = mP2
        self.velocity = velocity
        self.mode = mode
        self.acceleration = acceleration
        self.trailType = trailType
        self.trailPps = trailPps
        self.name = name
        self.mass = mass
        self.spin = spin
        self.charge = charge
        self.leptonParticleMode = leptonParticleMode
        self.particleColor = particleColor
        self.massList = [1.88e-28, 2.14e-37, 9.10e-31, 3.16e-27]
        self.spinList = [0.5, 0.5, 0.5, 0.5]
        self.chargeList = [-1, 1, 0, 0, -1, 1, -1, 1]
        self.radiusList = [1, 2, 9, 3]
        if self.leptonParticleMode == 1:
            muon = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[0], charge=self.chargeList[0], velocity=velocity, spin=self.spinList[0], color=vec(0.8,0.4,0.8), name=self.name, mass=self.convertToUseableMass(self.massList[0]), trailColor=vec(0.8,0.4,0.8), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Muon has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg "+", and a Spin of: "+str(self.spin))
            muon.executeEulerLagrange(muon, self.mP1, self.mP2, self.mode)
        elif self.leptonParticleMode == 2:
            antiMuon = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[0], velocity=velocity, spin=self.spinList[0], charge=self.chargeList[1], color=vec(0.5,0.4,0.5), name=name, mass=self.convertToUseableMass(self.massList[0]), trailColor=vec(0.5,0.4,0.5), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Anti Muon has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg "+", and a Spin of: "+str(self.spin))
            antiMuon.executeEulerLagrange(antiMuon, self.mP1, self.mP2, self.mode)
        elif self.leptonParticleMode == 3:
            nutrino = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[1], velocity=velocity, spin=self.spinList[1], charge=self.chargeList[2], color=vec(1,1,1), name=name, mass=self.convertToUseableMass(self.massList[1]), trailColor=vec(1,1,1), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Nutrino has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg "+", and a Spin of: "+str(self.spin))
            nutrino.executeEulerLagrange(nutrino, self.mP1, self.mP2, self.mode)
        elif self.leptonParticleMode == 4:
            antiNutrino = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[1], velocity=velocity, spin=self.spinList[1], charge=self.chargeList[3], color=vec(0.7,0.7,0.7), name=name, mass=self.convertToUseableMass(self.massList[1]), trailColor=vec(0.7,0.7,0.7), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Anti Nutrino has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg "+", and a Spin of: "+str(self.spin))
            antiNutrino.executeEulerLagrange(antiNutrino, self.mP1, self.mP2, self.mode)
        elif self.leptonParticleMode == 5:
            electron = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[2], velocity=velocity, spin=self.spinList[2], charge=self.chargeList[4], color=vec(0,0,0.7), name=name, mass=self.convertToUseableMass(self.massList[2]), trailColor=vec(0,0,0.7), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Electron has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg "+", and a Spin of: "+str(self.spin))
            electron.executeEulerLagrange(electron, self.mP1, self.mP2, self.mode)
        elif self.leptonParticleMode == 6:
            positron = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[2], velocity=velocity, spin=self.spinList[2], charge=self.chargeList[5], color=vec(0.7,0,0.3), name=name, mass=self.convertToUseableMass(self.massList[2]), trailColor=vec(0.7,0,0.3), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Positron has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg "+", and a Spin of: "+str(self.spin))
            positron.executeEulerLagrange(positron, self.mP1, self.mP2, self.mode)
        elif self.leptonParticleMode == 7:
            tau = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[3], velocity=velocity, spin=self.spinList[3], charge=self.chargeList[6], color=vec(0.7,0.7,0), name=name, mass=self.convertToUseableMass(self.massList[3]), trailColor=vec(0.7,0.7,0), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Tau has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg "+", and a Spin of: "+str(self.spin))
            tau.executeEulerLagrange(tau, self.mP1, self.mP2, self.mode)
        elif self.leptonParticleMode == 8:
            antiTau = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.radiusList[3], velocity=velocity, spin=self.spinList[3], charge=self.chargeList[7], color=vec(0.7,0.7,0.3), name=name, mass=self.convertToUseableMass(self.massList[3]), trailColor=vec(0.7,0.7,0.3), trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            print ("A new Anti Tau has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.mP1) + " kg "+", and a Spin of: "+str(self.spin))
            antiTau.executeEulerLagrange(antiTau, self.mP1, self.mP2, self.mode)
        elif self.leptonParticleMode is None:
            particle = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=mP1, velocity=velocity, spin=spin, charge=charge, color=particleColor, name=name, mass=self.convertToUseableMass(self.mass), trailColor=self.particleColor, trailRadius=mP1*0.2, trailType=self.trailType, trailPps=self.trailPps)
            particle.executeEulerLagrange(particle, self.mP1, self.mP2, self.mode)
    def convertColorToHSV(self, hsvColor):
        self.finalHsv = color.rgb_to_hsv(hsvColor)
        return self.finalHsv
createLeptonPath(1, 1, 0, 0, 0, 1, 1, 1, mass=1.22e-27, trailType="points", trailPps=1, leptonParticleMode=1, mode=1)