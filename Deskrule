import bpy
from bonsai.bim.ifc import IfcStore
model = IfcStore.get_file()

desks_required = 108  # Expected value of desks

# Find the building storey that corresponds to "Level 16"
storey_level_16 = None
for storey in model.by_type('IfcBuildingStorey'):
    if storey.Name == 'Level 16':  # Using the correct storey name
        storey_level_16 = storey
        break

if storey_level_16:
    # Get the desks (IfcFurniture) that are related to the found storey
    desks_in_storey = [
        furniture for furniture in model.by_type('IfcFurniture')
        if 'desk' in furniture.Name.lower() and 
           any(rel.RelatingStructure == storey_level_16 for rel in furniture.ContainedInStructure)
    ]

    desks_in_model = len(desks_in_storey)
    
    print('\n')
    print(f'There are {desks_in_model} desks in Level 16.')

    # Check to establish if we have the 'correct' number of desks
    if desks_required == desks_in_model:
        print(f"Result matches expected value ({desks_required})")
    elif desks_required > desks_in_model:
        print("There are fewer desks than expected")
    else:
        print("There are more desks than expected")
else:
    print("Storey 'Level 16' not found.")
    
print('\n')
