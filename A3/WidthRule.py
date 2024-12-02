import ifcopenshell
import ifcopenshell.geom
import numpy as np

def WidthRule(model_path):
    """
    Calculates the widths of all stairs (IfcStairFlight) in the model.
    """
    # Open the IFC model
    model = ifcopenshell.open(model_path)
    settings = ifcopenshell.geom.settings()
    settings.set(settings.USE_WORLD_COORDS, True)

    stair_widths = []  # List to store stair IDs and their widths
    stairs = model.by_type("IfcStairFlight")  # Retrieve all stairs in the model

    for stair in stairs:
        try:
            # Generate the geometry of the stair
            shape = ifcopenshell.geom.create_shape(settings, stair)
            vertices = np.array(shape.geometry.verts).reshape(-1, 3)

            # Calculate the range in x and y dimensions
            x_range = np.ptp(vertices[:, 0])
            y_range = np.ptp(vertices[:, 1])

            # The stair width is the smaller of x_range and y_range, converted to mm
            width = min(x_range, y_range) * 1000
            stair_widths.append((stair.GlobalId, round(width, 1)))
        except Exception as e:
            print(f"Error calculating width for stair {stair.GlobalId}: {e}")

    # Prepare results
    total_stairs = len(stair_widths)
    width_info = f"Calculated widths for {total_stairs} stairs:\n"
    for stair_id, width in stair_widths:
        width_info += f"- Stair ID {stair_id}: {width} mm wide\n"

    return total_stairs, width_info, stair_widths
