When working with many devices as the same time, data management becomes a challenge. Moreover, the system is used by many different people, all with different needs. The basic data storing method is to save all raw data of each separate device into its own folder. The standard folder hierarchy is as follows:
```
[…]\<username>\<start date>\<device name>_<channel>\<start time>\
``` 

This path is generated at the start of the measurement. Should the measurement take place over multiple days, the start date remains unchanged and all files are still saved in the same folder. The reason to add start time folder is to separate measurements should multiple be performed on the same day.

For a standard stability test, several files for each device will be generated at the start of and during the measurement:

1. [JV](jv-file.md) (one for each JV)
2. [Parameter](parameter-file.md)
3. [Tracking](tracking-file.md)

### File structure

To make data processing easier, all files have the same general structure, independent of the measurement type. Each file starts with a header section containing all measurement settings indicated by the `## Header ##` tag. Settings are further subdivided in categories indicated by the labels in square brackets. 

!!! note
	As the software evolves, settings may be added, modified or deleted. When this happens ensure that any post-processing script can handle this.

The `## Data ##` tag indicates where the actual measurement result begins. Data are always stored in a tab-delimited 2D array of values, always containing a header row. In the case of the JV file, a table with the JV parameters and a table with each raw data point of the JV scan is also stored.

```
## Header ##
[General info]
User	Cicci Research
Device	Sample
Cell area (cm2)	1
Test	Stability (JV)
Date	2024-10-01
Time	12:45:46
Note	SMU 1A

[JV Settings]
Vmin (V)	-0.100
Vmax (V)	1.000
Voltage Step (mV)	20.000
Scan Rate (mV/s)	100.000
Auto-detect Voc	Yes
Scan direction	FW then RV
Voltage Range (V)	10V
Current Range (V)	L
Inverted	No
Auto-range	Off

[Cell Settings]
Tipology	Cell
Cell Area (cm2)	1.00
#Cells	1.00
W cell area (cm2)	1.00
#W cells	1.00

## Data ##
...
```

