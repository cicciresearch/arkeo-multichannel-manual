# Source Measure Unit (SMU) Introduction

Each ARKEO SMU board contains four independent source-measure channels, brought out through a standardized DB25 connector. An SMU sources or sinks current, applies voltage, and measures the electrical response of a device with high precision. This section provides an overview of the SMU architecture, current ranges, measurement modes, and the DB25 pinout.

---

## SMU Architecture

Every SMU channel includes a programmable voltage source, a current drive stage, a precision shunt for current measurement, and a buffered voltage-sensing path connected to the system digitizer. The digitizer measures the device voltage directly, while the current measurement is derived from the shunt voltage. This architecture allows accurate and stable measurement during both slow and fast JV sweeps.

Four channels are grouped onto a single SMU board, which plugs into the ARKEO backplane. The backplane distributes power and communication signals, allowing fully independent multichannel operation.

---

## Current Ranges

Each SMU offers two selectable current ranges: a low-current range for higher precision, and a high-current range for larger devices. In the standard configuration, the low range supports measurements up to approximately 18 mA, while the high range extends to around 250 mA. These values are chosen to cover both small-area (< 1 cm²) and large-area (> 1 cm²) solar cells without requiring hardware changes.

For very low-current applications, such as detecting nA-level leakage or measuring early-stage materials, the system can be customized by modifying the shunt resistor or adding a low-noise current amplifier. This enables accurate measurements for currents below 100 µA.

---

## Four-Wire Sensing

ARKEO uses a four-wire (Kelvin) sensing configuration to improve measurement accuracy. Two wires carry the sourced current (Force+ and Force–), while the second pair (Sense+ and Sense–) measures the voltage directly across the device terminals. Because the sense wires carry negligible current, their measured voltage does not include any cable or contact resistance.

![4-wire-sensing](../assets/img/4-wire-sensing.png)

This configuration is particularly important for low-voltage devices, low-resistance samples, or measurements requiring high precision. In cases where absolute accuracy is required, separate probes should be used for force and sense contacts, since combined probes can introduce additional resistance at the contact point.

---

## 20 V Extension

A single SMU can apply up to ±10 V relative to ground. For applications requiring a wider voltage range, ARKEO supports a 20 V differential configuration. This is achieved by using two SMUs in series: one drives the positive terminal, and the other drives the negative terminal with an equal but opposite voltage. The device voltage then becomes the difference between the two.

The illustrations below show the wiring for both operating modes.

=== "10 V"

    ![10v-smu](../assets/img/10v-smu.png)

=== "20 V"

    ![20v-smu](../assets/img/20v-smu.png)

---

## DB25 Pinout

Each DB25 connector carries four SMU channels, with six pins allocated to each channel:

1. Force+  
2. Sense+  
3. Sense−  
4. Force−  
5. Ground (repeated twice)  

Pin 13 is not used.

![DB25-Pinout](../assets/img/DB25-Pinout.png)

[← Back to Hardware Overview](index.md)  
[Continue to SMU Installation →](new-smu-install.md)
