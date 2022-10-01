# Notes on setting up ethernet connection

## Network manager

Requires admin user on Ubuntu

Open "Wired Settings" on your desired ethernet port in the Ubuntu Gui

IPV4 --> set IPV4 Method to Manual

Address = 10.10.10.3, Net Mask = 255.255.255.0

Save and apply. Changes should show up when using `ip address show`

Config file is stored in `/etc/NetworkManager/system-connections/Wired Connection 1`

Apparently there is a cli tool called `nmcli` that allows you to manage this as well

## Temporary ip configuration

This ip configuration goes away with system restarts

For temporary ip configuration, use

```
sudo ip addr add <IP>/24 dev <ethernet interface>
```

In our case we use `<IP> =  10.10.10.3`. Determine `<ethernet interface>` using the `ip address show` command


