## Settings Overview ##

The measurement settings are organized into **five categories**.  
Each category contains a table for quick lookup, followed by an optional expandable section for deeper explanations.

### General ###

| **Parameter** | **Description**                 | **Example** | **Unit** | **Type** |
| ------------- | ------------------------------- | ----------- | -------- | -------- |
| Enable        | Enables or disables the channel | true        |          | boolean  |
| User          | Name of the user                | User        |          | string   |
| Device        | Device Name                     | Sample      |          | string   |
| Note          | Free to use field for comments  |             |          | string   |
    
### Cell ###

| **Parameter**    | **Description**         | **Example** | **Unit** | **Type** |
| ---------------- | ----------------------- | ----------- | -------- | -------- |
| Type             | Cell Type               | Cell        |          | enum     |
| InvertedStructure | Inverts the applied voltage | false       |          | boolean  |
| Area (cm2)       | Area of the cell        | 1           | cm²      | float    |
| NrCells          | Number of cells         | 1           |          | integer  |

???+ info "Additional notes on Channel settings"
    - **InvertedStructure:** Use this when the device polarity is physically reversed.

### Channel ###

| **Parameter**     | **Description**             | **Example** | **Unit** | **Type** |
| ----------------- | --------------------------- | ----------- | -------- | -------- |
| VoltageLimit      | Maximum Voltage             | 10 V        |          | enum     |
| CurrentLimit      | Current Range               | 0           |          | integer  |

???+ info "Additional notes on Channel settings"
    - **VoltageLimit:** Default is 10 V. Can be extend to 20 V by using 2 SMUs, for more detail see [Source Meter Boards/20 V Extension](../hardware/smu-introduction.md#20-v-extension).
    - **CurrentLimit:** Higher ranges allow larger currents but reduce resolution.  

### JV ###

| **Parameter**   | **Description**                               | **Example**  | **Unit** | **Type** |
| --------------- | --------------------------------------------- | ------------ | -------- | -------- |
| Vmin (V)        | Minimum voltage                               | -0.1         | V        | float    |
| Vmax (V)        | Maximum voltage                               | 2            | V        | float    |
| Step            | Voltage increment per step                    | 20           | mV       | float    |
| ScanRate (mV/s) | Rate at which the voltage is applied          | 100          | mV/s     | float    |
| VocDetect       | Enables the detection of open-circuit voltage | true         |          | boolean  |
| ScanOrder       | Order of scanning                             | _FW then RV_ |          | enum     |

???+ info "Additional notes on JV settings"
    - **Vmin/Vmax:** Ensure that the range fully covers expected operating points.  
    - **ScanRate:** A maximum of 10 points per second can be applied. Ensure that the scan rate is not too high with respect to the step size.
    - **VocDetect:** Automatically detects open-circuit voltage but may stop prematurely if polarity is inverted.  
    - **ScanOrder:** Options are: `FW then RV`, `RV then FW`, `FW only`, `RV only`.
      
### Tracking ###

| **Parameter**      | **Description**                                 | **Example** | **Unit** | **Type** |
| ------------------ | ----------------------------------------------- | ----------- | -------- | -------- |
| TrackEnable        | Enables tracking                                | true        |          | boolean  |
| Algorithm          | Specifies the algorithm used for tracking       | MPPT        |          | enum     |
| ConstantOutput     | Setting to maintain a constant output           | 0.2         | *        | float    |
| SaveInterval (s)   | Time between saved data points                  | 10          | s        | integer  |
| jvInterval.Value   | Time between JV scans                           | 10          |          | float    |
| jvInterval.Unit    | Unit for JV interval                            | min         |          | enum     |
| JV Timing          | Relative to test start or last JV               | Absolute    |          | enum     |
| TestDuration.Value | Duration of the tracking test                   | 100         |          | float    |
| TestDuration.Unit  | Unit for Test Duration                          | hours       |          | enum     |

???+ info "Additional notes on Tracking settings"
    - **TrackEnable:** When disabled, the system performs only a single JV.  
    - **SaveInterval:** Determines how often data is logged; lower values = larger file size.  
    - **jvInterval:** Automatic JV intervals allow stability studies during long tracking tests. 

??? info "Tracking Algorithms"
    - MPPT  
    - Open circuit  
    - Short circuit  
    - Fixed Voltage  
    - Fixed Current  
