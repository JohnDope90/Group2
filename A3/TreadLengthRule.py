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

# Function to check TreadLength for all IfcStairFlight elements in the model
def check_tread_length(ifc_model):
    stair_flights = ifc_model.by_type("IfcStairFlight")
    print(f"Found {len(stair_flights)} stair flights in the model.")

    non_compliant_tread_length = []

    for stair_flight in stair_flights:
        tread_length = None

        # Check if TreadLength exists as a direct attribute
        if "TreadLength" in stair_flight.get_info():
            tread_length = stair_flight.get_info()["TreadLength"]

        # If not found directly, search in property sets
        if tread_length is None:
            for definition in stair_flight.IsDefinedBy:
                if definition.is_a("IfcRelDefinesByProperties"):
                    property_set = definition.RelatingPropertyDefinition
                    if property_set.is_a("IfcPropertySet"):
                        for prop in property_set.HasProperties:
                            if prop.Name == "TreadLength":
                                tread_length = prop.NominalValue.wrappedValue
                                break

        # Check if tread length is outside the acceptable range
        if tread_length is not None:
            tread_length_rounded = round(tread_length, 1)
            if not (230 <= tread_length <= 250):
                non_compliant_tread_length.append((stair_flight.id(), tread_length_rounded))

    return non_compliant_tread_length

# Directly call the function and print results
non_compliant_tread_length = check_tread_length(ifc_model)

# Print summary and details of non-compliant stair flights for TreadLength
if non_compliant_tread_length:
    print("\nNon-compliant TreadLength stair flights found:")
    for stair_id, tread_length in non_compliant_tread_length:
        print(f"StairFlight ID {stair_id} has a TreadLength of {tread_length} mm, which is outside the acceptable range of 230-250 mm.")
    print(f"\nTotal non-compliant TreadLength stair flights: {len(non_compliant_tread_length)}")
else:
    print("All stair flights comply with the TreadLength requirement.")