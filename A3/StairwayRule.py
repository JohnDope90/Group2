import ifcopenshell
import ifcopenshell.util.shape
import ifcopenshell.geom
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import fcluster, linkage

def StairwayRule(model):
    # Find all stair flights
    stairs = model.by_type("IfcStairFlight")
    settings = ifcopenshell.geom.settings()
    settings.set(settings.SITE_LOCAL_PLACEMENT, True)
    stair_coords = []

    for element in stairs:
        shape = ifcopenshell.geom.create_shape(settings, element)
        inner_list = ifcopenshell.util.shape.get_element_bbox_centroid(element, shape.geometry)
        stair_coords.append(inner_list)

    # Cluster stairs into stairways
    def cluster_stairs(coords, max_horizontal_distance=5000, max_vertical_distance=5000):
        coords = np.array(coords)
        coords[:, 2] /= max_vertical_distance
        linkage_matrix = linkage(coords, method="single")
        clusters = fcluster(linkage_matrix, t=max_horizontal_distance, criterion="distance")
        grouped_stairs = {}
        for cluster_id, coord in zip(clusters, coords):
            grouped_stairs.setdefault(cluster_id, []).append(coord)
        return list(grouped_stairs.values())

    stairways = cluster_stairs(stair_coords)

    # Calculate building height
    def get_building_height(coords):
        z_values = [coord[2] for coord in coords]
        return min(z_values), max(z_values)

    # Estimate floor height
    def estimate_floor_height(z_values, tolerance=0.1):
        z_values = sorted(z_values)
        differences = [z_values[i + 1] - z_values[i] for i in range(len(z_values) - 1)]
        floor_heights = [d for d in differences if d > tolerance]
        return np.mean(floor_heights) if floor_heights else 1.0

    # Filter full-height stairways
    def filter_full_height_stairways(stairways, building_min_z, building_max_z, tolerance=1.0):
        full_height_stairways = []
        all_z_values = [coord[2] for stairway in stairways for coord in stairway]
        estimated_floor_height = estimate_floor_height(all_z_values, tolerance)
        expected_flights = (building_max_z - building_min_z) / estimated_floor_height
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
        return full_height_stairways

    all_coords = [coord for stairway in stairways for coord in stairway]
    building_min_z, building_max_z = get_building_height(all_coords)
    filtered_stairways = filter_full_height_stairways(stairways, building_min_z, building_max_z)

    # Prepare results
    total_stairways = len(filtered_stairways)
    stairway_info = f"A total of {total_stairways} full-height stairways were identified:\n"
    for i, stairway in enumerate(filtered_stairways, start=1):
        stairway_info += f"- Stairway {i} ({len(stairway)} flights)\n"







## Dataframe (table) so we can correlate coordinates and ID for the relevant stairs ##
    # Dataframe contains all stairs in model
    df = pd.DataFrame(stair_coords, columns = ["x", "y", "z"])
    # Taking IDs for all stairs and adding the column to the coordinate table
    IDs = []
    for stair in stairs:
        IDs.append(stair.GlobalId)

    # Adding "IDs" column to df (dataframe)
    df['Global_ID'] = IDs

    ## Taking relevant stairs' coordinates and finding their corresponding IDs ##

    row_num = ()

    for rel_stairs in filtered_stairways:
        for stair in rel_stairs:
            in_array = df[(df["x"] == stair[0]) & (df["y"] == stair[1])].index.to_numpy()
            row_num = np.append(row_num, in_array)

    row_num = np.unique(row_num).astype(int)
   
    ID_list=[]
    for number in row_num:
        inlist = df.iloc[number,3]
        ID_list.append(inlist)

    return [total_stairways, stairway_info, ID_list]