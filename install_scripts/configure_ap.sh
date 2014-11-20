# Automatic script to make the Beaglebone Black an Access Point
# Intended for the latest debian BBB image
# 3.8.13 Kernel Version

#!/bin/bash
cd ~
mkdir wireless_temp
apt-get install -y unzip

echo "Step 1. Attach rtl8192cu driver to the kernel"

# Links
# (1) http://wiesel.ece.utah.edu/redmine/projects/hacks/wiki/BeagleBone_Black_AP
# (2) http://www.codealpha.net/864/how-to-set-up-a-rtl8192cu-on-the-beaglebone-black-bbb/

echo "Installing kernel headers"
wget http://rcn-ee.net/deb/wheezy-armhf/v3.8.13-bone50/linux-headers-3.8.13-bone50_1.0wheezy_armhf.deb
dpkg -i linux-headers-3.8.13-bone26_1.0raring_armhf.deb
apt-get install -y dkms
ln -s /usr/src/linux-headers-3.8.13-bone50/arch/arm /usr/src/linux-headers-3.8.13-bone50/arch/armv7l
# Fix Timex.h error as specified in link (1)
TIMEX_FIX="#include </usr/src/linux-headers-3.8.13-bone26/arch/arm/include/asm/timex.h>"
sed -i '18s/.*/'$TIMEX_FIX'/' /usr/src/linux-headers-3.8.13-bone50/arch/armv7l/include/asm/timex.h

echo "Building rtl8192cu driver"
git clone git://github.com/cmicali/rtl8192cu_beaglebone.git
cd rtl8192cu_beaglebone
make CROSS_COMPILE=""

echo "Installing rtl9182u driver"
mv 8192cu.ko /lib/modules/$(uname -r)
depmod -a
cd /etc/modules-load.d
echo "8192cu" > rtl8192cu-vendor.conf

echo "Blacklisting native RTL drivers"
cd /etc/modprobe.d
echo "install rtl8192cu /bin/false" >wifi_blacklist.conf
echo "install rtl8192c_common /bin/false" >>wifi_blacklist.conf
echo "install rtlwifi /bin/false" >>wifi_blacklist.conf

echo "Step 2. Build an updated hostapd binary from REALTEK"
# hostapd binary obtained from 
# http://152.104.125.41/downloads/downloadsView.aspx?Langid=1&PNid=21&PFid=48&Level=5&Conn=4&ProdID=277&DownTypeID=3&GetDown=false&Downloads=true
cd ~/wireless_temp
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=0B0GMaPIpbJ97RVlkY1doZjFTdVU' -O wpa_supplicant_hostapd-0.8.zip
unzip wpa_supplicant_hostapd-0.8.zip
cd wpa_supplicant_hostapd-0.8/hostapd
make
make install
cp hostapd /usr/sbin/
cp hostapd /etc/
cp hostapd /usr/local/bin/

echo "Step 3. Set-up configuration files"
echo "Configuring /etc/network/interfaces"
INTERFACE_VAR="\n\n#WiFi AP Static Configuration\nauto wlan0\niface wlan0 inet static\naddress 192.168.42.1\nnetwork 192.168.42.0\nnetmask 255.255.255.0\nbroadcast 192.168.42.255" 
printf $INTERFACE_VAR >> /etc/network/interfaces
echo "Configuring hostapd"
wget https://raw.githubusercontent.com/surveycorps/c_apro/master/install_scripts/hostapd.conf
cp hostapd.conf /etc/hostapd/
wget https://raw.githubusercontent.com/surveycorps/c_apro/master/install_scripts/hostapd
cp hostapd /etc/default/

echo "Step 4. Configure DNS"
apt-get -y install dnsmasq
service dnsmasq stop
mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
touch /etc/dnsmasq.conf
printf "interface=wlan0\ndhcp-range=wlan0,192.168.42.2,192.168.42.10,4h" >> /etc/dnsmasq.conf

cd ~
rm -r ./wireless_temp

echo "Done! Don't forget to restart. :D"
echo "Add 'ifup wlan0' to /etc/rc.local to ensure the interface starts up during boot."


## Troubleshooting
# If wlan0 sometimes gets assigned to wlan1 check "/etc/udev/rules.d/70-persistent-net.rules"
# Remove any assignments of rtl to wlan1



