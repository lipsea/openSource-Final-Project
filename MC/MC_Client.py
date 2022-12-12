from mcpi.minecraft import Minecraft
import time 
import math
from multipledispatch import dispatch
from mcpi.vec3 import Vec3


# server = Minecraft.create("dev.linin.xyz",8301)
server = Minecraft.create("localhost",4711)

origin = Vec3(373,9,1317)

# Convert the exact coord in game
def coord(x,y,z):
    return (x-origin.x,y-origin.y,z-origin.z)

#Basic Methods

def getID(name): # Get in-game ID from username
    return server.getPlayerEntityId(name)

@dispatch(str)
def getPos(name): # Get player pos from username
    return server.entity.getPos(getID(name))

@dispatch(int)
def getPos(id): # Get player pos from ID
    return server.entity.getPos(id)

# Spells

def spell_Cage(id): # Cast ice-cage at the provided player's pos
    pos = server.entity.getPos(id)
    server.entity.setPos(id,math.floor(pos.x)+0.5,pos.y,math.floor(pos.z)+0.5)
    for i in range(3):
        for j in range(3):
            for k in range (3):
                server.setBlock(pos.x-1+i,pos.y+k,pos.z-1+j,79)
    server.setBlock(pos.x,pos.y+1,pos.z,8)

# Cast TNT ring at the provided player's pos
def spell_TNT(id):
    pos = server.entity.getPos(id)
    server.spawnEntity(pos.x,pos.y,pos.z,20)


# Main Process

username = "BlueMoon06"
id = getID(username)

CD_spell = 0 # Cooldown for normal spells, reach 50 to cast
CD_ult = 0 # Cooldown for ult (TNT?), reach 200 to cast
f_FB = False # Determine whether Fireball had been casted
f_TNT = False # Determine whether TNT had been casted
f_LN = False # Determine whether Lightning had been casted

while True:
    time.sleep(0.1)
    CD_spell += 1
    CD_ult += 1
    pos = getPos(id)

    # Reseting Command block
    if f_FB:
        server.setBlock(10002-origin.x,6-origin.y,9893-origin.z,0)
        f_FB = False

    # Code for Testing
    for text in server.events.pollChatPosts():
        if text.message == "clear":
            server.setBlocks(19647,1,18659,19657,6,18669,0)
        if text.message == "cage":
            spell_Cage(id)
        if text.message == "FB":
            server.setBlock(10002-origin.x,6-origin.y,9893-origin.z,76)
            f_FB = True
        if text.message == "Origin":
            server.entity.setPos(id,0,0,0)
        if text.message == "TNT":
            spell_TNT(id)