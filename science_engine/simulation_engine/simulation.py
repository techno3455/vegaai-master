from proceduralGeneratedExamples.createParticleCollision import *


# Simulate all of the possible scenarios in the Standard Model. (All 234 Scenarios)
class simulateNonCustomScenario:
    def __init__(self, scenario, mP1, mP2, mP3, mP4, type1, type2, xPos1, yPos1, zPos1, xPos2, yPos2, zPos2, spin1, spin2, trailType1, trailType2, trailPps1, trailPps2, mode, pC1_0, pC1_1, pC1_2, pC2_0, pC2_1, pC2_2, c1, c2, name1, name2):
        self.scenario = scenario
        self.mP1 = mP1
        self.mP2 = mP2
        self.mP3 = mP3
        self.mP4 = mP4
        self.xPos1 = xPos1
        self.yPos1 = yPos1
        self.zPos1 = zPos1
        self.xPos2 = xPos2
        self.yPos2 = yPos2
        self.zPos2 = zPos2
        self.spin1 = spin1
        self.spin2 = spin2
        self.type1 = type1
        self.type2 = type2
        self.trailType1 = trailType1
        self.trailType2 = trailType2
        self.trailPps1 = trailPps1
        self.trailPps2 = trailPps2
        self.mode = mode
        self.pC1_0 = pC1_0
        self.pC1_1 = pC1_1
        self.pC1_2 = pC1_2
        self.pC2_0 = pC2_0
        self.pC2_1 = pC2_1
        self.pC2_2 = pC2_2
        self.c1 = c1
        self.c2 = c2
        self.name1 = name1
        self.name2 = name2
        self.type1 = type1
        self.type2 = type2
        self.chooseParticleScenario(self.scenario)
    def chooseParticleScenario(self, scenario):
        if scenario == 1:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.9, 0.2, 0.2, 0.9, 0.2, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 2:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.9, 0.2, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 3:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.9, 0.2, 0.6, 0.3, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 4:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.9, 0.2, 0.3, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 5:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.9, 0.2, 0.8, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 6:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 7:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 0.2, 0.9, 0.2, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 8:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 0.3, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 9:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 0.6, 0.3, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 10:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 0.8, 0.6, 0.6,  self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 11:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.3, 0.6, 0.6, 0.3, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 12:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.3, 0.6, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 13:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.3, 0.6, 0.2, 0.9, 0.2, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 14:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.3, 0.6, 0.3, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 15:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 0, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.3, 0.6, 0.8, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 16:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 17:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.3, 0.2, 0.9, 0.2, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 18:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.3, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 19:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.3, 0.8, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 20:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.3, 0.6, 0.3, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 21:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.6, 0.6, 0.8, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 22:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.6, 0.6, 0.2, 0.9, 0.2, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 23:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.6, 0.6, 0.6, 0.3, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 24:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.6, 0.6, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 25:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 26:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.4, 0.8, 0.8, 0.4, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 27:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.4, 0.8, 0.5, 0.4, 0.5, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 28:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.4, 0.8, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 29:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.4, 0.8, 0.7, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 30:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 1, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.4, 0.8, 0, 0, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 31:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.4, 0.8, 0.7, 0, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 32:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.4, 0.8, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 33:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.4, 0.8, 0.7, 0, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 34:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.5, 0.4, 0.5, 0.5, 0.4, 0.5, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 35:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.5, 0.4, 0.5, 0.8, 0.4, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 36:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.5, 0.4, 0.5, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 37:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.5, 0.4, 0.5, 0.7, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 38:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.5, 0.4, 0.5, 0, 0, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 39:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.5, 0.4, 0.5, 0.7, 0, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 40:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.5, 0.4, 0.5, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 41:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.5, 0.4, 0.5, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 42:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 43:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 0.8, 0.4, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 44:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 0.5, 0.4, 0.5, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 45:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 2, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 0.7, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 46:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 0, 0, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 47:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 0.7, 0, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 48:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 49:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 1, 1, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 50:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 51:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0.7, 0.8, 0.4, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 52:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0.7, 0.5, 0.4, 0.5, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 53:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0.7, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 54:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0.7, 0, 0, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 55:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0.7, 0.7, 0, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 56:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0.7, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 57:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0.7, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 58:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0, 0.7, 0, 0, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 59:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0, 0.7, 0.8, 0.4, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 60:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 3, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0, 0.7, 0.5, 0.4, 0.5, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 61:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0, 0.7, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 62:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0, 0.7, 0.7, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 63:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0, 0.7, 0.7, 0, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 64:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0, 0.7, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 65:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0, 0.7, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 66:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0.7, 0, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 67:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0.8, 0.4, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 68:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0.5, 0.4, 0.5, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 69:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 70:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0.7, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 71:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0, 0, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 72:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 73:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 74:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 75:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 4, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.8, 0.4, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 76:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.5, 0.4, 0.5, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 77:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 78:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.7, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 79:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0, 0, 0.7, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 80:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.7, 0, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 81:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.7, 0, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 82:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0.7, 0, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 83:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0.8, 0.4, 0.8, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 84:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0.5, 0.4, 0.5, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 85:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 1, 1, 1, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 86:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0.7, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 87:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0, 0, 0.7, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 88:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 89:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0, 0.3, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 90:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 5, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.9, 0.4, 0.9, 0.9, 0.4, 0.9, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 91:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.9, 0.4, 0.9, 0.6, 0.4, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 92:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.9, 0.4, 0.9, 0.2, 0.2, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 93:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.9, 0.4, 0.9, 1, 0.2, 0.2, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 94:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.9, 0.4, 0.9, 0, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 95:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.9, 0.4, 0.9, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 96:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.9, 0.4, 0.9, 0.4, 0.4, 0.1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 97:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.9, 0.4, 0.9, 0.1, 0.4, 0.4, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 98:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.9, 0.4, 0.9, 0.6, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 99:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.9, 0.4, 0.9, 0.3, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 100:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.9, 0.4, 0.9, 0.8, 0.8, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 101:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.9, 0.4, 0.9, 0.3, 0.8, 0.8, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 102:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 0.6, 0.4, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 104:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 0.9, 0.4, 0.9, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 105:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 0.2, 0.2, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 106:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 6, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 1, 0.2, 0.2, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 107:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 108:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 0, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 109:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 110:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 0.4, 0.4, 0.1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 111:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 0.1, 0.4, 0.4, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 112:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 0.6, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 113:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 0.3, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 114:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 0.8, 0.8, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 115:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.4, 0.6, 0.3, 0.8, 0.8, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 116:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.2, 1, 0.2, 0.2, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 117:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.2, 1, 0.9, 0.4, 0.9, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 118:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.2, 1, 0.6, 0.4, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 119:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.2, 1, 1, 0.2, 0.2, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 120:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.2, 1, 0, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 121:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 7, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.2, 1, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 122:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.2, 1, 0.4, 0.4, 0.1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 123:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.2, 1, 0.1, 0.4, 0.4, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 124:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.2, 1, 0.6, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 125:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.2, 1, 0.3, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 126:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.2, 1, 0.8, 0.8, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 127:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.2, 0.2, 1, 0.3, 0.8, 0.8, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 128:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 0.2, 0.2, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 129:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 0.2, 0.2, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 130:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 0.2, 0.2, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 131:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 0.2, 0.2, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 132:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 0.2, 0.2, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 133:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 0.2, 0.2, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 134:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 0.2, 0.2, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 135:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 0.2, 0.2, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 136:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 8, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 0.2, 0.2, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 137:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 0.2, 0.2, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 138:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 1, 0.2, 0.2, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 139:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0.7, 0.7, 0, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 140:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0.7, 0.7, 0.9, 0.4, 0.9, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 141:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0.7, 0.7, 0.6, 0.4, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 142:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0.7, 0.7, 0.2, 0.2, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 143:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0.7, 0.7, 1, 0.2, 0.2, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 144:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0.7, 0.7, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 145:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0.7, 0.7, 0.4, 0.4, 0.1, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 146:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0.7, 0.7, 0.1, 0.4, 0.4, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 147:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0.7, 0.7, 0.6, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 148:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0.7, 0.7, 0.3, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 149:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0.7, 0.7, 0.8, 0.8, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 150:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0, 0.7, 0.7, 0.3, 0.8, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 151:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 9, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 152:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.9, 0.4, 0.9, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 153:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.6, 0.4, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 154:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.2, 0.2, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 155:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 1, 0.2, 0.2, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 156:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 157:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.4, 0.4, 0.1, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 158:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.1, 0.4, 0.4, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 159:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.6, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 160:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.3, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 161:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.8, 0.8, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 162:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.7, 0.7, 0, 0.3, 0.8, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 163:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.4, 0.4, 0.1, 0.4, 0.4, 0.1, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 164:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.4, 0.4, 0.1, 0.9, 0.4, 0.9, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 165:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.4, 0.4, 0.1, 0.6, 0.4, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 166:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 10, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.4, 0.4, 0.1, 0.2, 0.2, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 167:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.4, 0.4, 0.1, 1, 0.2, 0.2, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 168:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.4, 0.4, 0.1, 0, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 169:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.4, 0.4, 0.1, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 170:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.4, 0.4, 0.1, 0.1, 0.4, 0.4, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 171:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.4, 0.4, 0.1, 0.6, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 172:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.4, 0.4, 0.1, 0.3, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 173:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.4, 0.4, 0.1, 0.8, 0.8, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 174:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.4, 0.4, 0.1, 0.3, 0.8, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 175:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.1, 0.4, 0.4, 0.1, 0.4, 0.4, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 176:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.1, 0.4, 0.4, 0.9, 0.4, 0.9, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 177:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.1, 0.4, 0.4, 0.6, 0.4, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 178:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.1, 0.4, 0.4, 0.2, 0.2, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 179:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.1, 0.4, 0.4, 1, 0.2, 0.2, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 180:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.1, 0.4, 0.4, 0, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 181:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 11, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.1, 0.4, 0.4, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 182:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.1, 0.4, 0.4, 0.4, 0.4, 0.1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 183:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.1, 0.4, 0.4, 0.6, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 184:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.1, 0.4, 0.4, 0.3, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 185:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.1, 0.4, 0.4, 0.8, 0.8, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 186:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.1, 0.4, 0.4, 0.3, 0.8, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 187:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.6, 0.3, 0.6, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 188:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.6, 0.3, 0.9, 0.4, 0.9, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 189:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.6, 0.3, 0.6, 0.4, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 190:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.6, 0.3, 0.2, 0.2, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 191:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.6, 0.3, 1, 0.2, 0.2, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 192:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.6, 0.3, 0, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 193:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.6, 0.3, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 194:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.6, 0.3, 0.4, 0.4, 0.1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 195:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.6, 0.3, 0.1, 0.4, 0.4, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 196:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 12, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.6, 0.3, 0.3, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 197:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.6, 0.3, 0.8, 0.8, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 198:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.6, 0.6, 0.3, 0.3, 0.8, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 199:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.6, 0.3, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 200:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.6, 0.9, 0.4, 0.9, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 201:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.6, 0.6, 0.4, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 202:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.6, 0.2, 0.2, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 203:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.6, 1, 0.2, 0.2, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 204:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.6, 0, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 205:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.6, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 206:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.6, 0.4, 0.4, 0.1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 207:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.6, 0.1, 0.4, 0.4, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 208:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.6, 0.6, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 209:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.6, 0.8, 0.8, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 210:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 13, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.6, 0.6, 0.3, 0.8, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 211:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 0,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.8, 0.3, 0.8, 0.8, 0.3, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 212:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 1,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.8, 0.3, 0.9, 0.4, 0.9, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 213:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.8, 0.3, 0.6, 0.4, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 214:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 3,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.8, 0.3, 0.2, 0.2, 1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 215:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 4,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.8, 0.3, 1, 0.2, 0.2, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 216:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 5,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.8, 0.3, 0, 0.7, 0.7, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 217:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 6,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.8, 0.3, 0.7, 0.7, 0, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 218:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 7,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.8, 0.3, 0.4, 0.4, 0.1, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 219:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 8,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.8, 0.3, 0.1, 0.4, 0.4, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 220:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 9,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.8, 0.3, 0.6, 0.6, 0.3, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 221:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 10,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.8, 0.3, 0.3, 0.6, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 222:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 11,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.8, 0.8, 0.3, 0.3, 0.8, 0.8, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 223:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 12,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.8, 0.8, 0.3, 0.8, 0.8, self.c1, self.c2, self.name1, self.name2, True, False)
        elif scenario == 224:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 13,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.8, 0.8, 0.9, 0.4, 0.9, self.c1, self.c2, self.name1, self.name2, False, False)
        elif scenario == 225:
            simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, 14, 14,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.8, 0.8, 0.6, 0.4, 0.6, self.c1, self.c2, self.name1, self.name2, True, False)

#Simulate a custom Scenario if one is not present within the AI.
class simulateCustomScenario:
    def __init__(self, mP1, mP2, mP3, mP4, xPos1, yPos1, zPos1, xPos2, yPos2, zPos2, spin1, spin2, type1, type2, trailType1, trailType2, trailPps1, trailPps2, mode, pC1_0, pC1_1, pC1_2, pC2_0, pC2_1, pC2_2, c1, c2, name1, name2, isAnti1, isAnti2):
        self.mP1 = mP1
        self.mP2 = mP2
        self.mP3 = mP3
        self.mP4 = mP4
        self.xPos1 = xPos1
        self.yPos1 = yPos1
        self.zPos1 = zPos1
        self.xPos2 = xPos2
        self.yPos2 = yPos2
        self.zPos2 = zPos2
        self.spin1 = spin1
        self.spin2 = spin2
        self.type1 = type1
        self.type2 = type2
        self.trailType1 = trailType1
        self.trailType2 = trailType2
        self.trailPps1 = trailPps1
        self.trailPps2 = trailPps2
        self.mode = mode
        self.pC1_0 = pC1_0
        self.pC1_1 = pC1_1
        self.pC1_2 = pC1_2
        self.pC2_0 = pC2_0
        self.pC2_1 = pC2_1
        self.pC2_2 = pC2_2
        self.c1 = c1
        self.c2 = c2
        self.name1 = name1
        self.name2 = name2
        self.isAnti1 = isAnti1 
        self.isAnti2 = isAnti2
        self.simulateScenario()
    def simulateScenario(self):
        simulateAllParticleInteractions(self.mP1, self.mP2, self.mP3, self.mP4, self.type1, self.type2,  self.xPos1, self.yPos1, self.zPos1, self.xPos2, self.yPos2, self.zPos2, self.spin1, self.spin2, self.trailType1, self.trailType2, self.trailPps1, self.trailPps2, self.mode, 0.3, 0.8, 0.8, 0.7, 0.7, 0.3, self.c1, self.c2, self.name1, self.name2, self.isAnti1, self.isAnti2)

simulateNonCustomScenario(2, 8, 8, 2, 2, 0, 0, 0, 1, 0, 0, 2, 2, 1, 2, None, None, None, None, 1, 4, 4, 4, 4, 4, 4, 2, 3, "first particle", "second particle")