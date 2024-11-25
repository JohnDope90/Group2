import ifcopenshell
from pathlib import Path
import sys

# Import rules
from A3 import StairwayRule

print("Loading model")

# Specify the IFC model path
# Group 10
# path = r"C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_10_ARC.ifc"

# Group 6
path = r"C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_06_STR.ifc"

# Check if the file exists
if not Path(path).is_file():
    raise FileNotFoundError(f"No file found at {path}!")

# Call the function
try:
    results = StairwayRule.StairwayRule(path)
    total_stairways, stairway_info, ID_list = results

    print(f"\nNumber of full-height stairways found: {total_stairways}")
    print("Stairway information:")
    print(stairway_info)

    # Check if Id_list exists in the result
    if hasattr(stairway_info, "Id_list"):
        print("ID List:")
        print(stairway_info.Id_list)
    else:
        print("No ID list found in the stairway information.")
except Exception as e:
    print(f"An error occurred: {e}")