The settings consist of 5 categories. Below you can find a table detailing every available setting
### General ###

| **Parameter** | **Description**                 | **Example** | **Unit** | **Type** |
| ------------- | ------------------------------- | ----------- | -------- | -------- |
| Index         | Unique channel identifier       | 0           |          | integer  |
| Enable        | Enables or disables the channel | true        |          | boolean  |
| User          | Name of the user                | User        |          | string   |
| Device        | Device Name                     | Sample      |          | string   |
| Note          | Free to use field for comments  |             |          | string   |
### Channel ###

| **Parameter**     | **Description**             | **Example** | **Unit** | **Type** |
| ----------------- | --------------------------- | ----------- | -------- | -------- |
| VoltageLimit      | Maximum Voltage             | 10 V        |          | enum     |
| CurrentLimit      | Current Range               | 0           |          | integer  |
| InvertedStructure | Inverts the applied voltage | false       |          | boolean  |
### JV ###

| **Parameter**   | **Description**                               | **Example**  | **Unit** | **Type** |
| --------------- | --------------------------------------------- | ------------ | -------- | -------- |
| Vmin (V)        | Minimum voltage                               | -0.1         | V        | float    |
| Vmax (V)        | Maximum voltage                               | 2            | V        | float    |
| Step            | Voltage increment per step                    | 20           | mV       | integer  |
| ScanRate (mV/s) | Rate at which the voltage is applied          | 100          | mV/s     | float    |
| VocDetect       | Enables the detection of open-circuit voltage | true         |          | boolean  |
| ScanOrder       | Order of scanning                             | _FW then RV_ |          | enum     |
### Tracking ###

| **Parameter**      | **Description**                                 | **Example** | **Unit** | **Type** |
| ------------------ | ----------------------------------------------- | ----------- | -------- | -------- |
| TrackEnable        | Enables tracking                                | true        |          | boolean  |
| Algorithm          | Specifies the algorithm used for tracking       | MPPT        |          | enum     |
| Perturbation (V)   | Voltage differential for the tracking algorithm | 0.01        | V        | float    |
| ConstantOutput     | Setting to maintain a constant output           | 0.2         | *        | float    |
| SaveInterval (s)   | Time between saved data points                  | 10          | s        | integer  |
| jvInterval.Value   | Time between JV scans                           | 10          |          | float    |
| jvInterval.Unit    | Unit for JV interval                            | min         |          | enum     |
| TestDuration.Value | Duration of the tracking test                   | 100         |          | float    |
| TestDuration.Unit  | Unit for Test Duration                          | hours       |          | enum     |

### Cell ###

| **Parameter**    | **Description**         | **Example** | **Unit** | **Type** |
| ---------------- | ----------------------- | ----------- | -------- | -------- |
| Type5            | Cell Type               | Cell        |          | enum     |
| Area (cm2)       | Area of the cell        | 1           | cm²      | float    |
| NrCells          | Number of cells         | 1           |          | integer  |
| NrW cells        | Number of W cells       | 1           |          | integer  |
| W-cellArea (cm2) | The area of each W cell | 1           | cm²      | float    |
