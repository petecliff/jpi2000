# jpi2000 - Simple Pi-based demo sensors

Using a BME680 and an enviroPHAT as demo environmental sensors for UI demos.

See:

https://shop.pimoroni.com/products/bme680-breakout

https://shop.pimoroni.com/products/enviro-phat

Setup Wifi:

Using wicd-curses to manage network so:

sudo systemctl disable dhcpcd
sudo /etc/init.d/dhcpcd stop
sudo apt-get install wicd-curses
