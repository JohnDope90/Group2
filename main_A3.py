import ifcopenshell
from pathlib import Path

# Path to the IFC model
model_path = Path("C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_10_ARC.ifc")

# Check if the file exists
if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

# Open the IFC model
ifc_model = ifcopenshell.open(model_path)

# Check if model was loaded correctly
if ifc_model:
    print("IFC model loaded successfully!")
else:
    print("Failed to load IFC model.")
