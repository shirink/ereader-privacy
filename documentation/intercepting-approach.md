# Intercepting traffic on Kobo e-readers

## Setup

This guide details how to intercept traffic on Kobo e-readers, specifically using a Kobo Clara HD. Below are some interesting modifications you can make to these devices, sourced from the [mobilereads](https://www.mobileread.com/forums/forumdisplay.php?f=247) forum:

- Activate the e-reader without a Kobo account by modifying a `.sqlite` database file in a hidden folder when connected via USB.
- Enable developer mode by clicking the magnifying glass on the top right corner and typing `devmodeon` in the Kobo search bar. Developer mode grants telnet access to the device with a root account that has no password.
- The device likely runs a modified version of Alpine Linux.
- The earlier mentioned database file supposedly contains all user information, including data sent to the server.

### Backup

It is recommended to back up the device before proceeding. To back up:

1. Open the device using a small piece of plastic, credit card, or prying tool.
2. Remove the SD card containing the full filesystem.
3. Create a backup image of this SD card using [VC](https://www.mobileread.com/forums/showthread.php?t=209122) or [CloneDisk](https://www.mobileread.com/forums/showthread.php?t=351715).
4. Save the images for later use. You can also extend the storage by writing the image on a bigger SD card and extending the partition.

## Method

### Using Mitmproxy and Wireshark

> Note: Wireshark is not needed to intercept the traffic, but you can use it as an additional way to store and read traffic.

#### Requirements

- A Linux machine with two network interfaces (one must be wireless for the hotspot).
- Mitmproxy.
- Wireshark.

#### Internet Through Ethernet

1. Disconnect from WiFi and connect via Ethernet.
2. Install **wireshark** and **mitmproxy** using your package manager.

#### Setting Up the WiFi Access Point

Use Network Manager to create a WiFi hotspot:

1. Open Network Manager and click *Edit Connections...*, then *Add*.
2. Select Wi-Fi and set the mode to **hotspot**.
3. Name your SSID and set a WPA2 password.

Ensure your WiFi interface supports AP mode by running:
```
iw list | grep -A 10 modes:
```

Enable IP forwarding:
```
sudo sysctl -a | grep "net.ipv4.ip_forward"  # Should be 1
sysctl -w net.ipv4.ip_forward=1
```

Forward traffic from the wireless interface through ports 80 and 443 to the proxy port:
```
sudo iptables -t nat -A PREROUTING -i $WIRELESS_INTERFACE -p tcp --dport 80 -j REDIRECT --to-port 8080
sudo iptables -t nat -A PREROUTING -i $WIRELESS_INTERFACE -p tcp --dport 443 -j REDIRECT --to-port 8080
sudo ip6tables -t nat -A PREROUTING -i $WIRELESS_INTERFACE -p tcp --dport 80 -j REDIRECT --to-port 8080
sudo ip6tables -t nat -A PREROUTING -i $WIRELESS_INTERFACE -p tcp --dport 443 -j REDIRECT --to-port 8080
```

Start mitmproxy, specifying the `SSLKEYLOGFILE`:
```
SSLKEYLOGFILE="$HOME/.mitmproxy/sslkeylogfile.txt" mitmweb --mode transparent --web-port 3000 --showhost
```

#### Installing the Certificate on the E-reader

1. Connect to the e-reader with telnet:
```
telnet ip
```
2. Log in as root (no password).
3. Create the directory for the certificate:
```
mkdir /etc/ssl/certs
```
4. Transfer the `.crt` file from mitmproxy to this folder. You can use `wget` or transfer it via USB.

Ensure the certificate file has appropriate permissions (e.g., `chmod 644`).

#### Capturing Traffic

1. Start mitmproxy and enable the hotspot.
2. In Wireshark, select the WiFi interface used for the hotspot and capture traffic.
3. In Wireshark, specify the key file path to decrypt traffic (`Edit -> Preferences -> Protocols -> TLS -> (Pre)-Master-Secret log filename`).

Once mitmproxy is running and Wireshark is capturing, connect the e-reader to the network. You should see traffic details on mitmweb or Wireshark.

#### Bash Script

For ease of use, you can also use the following bash script if you adjust the variables to your own setup.

```
#!/bin/bash

# save the current iptables
sudo iptables-save > iptables-rules
sudo ip6tables-save > ip6tables-rules

# Enable IP forwarding
sudo sysctl -w net.ipv4.ip_forward=1

# Redirect HTTP traffic
sudo iptables -t nat -A PREROUTING -i $WIRELESS_INTERFACE -p tcp --dport 80 -j REDIRECT --to-port 8080

# Redirect HTTPS traffic
sudo iptables -t nat -A PREROUTING -i $WIRELESS_INTERFACE -p tcp --dport 443 -j REDIRECT --to-port 8080

# Redirect IPv6 HTTP traffic
sudo ip6tables -t nat -A PREROUTING -i $WIRELESS_INTERFACE -p tcp --dport 80 -j REDIRECT --to-port 8080

# Redirect IPv6 HTTPS traffic
sudo ip6tables -t nat -A PREROUTING -i $WIRELESS_INTERFACE -p tcp --dport 443 -j REDIRECT --to-port 8080

# Set SSLKEYLOGFILE environment variable
export SSLKEYLOGFILE="$HOME/.mitmproxy/sslkeylogfile.txt"

# Start mitmweb in transparent mode on port 3000, the traffic will be dumped in a har file when stopping the script with CTRL+C
./mitmweb --mode transparent --web-port 3000 --showhost --set hardump='test.har'

# restoring saved ip tables 
echo "restoring iptables..."
sudo iptables-restore < iptables-rules
sudo ip6tables-restore < ip6tables-rules
```
