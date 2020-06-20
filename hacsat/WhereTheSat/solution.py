import math
from skyfield.api import EarthSatellite, load
from numpy import atleast_1d
#import pyorbital.orbital
import datetime
import sys
import pwn
import re

class SatData:

    no = 0
    def __init__(self, name, l1, l2):
        self.name = name
        self.l1 = l1
        self.l2 = l2
        
        self.ts = load.timescale()
        self.sat = EarthSatellite(self.l1, self.l2, self.name, self.ts)
    
        self.no = SatData.no
        SatData.no += 1
    def posAtT(self, time):
        geocentric = self.sat.at(time)
        print(geocentric.position.km)

        return geocentric.position.km

   # def __str__(self):
   #     return ""
    #ts = load.timescale()
    #line1 = '1 13337U 98067A   20087.38052801 -.00000452  00000-0  00000+0 0  9995'
    #line2 = '2 13337  51.6460  33.2488 0005270  61.9928  83.3154 15.48919755219337'
    #satellite = EarthSatellite(line1, line2, 'REDACT', ts)
    #print(satellite)
if __name__ == "__main__":

    r = pwn.remote("where.satellitesabove.me", 5021)

    filePath = sys.argv[1]

    f = open(filePath)

    satRaw = f.read().split('\n')
   # print(satRaw)

    satList = []

    ts = load.timescale()
    time = ts.utc(2020, 3, 18, 22, 40, 47.0)
    for i in range(int(len(satRaw)/3)):
        satList.append(SatData(satRaw[3*i], satRaw[3*i+1], satRaw[3*i+2] ))
        print(i)
        print(satList[i].sat)
        print(satList[i].posAtT(time))


    x = pwn.raw_input("ticket: ")

    r.sendline(x)

    #time = ts.utc(2020, 3, 18, 1, 33, 38.0)
    #print(satList[43].sat)
    #print(satList[43].posAtT(time)) 

    while 1:
        x = r.recvline()
        print(x)
        if(b'time of:' in x):
            l = re.split('[,()]',x.decode('utf-8'))
            print(l)
            time = ts.utc(int(l[1]),int(l[2]),int(l[3]),int(l[4]),int(l[5]),float(l[6]))
            print(satList[43].sat)
            coord = satList[43].posAtT(time)
            if(b'X' in x):
                r.sendline(str(coord[0]))
            elif(b'Y' in x):
                r.sendline(str(coord[1]))
            elif(b'Z' in x):
                r.sendline(str(coord[2]))

