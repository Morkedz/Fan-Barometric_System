# Fan-Barometric System

Utilizes the L293 DC Motor Driver, fan, and BMP280 barometric sensor modules on Raspberry Pi. Based on temperature input from the BMP280, the fan will rotate at a set speed. Kernel and live data export scripts to .xlsx files for export in Excel. At script termination, graph of temperature as function of time over duration of program execution.

## Trouble-Shooting
**February 18, 2026: Motor Ground Wire Fatigue Failure**
Problem: Black (GND) Wire snapped at solder join

Impact: Electrical Circuit broken, total loss of fan actuation

Root Cause: Mechanical stress/vibration at the connection point.

Fix: February 21, 2026. Soldered severed wire onto fan joint. Reinforced/potted area with hot glue to prevent mechanical stress.