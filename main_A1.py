import ifcopenshell
import os

os.chdir('C:/Users/sofie/OneDrive - Danmarks Tekniske Universitet/DTU kandidat/41934 - Advanced BIM/IFC models/GR06')
model = ifcopenshell.open('CES_BLD_24_06_ARC.ifc')
#model = ifcopenshell.open("path/to/ifcfile.ifc")

from rules import windowRule
from rules import doorRule
from rules import deskRule


windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)
deskResult = deskRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)

# deskRule:

desks_required = 1620  # Expected value of desks
# Check to establish if we have the 'correct' number of desks
if desks_required == deskResult[0]:
        string = "the result matches the expected value of desks"
elif desks_required > deskResult[0]:
        string = "there are fewer desks than expected"
elif desks_required < deskResult[0]:
        string = "there are more desks than expected"

print("\n",deskResult[1],"\n")
print("There should be", desks_required,"desks in the model.\nThere are",deskResult[0],"desks in the model, which means",string)