#!/bin/sh
#
#DNS_update-script.sh
wget https://LRkDmmtkxqFErj3y:YFG60gjyn3hv9SPg@domains.google.com/nic/update?hostname=www.amrodriguez.net -O dns_update_results.txt
echo " Last run: `date`">>/home/pi/sysconfig/dns_update_results.txt
