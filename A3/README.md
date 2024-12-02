Link to github folder [main script](https://github.com/JohnDope90/Group2/blob/main/main_A3.py) and [A3 folder](https://github.com/JohnDope90/Group2/tree/main/A3)

## The Tool

The tool works on CC2 high risers with the escape stairs located in one or more cores. The stairs are found based on their placement in relation to other stairs - if they are in around the same x- and y-position, they are grouped together. This makes sure that no irrelevant stairs are checked.


### The Problem

The tool checks if all escape stairs comply with the preaccepted Danish safety standards ([BR18 - §57](https://bygningsreglementet.dk/Tekniske-bestemmelser/02/Krav/57#005499f7-eb23-4ff5-bbaa-16ac6a2bbefe)). If there are many stairs in a project, this can be tedious work - the Fire Stair Checker does it automatically.

This problem was identified based on the lack of overview of which stairs are already checked, the amount of stairs found in a high rise building, and the information that is not given directly by tha IFC file.


### Description

The Fire Stair Checker
1. Takes an IFC model as input
2. Finds all stairs in the model and their Global Ids
3. Locates stairs in cores by their x- and y-locations
4. Relates the coordinates back to each stair's Global Id
5. Creates a list of Global Ids that is used by the following functions:
6. **Thread Depth**
    1. The Id-list is used to find relevant stairs. 
    2. The tool looks at the pset "Thread Depth" and holds it against BR18's rule of 23-25cm. 
    3. A list on non-complying stairs is made.
7. **Riser Height**
    1. The Id-list is used to find relevant stairs. 
    2. The tool looks at the pset "Riser Height" and holds it against BR18's rule of max 18cm.
    3. A list on non-complying stairs is made.

8. **Head Height**
    1. The Id-list is used to find relevant stairs. 
    2. Via vertices and faces, the tool finds all flat upwards facing faces.
    3. It uses a defined geometry tree to only include "IfcBuiltElements" (meaning no railings, furniture, etc.)
    4. A ray with the distance 2.1m is used to find built elements within this range.
    5. A status and list is made with the Global Ids of non-complying stairs.
8. **Stair Width**
    1. The Id-list is used to find relevant stairs.
    2. The tool find verices of the stairs and the max range in which they lie for both the x- and y-direction.
    3. The minimum value is the width of the stair (assuming a stair is longer than it is wide).
    4. Returns if any stair does not comply with the minimum width of 1.0m.


### Instructions
In line 8 of main_A3.py, input own path where *"example.ifc"* is.

The tool does the rest. All outputs are in the terminal.

## Advanced Building Design


### Advanced Building Design Stage

The Fire Stair Checker is useful in the early design stage. The consequence of changes to the stairs can be large, and so it is a good idea to make sure they comply as early as possible.


### User Base

The tool might be used by architects or engineers checking for compliance with the Danish BR18.

### Information Required in the Model

The model should:
1. Have at least 5 building storeys
2. Contain its fire escape stairs in cores with the stairs in each core placed more or less in the same x- and y-position
3. Have fire escape stairs with the psets "Thread Depth" and "Riser Height"

### Problems in the IFC
* The stairs in the model did not contain any specifications that helped identify it as a fire stair.
* No materials were specified in the IFC model.
* The fire stairs were not connected or related to eachother in any way. This made it insanely hard to locate them.
    * If the stairs were related or specified as "Fire Escape Stairs", requirement 2 could have been avoided and the tool could have been more general.