# STM23

Basic python library for communications with the STM23 Motor + Drive

## Example usage

```
import STM23Q
motor = STM23Q.STM23Q_udp(socket_ip = ..., socket_port = ...)
motor.send(b'RS') # Request status 
motor.recv() # Get response from motor. Expected b'RS=R'
```

See [Notes on Ethernet Config](docs/Notes-On-Ethernet-Config.md) for configuration of `socket_ip`

Note: We assume that the 16 position rotary switch on the motor is set to 0 (ip address "10.10.10.10"). If your switch is in another setting, edit the `MOTOR_IP` variable in `STM23Q_udp.py`

`socket_port` is apparently not very important as long as it is unused. According to pg 22 of the [Hardware Manual](docs/STM23-Hardware_Manual_920-0021F.pdf) the STM23 drive responds to whatever ip/port sends the first command

## Motor commands

Queries are typically two letter capital commands. Changing motor settings typically is a two letter command followed by a number.

See [Host Command Reference](docs/Host-Command-Reference_920-0002W_0.pdf) for valid motor commands.
