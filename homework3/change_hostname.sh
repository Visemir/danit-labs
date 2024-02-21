#!/bin/bash

# Display the current hostname
current_hostname=$(hostname)
echo "Current hostname: $current_hostname"

# Ask the user for a new hostname
read -p "Enter the new hostname: " new_hostname

# Change the hostname in configuration files
sudo hostnamectl set-hostname $new_hostname
sudo sed -i "s/127.0.1.1.*/127.0.1.1\t$new_hostname/g" /etc/hosts

# Display a message about the hostname change
echo "Hostname successfully changed to $new_hostname."

# Display a colored message about the need to reboot
echo -e "\e[1;33mNow you need to reboot the system for the changes to take effect!\e[0m"
