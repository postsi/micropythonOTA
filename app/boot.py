# boot.py
import senko
import machine
import network

WIFI_SSID = "SETUP-CDD1"
WIFI_PASSWORD = "count8864depend"
import os

local_files = os.listdir()
print("Files to update:", local_files)

OTA = senko.Senko(
  user="postsi", # Required
  repo="micropythonOTA", # Required
  branch="master", # Optional: Defaults to "master"
  working_dir="app", # Optional: Defaults to "app"
  files = local_files

)

# Connect to Wi-Fi network.

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
  print('connecting to network...')
  sta_if.active(True)
  sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
  while not sta_if.isconnected():
    pass
print('network config:', sta_if.ifconfig())

if OTA.update():
    print("Updated to the latest version! Rebooting...")
    machine.reset()