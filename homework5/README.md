Task 1: User and Group Management
Create User Accounts:
Create user accounts for developers: "dev1," "dev2," and "dev3."
Create Groups:
Create two groups: "developers" and "webmasters."
Assign Users to Groups:
Add "dev1" and "dev2" to the "developers" group.
Add "dev3" to the "webmasters" group.
Set Default Group for Users:
Ensure that the default group for each developer is set to "developers."

![](https://github.com/Visemir/danit-labs/blob/main/homework5/userandgroups.jpg)

Create Home Directories:
Create home directories for each developer in the "/home" directory.

![](https://github.com/Visemir/danit-labs/blob/main/homework5/dir.jpg)

Clone a User Account:
Create a new user "backupdev" and clone the home directory of "dev1" for this user.
![](https://github.com/Visemir/danit-labs/blob/main/homework5/rsync.jpg)

Set Permissions for a Shared Project:
Create a directory called "web_project" in "/home."
Allow read and write access to the "developers" group.

![](https://github.com/Visemir/danit-labs/blob/main/homework5/webproject.jpg)

Immutable log file:
Create a my.log file at /home dir, prevent anyone from writing to it except to add new content to the end of the file.
Task 2: Disk Utilization Monitoring
Write a [script](https://github.com/Visemir/danit-labs/blob/main/homework5/disk_monitor.sh) and set up crontab to run this script which will check your / volume utilization and if it is higher than X percent (configurable in crontab),

![](https://github.com/Visemir/danit-labs/blob/main/homework5/crontab.jpg)

it will write a warning message to the log file /var/log/disk.log.

https://github.com/Visemir/danit-labs/blob/main/homework5/disklog.jpg

Task 3: Monit Configuration for Nginx Monitoring
Create [configuration](https://github.com/Visemir/danit-labs/blob/main/homework5/nginx) of Monit for monitoring nginx service. Monitoring should check if the service is available on port 80 of the local host. If the service is still not available after seven checks, the monit stops restart attempts.

![](https://github.com/Visemir/danit-labs/blob/main/homework5/monit.jpg)
