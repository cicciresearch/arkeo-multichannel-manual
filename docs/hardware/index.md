# ARKEO Hardware Overview

The ARKEO multichannel measurement system is built around a scalable hardware architecture designed for photovoltaic and optoelectronic device characterization.  
Multiple independent **source measure units (SMUs)** operate in parallel, each connected to its own device under test. This allows simultaneous JV scans, tracking measurements, and automated long-term reliability experiments.

Each SMU is a plug-and-play Eurocard module that inserts into a custom backplane.  
The backplane provides:

- :material-power-plug: **Power distribution**  
- :material-usb-port: **Communication with the PC**  
- :material-lan: **Coordination between channels**  

Together, these components create a robust and expandable multichannel test platform.

---

## Hardware Components

The hardware section of the documentation covers all physical modules used with the ARKEO system, including SMUs, sample holders, environmental chambers, and light soakers.  
Use the cards below to explore each subsystem.

<div class="grid cards" markdown>

-   :material-flash:{ .lg .middle }  
    **Source Measure Units (SMUs)**

    Independent Eurocard modules capable of sourcing and sinking up to ±250 mA and driving voltages up to ±10 V.  
    [Learn more →](smu-introduction.md)

-   :material-tools:{ .lg .middle }  
    **Installing a New SMU**

    Step-by-step instructions for adding or replacing SMU boards.  
    [Installation guide →](new-smu-install.md)

-   :material-test-tube:{ .lg .middle }  
    **Sample Holders**

    Supports device mounting, electrical contact, and efficient sample exchange during high-throughput testing.  
    [Sample holders →](sample-holders.md)

-   :material-fridge-outline:{ .lg .middle }  
    **Environmental Chambers** 

    Temperature-controlled and multi-sample enclosures for stability testing and accelerated degradation studies.  
    [Chambers overview →](chambers.md)

</div>

---

## How the Hardware Fits Into the ARKEO System

ARKEO’s measurement workflow operates across both software and hardware components:

- :material-flash: **SMUs** apply voltages or currents and acquire electrical characteristics.  
- :material-test-tube: **Sample holders** allow fast device swapping and repeatable contact.  
- :material-fridge-outline: **Chambers** maintain temperature, humidity, and irradiance conditions.  
- :material-weather-sunny: **Light soakers** provide stable illumination for MPPT or day–night cycles.  
- :material-chart-line: **Software** orchestrates JV scans, tracking loops, and data acquisition.  

This architecture allows ARKEO to support multichannel measurements, automated stability experiments, and high-throughput device testing.

---