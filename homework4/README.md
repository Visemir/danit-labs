The script generates a random number between 1 and 100 and stores it in a variable. The user is asked to guess the number. If the user's guess is correct, the script should print "Congratulations! You guessed the right number." and exit. If the user's guess is incorrect, the script should provide feedback like "Too high" or "Too low" and allow the user to guess again. The user should have a maximum of 5 attempts to guess the correct number. After 5 incorrect attempts, the script should print "Sorry, you've run out of attempts. The correct number was [the correct number]" and exit.
Сам скрипт [SCRIPT](https://github.com/Visemir/danit-labs/blob/main/homework4/random-num.sh)

Робота скрипта

![Скрін роботи](https://github.com/Visemir/danit-labs/blob/main/homework4/random-num.jpg)

Create user john with home folder at default path.

![](https://github.com/Visemir/danit-labs/blob/main/homework4/createjohn.jpg)

Install and configure an SSH server listening on port 2222, restricting root access and disallowing password authorization. Only john can connect to your server and only with an ssh key.

![](https://github.com/Visemir/danit-labs/blob/main/homework4/johnsshd.jpg)

In parallel, run ssh in debug mode listening on port 3333, with no user connection restrictions (except root), with the ability to connect by password and ssh key.

![](https://github.com/Visemir/danit-labs/blob/main/homework4/newsshd.jpg)

Try connecting to your servers.

![](https://github.com/Visemir/danit-labs/blob/main/homework4/newsshd2.jpg)

Check the status of both your ssh servers.

![](https://github.com/Visemir/danit-labs/blob/main/homework4/status.jpg)

