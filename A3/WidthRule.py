import ifcopenshell
import ifcopenshell.geom
import numpy as np

def WidthRule(ifc_model, ID_list, min_width=1000.):
    """
    Calculates the widths of all stairs (IfcStairFlight) in the model.
    """
    settings = ifcopenshell.geom.settings()
    settings.set(settings.USE_WORLD_COORDS, True)

    stair_widths = []  # List to store stair IDs and their widths
    stairs = []
    for ID in ID_list:
        stairs.append(ifc_model.by_id(ID))

    non_compliant_stairs = []

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

            stair_widths.append([stair.GlobalId, width])
        except Exception as e:
            print(f"Error calculating width for stair {stair.GlobalId}: {e}")

        for stair_width in stair_widths:
            if stair_width is not None and stair_width[1] < min_width:
                non_compliant_stairs.append((stair.GlobalId, round(stair_width, 1)))

    return non_compliant_stairs
