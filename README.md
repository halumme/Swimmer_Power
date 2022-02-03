# Swimmer_Power
## Testing device for swimmer power output in the pool.

I crafted this device to test my swimming team in the water.
The swimmer is wearing a belt with a bungee cord attached to a fisherman's scale.
The scale reading is used to plot a power graph while the swimmer is swimming with maximum effort
against the rubber cord.
There are two distinct software entities: 
1. Arduino microcontroller sketch reading the strain cell in the scale.
2. Python script on a laptop PC plotting the values as a bar graph.

The testing sequence is as follows:
* The Python script is started and the selections on the screen are done, but Start button is not yet pressed
* Swimmer with the rubber cord is in the water, end of the cord attached to the scale hook.
* Stop button at the scale is pressed to update the temperature compensation factor (*optional*)
* Start button on the screen is tapped to start the plotting (rubber cord still slack)
* Swimmer does his/her workout. When the cord starts to retract, the Stop button at the scale is pressed.
* The graphics are stored and the Python script ends.
* Repeat the above steps for each swimmer in the team.

The looping feature project adds a loop into the Python code so that after one test is finished, the code loops back to the selection of swimmer. 

It is necessary that the previous plotting window remains on the screen until the next selection is done. 
It is possible that there are currently some class instances which should not be redefined in the loop.
