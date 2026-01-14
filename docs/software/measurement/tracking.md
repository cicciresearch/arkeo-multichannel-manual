In the tracking phase of the measurement, the device is kept at a specific point (see [the tracking settings](../settings.md/#tracking) for all options). The first JV is used as the starting point of the tracking phase. For example, if the MPPT option is chosen, the tracking starts with the V_MPP of the JV. The steady-state MPP is often times lower than during a JV, especially with high hysteresis.

### Perturb and Observe ###

The Perturb and Observe (PAO) algorithm is the most widely used algorithm for this task due its simplicity and robustness. Starting from an initial V_MPP obtained from the JV, the device is slightly positively and negatively perturbed (ΔV) with respect to V_MPP. This results in 3 points: V_MPP-ΔV, V_MPP, V_MPP+ΔV. For each point, the device power recorded, and the voltage associated with the maximum power is set as the new V_MPP. The algorithm is then repeated.

???+ warning "Current spikes"
    Jumps in voltage, especially when far from the MPP where the current changes more with changes in voltages, can cause problems in the measurement due to the capacitive effects of many photovoltaic devices. A JV scan stops either at Jsc (when measuring in reverse direction) or at Voc (when measuring in forward direction). A jump in voltage from this point to MPP causes a large current spike as the capacitive effect wears off. To avoid this issue, the Arkeo Multichannel, slowly moves from the last JV point of the scan to the MPP. With a speed (in V/s) according to the JV scan speed. 
    
    Similarly, when oscillating the voltage during the PAO tracking the voltage is moving in a triangle pattern instead of a sawtooth pattern.

    <figure markdown="span">
    ![pao](../../assets/img/pao-shape.png)
    <figcaption>The PAO used in the Arkeo Multichannel software avoids sharp jumps in voltage (left). Instead, smoother transitions are always used (right).</figcaption>
    </figure>

The disadvantage of the PAO algorithm is the slow response if the MPP has large variation relative to the ΔV, for example when suddenly changing the intensity of the illuminating light source. Moreover, the ΔV must be chosen beforehand by the user, and an optimal value differs per device. Devices with higher VOC require a higher ΔV (choosing a ΔV that is too low compared to the V_MPP can result in the algorithm tracking the noise level of the voltage measurement instead). 
