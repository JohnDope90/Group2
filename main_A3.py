import ifcopenshell
from pathlib import Path
from A3 import StairwayRule, WidthRule

print("Loading model")

# Specify the IFC model path
path = r"C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_06_STR.ifc"

# Check if the file exists
if not Path(path).is_file():
    raise FileNotFoundError(f"No file found at {path}!")

# Call StairwayRule
stairway_results = StairwayRule.StairwayRule(path)
total_stairways, stairway_info, ID_list = stairway_results

print(f"\nNumber of full-height stairways found: {total_stairways}")
print("Stairway information:")
print(stairway_info)

# Call WidthRule to calculate widths for all stairs
total_stairs, width_info, all_stair_widths = WidthRule.WidthRule(path)

# Filter widths to only include IDs from StairwayRule
filtered_widths = [(stair_id, width) for stair_id, width in all_stair_widths if stair_id in ID_list]

# Print filtered results
print(f"\nNumber of stair widths calculated: {len(filtered_widths)}")
print("Width information for full-height stairways:")
for stair_id, width in filtered_widths:
    print(f"- Trappe ID {stair_id}: {width} mm bred")