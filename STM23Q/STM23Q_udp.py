import socket, select, json, os


class STM23Q_udp(object):
    """UDP Communications with the STM23Q Motor"""

    # See page 21-22 of STM23 Hardware Manual
    # The motor IP settings depend on the screw on the motor
    MOTOR_IP = "10.10.10.10"
    MOTOR_PORT = 7775

    # UDP settings
    buffer_size = 1024
    default_timeout = 0.1  # seconds

    # UDP protocol
    eSCL_header = b"\000\007"
    term_char = b"\r"

    def __init__(self, socket_ip="10.10.10.3", socket_port=7774):
        """Loads valid commands from `commands.json` and
        initializes socket bind with `socket_ip` and `socket_port` arguments
        """
        with open(os.path.dirname(__file__) + "/commands.json") as command_file:
            self.commands = json.load(command_file)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((socket_ip, socket_port))
            sock.setblocking(0)  # guarantee that recv will not block internally
            self._sock = sock
        except Exception as error:
            self._sock = None
            raise self._InitializationExcept(error)

    def send(self, msg):
        """Sends bytestring `msg` to socket"""
        if not isinstance(msg, (bytes, bytearray)):
            raise TypeError("`msg` should be a bytestring")
        sock = self._sock

        # Clean up if something is already there
        garbage = select.select([sock], [], [], 0)
        if garbage[0]:
            self.cleanup_socket()

        sock.sendto(
            self.eSCL_header + msg + self.term_char,
            (self.MOTOR_IP, self.MOTOR_PORT),
        )

    def recv(self):
        """Receive single response packet from motor. Returns bytestring"""
        sock = self._sock
        if select.select([sock], [], [], self.default_timeout)[0]:
            resp, address = sock.recvfrom(self.buffer_size)
            return self.check_response(resp)
        else:
            raise self._TimeoutExcept

    def cleanup_socket(self):
        """Remove all data in the socket."""
        sock = self._sock
        while 1:
            ready = select.select([sock], [], [], 0.0)
            if not ready[0]:
                break
            sock.recv(self.buffer_size)

    def check_response(self, resp):
        """Checks motor response for invalid header or term chars
        returns: Response without header and term chars
        """
        if resp[:2] != self.eSCL_header or resp[-1] != int.from_bytes(
            self.term_char, "big"
        ):
            raise self._UnexpectedResponse(f"Unexpected response {resp}")
        return resp[2:-1]

    def __del__(self):
        """Closes socket"""
        if self._sock:
            self._sock.close()

    # ---- Automatic attribute management ---- #

    def __getattr__(self, name):
        """Retrieves an attribute as defined by commands.json"""
        try:
            return self.commands[name]
        except KeyError:
            msg = "'{0}' object has no attribute '{1}'"
            raise AttributeError(msg.format(type(self).__name__, name))
    
    # ---- Exceptions ---- #
    
    class _TimeoutExcept(Exception):
        """Access timeout during request"""

    class _InitializationExcept(Exception):
        """Issue with socket binding on initialization"""

    class _UnexpectedResponse(Exception):
        """Received response in an unexpected format"""
