import ifcopenshell
import os
from pathlib import Path

# Path to the IFC model
model_path = Path("C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_10_ARC.ifc")

# Check if the file exists
if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

# Open the IFC model
ifc_model = ifcopenshell.open(model_path)

# Function to identify if the IFC model contains stairs
def identify_stairs(ifc_model):
    stairs = ifc_model.by_type("IfcStair")
    if len(stairs) == 0:
        return False, "No stairs in model"
    return True, stairs

# Call the function and print the results
has_stairs, result = identify_stairs(ifc_model)

if has_stairs:
    print(f"Stairs found: {result}")
else:
    print(result)
