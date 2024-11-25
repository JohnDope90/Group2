import ifcopenshell
from pathlib import Path
import sys
import threading
import time
sys.dont_write_bytecode = True

# Import rules
from A3 import StairwayRule

print("Loading model")

# Specify the IFC model path
# Group 10
path = r"C:\Users\sofie\OneDrive - Danmarks Tekniske Universitet\DTU kandidat\41934 - Advanced BIM\IFC models\GR2406\CES_BLD_24_06_STR.ifc"

# Group 6
#path = r"C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_06_STR.ifc"

# Check if the file exists
if not Path(path).is_file():
    raise FileNotFoundError(f"No file found at {path}!")


# Call the function
results = StairwayRule.StairwayRule(path)

# Results
total_stairways, stairway_info, ID_list = results

print("\nNumber of full-height stairways found: {total_stairways}")
print(stairway_info)

print(ID_list)