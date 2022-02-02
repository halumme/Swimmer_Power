# Swimmer_Power
Testing device for swimmer power output in the pool.<br>
I crafted this device to test my swimming team in the water.
The swimmer is wearing a belt with a bungee cord attached to a fisherman's scale.
The scale reading is used to plot a power graph while the swimmer is swimming with maximum effort
against the rubber cord.
There are two distinct software entities: 
1. Arduino microcontroller sketch reading the strain cell in the scale.
2. Python script on a laptop PC plotting the values as a bar graph.

In this feature branch I will implement individual power levels for the plots by the Python script.
The desktop file of swimmer data will be modified to a csv text file, where there is maximum power level for the swimmer after his/her name. 
This way the plotting area y-axis will be optimized for each swimmer individually.<br> 
No code editing by the user should be needed anymore.
<br><img src="power_plot1.png">
