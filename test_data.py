from data_process import DataProcess
from  flood_predict import FloodPerdiction

fp = open('test_data.txt') # Open file on read mode
lines = fp.read().split("\n") # Create a list containing all lines


from  flood_predict import FloodPerdiction
fp = FloodPerdiction()
dp = DataProcess()
for line in lines:
    print(line)
    protocol,instance = dp.prepareInstance(line)
    print(str(protocol)+">"+str(instance))
    result = fp.perdictAnomaly(protocol,instance)
    print(result)

fp.close() # Close file