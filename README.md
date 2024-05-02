# Cyber-Physical Teaching Kit
## General Description

The Cyber-Physical Teaching Kit (CPTK) is a miniature, modular building with a fully-functional control
system. The belief is that by building a robust model, students will better understand how to think about
potential cyber attacks. The code is mostly written in python for the Raspberry Pi 4, along with C++ code
for the Arduino. Students are more likely to encounter python and Arduino coding throughout high school
or college, which is why these two languages were chosen.

To see the full documentation, see the documentation PDF on our Github.

## Features

+ Sturdy, lightweight 3D printed frame with files available for re-printing
+ Accurate elevator with button controls on each floor and a re-calibration function
+ Temperature monitoring with an HVAC and duct work system for air conditioning
+ Security door system using RFID badges with a working door
+ Lights with individual floor motion detection
+ Full database for logging events, errors, and storing user configurations
+ Security assessment in pdf form detailing vulnerabilities, mitigation, and impact

## Links

+ [Github for open source code under the MIT license](https://github.com/lmurach)
+ [Security Assessment PDF](https://github.com/lmurach/AU_Capstone_Trideum/blob/ui_dev/TrideumCapstoneSecurityAssessment.pdf)

## Block Diagram

![image](https://github.com/lmurach/AU_Capstone_Trideum/assets/66843400/f48b7815-2aec-41e6-856a-bc79cbf6b2d5)

# Getting Started

An already constructed version of the CPTK was built for Trideum Corporation. The following are
instructions for running the program on the existing system.

## Running the App with a Monitor

This is the most ideal way to view the application, as the GUI is visible and intractable. If a monitor is
not available, see the next section.
1. Plug an HDMI cable, keyboard, and mouse into the Raspberry Pi and power the system. The Pi will
boot automatically.
2. Open the console using the icon at the top right of the screen or with the keyboard shortcut
CTRL+ALT+T
3. Run the application with the following command:
sudo python3 AU Capstone Trideum/application.py

## Running the App without a Monitor
Note that the GUI will not be accessible with this method.
1. Plug an Ethernet cable into the Pi and power the system. The Pi will boot automatically. Make sure
your Ethernet settings allow internet and file sharing.
2. For Windows users, install PuTTy.
3. Run the .exe file and enter in the following for the host name, then press enter:
```
cptk@raspberrypi.local
```
![image](https://github.com/lmurach/AU_Capstone_Trideum/assets/66843400/115094a1-b7f3-44b5-b6cc-0e1c10b9be70)

4. For macOS/Linux users, open the command prompt and enter the following command:
```
ssh cptk@[raspberrypi ip address]
```
To get the IP address, run ipconfig in the command line. Alternatively, follow the instructions for
Windows and install PuTTy.
5. Once connected, the command line will prompt for a password. The password for the cptk user is
CPTK-Project
The text will not show up while typing the password, but hitting enter will connect to the Pi.
6. Run the application with the following command:
```
sudo python3 AU Capstone Trideum/application.py -platform offscreen
```
