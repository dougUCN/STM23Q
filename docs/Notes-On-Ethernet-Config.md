# Notes on setting up ethernet connection

## Network manager

Requires admin user on Ubuntu

Open "Wired Settings" on the desired ethernet port in the Ubuntu Gui

```
IPV4 --> set IPV4 Method to Manual

Address = 192.168.1.30, Net Mask = 255.255.255.0
```

A reminder that the motor IP address of `192.168.1.30` should be avoided in this example.

Note that if the net mask is 255.255.255.0 then the pc can only talk to
a motor whose IP address matches the first three octects.

Save, apply, and reboot. Manual settings should appear when using `ip address show`

Config file is stored in `/etc/NetworkManager/system-connections/Wired Connection 1`. (Requires sudo to r/w)

There is a cli tool called `nmcli` that does the same things as the Gui.

[Useful reference link](https://devconnected.com/how-to-add-route-on-linux/)

## Temporary ip configuration

This ip configuration goes away with system restarts

For temporary ip configuration, use

```
sudo ip addr add <IP>/24 dev <ethernet interface>
```

In this example case `<IP> =  192.168.1.30` (and motor IP should not be set to `192.168.1.30`). Determine `<ethernet interface>` using the `ip address show` command

## Using a Netgear GS308 Switcher for multiple motors

The Netgear GS308 is an unmanaged switch that blindly forwards requests

Example usage:

```
import STM23Q
motor1 = STM23Q.STM23Q_udp(socket_port=7774, motor_ip="192.168.1.10") # Rotary switch set to 1
motor2 = STM23Q.STM23Q_udp(socket_port=7773, motor_ip="192.168.1.20") # Rotary switch set to 2
motor1.send(b"DI100000") # Set motor 1 dist to 100000
motor2.send(b"DI50000") # Set motor 2 dist to 50000
motor1.send(b"DI") # Query DI value from motor1
motor2.send(b"DI") # Query DI value from motor2
motor1.recv() # b'DI=100000'
motor2.recv() # b'DI=50000'
motor1.send(b"FL") # Tell motor 1 to move the set dist
motor2.send(b"FL") # Tell motor 2 to move the set dist
```
