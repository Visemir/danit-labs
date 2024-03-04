#!/bin/bash

# Шлях до файлу журналу
LOG_FILE="/var/log/disk.log"

# Поріг відсотка використання диска, за яким ви хочете отримувати сповіщення
THRESHOLD_PERCENTAGE=80

# Отримати відсоток використання диска
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | cut -d'%' -f1)

# Перевірити, чи відсоток використання перевищує поріг
if [ "$DISK_USAGE" -gt "$THRESHOLD_PERCENTAGE" ]; then
    # Записати попередження у файл журналу
    echo "$(date '+%Y-%m-%d %H:%M:%S') - WARNING: Disk usage is above ${THRESHOLD_PERCENTAGE}%" >> "$LOG_FILE"
else
    # Записати повідомлення "Все добре!" у файл журналу
    echo "$(date '+%Y-%m-%d %H:%M:%S') - All good! Disk usage is currently at $DISK_USAGE%" >> "$LOG_FILE"
fi
