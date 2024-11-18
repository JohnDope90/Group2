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

stairs = model.by_type("IfcStairFlight")

print("All stair flights found.\n")

elements = stairs
settings = ifcopenshell.geom.settings()
settings.set(settings.SITE_LOCAL_PLACEMENT, True)
stair_coords = []

print("... starting to find stair coordinates...\n")

for element in elements:
    shape = ifcopenshell.geom.create_shape(settings, element)
    inner_list = ifcopenshell.util.shape.get_element_bbox_centroid(element, shape.geometry)
    stair_coords.append(inner_list)

print(f"Extracted coordinates for {len(stair_coords)} stair flights.\n")

# --- Improved logic to group stairs into stairways ---

# Function to cluster stairs based on distances
def cluster_stairs(coords, max_horizontal_distance=5000, max_vertical_distance=5000):
    print("Clustering stair flights into stairways...\n")
    # Normalize vertical distance (Z-axis)
    coords = np.array(coords)
    coords[:, 2] /= max_vertical_distance

    # Perform hierarchical clustering
    linkage_matrix = linkage(coords, method="single")
    clusters = fcluster(linkage_matrix, t=max_horizontal_distance, criterion="distance")

    # Group stairs by cluster ID
    grouped_stairs = {}
    for cluster_id, coord in zip(clusters, coords):
        grouped_stairs.setdefault(cluster_id, []).append(coord)

    print(f"Clustered into {len(grouped_stairs)} stairways.\n")
    return list(grouped_stairs.values())

# Group stairs into stairways
stairways = cluster_stairs(stair_coords, max_horizontal_distance=5000, max_vertical_distance=5000)

# --- Improved logic to identify full-height stairways ---
def get_building_height(coords):
    print("Calculating building height range...\n")
    z_values = [coord[2] for coord in coords]
    return min(z_values), max(z_values)

def estimate_floor_height(z_values, tolerance=0.1):
    print("Estimating floor height...\n")
    z_values = sorted(z_values)
    differences = [z_values[i + 1] - z_values[i] for i in range(len(z_values) - 1)]
    floor_heights = [d for d in differences if d > tolerance]
    if floor_heights:
        print(f"Estimated floor height: {np.mean(floor_heights):.2f}\n")
        return np.mean(floor_heights)
    else:
        print("No valid floor height differences found. Using default value (1.0).\n")
        return 1.0

def filter_full_height_stairways(stairways, building_min_z, building_max_z, tolerance=1.0):
    print("Filtering full-height stairways...\n")
    full_height_stairways = []
    all_z_values = [coord[2] for stairway in stairways for coord in stairway]
    estimated_floor_height = estimate_floor_height(all_z_values, tolerance)
    expected_flights = (building_max_z - building_min_z) / estimated_floor_height

    print(f"Expected flights for full height: {expected_flights:.2f}\n")

    for stairway in stairways:
        z_values = sorted([coord[2] for coord in stairway])
        min_z, max_z = z_values[0], z_values[-1]
        height_span = abs(max_z - min_z)
        if height_span >= (building_max_z - building_min_z) * 0.8:
            is_continuous = all(
                z_values[i + 1] - z_values[i] <= estimated_floor_height + tolerance
                for i in range(len(z_values) - 1)
            )
            if is_continuous and len(z_values) >= expected_flights * 0.5:
                full_height_stairways.append(stairway)
    print(f"Identified {len(full_height_stairways)} full-height stairways.\n")
    return full_height_stairways

# Calculate building height
all_coords = [coord for stairway in stairways for coord in stairway]
building_min_z, building_max_z = get_building_height(all_coords)
print(f"Building height range: {building_min_z} to {building_max_z}\n")

# Filter full-height stairways
filtered_stairways = filter_full_height_stairways(stairways, building_min_z, building_max_z)

# Output stairway groups
print(f"Identified {len(filtered_stairways)} valid full-height stairways.\n")
for i, stairway in enumerate(filtered_stairways, start=1):
    print(f"Full-height Stairway {i} ({len(stairway)} flights):")
    for stair in stairway:
        print(f"  - {stair}")
    print()

print("Script finished.\n")
