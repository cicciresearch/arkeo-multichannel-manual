Figure 1 shows an example of a source meter board being installed using the Eurocard rails and being connected to the backplane. Each Eurocard board contains 4 independent source meter unit (SMU) modules that can be accessed using a standardized DB25 connector. Each SMU measures and supplies voltage and current to the device. The voltage measurement contact points are connected, though a buffer, directly to the high-speed digitizer, which has a programmable range of ±10 V. Current flows through a current sensing resistance and the voltage drop is measured by the digitizer.

Each SMU has 2 current sensing resistors of 562 Ω and 5 Ω. As the digitizer can measure and supply a maximum of 10V, these resistors allow for a maximum current of 18.8 mA and 2 A to flow. 2 A is too much for the small devices that the system is designed for, so it is limited to 250 mA to reduce cost and complexity of the SMUs.

The digitizer does not have infinite precision and at low currents, the signal-to-noise ratio starts to increase. The Low current range with the higher current sensing resistor improves the signal-to-noise ratio, but it may not be enough for currents less than ~1 µA. In that case, the current sensing resistor may be replaced by a higher resistance of, for example, 5 kΩ or 50 kΩ depending on the expected current of the devices. In addition, the SMUs have a current amplifier installed, which boosts the current by a factor of 10, 100 or 1000 for even more precision at the cost of maximum current to be measured.

To reduce load on both the devices and the SMUs, each SMU has an internal relay to switch the current to a high impedance (100 kΩ) state, blocking current flow. In this state, the connected devices may be considered in open-circuit voltage. This is useful both for checking whether the device is well connected as well as being able to measure the open-circuit voltage over time.

### DB25 Pinout
Each DB25 connector connects to 4 SMUs. Each SMU has 6 pins:

1. Force+
2. Sense+
3. Sense-
4. Force-
5. Ground (2x)

Pin 13 is not used.

![DB25-Pinout](assets/img/DB25-Pinout.png)