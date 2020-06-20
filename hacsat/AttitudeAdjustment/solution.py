import sys
import numpy as np
import quaternion

class StarList():
    
    idNum = 1

    def __init__(self, qx, qy, qz, qb):
        self.idNum = StarList.idNum
        StarList.idNum += 1

        self.qx = float(qx)
        self.qy = float(qy)
        self.qz = float(qz)
        self.qq = float(qb)

        q = np.quaternion(self.qx, self.qy, self.qz, self.qq)
#        print(quaternion.as_euler_angles(q))
        self.x = quaternion.as_euler_angles(q)[0]
        self.y = quaternion.as_euler_angles(q)[1]
        self.z = quaternion.as_euler_angles(q)[2]

#        print(self.x)



#    def __str__(self):
#        return "Id: {}, qx: {}, qy: {}, qz: {}, qb: {}".format(self.idNum, self.qx, self.qy, self.qz, self.qq)

    def __str__(self):
        return "Id: {}, x: {}, y: {}, z: {}".format(self.idNum, self.x, self.y, self.z) 


        

if __name__ == "__main__":
    dataFile = sys.argv[1]

    f = open(dataFile)
    starRaw = f.read().replace('\n',' ').replace('\t','').replace(',',' ').replace('  ', ' ')

    print(starRaw)
    starRaw = starRaw.split(' ')
    starRaw = starRaw[:-1]
    #print(starRaw)

    starList = []
    for i in range((int(len(starRaw)/4))):
        starList.append(StarList(starRaw[4*i], starRaw[4*i+1], starRaw[4*i+2], starRaw[4*i+3] ))
        print(i)

    for i in range(len(starList)):
        print(starList[i])


    print(len(starList))
