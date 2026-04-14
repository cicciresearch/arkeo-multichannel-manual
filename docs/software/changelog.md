#### v1.0
Initial version

#### v2.0

- Overhauled the graph interface to be more dynamic
- Reorganized the settings window to clarify which settings belong to which section
- Added sample holder tool

#### v2.1

- Added Voc overvoltage
- Added option for multiple chambers in Sample holder tool
- Added "Channel Current" to settings window
- Allowed option to disable "Voltage Homing" in the config file

#### v2.2

- UI Overhaul of the summary table
	- Now supports grouping
	- Added right-click option to quickly access data files
- API v0.1 added
- Added "Save Settings" and "Load Settings" option to sample holder tool
- Removed the TrackInterval setting

#### v2.2.1

- API updated to v0.2
- UI update for the load settings wizard

#### v2.2.2

- API updated to v0.3
- Added JV parameters to tracking graph

#### v2.2.3

- API updated to v0.4
- Added option to measure Irradiance from a sensor. The values are saved in the tracking file

#### v2.3.0 - 2025-10-14

- Updated the sensor manager to allow custom sensors
- Added Day-night cycling feature
- API updated to v0.4.1
- Changed JV graph selection from radio buttons to tabs
- Restructured some internal data structures for improved memory performance
- Added temperature sensor selection to device settings.

#### v2.3.1 - 2025-10-18

- New: Environments
	- Sensors can be combined into environments
	- Channels can select an associated environment. All environmental parameters are saved in the device's data files
- Removed selection of temperature sensor, it is now integrated in environments
- Removed option of "From sensor" from light source, it is now integrated in environments
- Clarified the "Mode" window

#### v2.3.2 - 2025-10-23

- Added crash recovery feature
- Added suspend feature
- Temporarily removed pause function
- Improved graph performance to reduce CPU load
- Fixed 20V not working properly

#### v2.3.3 - 2025-10-27

- Fixed Forward Only not working
- Settings auto-selected channel when opened now considers the current user as well
- Temporarily removed the "voltage homing" feature

#### v2.3.4 - 2025-11-20

- Sensors from chambers are now grouped together in the sensor manager
- Added x-axis range selection
- New version of Day-Night cycling
	- Improved algorithm
	- User-friendly sensor selection
- Updated API to v0.4.2
	- Added ```GetEnvironments``` to API
	- Added ```SetChannelEnvironment``` to API

#### v2.3.5 - 2026-01-13

- Updated API to v0.5.0
- Added day-night cycling per channel
	- Previous version still available by setting the "User Global" option
	- The settings window has been slightly rearranged to accommodate the new feature
	- Added option to select algorithm in night (previously was forced to open-circuit)
	- Added option to allow JV during night time
	- Added additional Day/Night column to summary table
- Added Temperature stage control in the sensor manager. They are considered as temperature sensors
- Fixed Parameter file not taking into account the irradiance value in the settings
- Fixed some settings not being copied when using the copy channels checkbox

#### v2.3.6 - 2026-01-13
- Fixed several Day-Night cycling bugs
- Fixed constant output not showing up in day-night cycle

#### v2.4.0 - 2026-03-09
- Changed file headers to now contain all settings (see [JV File](../software/data/jv-file.md) for more details).
	- Most notable, the environment and day-night cycling settings are now included (if enabled)
	- Legacy version is still available by setting `FileHeaderVersion = 1` in the config file
- Added generic sensors option when adding a custom sensor. Any sensor with a gain and offset can be used now
- Added [sensor data files](../software/sensors/data-file.md). Sensor data is saved here, independently of any configured devices

#### v2.5.0 - 2026-04-14
- Added JV preview on parameter point hover in the tracking and curve parameters view
- Added a JV history view, showing JV curves overlapped
- Fixed tracking in `Fixed Voltage` mode not moving beyond JV scan range limits
- Improved MPPT speed
- Removed the `Perturbation` setting
	- `MPPT` now automatically uses 5% of the JV scan range
	- Other modes now use a proportional algorithm instead of a perturb and observe algorithm to apply the setpoint ([details](measurement/tracking.md#fixed-setpoint))
- Removed `Fixed Voltage (no track)`