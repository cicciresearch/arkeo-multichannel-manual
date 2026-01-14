# ARKEO Documentation

Welcome to the ARKEO documentation hub.  
This site provides a complete reference for operating ARKEO software and hardware, understanding measurement workflows, configuring channels and sensors, and interpreting recorded data files.

This guide is organized into four major areas:

- **Software usage** - How to run JV scans, tracking, day–night cycles, sample holder tools, and more.  
- **Settings & configuration** - All parameters and their meanings, covering channels, JV settings, tracking settings, and cell configuration.  
- **Data formats** - Understanding JV files, tracking files, parameter files, and how ARKEO stores measurement results.  
- **Hardware** - Environmental chambers, sample holders, SMU installation, light soakers, and compatibility information.

---

## Quick Start

Use the links below to jump directly to the most important sections.

<div class="grid cards" markdown>

-   :material-book-open-variant:{ .lg }  **Continue to Software**  

    ---

    Dive into measurement workflows, tools, and UI reference.  
    [Open Software Documentation](software/index.md)

-   :material-chip:{ .lg }  **View Hardware Guides**  

    ---

    Installation, wiring, chambers, light soakers, and sample holders.  
    [Open Hardware Docs](hardware/index.md)

-   :material-play-circle-outline:{ .lg .middle } **Starting a Measurement**  

    ---

    Learn the full workflow for configuring channels and initiating JV measurements.  
    [:octicons-arrow-right-16: Start here](software/measurement/starting-a-measurement.md)

-   :material-database:{ .lg .middle } **Data Structure & File Formats**  

    ---

    Learn how ARKEO stores JV scans, tracking data, and measurement settings.  
    [:octicons-arrow-right-16: Data Format Overview](software/data/index.md)

</div>

---

## Software Overview

ARKEO is structured into several modules that work together during measurements:

### **Measurement Workflows**
- **JV scan** – Extracts Voc, Jsc, MPP parameters, FF, efficiency, Rs, Rsh.  
- **Tracking** – Runs MPPT or fixed-voltage tracking with periodic JV scans.  
- **Day–Night** – Automates illumination cycles for stability testing.  
- **Sample Holder Tool** – Visualizes and manages sample holder configurations.

Explore these pages:

- [Starting a Measurement](software/measurement/starting-a-measurement.md)  
- [JV Scan](software/measurement/jv-scan.md)  
- [Tracking](software/measurement/tracking.md)  
- [Day–Night](software/day-night.md)  
- [Sample Holder Tool](software/sample-holder-tool.md)

---

## Configuration & Settings

All ARKEO settings are separated into clear categories:

- **General settings** – User, device name, notes  
- **Channel settings** – Voltage/current limits, inverted structure  
- **JV parameters** – Vmin, Vmax, step size, scan rate, scan order  
- **Tracking parameters** – Algorithm, perturbation voltage, save interval, JV interval  
- **Cell parameters** – Area, number of cells, W-cell configuration  

A complete reference is available here:

[:material-cog: **Settings Reference**](software/settings.md)

---

## Data File Formats

ARKEO stores every measurement in clearly structured data files.  
Each file type has its own documentation:

- [JV File Format](software/data/jv-file.md)  
- [Tracking File Format](software/data/tracking-file.md)  
- [Parameter File](software/data/parameter-file.md)

This helps with automation, post-processing, and integration with third-party tools.

---

## Sensors & Environments

ARKEO supports multi-sensor environments for chamber control, irradiance logging, and device monitoring.

- [Sensors Overview](software/sensors/sensor.md)  
- [Environments](software/sensors/environments.md)

---

## Hardware Documentation

Detailed guides for installing and using ARKEO-compatible hardware:

- [SMU Installation](hardware/new-smu-install.md)  
- [SMU Introduction](hardware/smu-introduction.md)  
- [Sample Holders](hardware/sample-holders.md)  
- [Environmental Chambers](hardware/chambers.md)  
- [Light Soaker](hardware/light-soaker.md)

---

## Changelog

Want to see what changed in the latest ARKEO version?

[:material-history: **Changelog**](software/changelog.md)

---

## Need Help?

If you have questions or encounter unexpected behavior, consult:

- [JV troubleshooting notes](software/measurement/jv-scan.md#parameters)  
- Hardware safety documents  
- Data file specifications  

Or reach out to support channels associated with your installation.

---
