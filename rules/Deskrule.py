import ifcopenshell

def checkRule(model):
    desk_total = 0
    desk_in_stories = str()
    storeys = model.by_type('IfcBuildingStorey')

    #no_of_storeys = len(storeys)
    
    for storey in storeys:
        #print("Storey name:", storey.Name)
        # ^^ Toggle to print every storey name.

        # vv We define desks as an empty list for each floor.
        desks = []

        # vv The for-loop below is contained in the storey for-loop
        for rel in storey.ContainsElements:
            for elem in rel.RelatedElements:
            # vv Below checks if element is a desk
                if (elem.is_a("IfcFurniture") or elem.is_a("IfcFurnishingElement")) and 'desk' in elem.Name.lower():
                    desks.append(elem)
                    #every time elem is a desk, it appends to the desks-list
    
        # then we print all desks in the storey
        desk_in_stories += f"Number of desks in {storey.Name}: {len(desks)}\n"

        desk_total = desk_total + len(desks)
    # Toggle to print the desk name on each floor.    
    #    for desk in desks:
    #        print("Desk name:", desk.Name)

    result = [desk_total, desk_in_stories]
    return result