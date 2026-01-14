Every measurement start with a JV scan to obtain the device's key parameters such as Voc[^1], Jsc[^2] and MPP[^3]. If tracking is enabled, a JV scan is repeated a fixed intervals to obtain these parameters over time.

![jv-scan](../../assets/img/jv-scan.png)
A staircase voltage ramp is applied from the start to the end voltage. The time each point is applied is determined by step size / scan rate. 

### Parameters ###
After a JV scan is completed, the following parameters are extracted. All parameters are saved in each [JV file](../data/jv-file.md).

- **Voc**[^1]: The voltage at which current is 0 A.
- **Jsc**[^2]: The current at which voltage is 0 V.
- **V_MPP**: The voltage at the MPP[^3]
- **J_MPP**: The current at the MPP[^3]
- **P_MPP**: The power at the MPP (V_MPP * J_MPP)
- **Fill Factor**: P_MPP / (Voc * Jsc)
- **Efficiency**: P_MPP / I_Incident
- **R_series**: 1/slope at Voc
- **R_shunt**: 1/slope at Jsc

???+ info "R calculation"
    The resistance calculation at Voc and Jsc are done with 10% of the JV range. e.g. if the JV is done from -0.2 V to 1.2 V, the taken range is (1.2 - -0.2) * 0.1 = 0.14 V.

### JV Parameters Reference ###

![jv-parameters](../../assets/img/jv-parameters.png)

[^1]: Open-circuit Voltage
[^2]: Short-circuit Current
[^3]: Maximum Power Point