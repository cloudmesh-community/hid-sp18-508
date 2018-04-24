## Install Ubuntu on an SD card using MacOS

* Some steps are copied from <https://www.ubuntu.com/download/iot/raspberry-pi-2-3>

### Setup an Ubuntu SSO account 

* An Ubuntu SSO account is required to create the first user on an Ubuntu Core installation.

* Start by creating an Ubuntu SSO account <https://login.ubuntu.com/?_ga=2.221155864.1898702810.1524526990-1206082497.1519750630>

* Import an SSH key into your Ubuntu SSO accout <https://help.ubuntu.com/community/SSH/OpenSSH/Keys?_ga=2.221155864.1898702810.1524526990-1206082497.1519750630>

### Create installation medias for Ubuntu Core on Mac OS, some steps are copied from 
  <https://developer.ubuntu.com/core/get-started/installation-medias?_ga=2.157227707.1898702810.1524526990-1206082497.1519750630>
* Download Raspberry Pi 3 
* Insert your SD card or USB flash drive
* Open a terminal window (Go to Application -> Utilities, you will find the Terminal app there), then run the following command:

    diskutil list
    
* In the results, identify your removable drive device address, it will probably look like an entry like the ones below:
  
  
  /dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *500.3 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:                 Apple_APFS Container disk1         500.1 GB   disk0s2

  /dev/disk1 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +500.1 GB   disk1
                                 Physical Store disk0s2
   1:                APFS Volume Macintosh HD            356.3 GB   disk1s1
   2:                APFS Volume Preboot                 21.4 MB    disk1s2
   3:                APFS Volume Recovery                517.8 MB   disk1s3
   4:                APFS Volume VM                      19.3 GB    disk1s4

  /dev/disk2 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *31.9 GB    disk2
   1:             Windows_FAT_32 NO NAME                 31.9 GB    disk2s1

* In this example, /dev/disk2 is the drive address of an 32GB SD card.
* Unmount your SD card with the following command:

    diskutil unmountDisk <drive address>
 
* When successful, you should see a message similar to this one:
  
  Unmount of all volumes on <drive address> was successful
  
* You can now copy the image to the SD card, using the following command:

  sudo sh -c 'xzcat ~/Downloads/<image file> | sudo dd of=<drive address> bs=32m'
  
When finalised you will see the following message:

  0+11063 records in
  0+11063 records out
  724980736 bytes transferred in 161.095270 secs (4500323 bytes/sec)

* You can now eject your removable drive.
