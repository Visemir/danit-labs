#!/bin/bash

# Path to the log file
LOG_FILE="/var/log/disk.log"

# Threshold percentage of disk usage for receiving notifications
THRESHOLD_PERCENTAGE=80

# Get the percentage of disk usage
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | cut -d'%' -f1)

# Check if the usage percentage exceeds the threshold
if [ "$DISK_USAGE" -gt "$THRESHOLD_PERCENTAGE" ]; then
    # Write a warning to the log file
    echo "$(date '+%Y-%m-%d %H:%M:%S') - WARNING: Disk usage is above ${THRESHOLD_PERCENTAGE}%" >> "$LOG_FILE"
else
    # Write an "All good!" message to the log file
    echo "$(date '+%Y-%m-%d %H:%M:%S') - All good! Disk usage is currently at $DISK_USAGE%" >> "$LOG_FILE"
fi


