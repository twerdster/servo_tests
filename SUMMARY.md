# servo_tests context

## Purpose

Five per-motor scripts that configure ODrive axis 0 for sensorless gimbal-motor velocity control and issue an open-ended velocity command.

## Implementation evidence

Each script relies on odrivetool dev0/enums, sets pre_calibrated=True, requests closed-loop control, waits and sets input_vel. The MiToot_2206_100T folder name is preserved accurately.

Key entry points: `iPOWER_Motor_GM5208-24/test_sensorless.py`, `iPOWER_Motor_GM2804/test_sensorless.py`, `iPOWER_Motor_GM4109/test_sensorless.py`, `MiToot_2804_100KV/test_sensorless.py`, `MiToot_2206_100T/test_sensorless.py`, `docs/odrive-setup-record.md`.

## Documentation state

The README explains operations, requirements, validation scope and limitations. Its pre-existing explanatory SVG is retained and labeled as a schematic rather than a runtime result. Source files and attribution are unchanged.

## Validation scope

All five scripts inspected; no hardware connected, firmware changed, motor run or measurements collected. No assertions, traces or quantitative pass/fail record.

## Documented stop request

The README shows a zero-velocity request through the same controller field used by the scripts. Its physical stop behavior and stopping distance were not validated.

## Limitations

Historical firmware/tool setup, unverified macOS operation, motor-specific limits/gains and no automatic stop or measurement loop. Folder presence is not a successful hardware test.
