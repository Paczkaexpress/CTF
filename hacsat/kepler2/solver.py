from ast import Or
from pwn import *
from numpy.linalg import norm
from astropy import units
from astropy.time import Time, TimeDelta
from astropy.units.quantity import Quantity
from poliastro.bodies import Earth
from poliastro.twobody import Orbit
import re

# cannot connect sine we dont have an ssh connection
# io = remote('192.168.1.37', 54321)
TARGET_ICRF_RADIUS = 42164


# ######## GET STARTING ORBIT FROM STATE VECTOR ########
# io.recvuntil(b'Pos (km):   [')
# position = [float(i) for i in io.recvuntil(b']')[:-1].decode('ascii').split(', ')]

# io.recvuntil(b'Vel (km/s): [')
# velocity = [float(i) for i in io.recvuntil(b']')[:-1].decode('ascii').split(', ')]

# io.recvuntil(b'Time:       ')


time = "2021-06-26-19:20:00.000000-UTC"
pos = [8449.401305, 9125.794363, -17.461357]
vel = [-1.419072, 6.780149, 0.002865]

print("Initialized setting")

time = re.findall(".*\.000",time)[0][:-4]
time = Time(f"{time[:10]}T{time[11:]}")
print(time)

transfer_orbit = Orbit.from_vectors(Earth, pos * units.km, vel * units.km / units.s, epoch=time)
print(f"\n\ngot challange state vector: \nPos: {transfer_orbit.r},\nVel: {transfer_orbit.v}, \nTime: {transfer_orbit.epoch},\nR(ICRF): {norm(transfer_orbit.r.value)}")

print(f"Find the burn valid tieme opportunity {TARGET_ICRF_RADIUS} km\n")

while(norm(transfer_orbit.r.value) < TARGET_ICRF_RADIUS):
    transfer_orbit = transfer_orbit.propagate(transfer_orbit.epoch + TimeDelta(1, format="sec"))
    print(f"Current distance: {norm(transfer_orbit.r.value)}km\r", end="")

print(f"\n\ngot challange state vector: \nPos: {transfer_orbit.r},\nVel: {transfer_orbit.v}, \nTime: {transfer_orbit.epoch},\nR(ICRF): {norm(transfer_orbit.r.value)}")

final_orbit = Orbit.from_classical(Earth, Quantity(TARGET_ICRF_RADIUS, unit="km"), Quantity(0.0), Quantity(0.0, unit="rad"),
transfer_orbit.raan, transfer_orbit.argp, transfer_orbit.nu, epoch = transfer_orbit.epoch)

print(f"\n\ngot final state vector: \nPos: {final_orbit.r},\nVel: {final_orbit.v}, \nTime: {final_orbit.epoch}")
