#!/bin/sh
# @author: Aravind Voggu @zeroby0

function setStatus () {
  if { [ "$TERM" = "screen" ] && [ -n "$TMUX" ]; } then
    tmux set status-right "Status: $1"   
  fi

  echo -e "\n********** ----- Status: $1 ----- ***********"
  echo "$1" >> '/home/pi/nexmoncsi_update.log'
}

cd /home/pi/nexmon
NEXDIR=$(pwd)

setStatus "Setting up Build Environment"
source setup_env.sh

setStatus "Downloading Nexmon_CSI"
cd $NEXDIR/patches/bcm43455c0/7_45_189/
rm -rf nexmon_csi
git clone https://github.com/nexmonster/nexmon_csi.git

setStatus "Building and installing Nexmon_CSI"
cd nexmon_csi
git checkout pi-4.19.97
make install-firmware

setStatus "Installing makecsiparams"
cd utils/makecsiparams
make
rm /usr/local/bin/mcp
ln -s $PWD/makecsiparams /usr/local/bin/mcp

setStatus "Setting up Persistance"
cd $NEXDIR/patches/bcm43455c0/7_45_189/nexmon_csi/
cd brcmfmac_5.4.y-nexmon
mv $(modinfo brcmfmac -n) ./brcmfmac.ko.orig
cp ./brcmfmac.ko $(modinfo brcmfmac -n)
depmod -a

setStatus "Completed"