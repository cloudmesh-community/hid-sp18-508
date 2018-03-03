
## Install Raspbian on an SD card using MacOS

* Some steps are copied from <https://www.raspberrypi.org/documentation/installation/installing-images/>
* Some steps are copied from <https://www.raspberrypi.org/documentation/installation/noobs.md>

### Install Etcher

* Follow the instructions at the beginning, download and install Etcher https://etcher.io/

### Install Rasbian 

* Download The Rasbian OS from <https://www.raspberrypi.org/downloads/>
* Make sure to select the Raspbian OS and not NOOBS
* Within raspbian, there are two versions, RASPBIAN STRETCH WITH DESKTOP and RASPBIAN STRETCH 
  LITE. The first one was downloaded (full version)
* Connect an SD card reader with the SD card inside 
* Open Etcher and select from hard drive the Raspberry Pi `.img` or  `.zip` file to write to the 
  SD card.
* Select the SD card to write the image to.
* Review selections and click `Flash!` to begin writing data to the SD card.

### Install Rssbian via NOOBS

* Download page is <https://www.raspberrypi.org/downloads/noobs/>
* Once you've downloaded the `NOOBS` zip file, you'll need to copy the contents to a formatted SD 
  card on your computer. Here are the detailed steps: 
* Format an SD card which is 8GB or larger as FAT. 
* Download and extract the files from the `NOOBS` zip file.
* Copy the extracted files onto the SD card that you just formatted, so that this file is at 
  the root directory of the SD card. Please note that in some cases it may extract the files into 
  a folder; if this is the case, then please copy across the files from inside the folder rather 
  than the folder itself.
* On first boot, the `RECOVERY` FAT partition will be automatically resized to a minimum, and a 
  list of OSes that are available to install will be displayed.
