# osm2xodr
converter for OpenStreetMaps (.osm) to OpenDrive (.xodr) format (just the drivable roads right now - you can edit the code for other osm-ways - its in the function "parseAll()").

just adjust the filenames/paths in the main.py and run it.

The requirements are osmread, numpy, PIL and pyproj

If a topographymap is used it should be in 16bit integer format and the max/min latitudes/longitudes of the map should match the points in the osm-file.

## How to use

```
$ ./osm2xodr.sh osm_file [-o xodr_file] [-t topograph_file]
```


## OpenDrive data Viewer
https://odrviewer.io/

https://sebastian-pagel.net/odrviewer/index.html
