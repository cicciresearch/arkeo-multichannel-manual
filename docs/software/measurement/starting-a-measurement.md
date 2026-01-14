## Starting a measurement ##
Before starting any measurement, ensure that your device are properly connected (see connecting device). Then follow these steps to setup the software.
![settings](../../assets/img/main-settings.png)

1. In the Main Window, click ⚙ Settings to open the channel configuration window. If you use a sample holder, open the "Holder UI" instead. The following steps are the same for both options. 
2. Select the channel where your device is connected to. 
3. On first launch, the default settings are set for an MPPT measurement on a photovoltaic device with a Voc <1.2 V at 100 mW/cm² irradiance. If these settings are not ok for your device, ensure the JV settings are appropriately set before proceeding (see [[settings]] for more details). 
4. Next, set the device name, area and type (the user will be set automatically). 
5. If tracking is not required (i.e. just a single JV), disable it now. 
6. Enable the channel by pressing the green rectangle. 
7. Repeat steps 2-5 for each channel where you have a device connected. 
8. Press Apply. 

!!! Tip
    If multiple channels need to be configured in the same way, consider saving the configuration to a file with the "Save Channel" option. The file can then be loaded and applied to multiple channels.

!!! Tip
    The live channel voltage can be used to check if a Voc is present, i.e. if the device is well connected

### Starting a measurement ###
![summary-table-ready-to-start](../../assets/img/summary-table-ready-to-start.png)

1. After applying the settings to the selected, you should see them appear in the table on the main window in the "Ready to Start" state. They also appear above the corresponding graphs.
2. Press "Start" on the top-left to start the measurement.
3. A JV will be performed on all channels. Confirm that a graph appears on the corresponding channel. Then, if Tracking was enabled, the channels will go the to corresponding Tracking state.
4. Use the "Plot Selection" options to visualize the data.
5. Right-click on any channel in the table to open the data files for further processing

### Troubleshooting ###

Below are common issues that may occur during a measurement, along with their causes and solutions.

---

???+ failure "Only noise is shown in the graph"
    **Cause 1:** Poor connection of the device.  
    **Solution:** The system attempts to apply a voltage, but no current is detected. Double-check the device connection.

    **Cause 2:** Incorrect channel selected.  
    **Solution:** Verify that the selected channel matches the actual connection.

???+ failure "A single dot appears and the JV stops immediately"
    **Cause:** Auto-detect Voc stops the scan when the measured current is negative.  
    If the device polarity is inverted, the *first* point will be negative, causing an immediate stop.

    **Solution:**  
    - Disable **Auto-detect Voc**, or  
    - Enable the **Inverted** polarity flag.

???+ failure "Current saturates"
    **Cause:** The SMU has reached its physical current limit.

    **Solution:** Increase the current limit for the board.

???+ failure "Efficiency is unrealistic"
    **Cause:** Wrong irradiance value used for efficiency computation.

    **Solution 1 (if irradiance sensor is present):**  
    Ensure the correct sensor is selected and properly placed.

    **Solution 2 (if no sensor is present):**  
    Measure irradiance manually and set the correct value in the settings.
