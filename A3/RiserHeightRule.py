import ifcopenshell
from pathlib import Path

# Path to the IFC model
model_path = r"C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_06_STR.ifc"

# Check if the file exists and load the model
if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

ifc_model = ifcopenshell.open(model_path)
if ifc_model:
    print("IFC model loaded successfully!")
else:
    raise Exception("Failed to load IFC model.")

# Function to check RiserHeight compliance for all IfcStairFlight elements
def check_riser_height_compliance(ID_list, max_height=180.0):
    stair_flights = []
    for ID in ID_list:
        stair_flights.append(ifc_model.by_id(ID))
    print(f"Found {len(stair_flights)} stair flights in the model.")

    non_compliant_stairs = []

    for stair_flight in stair_flights:
        # Attempt to retrieve RiserHeight as a direct attribute or from property sets
        riser_height = stair_flight.get_info().get("RiserHeight")
        
        if riser_height is None:
            for definition in stair_flight.IsDefinedBy:
                if definition.is_a("IfcRelDefinesByProperties"):
                    property_set = definition.RelatingPropertyDefinition
                    if property_set.is_a("IfcPropertySet"):
                        for prop in property_set.HasProperties:
                            if prop.Name == "RiserHeight":
                                riser_height = prop.NominalValue.wrappedValue
                                break
                if riser_height is not None:
                    break
        
        # Add non-compliant stair flights to the list
        if riser_height is not None and riser_height > max_height:
            non_compliant_stairs.append((stair_flight.id(), round(riser_height, 1)))

    return non_compliant_stairs



import StairwayRule

# Call the function
results = StairwayRule.StairwayRule(model_path)

# Results
total_stairways, stairway_info, ID_list = results

# Call function and print results
non_compliant_stairs = check_riser_height_compliance(ID_list)

# Print summary and details of non-compliant stair flights for RiserHeight
if non_compliant_stairs:
    print("\nNon-compliant stair flights found:")
    for stair_id, riser_height in non_compliant_stairs:
        print(f"StairFlight ID {stair_id} has a RiserHeight of {riser_height} mm, which exceeds the 180 mm limit.")
    print(f"\nTotal non-compliant stair flights: {len(non_compliant_stairs)}")
else:
    print("All stair flights comply with the RiserHeight requirement.")