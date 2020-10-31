import nmap
import json
import pprint
from pymongo import MongoClient

#Determinate the Ip to be scanned
theScannedIp = "172.18.231.178"

def connectAndUpdateToDB(packet):
    # Determinate the host and the port number of mongodb
    client = MongoClient('localhost', 27017)

    # Determinate the Database's name
    dataBaseName = client['network_scan_db']

    # Determinate the Collection's name
    collectionName = dataBaseName['network_info']

    # Convert the result to JSON_OBJECT to insert it int the DB
    foundedPacketConvertedInJson = json.dumps(packet)

    return collectionName.insert_one({"packet": foundedPacketConvertedInJson})


def scanNetwork(theIP):
    #Create new scanner
    nMapPortScanner = nmap.PortScanner()

    #Determintate the ip, that we want to explore
    nMapScanner = nMapPortScanner.scan(hosts=theIP)

    #Write the result of the scan as a variable
    resultOfScan = nMapScanner['scan']

    #Save the result in the database
    connectAndUpdateToDB(resultOfScan)

    #Print the result as pretty json object
    return pprint.pprint(resultOfScan)

#Run the scan
scanNetwork(theScannedIp)
