## Starting a measurement
Before starting any measurement, ensure that your device are properly connected (see [connecting device]). Then follow these steps to setup the software.
![[main-settings.png]]
1. In the Main Window, click ⚙ Settings to open the channel configuration window. If you use a sample holder, open the “Holder UI” instead. The following steps are the same for both options.
2. Select the channel where your device is connected to.
3. On first launch, the default settings are set for an MPPT measurement on a photovoltaic device with a Voc <1.2 V at 100 mW/cm² irradiance. If these settings are not ok for your device, ensure the JV settings are appropriately set before proceeding (see [[settings]] for more details).
4. Next, set the device name, area and type (the user will be set automatically).
5. If tracking is not required (i.e. just a single JV), disable it now.
6. Enable the channel by pressing the green rectangle.
7. Repeat steps 2-5 for each channel where you have a device connected.
8. Press Apply

**Tips**
If multiple channels need to be configured in the same way, consider saving the configuration to a file with the “Save Channel” option. The file can then be loaded and applied to multiple channels.

Tip
The live voltage can be used to check if a Voc is present, i.e. if the device is well connected

**Starting a measurement**
![[summary-table-ready-to-start.png]]
1. After applying the settings to the selected, you should see them appear in the table on the main window in the “Ready to Start” state. They also appear above the corresponding graphs.
2. Press “Start” on the top-left to start the measurement.
3. A JV will be performed on all channels. Confirm that a graph appears on the corresponding channel. Then, if Tracking was enabled, the channels will go the to corresponding Tracking state.
4. Use the “Plot Selection” options to visualize the data.
5. Right-click on any channel in the table to open the data files for further processing

**Troubleshooting**

**Problem**: Only noise is shown in the graph  
**Cause 1:** Poor connection of the device.  
**Solution**: The system tries to apply a voltage, but no current response is measured. Double-check the device connection  
**Cause 2:** Incorrect channel selected. The system tried to measure a channel different from the actual channel where the device is connected to.  
**Solution**: Double-check the channel of the device

**Problem**: A single dot appears and the JV stops  
**Cause**: Auto-detect Voc stops the scan when the current is negative. If the device polarity is inverted, the first point will be negative and the scan stops immediately  
**Solution**: Retry the scan with “Auto-detect Voc” disabled. Or select the “Inverted” flag.

**Problem**: Current saturates  
**Cause**: The SMU have a physical limit on the current they can source/sink. If this is exceeded, the scan fails  
**Solution**: Set the board to a higher current limit

**Problem**: Efficiency is unrealistic  
**Cause**: Wrong irradiance used for efficiency calculation  
**Solution 1** (if irradiance sensor is present): Ensure the correct sensor is used and is placed correctly.  
**Solution 2** (if no sensor is present): Measure the irradiance and set the correct value manually in the settings