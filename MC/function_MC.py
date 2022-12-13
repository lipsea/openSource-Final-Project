import sys
sys.path.append("MC")
from MC_utils import *
from Coord import *
sys.path.append("Gesture/type")
import Msg 

origin = Vec3(553,8,1373)

players = {
    "BlueMoon06":BlueMoon06,
    "User2":User2,
    "User3":User3,
    "User4":User4    
}

ready = {
    "BlueMoon06":[False,False,False],
    "User2":[False,False,False],
    "User3":[False,False,False],
    "User4":[False,False,False]
}

def my_handleWearing(_players: list, msg: str) -> bool:
    [username, pose] = msg.split(':')
    id = getID(username)
    if not ready.get(username)[0] and (pose == Msg.RIGHTLEG or pose == Msg.LEFTLEG) :
        [x,y,z] = players.get(username).get("coord_boots")
        armor_b(id,x,y,z)
        print(msg)
        ready.get(username)[0] = True
    if pose == Msg.BODY and not ready.get(username)[1]:
        [x,y,z] = players.get(username).get("coord_chestplate")
        armor_c(id,x,y,z)
        print(msg)
        ready.get(username)[1] = True
    if pose == Msg.HEAD and not ready.get(username)[2]:
        [x,y,z] = players.get(username).get("coord_helmet")
        armor_h(id,x,y,z)
        print(msg)
        ready.get(username)[2] = True
    for user in ready.values():
        if user[0] == False:
            return False
        if user[1] == False:
            return False
        if user[2] == False:
            return False
    return True
    
def my_handleFighting(players: dict, msg: str) -> bool:
    [username, skill] = msg.split(':')
    id = getID(username)
    if skill == Msg.FIREBALL:
        spell_FireBall(id)
    if skill == Msg.CAGE:
        [x,y,z] = players.get(username).get("coord_cage")
        spell_Cage(id,x,y,z)
    if skill == Msg.LIGHTNING:
        [x,y,z] = players.get(username).get("coord_ln")
        spell_LN(id,x,y,z)
    if skill == Msg.TNT:
        [x,y,z] = players.get(username).get("coord_tnt")
        spell_TNT(id,x,y,z)

    