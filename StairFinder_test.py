import ifcopenshell
from pathlib import Path
import ifcopenshell.util
import ifcopenshell.util.element
import ifcopenshell.util.placement
import ifcopenshell.util.shape
import ifcopenshell.geom
import numpy as np

print("All imported.\n")

# Group 10
path = r"C:\Users\sofie\OneDrive - Danmarks Tekniske Universitet\DTU kandidat\41934 - Advanced BIM\IFC models\GR2410\CES_BLD_24_10_ARC.ifc"

# Group 6
# path = r"C:\Users\sofie\OneDrive - Danmarks Tekniske Universitet\DTU kandidat\41934 - Advanced BIM\IFC models\GR2406\CES_BLD_24_06_ARC.ifc"
corrected_path = path.replace("\\", "/")

model_path = Path(corrected_path)
if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

model = ifcopenshell.open(model_path)

print("Model loaded.\n")

stairs = model.by_type('IfcStairFlight')

print("All stair flights found.\n")

stair = stairs[10]


elements = stairs
settings = ifcopenshell.geom.settings()
settings.set(settings.SITE_LOCAL_PLACEMENT, True)
stair_coords = []

print("... starting to find stair coordinates...\n")

for element in elements:
    shape = ifcopenshell.geom.create_shape(settings, element)
    inner_list = (ifcopenshell.util.shape.get_element_bbox_centroid(element, shape.geometry))
    stair_coords.append(inner_list)

print("Coordinates for stair no. 4:\n")
print(stair_coords[3],"\n")

# Check x-coordinate
print(stair_coords[3][0])

lst = []

for i in range(0, len(stair_coords)-1):
    for row in stair_coords:
        if row[0] == stair_coords[i][0]:
            lst.append(stair_coords[i])

print(f"Length of stair_coords: {len(stair_coords)},\n vs \n lenght of matching x-values?: {len(lst)}")