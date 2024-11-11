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

# Function to check RiserHeight for all IfcStairFlight elements in the model and return non-compliant stair flights
def check_riser_height(ifc_model):
    stair_flights = ifc_model.by_type("IfcStairFlight")
    print(f"Found {len(stair_flights)} stair flights in the model.")

    non_compliant_stairs = []

    for stair_flight in stair_flights:
        riser_height = None
        
        # Check if direct attribute RiserHeight exists
        if "RiserHeight" in stair_flight.get_info():
            riser_height = stair_flight.get_info()["RiserHeight"]

        # If not found directly, search in property sets
        if riser_height is None:
            for definition in stair_flight.IsDefinedBy:
                if definition.is_a("IfcRelDefinesByProperties"):
                    property_set = definition.RelatingPropertyDefinition
                    if property_set.is_a("IfcPropertySet"):
                        for prop in property_set.HasProperties:
                            if prop.Name == "RiserHeight":
                                riser_height = prop.NominalValue.wrappedValue
                                break

        # Check if the riser height exceeds the limit
        if riser_height is not None:
            riser_height_rounded = round(riser_height, 1)
            if riser_height > 180:
                non_compliant_stairs.append((stair_flight.id(), riser_height_rounded))
    
    return non_compliant_stairs

# Directly call the function and print results
non_compliant_stairs = check_riser_height(ifc_model)

# Print summary and details of non-compliant stair flights
if non_compliant_stairs:
    print("\nNon-compliant stair flights found:")
    for stair_id, riser_height in non_compliant_stairs:
        print(f"StairFlight ID {stair_id} has a RiserHeight of {riser_height} mm, which exceeds the 180 mm limit.")
    print(f"\nTotal non-compliant stair flights: {len(non_compliant_stairs)}")
else:
    print("All stair flights comply with the RiserHeight requirement.")