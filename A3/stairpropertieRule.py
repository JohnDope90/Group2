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

# Function to calculate free width between railings
def calculate_free_width(stair):
    railings = []
    for rel in stair.IsDecomposedBy:
        for obj in rel.RelatedObjects:
            if obj.is_a("IfcRailing"):
                railings.append(obj)
    
    if len(railings) < 2:
        print(f"Stair ID: {stair.GlobalId} - Less than two railings found.")
        return None  # Insufficient data to calculate free width
    
    # Extract positions if available
    railing_positions = []
    for railing in railings:
        if railing.ObjectPlacement and railing.ObjectPlacement.RelativePlacement:
            location = railing.ObjectPlacement.RelativePlacement.Location
            if location:
                railing_positions.append(location.Coordinates)
    
    if len(railing_positions) == 2:
        # Calculate the distance between the two railing positions
        x_diff = railing_positions[1][0] - railing_positions[0][0]
        y_diff = railing_positions[1][1] - railing_positions[0][1]
        free_width = (x_diff**2 + y_diff**2)**0.5
        return free_width
    else:
        print(f"Stair ID: {stair.GlobalId} - Could not extract positions for both railings.")
        return None

# Function to check stair requirements, including free width check
def check_stair_requirements(stair):
    issues = []
    
    # Check Free Stair Width between railings
    free_width = calculate_free_width(stair)
    if free_width is not None and free_width < 1.0:
        issues.append(f"Free Stair Width between railings is too narrow: {free_width:.2f} m")
    elif free_width is None:
        issues.append("Unable to calculate free stair width between railings.")
    
    # Other checks (like tread depth and riser height)
    for rel in stair.IsDecomposedBy:
        for stair_flight in rel.RelatedObjects:
            if stair_flight.is_a("IfcStairFlight"):
                # Check Tread Depth
                tread_depth = getattr(stair_flight, 'TreadLength', None)
                if tread_depth and not (0.23 <= tread_depth <= 0.25):
                    issues.append(f"Tread Depth out of range: {tread_depth} m")
                
                # Check Riser Height
                riser_height = getattr(stair_flight, 'RiserHeight', None)
                if riser_height and riser_height > 0.18:
                    issues.append(f"Riser Height is too high: {riser_height} m")
    
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