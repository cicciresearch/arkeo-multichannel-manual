If a light sensitive sensor is available, it can be used to tell the system about the intensity of the incident light. It can then place the devices in different states during "day"-time or "night"-time.

![day-night](../assets/img/day-night.png)

To setup the day-night cycling, go to the Day-Night tab in the [settings](settings.md) window. Select a sensor from the drop down menu. Confirm that the value of the sensor is updated correctly. Select the day-night threshold value. An optional delay can be configured. This is generally recommended to avoid a single spike causing a false transition. The sensor has to be below/above the threshold for the entire delay time in order to switch state. By default, the system places the devices in Voc during night. This can be configured as needed.
!!! note
	Only irradiance sensors are listed. Ensure that at least 1 sensor is configured from the [senor manager](sensors/sensor.md). If not, the day-night cycling will be unavailable

The Day-Night tab configures the system-wide settings for the day-night cycling. Each channel must also be setup in the [settings](settings.md) to enable to the day-night cycling. This can be done with "Use Global" option or be configured with channel specific settings using the "Configure button."