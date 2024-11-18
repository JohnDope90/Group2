import ifcopenshell
from pathlib import Path
import ifcopenshell.util
import ifcopenshell.util.shape
import ifcopenshell.geom
import numpy as np
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial import distance

print("All imported.\n")

# Load IFC model

# Group 10
path = r"C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_10_ARC.ifc"

# Group 6
#path = r"C:/Users/de_Vo/OneDrive - Danmarks Tekniske Universitet/Dokumenter/Kandidat/41934 - Advanced Building Information Modeling/A2/CES_BLD_24_06_STR.ifc"

corrected_path = path.replace("\\", "/")

model_path = Path(corrected_path)
if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

model = ifcopenshell.open(model_path)

print("Model loaded.\n")

 # Step 1: Extract stair coordinates
    stair_coords = get_stair_coordinates(model)

    # Step 2: Cluster stairs into stairways
    stairways = cluster_stairs(stair_coords)

    # Step 3: Calculate building height
    all_coords = [coord for stairway in stairways for coord in stairway]
    building_min_z, building_max_z = get_building_height(all_coords)
    print(f"Building height range: {building_min_z} to {building_max_z}\n")

    # Step 4: Filter full-height stairways
    filtered_stairways = filter_full_height_stairways(stairways, building_min_z, building_max_z)

    # Step 5: Output results
    print(f"Identified {len(filtered_stairways)} valid full-height stairways.\n")
    for i, stairway in enumerate(filtered_stairways, start=1):
        print(f"Full-height Stairway {i} ({len(stairway)} flights):")
        for stair in stairway:
            print(f"  - {stair}")
        print()

    print("Script finished.\n")

