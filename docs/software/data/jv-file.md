The JV file contains a table with the [JV parameters](../measurement/jv-scan.md/#parameters). Followed by the JV scan itself.

### Example data ###
!!! Warning "Updated header structure"
	As of [v2.3.6](../changelog.md#v236-2026-01-13), the file headers are updated to include all available settings. The legacy version is still available by setting `FileHeaderVersion = 1` in the configuration file.

**Notes**  
`[General Info]:Temperature` is included only if a temperature sensor is configured.  
`[Environment Settings]` shows the fixed `Irradiance (mW/cm²)` value instead if no environment is selected.  
`[Day-Night Settings]` is only included if it is configured.  
`[Environment]` shows the value of the associated sensors during the JV. It is only included if an environment is selected

Below you can find several example header structures based on which settings are configured. The `v1 (legacy)` header is static and doesn't change based on the settings.

=== "Basic"

	```
	## Header ##
	[General info]
	User	Cicci Research
	Device	Sample
	Cell area (cm2)	1
	Test	Stability (JV)
	Date	2026-02-24
	Time	11:49:25
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
	Irradiance (mW/cm²)	100

	## Data ##
	Scan	Voc	Jsc	V_MPP	J_MPP	P_MPP	Rs	R//	FF	Eff
		V	mA/cm²	V	mA/cm²	mW/cm²	Ohm	Ohm	%	%
	FW	-1.230104	-3.021945	-0.655025	-1.666126	1.091354	2.94E+2	5.65E+2	29.36	11.73
	RV	0.761543	1.087563	0.374948	0.521392	0.195495	7.84E+2	6.26E+2	23.60	2.10
										
	V_FW (V)	J_FW (mA/cm²)	V_RV (V)	J_RV (mA/cm²)						
	-3.187902E+0	7.089213E+0	6.761269E+0	-1.309565E+1						
	-6.326601E+0	1.234149E+1	8.817806E+0	-1.625949E+1						
	-8.570556E+0	1.588318E+1	9.645930E+0	-1.715583E+1						
	...
	```

=== "With Environment"

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
	Name	test
	Humidity	Square4x6:Humidity
	Temperature	Square4x6:Temperature
	Luminosity	:lum

	[Environment]
	Irradiance (mW/cm²)	9.30
	Temperature (°C)	355.01
	Humidity (%)	225.08

	## Data ##
	Scan	Voc	Jsc	V_MPP	J_MPP	P_MPP	Rs	R//	FF	Eff
		V	mA/cm²	V	mA/cm²	mW/cm²	Ohm	Ohm	%	%
	FW	-1.230104	-3.021945	-0.655025	-1.666126	1.091354	2.94E+2	5.65E+2	29.36	11.73
	RV	0.761543	1.087563	0.374948	0.521392	0.195495	7.84E+2	6.26E+2	23.60	2.10
										
	V_FW (V)	J_FW (mA/cm²)	V_RV (V)	J_RV (mA/cm²)						
	-3.187902E+0	7.089213E+0	6.761269E+0	-1.309565E+1						
	-6.326601E+0	1.234149E+1	8.817806E+0	-1.625949E+1						
	-8.570556E+0	1.588318E+1	9.645930E+0	-1.715583E+1						
	...
	```

=== "With Day-Night"

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
	Name	test
	Humidity	Square4x6:Humidity
	Temperature	Square4x6:Temperature
	Luminosity	:lum

	[Day-Night Settings]
	Sensor	lum
	Unit	mW/cm²
	Threshold Value	5
	Threshold Duration	0
	Night Algorithm	Fixed Voltage (no track)
	Night JV	Disable
	Constant Output	0.2

	[Environment]
	Irradiance (mW/cm²)	9.30
	Temperature (°C)	355.01
	Humidity (%)	225.08

	## Data ##
	Scan	Voc	Jsc	V_MPP	J_MPP	P_MPP	Rs	R//	FF	Eff
		V	mA/cm²	V	mA/cm²	mW/cm²	Ohm	Ohm	%	%
	FW	-1.230104	-3.021945	-0.655025	-1.666126	1.091354	2.94E+2	5.65E+2	29.36	11.73
	RV	0.761543	1.087563	0.374948	0.521392	0.195495	7.84E+2	6.26E+2	23.60	2.10
										
	V_FW (V)	J_FW (mA/cm²)	V_RV (V)	J_RV (mA/cm²)						
	-3.187902E+0	7.089213E+0	6.761269E+0	-1.309565E+1						
	-6.326601E+0	1.234149E+1	8.817806E+0	-1.625949E+1						
	-8.570556E+0	1.588318E+1	9.645930E+0	-1.715583E+1						
	...
	```

=== "v1 (legacy)"

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