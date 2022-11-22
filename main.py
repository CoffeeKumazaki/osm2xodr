import argparse
import pathlib
from math import floor, pi
import numpy as np
from OSMParser.testing import TestEntity, _test_nodes, testSimpleRoad, test_3WayTCrossing2
from OSMParser.osmParsing import parseAll,rNode, OSMWay,JunctionRoad, OSMWayEndcap, createOSMJunctionRoadLine, createOSMWayNodeList2XODRRoadLine
from OSMParser.xodrWriting import startBasicXODRFile,fillNormalRoads,fillJunctionRoads

parser = argparse.ArgumentParser(
          prog = 'osm2xord',
          description = 'converter for OpenStreetMaps (.osm) to OpenDrive (.xodr) format')

parser.add_argument('osm_file', type=str) 
parser.add_argument('--xodr_file', '-o', nargs='?', type=str)
parser.add_argument('--topograph_file', '-t', nargs='?', type=str)
args = parser.parse_args()

osmPfad = args.osm_file
topographieKartenPfad = args.topograph_file #'topomap.png'
xodrPfad = args.xodr_file if args.xodr_file is not None else pathlib.Path(osmPfad).with_suffix('.xodr').as_posix()

parseAll(osmPfad, bildpfad=topographieKartenPfad, minimumHeight = 163.0, maximumHeight= 192.0, curveRadius=12)

startBasicXODRFile(xodrPfad)
fillNormalRoads(xodrPfad)
fillJunctionRoads(xodrPfad)

