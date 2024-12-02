import ifcopenshell
from pathlib import Path
from A3 import StairwayRule, RiserHeightRule, TreadLengthRule, WidthRule, HeadHeightRule

print("Loading model")

# Specify the IFC model path
# model_path = r"C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_06_STR.ifc"
model_path = Path(r"C:\Users\sofie\OneDrive - Danmarks Tekniske Universitet\DTU kandidat\41934 - Advanced BIM\IFC models\GR2406\CES_BLD_24_06_STR.ifc")

# Check if the file exists and load the model
if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

ifc_model = ifcopenshell.open(model_path)
if ifc_model:
    print("IFC model loaded successfully!")
else:
    raise Exception("Failed to load IFC model.")


# Call StairwayRule
stairway_results = StairwayRule.StairwayRule(ifc_model)
total_stairways, stairway_info, ID_list = stairway_results

print(f"\nNumber of full-height stairways found: {total_stairways}")
print("Stairway information:")
print(stairway_info)


# Call Riser Height
non_compliant_stairs = RiserHeightRule.check_riser_height_compliance(ifc_model, ID_list)
# Print summary and details of non-compliant stair flights for RiserHeight
if non_compliant_stairs:
    print("\nNon-compliant stair flights found:")
    for stair_id, riser_height in non_compliant_stairs:
        print(f"StairFlight ID {stair_id} has a RiserHeight of {riser_height} mm, which exceeds the 180 mm limit.")
        print(f"\nTotal non-compliant stair flights: {len(non_compliant_stairs)}")
else:
    print("All stair flights comply with the RiserHeight requirement.")


# Call Thread Length
non_compliant_tread_length = TreadLengthRule.check_tread_length_compliance(ifc_model, ID_list)

# Print summary and details of non-compliant stair flights for TreadLength
if non_compliant_tread_length:
    print("\nNon-compliant TreadLength stair flights found:")
    for stair_id, tread_length in non_compliant_tread_length:
        print(f"StairFlight ID {stair_id} has a TreadLength of {tread_length} mm, which is outside the acceptable range of 230-250 mm.")
    print(f"\nTotal non-compliant TreadLength stair flights: {len(non_compliant_tread_length)}")
else:
    print("All stair flights comply with the TreadLength requirement.")

# Call WidthRule to calculate widths for all stairs
narrow_stairs = WidthRule.WidthRule(ifc_model, ID_list)
if len(narrow_stairs) > 0:
    print("\nNon-compliant Stair Width stair flights found:")
    for stair_id, width in narrow_stairs:
        print(f"StairFlight ID {narrow_stairs[0]} has a Width of {narrow_stairs[1]} mm, which is less than 1000m.")
    print(f"\nTotal non-compliant Stair Width stair flights: {len(narrow_stairs)}")
elif len(narrow_stairs) == 0:
    print("\nAll stair flights comply with the Stair Width requirement.")


print("\n")

# Call Head Height
too_low_stairs = HeadHeightRule.HeightRule(ifc_model,ID_list)

print("\n")