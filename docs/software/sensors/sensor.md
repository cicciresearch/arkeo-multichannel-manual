The Arkeo Multichannel software can manage analog and digital sensor as part of the measurements. This allows you to include the environment of the device into the data files. This can be especially important for the irradiance and temperature of the device, which greatly affect its performance.

![sensor-manager](../../assets/img/sensor-manager.png){ .on-glb }
Sensors are managed in the "Sensor Manager" window. It is accessed from the main windows with the "Sensors" button. Here you will see a list of all sensors currently configured for the system. To associate them to your device, see [environments](environments.md).

All sensors save their data at regular intervals to a dedicated save file. See [Data File](data-file.md).

### Managing sensors ###

Sensors from sample holder (managed by the [sample holder tool](../sample-holder-tool.md)) are added automatically as they are added by the sample holder tool. To add a custom analog sensor, click on the + button and follow the instruction of the wizard.  

Generic sensors are available for the following parameters.

* Temperature
* Humidity
* Irradiance
* Oxygen
* CO2

These sensors can be configured with a gain and offset according the following formula.
$$
\text{value} = V_{in} \cdot \text{gain} + \text{offset}
$$
Sensors with custom conversion functions can be requested.

### Sensor Board Pinout ###

!!! danger "HIGH CURRENT"
    The +15V and +5V outputs can deliver high currents. Ensure a proper connection before turning on the system.

The channel is linked to the sensor board adapters present on the system. To choose the channel, please follow the pinout as shown below.

![db37-signal-out-pinout](../../assets/img/db37-signal-out-pinout.png){ .on-glb }
