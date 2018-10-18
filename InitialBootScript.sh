#this script will run everything that is needed to set up:
#opencv 3-4-3

#!/bin/bash
echo "Running the IntialBootScript written by Jeremy"

#updates the distro and the packages
sh ./systemupdater.sh

#runs the script to unstall opencv 3-4-3
sh ./easycvinstall.sh

#this could bring in the file from the guys github for flask? and unzip it
