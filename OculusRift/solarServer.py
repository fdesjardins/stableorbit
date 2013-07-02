#Server code solarClient
import orbitSystem
import cPickle
import SimpleXMLRPCServer
import sys
#sys.path.append('./beta')
#import StableOrbitDAO
import os
from orbitSystem import System
from orbitSystem import Galaxy
import soSession
import datetime
class solarServer(object):
    def __init__(self,xString):
        import string
        print "solarServer launched: "+xString+":8000"
        self.galaxy = Galaxy()
        self.python_string = string
        self.seedcount = 1
        self.players = []
        self.onPlayers = []
        
    def getSystem(self):
        print "recieved system request"
        self.seedcount += 1
        aSystem = orbitSystem.System(self.seedcount)
        aString = cPickle.dumps(aSystem)
        print "sending system"
        return aString
        #xfile = open("serialSystem.txt")
        #print xfile.read()
    
        
    def playerLogin(self, uname, passw):
        if uname == "Default":
            return soPlayer()
        for player in self.players:
            if player.name == uname:
                if player.passw == passw:
                    return player
                else:
                    return "password unknown"
        print SimpleXMLRPCServer.SimpleXMLRPCServer.get_request()
        #print client.address
        player = soPlayer(uname, passw)
        self.players.append(player)
        self.onPlayers.append(player)
      
    def getNextStar(self):
        print "Getting Next Star #", self.seedcount
        self.seedcount+=1
        starfile = cPickle.dumps(
            self.galaxy.stars[
                len(self.galaxy.stars)-self.seedcount])
        return starfile
      
        
    def getAllStars(self):
        print "Get All Stars"
        allStarFiles = os.listdir('data')
        print allStarFiles
        #os.chdir('..')
        return allStarFiles
    
    def getGalaxy(self):
        return cPickle.dumps(self.galaxy)
        
        
    def insertSystem(self, xfile):# playerName, fitness, iterations):
        print"connection acquired"
        os.chdir('data')
        sysName = 'system'+str(self.seedcount)+'.sys'
        print "saving system as:"
        print sysName
        saveFile = open(sysName, "w+")
        saveFile.write(xfile)
        saveFile.close()
        os.chdir("..")
        return sysName
    def retrieveSystem(self, sysName):
        print "recieved request to retrieve system"
        print sysName
        os.chdir('data')
        xfile = open(sysName).read()
        os.chdir("..")
        print "sending system"
        return xfile

if __name__=='__main__':
    xString = "192.168.1.101"
    server = SimpleXMLRPCServer.SimpleXMLRPCServer((xString, 8000))
    server.register_instance(solarServer(xString))
    server.serve_forever()
    
