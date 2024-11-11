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

# Function to identify all stairs in the IFC model
def get_stairs(ifc_model):
    stairs = ifc_model.by_type("IfcStair")
    print(f"Found {len(stairs)} stairs in the model.")  # Debugging output
    return stairs

# Function to check stair properties
def check_stair_requirements(stair):
    issues = []
    
    # Iterate through related components (like flights) for each stair
    for rel in stair.IsDecomposedBy:
        for stair_flight in rel.RelatedObjects:
            if stair_flight.is_a("IfcStairFlight"):
                # Check Free Stair Width
                width = getattr(stair_flight, 'Width', None)
                if width and width < 1.0:
                    issues.append(f"Free Stair Width is too narrow: {width} m")
                
                # Check Tread Depth
                tread_depth = getattr(stair_flight, 'TreadLength', None)
                if tread_depth and not (0.23 <= tread_depth <= 0.25):
                    issues.append(f"Tread Depth out of range: {tread_depth} m")
                
                # Check Riser Height
                riser_height = getattr(stair_flight, 'RiserHeight', None)
                if riser_height and riser_height > 0.18:
                    issues.append(f"Riser Height is too high: {riser_height} m")
                
                # Check Ceiling Height
                # Assuming `CeilingHeight` is available or calculated separately
                ceiling_height = getattr(stair_flight, 'CeilingHeight', None)
                if ceiling_height and ceiling_height < 2.1:
                    issues.append(f"Ceiling Height is too low: {ceiling_height} m")
    
    return issues

# Main logic to get stairs and check requirements
stairs = get_stairs(ifc_model)

if stairs:
    for stair in stairs:
        issues = check_stair_requirements(stair)
        if issues:
            print(f"Stair ID: {stair.GlobalId} has issues:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"Stair ID: {stair.GlobalId} meets all requirements.")
else:
    print("No stairs found in the model.")