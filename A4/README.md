Link to github folder [main script](https://github.com/JohnDope90/Group2/blob/main/main_A3.py) and [A4 folder](https://github.com/JohnDope90/Group2/tree/main/A4)

## IFC Model Analysis for Staircase Fire Safety Compliance

### Summary:
This Python script processes IFC models of high-rise buildings to assess
the fire safety compliance of emergency staircases against BR18 regulations.
It verifies staircase dimensions, including tread depth, riser height,
free height, and width, ensuring adherence to safety standards.
The script also identifies emergency staircases by clustering stair-elements 
within a 5 m proximity in the xy-plane and stacked along the z-axis.

### Tutorial
1. Download an IFC model to a desired path
2. In line 8 of *main_A3.py*, input the path where *"example.ifc"* is
3. Run the main_A3.py script
4. All outputs are in the terminal.
    1. If some or all stairs do not comply, for each stair the tool will write the Global Id of the problematic stair(s) and the problem
        * The stair can then be checked manually in the IFC model and the model reloaded
    2. If all stairs comply (no problems), there will be a short message confirming this.