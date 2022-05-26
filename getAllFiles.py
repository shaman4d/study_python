
import os

basepath = "d:/Projects/_Qublix/TropicTroubleGen3/work/TropicTrouble/"
addpath = "assets/loe/"
path = basepath + addpath
flist = []
for root, dirs, files in os.walk(path):
   for name in files:
       fname = os.path.join(root, name).replace(basepath,"").replace("\\", "/")
       flist.append(fname)

sAssets = '['
for f in flist:
    sAssets += '"' + f + '",'

sAssets = sAssets[:-1]
sAssets += ']'
print(sAssets)

f = open("assetsList.txt","w")
f.write(sAssets)
f.close()
