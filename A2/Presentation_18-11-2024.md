### What does our tool do?

* Finds **relevant** fire/escape stairs in building.
    * Made specifically for tall buildings with escape route in cores
    * Finds staircases in close proximity
* Finds parameters (riser height, treads depth, stair width)
* Checks against BR18, Chapter 5 "Fire Regulations"
* Gives list of accepted and not accepted stairs
* Adds the pset "Fire Stair" on stairs that pass inspection if it is not there already

### Course wishes

* Better understanding of IFCs from the start
    * How to use them practically in code
    * **A real intro** to [IFCOpenshell Documentation](https://docs.ifcopenshell.org/index.html)
* A "forced" way for groups to talk together about script/coding solutions and ideas
    * Also, brainstorming for ideas for script?


### Presentation Peer Review

#### Group 8 - Optimising Office Area Use

* Seems useful, area optimising is important for large constructions
    * Optimises square meter price per office worker
* A challenge to do the optimisation, BUT
* Also a challenge to find required information (floor area)
    * This shouldn't be the case. Perhaps solveable if there were modelling guidelines in general..

#### Group 9 - Assessing Fire Requirements

* Wants to look at specific building codes and determine if e.g. fire fighter elevators are required
    * Seems fine and useful as a part of a bigger check of an almost designed building
* Was difficult for them to understand building codes from other countries
    * Could have been easily made for "all" countries if everyone had excel/csv data over requirements
* They say they might have underestimated their time/could have done more
    * For the course: It is a bit difficult to know what can be done when you have limited knowledge of both topic and coding

#### Group 4 - LCA/CO2 of all elements
* Gathers all materials and amounts and finds CO2 emissions
* Could be a nice initial LCA in the modelling phase
* Needs better IFC modelling guidelines as not all elements have materials or amount
    * Or else it is a lot of estimating

#### Group 1 - Detecting mislabelled materials
* Aims to reduce the amount of mislabelled elements
* Simplifies the model by cleaning it up AND finds "missing" elements
* A lot of manual work initially - might be less the more it is used
    * i.e. building a library of predefined names/types
