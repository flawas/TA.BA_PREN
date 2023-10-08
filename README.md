# TA.BA_PREN

## Installation instructions raspbery pi
Supported and tested with Raspberry Pi
- [Raspberry Pi 2 Model B](https://www.raspberrypi.com/products/raspberry-pi-2-model-b/)
 
### Required and optional software 
#### Update all raspberry pi dependencies
``` 
sudo apt update
``` 
#### Upgrade all raspberry pi pending upgrades
``` 
sudo apt upgrade
``` 
#### Install xrdp for rdp connection
``` 
sudo apt-get install xrdp
```

#### Install git
``` 
sudo apt install git
```
#### Download PREN code
``` 
cd /usr/src
git clone https://github.com/flawas/TA.BA_PREN_PY.git | sudo /usr/src
``` 

## Uninstallation
#### Delete PREN code
``` 
sudo rm -r -v TA.BA_PREN_PY
``` 