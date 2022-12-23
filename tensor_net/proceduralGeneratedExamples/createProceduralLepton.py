from utilities.vega_util import *
import numpy as np
import scipy.constants as spc 
from sympy.physics.mechanics import *
class createLeptonPath:
    def __init__(self, xPos, yPos, zPos, acceleration, velocity, trailType, trailPps, trailRetain, leptonParticleMode=None, charge=None, particleColor=color.white, mass=None, name="Unnamed Lepton"):
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos
        self.velocity = velocity
        self.acceleration = acceleration
        self.trailType = trailType
        self.trailRetain = trailRetain
        self.trailPps = trailPps
        self.name = name
        self.mass = mass
        self.charge = charge
        self.leptonParticleMode = leptonParticleMode
        self.particleColor = particleColor
        self.particle = None
        self.massConversionList = [1.88+exp(-28), 2.14+exp(-37), 9.1+exp(-31), 3.167+exp(-27)]
        self.pi = pi
        if self.leptonParticleMode == 1:
            mass = self.convertToUseableMass(self.mass) 
            muon = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.mass, charge=self.charge, velocity=velocity, color=vec(0.8,0.4,0.8), name=self.name, mass=mass, trailColor=vec(0.8,0.4,0.8), trailRadius=mass*0.2, trailType=self.trailType, trailRetain=self.trailRetain, trailPps=self.trailPps)
            print ("A new Muon has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.massConversionList[0]) + " kg")
            muon.executeEulerLagrange(muon, 0.5, 0.5)
        elif self.leptonParticleMode == 2:
            mass = self.convertToUseableMass(self.mass)
            antiMuon = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.mass, velocity=velocity, charge=charge, color=vec(0.5,0.4,0.5), name=name, mass=mass, trailColor=vec(0.5,0.4,0.5), trailRadius=mass*0.2, trailType=self.trailType, trailRetain=self.trailRetain, trailPps=self.trailPps)
            antiMuon.executeEulerLagrange(antiMuon, 0.5, 0.5)
            print ("A new Anti Muon has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.massConversionList[0]) + " kg")
        elif self.leptonParticleMode == 3:
            mass = 2.14
            nutrino = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.mass, velocity=velocity, charge=charge, color=vec(1,1,1), name=name, mass=mass, trailColor=vec(1,1,1), trailRadius=mass*0.2, trailType=self.trailType, trailRetain=self.trailRetain, trailPps=self.trailPps)
            nutrino.executeEulerLagrange(nutrino, 0.5, 0.5)
            print ("A new Nutrino has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.massConversionList[1]) + " kg")
        elif self.leptonParticleMode == 4:
            mass = 2.14
            antiNutrino = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.mass, velocity=velocity, charge=charge, color=vec(0.7,0.7,0.7), name=name, mass=mass, trailColor=vec(0.7,0.7,0.7), trailRadius=mass*0.2, trailType=self.trailType, trailRetain=self.trailRetain, trailPps=self.trailPps)
            antiNutrino.executeEulerLagrange(muon, 0.5, 0.5)
            print ("A new Anti Nutrino has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.massConversionList[1]) + " kg")
        elif self.leptonParticleMode == 5:
            mass = 9.1
            electron = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.mass, velocity=velocity, charge=charge, color=vec(0,0,0.7), name=name, mass=mass, trailColor=vec(0,0,0.7), trailRadius=mass*0.2, trailType=self.trailType, trailRetain=self.trailRetain, trailPps=self.trailPps)
            electron.executeEulerLagrange(electron, 0.5, 0.5)
            print ("A new Electron has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.massConversionList[2]) + " kg")
        elif self.leptonParticleMode == 6:
            mass = 9.1
            positron = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.mass, velocity=velocity, charge=charge, color=vec(0.7,0,0.3), name=name, mass=mass, trailColor=vec(0.7,0,0.3), trailRadius=mass*0.2, trailType=self.trailType, trailRetain=self.trailRetain, trailPps=self.trailPps)
            positron.executeEulerLagrange(positron, 0.5, 0.5)
            print ("A new Positron has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.massConversionList[2]) + " kg")
        elif self.leptonParticleMode == 7:
            mass = 3.167
            tau = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.mass, velocity=velocity, charge=charge, color=vec(0.7,0.7,0), name=name, mass=mass, trailColor=vec(0.7,0.7,0), trailRadius=mass*0.2, trailType=self.trailType, trailRetain=self.trailRetain, trailPps=self.trailPps)
            tau.executeEulerLagrange(tau, 0.5, 0.5)
            print ("A new Tau has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.massConversionList[3]) + " kg")
        elif self.leptonParticleMode == 8:
            mass = 3.167
            antiTau = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.mass, velocity=velocity, charge=charge, color=vec(0.7,0.7,0.3), name=name, mass=mass, trailColor=vec(0.7,0.7,0.3), trailRadius=mass*0.2, trailType=self.trailType, trailRetain=self.trailRetain, trailPps=self.trailPps)
            antiTau.executeEulerLagrange(antiTau, 0.5, 0.5)
            print ("A new Anti Tau has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + str(self.massConversionList[3]) + " kg")
        elif self.leptonParticleMode is None:
            particle = createStandardModelParticle(pos=vec(self.xPos, self.yPos, self.zPos), radius=self.mass, velocity=velocity, charge=charge, color=self.particleColor, name=name, mass=self.mass, trailColor=self.particleColor, trailRadius=self.mass*0.2, trailType=self.trailType, trailPps=self.trailPps, trailRetain=self.trailRetain)
            particle.executeEulerLagrange(particle, 0.5, 0.5)
            print ("A new Anti Tau has been created with a charge of " + str(self.charge) + " columbs, has an acceleration of " + str(self.acceleration) + " m/s^2, has a velocity of " + str(self.velocity) + " m/s, is named as a " + str(self.name) + " and has a mass of " + " kg")
    def convertToUseableMass(self, massToConvert):
        print(str(massToConvert[:4].join()))
        return str(massToConvert[:4].join())
createLeptonPath(0, 0, 0, 1, 1, leptonParticleMode=2, mass=1.22e-27, trailType="points", trailPps=1, trailRetain=10)