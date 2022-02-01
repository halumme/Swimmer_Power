# Swimmer_Power
Testing device for swimmer power output in the pool.<br>
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
* Stop button at the scale is pressed to update the temperature compensation factor (<i>optional</i>)
* Start button on the screen is tapped to start the plotting (rubber cord still slack)
* Swimmer does his/her workout. When the cord starts to retract, the Stop button at the scale is pressed.
* The graphics are stored and the Python script ends.
* Repeat the above steps for each swimmer in the team.

Arduino uses the HX711 cell bridge ADC module to read the strain cell values on channel A and
the cell temperature using an NTC thermistor on channel B.
I enclose technical information of the scale electronics on a separate pdf file in this folder.

This was my first ever Python script (apart of some testing scripts) and it shows in the code structure.
You are welcome to improve the code to any conceivable direction. 
You notice that I have not used the most obvious libraries for this kind of script. 
Frankly, I cannot remember my reasoning in 2019 when I started the project.
