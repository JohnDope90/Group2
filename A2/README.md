## Group 02, Assignment 2

## 2A:

> **I am confident coding in Python:**  
Group result: 1

We, as analysts, are focusing on the compliance of the stairs with fire safety regulations, particularly ensuring they meet the preaccepted solutions for escape routes in the building

## 2B:

We have chosen to work with the report and building from **#2410**. We want to check that the stairs placed in the cores comply with the preaccepted solutions for fire safety regulations, as these are used as escape routes in the building. The claim is found on page 18 in the report.

The claims we want to check are:

* **Free Stair Width**: The free width of the staircase must be at least 1.0 m. This ensures that the staircase is wide enough to allow for safe passage.

* **Tread Depth**: The depth of the tread (the part of the stair where you step) must be at least 23-25 cm. This dimension is critical for ensuring that the stair is comfortable and safe to walk on. A tread depth within this range provides sufficient surface area for a secure footing.

* **Riser Height**: The height of the riser (the vertical part between each tread) should not exceed 18 cm. This ensures that the steps are not too steep, making the staircase easier to climb and reducing the risk of tripping.

* **Ceiling Height**: There must be a minimum clearance of 210 cm from the tread to the ceiling above. This ensures that there is enough headroom for people using the stairs.

These claims need to be verified to ensure the staircase meets safety standards ([BR18 - §57](https://bygningsreglementet.dk/Tekniske-bestemmelser/02/Krav/57#005499f7-eb23-4ff5-bbaa-16ac6a2bbefe)).


## 2C:

* **How you would check this claim?**  
    * By checking the IFC model according to the regulations.

* **When would this claim need to be checked?**  
    * All projects.

* **What information does this claim rely on?**  
    * Building regulations and model data.

* **What phase? planning, design, build or operation.**  
    * Early design phase.

* **What BIM purpose is required? Gather, generate, analyse, communicate or realise?**  
    * We gather information and compare it to stakeholder requirements.

* **Review use case examples - do any of these help?, What BIM use case is this closest to? If you cannot find one from the examples, you can make a new one.**

    ### Potential Use Cases  
    * [4. Programming](https://timmcginley.github.io/41934/Uses/Cases/12.html)  
        ##### Description:
        A process in which a spatial program is used to efficiently and accurately **assess design performance in regard to spatial requirements**. The developed BIM model allows the project team to analyze space and understand the complexity of **space standards and regulations**. Critical decisions are made in this phase of design and bring the most value to the project when needs and options are discussed with the client and the best approach is analyzed.

    * [12. Code Validation](https://timmcginley.github.io/41934/Uses/Cases/12.html)  
        ##### Description:
        A process in which code validation software is utilized to **check the model parameters against project specific codes**. Code validation is currently in its infant stage of development within the U.S. and is not in widespread use. However, as model checking tools continue to develop, code compliance software with more codes, code validation should become more prevalent within the design industry.


* **Produce a BPMN drawing for your chosen use case. link to this so we can see it in your markdown file. To do this you will have to save it as an SVG, please also save the BPMN with it.mYou can use this online tool to create a BPMN file.**  
    * BPMN Diagram is [here](https://github.com/JohnDope90/Group2/blob/main/A2/BPMN_Stair-Fire-Safety.bpmn).

![BPMN Diagram](https://raw.githubusercontent.com/JohnDope90/Group2/7bf15f2b519f4007e4e0160939d07b90cf9b5e9e/A2/BPMN_Stair-Fire-Safety.svg)

## 2D:
*  **Identify where a new script / function / tool is needed.**  
The areas in blue are where our tool is used.

![Marked BPMN Diagram](https://raw.githubusercontent.com/JohnDope90/Group2/58b8a92c01c045b9e671328e037ef334a3344932/A2/Marked-BPMN_Stair-Fire-Safety.svg)

## 2E:
* **Describe in words your idea for your own OpenBIM ifcOpenShell Tool in Python.**
    * The tool should check if there is stairs in the building, and if the dimensions and design of these stairs comply with current fire regulations.

* **What is the business and societal value of your tool?**  
    * It is a quick way to check if the stairs comply with regulations. If they are, they can potentially save lives.  
    If the stairs do not comply, and it is discovered too late, the mistake will be very expensive to correct.

* **Produce a BPMN diagram to summarise your idea.**
    * The diagram of the code idea is [here](https://github.com/JohnDope90/Group2/blob/main/A2/BPMN_Script-Idea.bpmn).

![Script BPMN Diagram](https://raw.githubusercontent.com/JohnDope90/Group2/58b8a92c01c045b9e671328e037ef334a3344932/A2/BPMN_Script-Idea.svg)

## 2F:

* **Identify what information you need to extract from the model.**  
    Properties within IFCstairs and
    dimensions between stair elements.
    
    * **Where is this in IFC?**  
    Architecture model.

    * **Is it in the model?**  
    Yes, the core stairs are modelled in the IFC from #2410.

    * **Do you know how to get it in ifcOpenShell?**  
    Not yet. We need to become better at this.

    * **What will you need to learn to do this?**  
    Learn how to get relevant information out of ifcOpenShell. Naming of elements, properties, etc.

## 2G:
* **What software licence will you choose for your project?**  
    * Visual Studio Code