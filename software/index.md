## The Arkeo Multichannel Software

![[main-software1.png]]
![[main-software2.png]]
![[main-software3.png]]
The main window is shown above. It shows a summary table of all channels with the status of each device. Under it, graphs showing the active measurements are shown. They can be switched between voltage-current, voltage-power, tracking over time, and JV parameters over time. 4 channels are always shown to reflect the 4 channels per SMU. All graphs are updated in real-time as the measurement is running.

The Arkeo Multichannel software is designed to be used by multiple users in parallel. While a measurement of another user is running, another user can log in to their appropriate account, setup their own device settings and add them to the ongoing measurement without disturbing the already ongoing measurements. The software manages each channel independently and in parallel. Each user has their own separate folder where their corresponding measurements are stored (see chapter: Data management).

## Measurement process

The Arkeo Multichannel system is designed to perform parallelized JV and maximum power point tracking measurement. At the start of each measurement, a JV is always performed to get an estimate for the MPP. Once completed (if tracking is enabled), the voltage slowly (at the scan rate of the JV) moves to the MPP where it will perform any of the selected algorithms to keep the device at the desired point. This point can be any of the following:
- Maximum power point
- Open-circuit voltage (by setting the channel in high impedance)
- Short-circuit current
- A fixed voltage
- A fixed current

![[mppt-flowchart.png]]

Since the boards are potentiostatic and lack a galvanostatic mode, all the above algorithms (except the open-circuit voltage, which simply sets the board in a high impedance state) use the PAO algorithm to keep the device at the desired set point. In the case of a fixed voltage, because there is no closed feedback loop, a small voltage drop due to the current flow, may introduce an offset between the set voltage and measurement voltage. This can be compensated by tracking the setpoint. 

During the JV scan, this may pose to be a problem as the voltage set is not the same as the actual voltage drop over the device. By default, JV scans start at a set voltage of -0.2 V instead of 0 V to make sure the JV scan crosses the current axis. Another solution is starting the scan in reverse. At Voc the current is zero and therefore no voltage difference occurs. The voltage scan can then continue until the current axis is crossed.

For all points, at fixed intervals, a new JV is performed by default. This has 2 purposes. The first is to obtain JV parameters such as efficiency, fill factor, Voc and Jsc over time. These parameters give additional information about the degradation of devices compared to just measuring the MPP. The second is to ensure that the MPP is tracking the global maximum, and not a local maximum that may have formed over time.