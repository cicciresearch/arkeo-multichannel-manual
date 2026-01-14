# Sample Holders

A sample holder is a custom PCB with several spring-loaded probes positioned according to the device structure. The traces connect to a custom connector, which in turn connects through a cable back to the [source measure units](smu-introduction.md). Devices on a sample holder are usually back-contacted. This simplifies the design of the sample holder and avoids having the contact probes block the incident light. Devices are pressed onto the spring-loaded contacts using a metal mask with openings for the incident light. The mask can be fixed in place using screws or magnets depending on the design.

<figure markdown="span">
  ![sample-holder](../assets/img/sample-holder.png)
  <figcaption>
    Example of a sample holder for 32 devices distributed across 4 substrates. 
    On the bottom left, temperature, humidity, and luminosity sensors can be found.
  </figcaption>
</figure>

The figure above shows an example of a sample holder for 32 devices in a small area. Since the devices are always grouped together in the same order, smaller and more flexible Samtec® cables are used instead of eight bulky DB25 connectors. These cables also carry the signals used to measure the [environmental sensors](../software/sensors/sensor.md) present on the sample holder.

Testing each sample holder is not reliable when using lab-level devices, since failing to measure a signal may be due to a failing device rather than a fault in the sample holder. For each type of sample holder, a custom PCB with the same layout as the solar cells is therefore made. The solar cells are substituted with resistors to reliably test the entire connection chain.