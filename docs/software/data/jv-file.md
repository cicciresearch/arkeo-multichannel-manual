The JV file contains a table with the [JV parameters](../measurement/jv-scan.md/#parameters). Followed by the JV scan itself.

### Example data ###

```
## Header ##
[General info]
User	Cicci Research
Device	Silicon
Cell area (cm2)	1
Test	Stability (JV)
Date	2026-01-13
Time	16:53:26
Note	SMU 1D

[JV Settings]
Vmin (V)	-0.100
Vmax (V)	0.700
Voltage Step (mV)	20.000
Scan Rate (mV/s)	100.000
Auto-detect Voc	Yes
Scan direction	FW then RV
Voltage Range (V)	10 V
Current Range (V)	L
Inverted	No
Auto-range	On

[Cell Settings]
Tipology	Cell
Cell Area (cm2)	1.00
#Cells	1.00
W cell area (cm2)	1.00
#W cells	1.00

## Data ##
Scan	Voc	Jsc	V_MPP	J_MPP	P_MPP	Rs	R//	FF	Eff
	V	mA/cm²	V	mA/cm²	mW/cm²	Ohm	Ohm	%	%
FW	0.458325	1.059331	0.364180	0.932366	0.339549	3.75E+1	6.20E+5	69.94	0.34
RV	0.458902	1.059199	0.357920	0.941816	0.337095	3.65E+1	8.73E+4	69.35	0.34
									
V_FW (V)	J_FW (mA/cm²)	V_RV (V)	J_RV (mA/cm²)						
-1.10653E-1	1.05974E+0	5.20086E-1	-4.66223E+0						
-9.06952E-2	1.06152E+0	5.02734E-1	-2.51252E+0						
-7.07408E-2	1.05924E+0	4.84707E-1	-1.11390E+0						
-5.01796E-2	1.06117E+0	4.67572E-1	-2.65807E-1						
-3.05984E-2	1.06002E+0	4.46978E-1	2.46510E-1						
-1.06036E-2	1.05916E+0	4.27515E-1	5.44715E-1						
1.03375E-2	1.05961E+0	4.07865E-1	7.32007E-1						
2.93350E-2	1.05967E+0	3.87815E-1	8.44080E-1						
4.88898E-2	1.05894E+0	3.67467E-1	9.14722E-1						
6.97690E-2	1.05831E+0	3.49364E-1	9.62141E-1						
...
```