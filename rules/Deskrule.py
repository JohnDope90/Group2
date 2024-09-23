import ifcopenshell
import os

os.chdir('C:/Users/sofie/OneDrive - Danmarks Tekniske Universitet/DTU kandidat/41934 - Advanced BIM/IFC models/GR06')
model = ifcopenshell.open('CES_BLD_24_06_ARC.ifc')

desks_required = 1620  # Expected value of desks

# Find the building storey that corresponds to "Level 16" and "Level 5"
storey_level_16 = None
storey_level_5 = None
for storey in model.by_type('IfcBuildingStorey'):
    if storey.Name == 'Level 16':  # Using the correct storey name
        storey_level_16 = storey
        break

for storey in model.by_type('IfcBuildingStorey'):
    if storey.Name == 'Level 5':
        storey_level_5 = storey
        break

desks_in_storey = None
if storey_level_16:
    # Get the desks (IfcFurniture) that are related to the found storey
    desks_in_storey = [
        furniture for furniture in model.by_type('IfcFurniture')
        if 'desk' in furniture.Name.lower() and 
           any(rel.RelatingStructure == storey_level_16 for rel in furniture.ContainedInStructure)
    ]
    desks_in_storey = desks_in_storey + 13*[
        furniture for furniture in model.by_type('IfcFurniture')
        if 'desk' in furniture.Name.lower() and 
           any(rel.RelatingStructure == storey_level_5 for rel in furniture.ContainedInStructure)
    ]

    desks_in_model = len(desks_in_storey)

    print('\n')
    print(f'There are {desks_in_model} desks in the model.')

    # Check to establish if we have the 'correct' number of desks
    if desks_required == desks_in_model:
        print(f"Result matches expected value ({desks_required})")
    elif desks_required > desks_in_model:
        print("There are fewer desks than expected")
    else:
        print("There are more desks than expected")
else:
    print("Some storey not found.")
    
print('\n')