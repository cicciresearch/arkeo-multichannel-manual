Figure 1 shows an example of a source meter board being installed using the Eurocard rails and being connected to the backplane. Each Eurocard board contains 4 independent source meter unit (SMU) modules that can be accessed using a standardized DB25 connector. Each SMU measures and supplies voltage and current to the device. The voltage measurement contact points are connected, though a buffer, directly to the high-speed digitizer, which has a programmable range of ±10 V. Current flows through a current sensing resistance and the voltage drop is measured by the digitizer.

Each SMU has a low and high current range. This range can be custom made depending on the type of devices that are to be measured. A typical SMU made for solar cells has current ranges of 18 mA in low range and 250 mA in high range. These values were chosen such that both small scale (< 1 cm²) and large scale (> 1 cm²) device can be measured without changing hardware. The higher current range comes with a trade-off of lower precision for higher current range. For lower current devices <100 µA, these ranges can be reduced even further for higher precision (nA precision), by modifying the shunt resistor or by adding a current amplifier.

Devices are measured using 4-wire sensing, compared to the easier, but less accurate 2-wire sensing found in cheaper measurement systems. The purpose of four-wire sensing is to avoid measuring contact and probe wire resistance by separating the measurement current from the voltage sensing. It involves the use of four separate wires: two for the current path and two for voltage sensing.

![[4-wire-sensing.png]]

The current wires push a current to the device, while the voltage sensing wires measure the voltage drop across the device. Since the voltage sensing wires are connected directly to the device terminals, they bypass any resistance present in the current wires or connectors. This ensures that the measured voltage accurately represents the voltage across the device.

The contacts themselves may also be divided into 4 separate probes, or as shown in Figure 10, may be connected together for ease of connection. The former gives an even higher precision, by eliminating the contact resistance as well.

### DB25 Pinout
Each DB25 connector connects to 4 SMUs. Each SMU has 6 pins:

1. Force+
2. Sense+
3. Sense-
4. Force-
5. Ground (2x)

Pin 13 is not used.

![DB25-Pinout](assets/img/DB25-Pinout.png)