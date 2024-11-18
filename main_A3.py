import ifcopenshell
from pathlib import Path
import sys
import threading
import time
sys.dont_write_bytecode = True

# Import rules
from A3 import StairwayRule

# Function to display dots
def show_dots():
    while running:
        print(".", end="", flush=True)  # Print a dot without a newline
        time.sleep(0.5)  # Wait a bit before printing the next dot

print("Loading model")

# Specify the IFC model path
# Group 10
path = r"C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_10_ARC.ifc"

# Group 6
#path = r"C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_06_STR.ifc"

# Check if the file exists
if not Path(path).is_file():
    raise FileNotFoundError(f"No file found at {path}!")

# Start dots while the function runs
running = True
dot_thread = threading.Thread(target=show_dots)
dot_thread.start()

# Call the function
results = StairwayRule.StairwayRule(path)

# Stop dots
running = False
dot_thread.join()  # Wait for the dot thread to finish

# Results
total_stairways, stairway_info = results
print("\nNumber of full-height stairways found: {total_stairways}")
print(stairway_info)
