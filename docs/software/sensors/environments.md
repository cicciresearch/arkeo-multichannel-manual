Associating sensors to your devices is done through the use of environments. Individual sensors can be associated to one or more environments. Each device can then be associated to its specific environment. All sensor data of the device's environment is saved into its data files.
The section below describes how to create, modify and delete environments and how to link them to your devices.

### Creating an environment ###

To create a new environment and add sensors to it follow these steps

1. Open the sensor manager from the main window.
2. Click the "Add environment"  button and give it a name.
3. Select the sensor you wish to add to the environment from the sensor list.
4. Drag it to the name of the newly created environment.
5. Repeat steps 3 and 4 for each sensor of the environment.
### Linking a device to an environment ###

To associate a device to an environment, open the settings window and select the device's channel. From the "Environment" drop-down select the environment you just created. This list is dynamically update and you create and delete environment from the sensor manager window.

Once an environment is selected, start a measurement and note the addition sensor data appear in the data files. 

The JV files will contain an addition header section with all sensor data at the time of the JV scan. The tracking files will have an additional column for each sensor.