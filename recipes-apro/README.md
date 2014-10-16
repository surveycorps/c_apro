First you should follow the directions on openembedded ros up to sourcing the 
enivornment and setting up the build on your machine:
http://wiki.ros.org/hydro/Installation/OpenEmbedded

Then you can use the provided local.conf and bblayers.conf

To add packages, just modify local.conf to include more packages like so:
http://wiki.wandboard.org/index.php/Building_Qt5_using_yocto_on_Wandboard

Lastly you can go back to the ros guide and bitbake the image then you can
go to the SD card and rm -rf BBB_ROOT/*

Then sudo tar -xvf tmp-glibc/deploy/images/beaglebone/$(image_name).tar.gz -C /BBB_ROOT/

We have to include the am335x-boneblack.dtb and the uImage in /BBB_ROOT/boot/ 

The rest should be all set then you can boot with the serial cable. Not yet 
tried with regular usb. 
