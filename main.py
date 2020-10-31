import nmap
import json
import pprint
from pymongo import MongoClient


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


def scanNetwork():
    nMapPortScanner = nmap.PortScanner()
    nMapScanner = nMapPortScanner.scan(hosts="172.18.231.178")
    resultOfScan = nMapScanner['scan']
    connectAndUpdateToDB(resultOfScan)
    return pprint.pprint(resultOfScan)


scanNetwork()
