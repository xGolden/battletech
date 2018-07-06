import json
import os
from glob import glob

#F:\Steam Games\steamapps\common\BATTLETECH\BattleTech_Data\StreamingAssets\data\movement

#read from the file and multiply specific values by x, then overwrite the file
def mult_move_values(json_file, x):
  j = {}
  
  with open(json_file, "r+") as f:
    j = json.load(f)
    j['WalkVelocity'] = x * j['WalkVelocity']
    j['RunVelocity'] = x * j['RunVelocity']
    j['SprintVelocity'] = x * j['SprintVelocity']
    j['LimpVelocity'] = x * j['LimpVelocity']
    f.seek(0)
    json.dump(j,f,sort_keys=True,indent=4)
    f.truncate()

#grab a list of all the files that match file name format
def list_files():
  return glob("movedef*.json")


#query the user for a multiplier value
def query_user():
  return input("What value would you like to multiply by: ")


def bt_edit_jsons():
  x = int(query_user())
  files = list_files()
  print("The following files are to be editted:")
  print(files)
  
  for f in files:
    mult_move_values(f,x)
  

bt_edit_jsons()


