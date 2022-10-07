# STM23

Basic python library for communications with the STM23 Motor + Drive over an ethernet connection

## Example usage

```
import STM23Q
motor = STM23Q.STM23Q_udp(socket_ip = ..., socket_port = ..., motor_ip = ...)
motor.send(b'RS') # Request status 
motor.recv() # Get response from motor. Expected b'RS=R'
```

A `STM23Q.STM23Q_udp._TimeoutExcept` is raised if there is no reply from the motor available

See [Notes on Ethernet Config](docs/Notes-On-Ethernet-Config.md) for configuration of `socket_ip`

`socket_port` is apparently not very important as long as it is unused. A new socket port is required for each motor connected. According to pg 22 of the [Hardware Manual](docs/STM23-Hardware_Manual_920-0021F.pdf) the STM23 drive responds to whatever ip/port sends the first command

`motor_ip` is dependent on the rotary switch located on the motor. See page 21 of the [Hardware Manual](docs/STM23-Hardware_Manual_920-0021F.pdf). Please remember to power cycle the motor after adjusting the rotary switch.

## Motor commands

Queries are typically two letter capital commands. Changing motor settings typically is a two letter command followed by a number.

See [Host Command Reference](docs/Host-Command-Reference_920-0002W_0.pdf) for valid motor commands.

## STM23 udp object

```
NAME
    STM23Q_udp

CLASSES
    builtins.object
        STM23Q_udp
    
    class STM23Q_udp(builtins.object)
     |  STM23Q_udp(socket_ip='192.168.1.30', socket_port=7774, motor_ip='192.168.1.10')
     |  
     |  UDP Communications with the STM23Q Motor
     |  
     |  Methods defined here:
     |  
     |  __del__(self)
     |      Closes socket
     |  
     |  __init__(self, socket_ip='192.168.1.30', socket_port=7774, motor_ip='192.168.1.10')
     |      See page 21-22 of STM23 Hardware Manual for `motor_ip` and `motor_port` info
     |      
     |      See docs/Notes-On-Ethernet-Config.md for `socket_ip` and `socket_port` info
     |  
     |  check_response(self, resp)
     |      Checks motor response for invalid header or term chars
     |      returns: Response without header and term chars
     |  
     |  cleanup_socket(self)
     |      Remove all data in the socket.
     |  
     |  recv(self)
     |      Receive single response packet from motor. Returns bytestring
     |  
     |  send(self, msg)
     |      Sends bytestring `msg` to socket
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  buffer_size = 1024
     |  
     |  default_timeout = 0.1
     |  
     |  eSCL_header = b'\x00\x07'
     |  
     |  motor_port = 7775
     |  
     |  term_char = b'\r'

FILE
    /home/daq/valveBoxMotor/STM23Q/STM23Q_udp.py
```
