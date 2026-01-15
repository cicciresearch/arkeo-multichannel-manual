# Measurement Process

The ARKEO system performs parallelized JV and maximum power point tracking (MPPT) measurements. Each measurement begins with a JV scan, which provides the initial device parameters and an estimate of the maximum power point. This initial scan ensures that the system has a reliable starting point before entering tracking mode.

Once the JV scan is complete, the system moves the device voltage toward the estimated MPP at the defined JV scan rate. If tracking is enabled, the system then applies a control algorithm that keeps the device at the chosen operating point. Depending on the configuration, this operating point may correspond to the maximum power point, open-circuit voltage, short-circuit current, or a user-defined voltage or current.

![mppt-flowchart](../../assets/img/mppt-flowchart.png)

Although the SMU hardware does not support galvanostatic operation, the potentiostatic behavior is sufficient for most algorithms. All algorithms except open-circuit voltage rely on a proportional adjustment operation (PAO) to maintain the desired setpoint. In open-circuit mode, the SMU simply enters a high-impedance state, causing the device to float naturally to Voc.

When operating at a fixed voltage, it is important to consider that the SMU regulates the source voltage rather than the voltage directly at the device terminals. Under load, a small voltage drop can occur across the output stage, creating a difference between the set voltage and the voltage actually applied to the device. Tracking can be used to compensate for this offset when maintaining a fixed-voltage operating condition.

!!! warning
    This limitation is especially relevant during JV scans. The set voltage may not correspond exactly to the actual device voltage, which can cause the scan to miss the current axis crossing if it starts at 0 V. To avoid this, JV scans start at -0.2 V by default, ensuring that the voltage sweep always crosses the J=0 axis. Another approach is to begin the scan in reverse. At Voc the current is zero, so no voltage drop occurs, and the scan naturally moves toward the required crossing point.

At regular intervals, the system performs an additional JV scan. These periodic scans serve two purposes. First, they provide updated JV parameters—such as efficiency, fill factor, Voc, and Jsc—allowing users to follow the evolution of device performance over time. This offers better insight into degradation behavior than monitoring MPP alone. Second, periodic scans confirm that the MPP being tracked remains the true global maximum and has not shifted due to device changes during the measurement period.

The combination of JV initialization, continuous tracking, and periodic full scans enables ARKEO to characterize device performance accurately while maintaining stable long-term operation.
