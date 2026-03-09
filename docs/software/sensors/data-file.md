## Environmental Sensor Data Files

During operation the system continuously records the environmental parameters from the configured sensors. This data is stored independently from device measurement files so that environmental conditions remain available even when no device measurements are running.

Sensor values are written periodically at a configurable interval (typically **10 s**) and stored in daily log files. This approach keeps file sizes manageable while allowing the system to operate continuously for long periods without interruption.

### File Organization

Environmental data is stored in the `C:\Arkeo\Sensors\` folder using a hierarchical structure that separates different sensors. Files are organized by year and month to avoid excessively large directories.

```text
Sensors/
  <Sensor Name>/
    2026/
      2026-03/
        2026/03/09 - <Sensor Name> (<channel>).txt
        2026/03/10 - <Sensor Name> (<channel>).txt
```

**Note** The parts above in <> brackets are replaced by the actual values of the sensors.

Each file contains all measurements recorded during a single day. If the application is restarted during the same day, data logging automatically continues in the existing file.

### File Format

Sensor data is stored as a tab-separated values table. The first rows contain some metadata about the sensor.

Example:

```text
# sensor_type: Temperature
# sensor_name: Outdoor Temperature
# sensor_channel: 2
# file_date: 09/03/2026

Time	Temperature (°C)
17:16:16 09/03/2026 24.45
17:16:16 09/03/2026 23.73
17:16:26 09/03/2026 24.21
17:16:36 09/03/2026 23.97
...
```

### Data Volume

Because environmental parameters change slowly, the logging interval can remain relatively large. With five sensors sampled every 10 seconds, the resulting data volume is approximately:

| Period | Data Size   |
| ------ | ----------- |
| Day    | ~0.5–1 MB   |
| Month  | ~15–30 MB   |
| Year   | ~150–400 MB |

This modest data rate allows the system to store environmental data continuously for many years without significant storage requirements.