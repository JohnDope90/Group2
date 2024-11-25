import ifcopenshell
from pathlib import Path

# Path to the IFC model
model_path = Path(r"C:\Users\sofie\OneDrive - Danmarks Tekniske Universitet\DTU kandidat\41934 - Advanced BIM\IFC models\GR2406\CES_BLD_24_06_STR.ifc")

# Check if the file exists and load the model
if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

ifc_model = ifcopenshell.open(model_path)
if ifc_model:
    print("IFC model loaded successfully!")
else:
    raise Exception("Failed to load IFC model.")

# Function to check TreadLength compliance for all IfcStairFlight elements
def check_tread_length_compliance(ID_list, min_length=230.0, max_length=250.0):
    stair_flights = []
    for ID in ID_list:
        stair_flights.append(ifc_model.by_id(ID))
    print(f"Found {len(stair_flights)} stair flights in the model.")

    non_compliant_stair_flights = []
    
    for stair_flight in stair_flights:
        # Attempt to retrieve TreadLength as a direct attribute or from property sets
        tread_length = stair_flight.get_info().get("TreadLength")
        
        if tread_length is None:
            for definition in stair_flight.IsDefinedBy:
                if definition.is_a("IfcRelDefinesByProperties"):
                    property_set = definition.RelatingPropertyDefinition
                    if property_set.is_a("IfcPropertySet"):
                        for prop in property_set.HasProperties:
                            if prop.Name == "TreadLength":
                                tread_length = prop.NominalValue.wrappedValue
                                break
                if tread_length is not None:
                    break
        
        # Add non-compliant stair flights to the list
        if tread_length is not None and not (min_length <= tread_length <= max_length):
            non_compliant_stair_flights.append((stair_flight.id(), round(tread_length, 1)))

    return non_compliant_stair_flights

import StairwayRule

# Call the function
results = StairwayRule.StairwayRule(model_path)

# Results
total_stairways, stairway_info, ID_list = results

# Call function and print results
non_compliant_tread_length = check_tread_length_compliance(ID_list)

# Print summary and details of non-compliant stair flights for TreadLength
if non_compliant_tread_length:
    print("\nNon-compliant TreadLength stair flights found:")
    for stair_id, tread_length in non_compliant_tread_length:
        print(f"StairFlight ID {stair_id} has a TreadLength of {tread_length} mm, which is outside the acceptable range of 230-250 mm.")
    print(f"\nTotal non-compliant TreadLength stair flights: {len(non_compliant_tread_length)}")
else:
    print("All stair flights comply with the TreadLength requirement.")