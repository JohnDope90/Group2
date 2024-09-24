# BIManalyst Group2

Architecture specifically evacuation / safety.

The claim we are checking is the number desks on in total. In the report it is stated that there is 1620 desks in total in the building.

The report is CES_BLD_24_06_ARC and the claim is on page 15.

Our code works with an IFC (Building Information Model) file to find and count desks on each storey. It loads the model using IfcStore, finds all storeys and compile them into a list called "storeys". It then uses a for-loop where it for each storey finds all IfcFurniture or IfcFurnishingElement that contain 'desk' and makes a list so that len(desks) = amount of desks on each storey. It also sums up all desks in the model.

The results given by the function are a list of storeys and how many desks are in it, and the total amount of desks in the building.

The main.py document is loading the model, calling the function, printing the list of desks on each storey, and comparing the total amount of desks to the expected amount by printing a line of text.