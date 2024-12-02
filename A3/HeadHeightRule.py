import multiprocessing
import ifcopenshell
import ifcopenshell.geom
from pathlib import Path
from OCC.Core.gp import gp_Pnt, gp_Dir

# # Path to the IFC model
# model_path = Path(r"C:\Users\sofie\OneDrive - Danmarks Tekniske Universitet\DTU kandidat\41934 - Advanced BIM\IFC models\GR2406\CES_BLD_24_06_STR.ifc")

# # Check if the file exists and load the model
# if not model_path.is_file():
#     raise FileNotFoundError(f"No file found at {model_path}!")

# ifc_model = ifcopenshell.open(model_path)
# if ifc_model:
#     print("IFC model loaded successfully!")
# else:
#     raise Exception("Failed to load IFC model.")


# from A3 import StairwayRule

# # Call the function
# results = StairwayRule.StairwayRule(model_path)

# # Results
# total_stairways, stairway_info, ID_list = results

def HeightRule(ifc_model, ID_list, min_height=2.1):
    
    tree = ifcopenshell.geom.tree()
    settings = ifcopenshell.geom.settings()
    settings.set(settings.USE_WORLD_COORDS, True)
    settings.set(settings.USE_PYTHON_OPENCASCADE, True)
    iterator = ifcopenshell.geom.iterator(settings, ifc_model, multiprocessing.cpu_count(), include=ifc_model.by_type('IfcBuiltElement'))
    if iterator.initialize():
        while True:
            # Use triangulation to build a BVH tree
            # tree.add_element(iterator.get())

            # Alternatively, use this code to build an unbalanced binary tree
            tree.add_element(iterator.get_native())

            if not iterator.next():
                break
    #print("Tree defined.")

    import numpy as np

    def find_normal_vector(A, B, C):
        # Beregn vektorer AB og AC
        AB = np.array(B) - np.array(A)
        AC = np.array(C) - np.array(A)
        
        # Krydsproduktet af AB og AC
        normal_vector = np.cross(AB, AC)
        
        return normal_vector

    def find_centroid(A, B, C):
        # Beregn middelpunktet af de tre hjørner
        centroid = (np.array(A) + np.array(B) + np.array(C)) / 3
        return centroid

    for ID in ID_list:
        # Mesh Faces
        element = ifc_model.by_id(ID)

        settings2 = ifcopenshell.geom.settings()
        settings2.set(settings2.USE_WORLD_COORDS, True)

        shape = ifcopenshell.geom.create_shape(settings2, element)

        grouped_faces = ifcopenshell.util.shape.get_faces(shape.geometry)

        #print(grouped_faces)
        #print("Grouped faces found\n")

        grouped_verts = ifcopenshell.util.shape.get_vertices(shape.geometry)

        #print(grouped_verts)
        #print("Grouped vertices found\n")

        vert_normals = []
        failed_elements = []

        for face in grouped_faces:
            A = grouped_verts[face[0]]
            B = grouped_verts[face[1]]
            C = grouped_verts[face[2]]
            normal = find_normal_vector(A, B, C).tolist()

            if normal[0] == 0 and normal[1] == 0 and normal[2]>0:
                vert_normals.append(normal)
                center = find_centroid(A,B,C)

                origin = (float(center[0]),float(center[1]),float(center[2]))
                direction = (0., 0., 1.)
                # origin = (0.0,0.0,0.0)
                # direction = (1.0,0.0,0.0)
                results = tree.select_ray(origin, direction, min_height)

                #print("Ray sent")

                for result in results:
                    entity = ifc_model.by_id(result.instance.id())
                    if entity.GlobalId != ID and result.distance > 0.181:
                        #print(ifc_model.by_id(result.instance.id())) # The element the ray intersects with
                        #print(list(result.position)) # The XYZ intersection point
                        #print(result.distance) # The distance between the ray origin and the intersection
                        # print(list(result.normal)) # The normal of the face being intersected
                        # print(result.dot_product) # The dot product of the face being intersected with the ray
                        failed_elements.append(ID)
                        print("Stair", ID, "does not comply with the minimum free height of", min_height,"\nHits:", entity, "at", result.distance)

    if len(failed_elements) == 0:
            print("All stairs comply with the minimum required free height of", min_height,"m.")
    
    return failed_elements