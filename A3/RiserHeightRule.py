import ifcopenshell
from pathlib import Path

# Function to check RiserHeight compliance for all IfcStairFlight elements
def check_riser_height_compliance(ifc_model, ID_list, max_height=180.0):
    stair_flights = []
    for ID in ID_list:
        stair_flights.append(ifc_model.by_id(ID))

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
            non_compliant_stairs.append((stair_flight.GlobalId, round(riser_height, 1)))
    return non_compliant_stairs




# #Try the function
# import StairwayRule

# model_path = r"C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_06_STR.ifc"
# ifc_model = ifcopenshell.open(model_path)
# # Call the function
# results = StairwayRule.StairwayRule(ifc_model)

# # Results
# total_stairways, stairway_info, ID_list = results

# # Call function and print results
# non_compliant_stairs = check_riser_height_compliance(ID_list)