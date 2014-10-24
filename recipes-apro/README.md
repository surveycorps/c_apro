First you should follow the directions on openembedded ros up to sourcing the 
enivornment and setting up the build on your machine:
http://wiki.ros.org/hydro/Installation/OpenEmbedded

Then you can use the provided local.conf and bblayers.conf

To add packages, just modify local.conf to include more packages like so:
http://wiki.wandboard.org/index.php/Building_Qt5_using_yocto_on_Wandboard

Lastly you can go back to the ros guide and bitbake the image then you can
go to the SD card (name BOOT) and format 32MB partition to FAT32 with a boot 
flag. Other partition name ROOT with EXT4. 

sudo cp to /BOOT/
u-boot.img
MLO
uImage

sudo tar -xzf {IMAGE}.tar.gz -C /ROOT/
sudo cp am335x-boneblack.dtb /ROOT/boot/
sudo cp uImage /ROOT/boot/

Then you should be able to boot with the serial cable
