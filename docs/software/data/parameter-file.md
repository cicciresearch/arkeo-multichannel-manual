The parameter file saves all [JV parameters](../measurement/jv-scan.md/#parameters) in a single file. It contains the same data as in each of the JV file, but summarized in a single table. The columns are the following:

- Time (Hours)
- Voc (V) FW
- Jsc (mA/cm2) FW
- V_MPP (V) FW
- J_MPP (mA/cm2) FW
- P_MPP (mW/cm2) FW
- Rs (Ohm) FW
- R// (Ohm) FW
- Fill Factor (%) FW
- Efficiency (%) FW
- Voc (V) RV
- Jsc (mA/cm2) RV
- V_MPP (V) RV
- J_MPP (mA/cm2) RV
- P_MPP (mW/cm2) RV
- Rs (Ohm) RV
- R// (Ohm) RV
- Fill Factor (%) RV
- Efficiency (%) RV

### Example data ###

!!! Warning "Updated header structure"
    This page shows the latest header structure as of software version [v2.4.0](../changelog.md#v240-2026-03-09). Please refer to the [JV File](jv-file.md) page for more information

```
## Header ##
[General info]
User	Cicci Research
Device	Sample
Cell area (cm2)	1
Test	Stability (JV)
Date	2026-02-24
Time	11:49:25
Temperature	355.01
Note	SMU 1A

[Channel Settings]
Voltage Range	10 V
Current Range	18 mA (L)

[Cell Settings]
Inverted	No
Type	Cell
Cell Area (cm2)	1
#Cells	1

[JV Settings]
Vmin (V)	-0.1
Vmax (V)	0.7
Voltage Step (mV)	40
Scan Rate (mV/s)	200
Scan Direction	FW then RV
Auto-detect Voc	Yes
Overvoltage (%)	0

[Environment Settings]
Name	Light Soaker
Humidity	Square4x6:Humidity
Temperature	Square4x6:Temperature
Luminosity	Pyranometer:lum

[Day-Night Settings]
Sensor	lum
Unit	mW/cm²
Threshold Value	5
Threshold Duration	0
Night Algorithm	Fixed Voltage (no track)
Night JV	Disable
Constant Output	0.2

## Data ##
Time (Hours)	Voc (V) FW	Jsc (mA/cm2) FW	V_MPP (V) FW	J_MPP (mA/cm2) FW	P_MPP (mW/cm2) FW	Rs (Ohm) FW	R// (Ohm) FW	Fill Factor (%) FW	Efficiency (%) FW	Voc (V) RV	Jsc (mA/cm2) RV	V_MPP (V) RV	J_MPP (mA/cm2) RV	P_MPP (mW/cm2) RV	Rs (Ohm) RV	R// (Ohm) RV	Fill Factor (%) RV	Efficiency (%) RV
3.710639E-3	4.619658E-1	1.119090E+0	3.651298E-1	9.916345E-1	3.620753E-1	3.450411E+1	2.618983E+4	7.003644E+1	3.620753E-1	4.611090E-1	1.120610E+0	3.604837E-1	9.997452E-1	3.603919E-1	3.357265E+1	2.066390E+4	6.974562E+1	3.603919E-1
1.701685E-1	4.584664E-1	1.077215E+0	3.636256E-1	9.511814E-1	3.458739E-1	3.485409E+1	1.718026E+4	7.003382E+1	3.458739E-1	4.583488E-1	1.075604E+0	3.660001E-1	9.423536E-1	3.449015E-1	3.648911E+1	1.221063E+6	6.995950E+1	3.449015E-1
3.368119E-1	4.583247E-1	1.059331E+0	3.641803E-1	9.323658E-1	3.395493E-1	3.746153E+1	6.202327E+5	6.993555E+1	3.395493E-1	4.589018E-1	1.059199E+0	3.579204E-1	9.418164E-1	3.370953E-1	3.648763E+1	8.734668E+4	6.935142E+1	3.370953E-1
...
```
