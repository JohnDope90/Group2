# BIManalyst Group2

Architecture specifically evacuation / safety.

The claim we are checking is the number desks on the top floor. In the report it is stated to be 108 desks.

The report is CES_BLD_24_06_ARC and its on page 15.

Our code works with an IFC (Building Information Model) file to find and count desks on "Level 16." It loads the model using IfcStore, searches for the "Level 16" building story, and then counts the furniture items labeled as desks on that floor. It compares the number of desks found to a predefined expected value (108) and prints whether the result matches, or if there are more or fewer desks than expected. If "Level 16" is not found, it prints an error message.
