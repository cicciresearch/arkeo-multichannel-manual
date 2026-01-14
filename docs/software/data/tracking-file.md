The tracking file contains the temporal voltage and current data of the tracking phase of the measurement. 

The columns are the following:

- Time (Hours)
- Voltage (V)
- Current Density (mA/cm²)
- Power (mW/cm²)

In addition, if an environment is configured (see [environments](../sensors/environments.md)), an additional column is added after the power column for each sensor.

### Example data ###

```
## Header ##
[General info]
User	Cicci Research
Device	8A
Cell area (cm2)	1
Test	Stability (Tracking)
Date	2021-12-10
Time	17:42:47
Note	

[Tracking Settings]
Algorithm	MPPT
dV track (V)	0.02
JV interval (min)	10.00
Test duration (hours)	1000.00
Start-up Time	17:42:47 10/12/2021

[Cell Settings]
Tipology	Cell
Cell Area (cm2)	0.03
#Cells	1.00

## Data ##
Time (Hours)	Voltage (V)	Current Density (mA/cm²)	Power (mW/cm²) Irradiance (mW/cm²)
0.004301	0.955799	20.609551	19.698582   98.354
0.009878	0.956809	20.576135	19.687427   98.245
0.015478	0.956618	20.535365	19.644494   98.458
0.021027	0.956652	20.491804	19.603522   98.118
...
```
