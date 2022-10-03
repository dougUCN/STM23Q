# STM23

Basic python library for communications with the STM23 Motor + Drive

## Example usage

```
import STM23Q
motor = STM23Q.STM23Q_udp(socket_ip = ...)
motor.send(b'RS') # Request status 
motor.recv() # Get response from motor. Expected b'RS=R'
```

See [Notes on Ethernet Config](docs/Notes-On-Ethernet-Config.md) for configuration of `socket_ip`

## Motor commands

See [Host Command Reference](docs/Host-Command-Reference_920-0002W_0.pdf) for valid motor commands.
