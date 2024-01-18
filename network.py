# https://stackoverflow.com/questions/63801369/try-multiple-aps-and-passwords-until-connected-on-esp32-with-micropython

import network

# Set up the Wi-Fi networks you want to try to connect to
networks = [("SSID1", "PSK1"), ("SSID2", "PSK2")]

# Attempt to connect to each network in order
for ssid, psk in networks:
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, psk)

    # Wait for the connection to succeed or fail
    for _ in range(20):
        if wlan.isconnected():
            print("Connected to", ssid)
            break
        else:
            time.sleep(0.5)

    # If we successfully connected to a network, stop trying
    if wlan.isconnected():
        break
