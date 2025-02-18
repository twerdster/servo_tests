# Servo Sensorless Testing Repository

This repository contains simple first test setups and configurations for evaluating sensorless control of various servos using an ODrive motor controller. The current goal is to understand what makes these servos run sensorless. 

## Current List Of Tested Servos

- **iPOWER Motor GM5208-24**
- **iPower Motor GM2804**
- **MiToot 2804/100KV**

Each servo has its own folder containing dedicated test scripts, configurations, and documentation.

## Repository Structure

```
/repo-root
├── iPOWER_Motor_GM5208-24/
│   ├── README.md
│   └── test_sensorless.py
├── iPower_Motor_GM2804/
│   ├── README.md
│   └── test_sensorless.py
├── MiToot_2804_100KV/
│   ├── README.md
│   └── test_sensorless.py
├── requirements.txt
└── README.md
```

## Getting Started

# M5Stack ODrive (v3.5 Lite, 24V) Setup Instructions

These instructions are a reference for setting up the M5Stack 13.2 ODrive device  
(labeled as ODrive v3.5 Lite with a 24V driver) which can be obtained from  
[the M5Stack ODrive page](https://docs.m5stack.com/en/module/odrive).

> **Note:** The official instructions were not helpful for my setup.  
> The odrive they suggested was version **0.5.1.post0** which is very old and current versions of `odrivetool`  
> refused to communicate and upgrade the firmware (which on my unit was shipped as v0.3.7-dev). To work around this, I built a virtual environment,  
> installed **odrive 0.5.1**, then used `odrivetool dfu` to update the firmware to **0.5.4**.  
> I was unable to upgrade further because the device did not immediately enter DFU mode  
> after the 0.5.4 update, so I left the firmware at 0.5.4.

---

## Prerequisites

- A Linux system with Python 3.8 installed (3.9 didnt work and 3.8 is not available on latest Ubuntu versions by default).
- Note: this should work on a Mac also
- The following packages (using apt):
  ```bash
  sudo apt update && sudo apt install -y python3.8 python3.8-venv python3.8-dev software-properties-common
  sudo add-apt-repository ppa:deadsnakes/ppa -y
  sudo apt update
  sudo apt install -y python3.8 python3.8-venv python3.8-dev
  ```
  
---

## Setting Up the Virtual Environment 

   ```bash
# Create a virtual environment (named odrive-env)
python3.8 -m venv ~/odrive-env

# Activate the virtual environment
source ~/odrive-env/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

   ```

---

## Odrive Installation and Firmware Update Procedure
   ```bash

# Install ODrive 0.5.1.post0 because newer versions refused to upgrade firmware
pip install odrive==0.5.1.post0

# Verify the installation by printing the installed ODrive version
python -c "import odrive; print(odrive.__version__)"

# Launch odrivetool to make sure the odrive device is visible to the tool - it should show a connected message
odrivetool

# Leave odrivetool and then enter dfu mode to upgrade the FW to one later (if I remember correctly it updated to 0.5.1 from 0.3.7)
odrivetool dfu

# Then update odrivetool to 0.5.4 and then repeat the FW upgrade for the odrive
pip install odrive==0.5.4
odrivetool dfu

# The result of this should be a device with FW upgraded to at least 0.5.4
   ```

---

## Launching odrivetool After Firmware Update

After completing the firmware update, you can launch the tool to interact with your device. The tests I did are in each folder.
```bash
odrivetool
```

---

## Future Work

- Integrate encoder feedback
- Add more off the shelf servos/steppers
- Add visualizations for easier debugging. The current Odrive gui doesnt support non official odrives or older versions

## Contributing

Feedback, issue reports, and contributions are welcome. Please follow proper coding practices and safety guidelines.

## License

MIT License
