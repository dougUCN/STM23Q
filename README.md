# STM23

Basic python library for communications with the STM23 Motor + Drive

## Example usage

```
import STM23Q
motor = STM23Q.STM23Q_udp(socket_ip = ...)
#TODO example commands
```

See [Notes on Ethernet Config](docs/Notes-On-Ethernet-Config.md) for configuration of `socket_ip`

## Motor commands

Valid motor commands are found in `STM23Q/commands.json`. New commands may be added by editing this file.

A command needs to follow the format of the example below
```json
"AccelRate":{                           // Name of the property or command
    "command":"AC",                     // Two-letter command defined in the command manual
    "description":"Acceleration Rate",  // Unabbreviated name of the command
    "type:"float",                      // Expected data type
    "read":true,                        // Read access
    "write":true,                       // Write access
    "range":{                           // [Optional] limits on write access commands
        "min":0.167,
        "max":5461.167
    },
    "help":"[rev/sec/sec]"              // Additional documentation on the command (e.g. units)
```

Note: if "type" is set to "bool", setting the attribute to `True` sends the command to 
the motor.
