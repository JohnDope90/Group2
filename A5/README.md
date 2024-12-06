# A5: Reflect

### Your learning experience for the concept you focused on. 

#### Identify your own level at the beginning of this course and where you ended : 

Anders: I started at a basic level (modeller), but I feel like I've learned a lot from the course (might be a self-learner by now). 

Adrian: Started as a Modeller, ended as a self learner, wouldn't call myself BIM Manager just yet :). 

Sofie: Started as modeller, ended as an analyst. 

#### What else do you still need to learn? 

Anders: I could dig deeper into cooding, but i think i got a good start, where i can I could dive deeper into coding, but I feel like I’ve gained a solid foundation to build upon.  

Adrian: I would like to learn more python code to be able to extract and create spaces in the model. 

Sofie: It is difficult to know excactly what there is to learn. I would like to be able to get more real-life cases, and find creative solutions for them, enabling me to self-learn. 

#### How you might use OpenBIM in the future? 

Anders: I might use OpenBIM in the future to extract and analyze data from models, making workflows more efficient and simplifying complex tasks in my projects.  

Adrian: Learning to extract and create areas in a 3D model could be useful for my future work with fire safety, specially evacuation times and routes. 

Sofie: I would like to be able to use it to optimise material usage in construction, LCA, and design for disassembly. 

#### Your process of developing the tutorial 

#### Did the process of the course enable you to answer or define questions that you might need later for thesis? 

Anders: I haven’t decided on my thesis’s focus yet, but I might find OpenBIM useful in the future.  

Adrian: No, as I'm already halfway through my thesis at this point and it would be too late to implement what I've learned into the project. 

Sofie: I do not know the subject of my thesis yet, but if I can incorporate the things I learned in this course I would love to do so! 

#### Would you have preferred to have been given less choice in the use cases? 

Anders: I like the freedom to be honest.  

Adrian: No, I would prefer for it to be 100% free what you do, instead of the "fire come first serve" we got at the beginning while distributing areas of interest. There was alot of chaos. 

Sofie: I like that it was a completely free choice and know that examples can limit people’s own creativity and abilities. Still, it was difficult to know if the scope was realistic, too little or too much. 

#### Was the number of tools for the course ok - should we have more or less? - if so which ones would you leave out? 

Anders: I think there should be more focus on the coding itself, and Blender could perhaps be skipped entirely. Instead, BIMvision could be implemented to simplify things a bit, allowing for greater focus on what truly matters. 

Adrian: I would personally remove blender as an option, due to the file size and complexity of the building it was impossible to code inside blender, BIM-Vision would be preferable option 

instead. 

Sofie: BlenderBIM was very unstable and crashed a lot, and the coding option was also quite bad. BIMvision was nice to see the building in 3D and VisualStudio was nice to code in. 

### (As a group) summary of the feedback you received on your tutorial 

The feedback provided was more of a summary of our presentation, as seen below: 

> Group 2 -> tool: check fire escape stairs and roads   

> * Script to find all stairs -> but just want the fire escape stairs  

> * Problem: stairs do not have properties  

> * Found global coordinates of stairs and they grouped it together  

> * They want to update the model as well since they do not have any properties 

> * Want to make the tool universal  

> * Want to check the width, length... 

> * Ceiling height is not the same as stair heights…  

> * Model: the seats are made of stairs -> problem -> solved because they do not want these kind of stairs  

> * They would have liked more information of the function for ifcimports and how to use them 

#### Did the tool address the use case you identified? 

Group:  

The use case was addressed; however, we did not have time to check everything we wanted to. We did not figure out the effective width (width between railings) and did not set new properties for the stairs complying with all “tests” [Property: “Emergency Staircase”]. We could also have set the results up more visually nice. 

### (Individual) Your future for Advanced use of OpenBIM 

#### Are you likely to use OpenBIM tools in your thesis? 

Anders: It’s possible that I will use OpenBIM tools in my thesis, depending on the focus of my research and whether they can support data analysis, modeling, or collaborative aspects of the project. 

Adrian: No, I’ve already started my thesis so I won’t be implementing it this late into the project. 

Sofie: Yes, I would like to do so. I feel like the possibilities are endless and I want to learn them. 

#### Are you likely to use OpenBIM tools in your professsional life in the next 10 years? 

Anders: Yes, it’s very likely that I will use OpenBIM tools in my professional life over the next 10 years, as they support collaboration, data-driven decision-making, and efficient workflows in building and design projects. 

Adrian: For personal interest perhaps, but I don’t see myself using the tools alone in the company for results as I would fear making mistakes that I cannot see on my own, if no one else is making a quality assurance then it’s just a hobby project. 

Sofie: Yes, if it is a possibility that would be great!

### (Individual) Wrap up 

#### Conclude the journey through A1-A5 

Anders: This course has taught me a lot about BIM. I’ve learned how to analyze models, use OpenBIM tools, and apply them to “real projects”. Sharing ideas with others has helped me understand more, and I now have a solid foundation for future studies and work. I’m confident I’ll use BIM a lot going forward. 

Adrian: At the beginning the opportunities seemed endless. Everything can be done with a little bit of python scripting, right...? Well did I underestimate the amount of missing or misplaced data in the IFC-files! The idea was to create evacuation times based on the model’s geometry, door widths, effective widths in emergency staircases, furthest position inside a space [floor] to the staircase. With our limited knowledge in python coding with IFC-files we had to dump it more down to fire safety regarding the pre-accepted solutions for emergency staircase dimensions. Even then problems appeared specially with checking the height-criteria of 2.1m as each staircase step had to be checked if there’s any element in the structural file blocking the free height. Presenting for the other teams in our area helped out as questions and ideas were exchanged as well as tools (programs) to use. 

Sofie: At the start, it was difficult to know what was possible. It was nice to have the desk counting example in A1 to get started, however the basic principles for the code was not really clear to me at that point. In A2, the BPMN diagram helped us a lot to understand our own thinking and the process we wanted to code. For A3, we got help to really come up with creative and alternative solutions and the possibilities seemed to widen as we learned more about the language of IfcOpenShell. Here, I really learned a lot about what was possible, and I know there are many more things that can be done and ways to do our code more efficient, but it was satisfying to learn!. The tutorial in A4 was a bit difficult to do thoroughly, as we were so much in the code and understood it ourselves. If there had been more time to test it with the other groups, that would have been nice! 