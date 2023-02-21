'''
Copyright (C) Tetra System Solutions, 2023. All rights reserved.
'''

# Get proper imports.
from . import vega_util
from . import theory
import tensorflow as tf
# Class that allows us to simulate all particle interactions at once with entirely custom values.
class simulateAllParticleInteractions:
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
        if int(self.type1) and int(self.type2):
            if (type1 >= 0 or type1 <= 14) and (type2 >= 0 or type2 <= 14):
                self.executeParticleInteractionGraphics(self.type1, self.type2, self.mode)
            else:
                print("Please enter a number that's 1-15 to get a proper result, thank you.")
        else:
            print("Please enter an integer for an appropriate result, thank you.")
    def createBosonShape(self, eColor, xVec, yVec, zVec):
        self.boson = vega_util.camera_utils.shapes.circle(thickness=0.3)
        circlePath = [vega_util.camera_utils.vector(xVec,yVec,zVec), vega_util.camera_utils.vector(xVec,0.1,zVec)]
        finalShape = vega_util.camera_utils.extrusion(path=circlePath, shape=self.boson, color=eColor)
        return finalShape
    def convertToUseableMass(self, massToConvert):
        finalMass = str(massToConvert)
        finalHalf = finalMass[:len(finalMass)//2]
        print(finalHalf)
        return finalHalf
    def returnPathLagrangian(self, m1, m2, v1, v2):
        return self.calculateKineticEnergy(m1, v1) - self.calculatePotentialEnergy(m2, v2)
    def returnPathHamiltonian(self, m1, m2, v1, v2):
        return self.calculateKineticEnergy(m1, v1) + self.calculatePotentialEnergy(m2, v2) 
    def calculatePotentialEnergy(self, m, v):
        self.totalPotentialEnergy = float(m)*9.8*v
        return self.totalPotentialEnergy
    def calculateKineticEnergy(self, m, v):
        self.totalKineticEnergy = (float(m)*v**2)/2
        return self.totalKineticEnergy
    def executeParticleInteractionGraphics(self, type1, type2, mode):
        if mode == 1:
            self.executeEulerLagrange(self.mP1,self.mP2,self.mP3,self.mP4,type1,type2,self.spin1,self.spin2,self.c1,self.c2)
        elif mode == 2:
            self.executeEulerHamiltonian(self.mP1,self.mP2,self.mP3,self.mP4,type1,type2,self.spin1,self.spin2,self.c1,self.c2)
    # Joins two values or integers together to make them into usable numbers we can manipulate.
    def joinValue(self, value1, value2):
        p1valuestr1 = str(value1)
        p1valuestr2 = str(value2)
        global listIndex1
        global listIndex2  
        listIndex1 = list(p1valuestr1)
        listIndex2 = list(p1valuestr2)
    
        print(listIndex1)
        print(len(listIndex1)-1)
        for element in listIndex1:
            if element == "<" or element == ">":
                listIndex1 = str(listIndex1)
                listIndex1 = listIndex1.replace(element, '')
                listIndex1 = listIndex1.replace(",", "")
                list(listIndex1)
        for element in listIndex2:
            if element == "<" or element == ">":
                listIndex2 = str(listIndex2)
                listIndex2 = listIndex2.replace(element, '')
                listIndex2 = listIndex2.replace(",", "")
                list(listIndex2)
        listIndex1 = listIndex1[20:len(listIndex1)-24]
        listIndex2 = listIndex2[28:len(listIndex2)-24]
        print(listIndex1)
        print(listIndex2)
        finalValue1 = int(listIndex1)
        finalValue2 = int(listIndex2)
        print(finalValue1)
        print(finalValue2)
        return finalValue1, finalValue2
    #Euler Lagrangian Mechanics and Euler Hamiltonian Mechanics implemented below.
    def executeEulerLagrange(self, v1, v2, v3, v4, numArray1, numArray2, spin1, spin2, charge1, charge2):
        self.massList = [1.6e-36, 1.6e-36, 1.6e-36, 1.6e-36, 1.6e-36, 1.88e-28, 2.14e-37, 9.10e-31, 3.16e-27, 1.41e-14, 1.05e-15, 2.44e-17, 5.22e-17, 1.92e-14, 4.65e-17]
        m1 = self.convertToUseableMass(self.massList[numArray1])
        m2 = self.convertToUseableMass(self.massList[numArray1])
        m3 = self.convertToUseableMass(self.massList[numArray2])
        m4 = self.convertToUseableMass(self.massList[numArray2])
        

        particle1Vector=vega_util.camera_utils.vector(-0.2,0,0)
        RA=0.05
        particle1=vega_util.camera_utils.sphere(pos=particle1Vector, radius=RA, color=vega_util.camera_utils.vec(self.pC1_0,self.pC1_1,self.pC1_2), mass=m1, spin=spin1, charge=charge1, name=self.name1)

        particle2Vector=vega_util.camera_utils.vector(0.2,0,0)
        RB=0.05
        particle2=vega_util.camera_utils.sphere(pos=particle2Vector, radius=RB, color=vega_util.camera_utils.vec(self.pC2_0,self.pC2_1,self.pC2_2), mass=m2, spin=spin2, charge=charge2, name=self.name2)

        particle1.m=0.1
        particle2.m=0.1

        t = 0
        dt = 0.0001
        self.m1_0 = m1
        self.m2_0 = m2
        
        self.p1 = int(float(self.m1_0))*vega_util.camera_utils.vector(int(abs(self.returnPathLagrangian(m1, m2, v1, v2))), int(abs(self.returnPathLagrangian(m1, m2, v1, v2))), int(abs(self.returnPathLagrangian(m1, m2, v1, v2))))
        self.p2 = int(float(self.m2_0))*vega_util.camera_utils.vector(int(abs(self.returnPathLagrangian(m3, m4, v3, v4))), -int(abs(self.returnPathLagrangian(m3, m4, v3, v4))), -int(abs(self.returnPathLagrangian(m3, m4, v3, v4))))

        vecVal1, vecVal2 = self.joinValue(self.p1, self.p2)

        print(vecVal1) 
        print(vecVal2)

        vecVal1 = 0.1*vecVal1
        vecVal2 = 0.1*vecVal2

        vA=0.2*vecVal1
        vB=-0.2*vecVal2
        print(vA)
        print(vB)
        particle1.p=particle1.m*vega_util.camera_utils.vector(vA,vA,0)
        particle2.p=particle2.m*vega_util.camera_utils.vector(vB,-vB,0)
        k=999
        
        hasCollided=False
        
            
        while t<4.5:
            vega_util.camera_utils.rate(100000)
            firstVector1=vega_util.camera_utils.vector(0,0,0)
            firstVector2=vega_util.camera_utils.vector(0,0,0)
            r=particle2.pos-particle1.pos
            if vega_util.camera_utils.mag(r)<(RA+RB) or hasCollided:
                firstVector1=k*(vega_util.camera_utils.mag(r)-(RA+RB))*vega_util.camera_utils.norm(r)
                firstVector2=-firstVector1
                contact=True
                if contact:
                    if self.isAnti1 or self.isAnti2:
                        particle1.visible = False
                        particle2.visible = False
                    elif self.isAnti1 and self.isAnti2:
                        particle1.visible = True
                        particle2.visible = True
                    elif not(self.isAnti1 or self.isAnti2):
                        particle1.visible = True
                        particle2.visible = True
                    else:
                        particle1.visible = True
                        particle2.visible = True 


            particle1.p=particle1.p+firstVector1*dt
            particle2.p=particle2.p+firstVector2*dt

            particle1.pos=particle1.pos+particle1.p*dt/particle1.m
            particle2.pos=particle2.pos+particle2.p*dt/particle2.m

            

            t+=dt
            while t>4.5:
                
                
                def createTheory(data1, data2):
                    initialPrediction = tf.keras.Model(data1)
                    finalPrediction = tf.keras.Model(data2)
                    print("Hello")
                    theory.Theory(initialPrediction, finalPrediction)
                createTheory(particle1.pos, particle2.pos)
        while True:
            vega_util.camera_utils.scene.bind('click', self.getevent)
        
            
    def getevent(self):
        lasthit = None
        lastpick = None
        lastcolor = None
        if lasthit != None:
            if lastpick != None: lasthit.modify(lastpick, color=lastcolor)
            else: lasthit.color = vega_util.camera_utils.vector(lastcolor)
            lasthit = lastpick = None
        hit = vega_util.camera_utils.scene.mouse.pick
        if hit != None:
            lasthit = hit
            lastpick = None
            if isinstance(hit, vega_util.camera_utils.sphere):
                lasthit = hit.pos
                vega_util.camera_utils.basicFollow(hit, 1)
    
       
    def executeEulerHamiltonian(self, v1, v2, v3, v4, numArray1, numArray2, spin1, spin2, charge1, charge2):
        self.massList = [1.6e-36, 1.6e-36, 1.6e-36, 1.6e-36, 1.6e-36, 1.88e-28, 2.14e-37, 9.10e-31, 3.16e-27, 1.41e-14, 1.05e-15, 2.44e-17, 5.22e-17, 1.92e-14, 4.65e-17]
        
        m1 = self.convertToUseableMass(self.massList[numArray1])
        m2 = self.convertToUseableMass(self.massList[numArray1])
        m3 = self.convertToUseableMass(self.massList[numArray2])
        m4 = self.convertToUseableMass(self.massList[numArray2])
        

        particle1Vector=vega_util.camera_utils.vector(-0.2,0,0)
        RA=0.05
        particle1=vega_util.camera_utils.sphere(pos=particle1Vector, radius=RA, color=vega_util.camera_utils.vec(self.pC1_0,self.pC1_1,self.pC1_2), mass=m1, spin=spin1, charge=charge1, name=self.name1)

        particle2Vector=vega_util.camera_utils.vector(0.2,0,0)
        RB=0.05
        particle2=vega_util.camera_utils.sphere(pos=particle2Vector, radius=RB, color=vega_util.camera_utils.vec(self.pC2_0,self.pC2_1,self.pC2_2), mass=m2, spin=spin2, charge=charge2, name=self.name2)

        particle1.m=0.1
        particle2.m=0.1

        t = 0
        dt = 0.0001
        self.m1_0 = m1
        self.m2_0 = m2
        
        self.p1 = int(float(self.m1_0))*vega_util.camera_utils.vector(int(abs(self.returnPathHamiltonian(m1, m2, v1, v2))), int(abs(self.returnPathHamiltonian(m1, m2, v1, v2))), int(abs(self.returnPathHamiltonian(m1, m2, v1, v2))))
        self.p2 = int(float(self.m2_0))*vega_util.camera_utils.vector(int(abs(self.returnPathHamiltonian(m3, m4, v3, v4))), -int(abs(self.returnPathHamiltonian(m3, m4, v3, v4))), -int(abs(self.returnPathHamiltonian(m3, m4, v3, v4))))

        vecVal1, vecVal2 = self.joinValue(self.p1, self.p2)

        print(vecVal1)
        print(vecVal2)

        vecVal1 = 0.1*vecVal1
        vecVal2 = 0.1*vecVal2

        vA=0.2*vecVal1
        vB=-0.2*vecVal2
        print(vA)
        print(vB)
        particle1.p=particle1.m*vega_util.camera_utils.vector(vA,vA,0)
        particle2.p=particle2.m*vega_util.camera_utils.vector(vB,-vB,0)
        k=999
        
        hasCollided=False
        while t<4.5:
            vega_util.camera_utils.rate(100000)
            firstVector1=vega_util.camera_utils.vector(0,0,0)
            firstVector2=vega_util.camera_utils.vector(0,0,0)
            r=particle2.pos-particle1.pos
            if vega_util.camera_utils.mag(r)<(RA+RB) or hasCollided:
                firstVector1=k*(vega_util.camera_utils.mag(r)-(RA+RB))*vega_util.camera_utils.norm(r)
                firstVector2=-firstVector1
                contact=True
                if contact:
                    if self.isAnti1 or self.isAnti2:
                        particle1.visible = False
                        particle2.visible = False
                    elif self.isAnti1 and self.isAnti2:
                        particle1.visible = True
                        particle2.visible = True
                    elif not(self.isAnti1 or self.isAnti2):
                        particle1.visible = True
                        particle2.visible = True
                    else:
                        particle1.visible = True
                        particle2.visible = True

            particle1.p=particle1.p+firstVector1*dt
            particle2.p=particle2.p+firstVector2*dt

            particle1.pos=particle1.pos+particle1.p*dt/particle1.m
            particle2.pos=particle2.pos+particle2.p*dt/particle2.m
            
            t=t+dt

# Class execution and simulation begins here:
#simulateAllParticleInteractions(8, 8, 2, 2, 0, 0, 0, 1, 0, 0, 2, 2, 1, 2, None, None, None, None, 1, 4, 4, 4, 4, 4, 4, 2, 3, "first particle", "second particle", isAnti1=False, isAnti2=False)
    

        