
from influxdb import InfluxDBClient
import uuid
import random
import time

# Author: Daniel C. Hirt
# Commented code represents the general process for how, assuming we have parsed the syslogs previously, we could generate a visualization on a subset of time-stamped data. 

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('pythontestdb')
number_of_points = 10000

#location_tags = [ "atkins", "woodward", "colvard", "union", "fretwell", "cone"]

access_point_tags = ["001", "002", "003", "004", "005", "006", "007", "008", "009"]

time_stamp_tags = ["2019-09-14T08:00:00Z", "2019-09-14T12:00:00Z", "2019-09-14T17:00:00Z"]

capacity_values = [0.23, 0.37, 0.64, 0.79, 0.94]

print("Dumping...")

#for i in range(1, number_of_points):
while(True):    
    json_body = [
            {
                "measurement": "capacity",
                "tags": {
                    "location": "Atkins Library",
                    "access_point": random.choice(access_point_tags)
                },

                # Un-comment to utilize fixed time intervals

                #"time": random.choice(time_stamp_tags),
                "fields": {
                    "value": random.choice(capacity_values)
                   
                }
            }
        ]

    client.write_points(json_body, database='pythontestdb', protocol='json', time_precision='s')
    time.sleep(5)
#else:
    #print("Dump successful.")
