1. Explain the stages involved in booting the Linux system.
Етапи завантаження системи Linux:
. BIOS:
Процес завантаження починається з BIOS (Basic Input/Output System), прошивки, що знаходиться на материнській платі.
BIOS проводить POST (Power-On Self Test) для перевірки працездатності апаратного забезпечення.
BIOS шукає завантажувальний пристрій, який може бути жорстким диском, SSD, CD/DVD або USB-накопичувачем.

. Завантажувач:
Якщо завантажувальний пристрій знайдено, BIOS передає йому управління.
Завантажувач - це невелика програма, яка завантажує ядро Linux.
Завантажувач може бути GRUB (Grand Unified Bootloader) або LILO (Linux Loader).

. Ядро:
Ядро - це центральна частина операційної системи Linux.
Ядро завантажується в пам'ять і починає ініціалізацію апаратного забезпечення.
Ядро монтує кореневу файлову систему, яка містить всі файли, необхідні для роботи системи.
Ядро запускає init-процес, який відповідає за запуск інших системних служб.

. Init-процес:
Init-процес - це перша програма, що запускається ядром.
Init-процес читає сценарії ініціалізації, які налаштовують систему та запускають необхідні служби.
Init-процес може бути SysVinit, Systemd або Upstart.

. Запуск користувацького середовища:
Після того, як init-процес завершить свою роботу, запускається користувацьке середовище.
Користувацьке середовище (англ. User Environment) - це комплекс програм та інструментів, 
який надає інтерфейс для взаємодії користувача з операційною системою. 
Воно включає графічне оточення, додатки та інші компоненти, які дозволяють користувачеві працювати з комп'ютером.
Деякі поширені користувацькі середовища - це GNOME, KDE,  Xfce, LXDE і MATE.

. Робота користувача:
Користувач може входити в систему, запускати програми, редагувати файли, переглядати веб-сторінки та виконувати інші дії.



2. How to view system logs?
Перегляд системних журналів в Linux:

1. Команда journalctl:
journalctl - це основна команда для перегляду системних журналів в Linux.
Вона використовується для перегляду, фільтрації та аналізу журналів, зібраних службою журналів systemd.
Деякі приклади використання journalctl:
# Переглянути останні записи журналу
journalctl
# Переглянути записи журналу для певної служби
journalctl -u <назва_служби>
# Переглянути записи журналу за певний період часу
journalctl --since "2023-11-14 10:00" --until "2023-11-14 12:00"
# Фільтрувати записи журналу за ключовим словом
journalctl | grep <ключове_слово>

2. Команда dmesg:
dmesg використовується для перегляду журналу повідомлень ядра.
Цей журнал містить інформацію про завантаження системи, драйвери пристроїв та апаратне забезпечення.

3. Команда lastlog:
lastlog використовується для перегляду інформації про останні входи в систему.

4. Файли журналів:
Системні журнали також можна переглядати, читаючи відповідні файли журналів.
Деякі поширені файли журналів:
/var/log/syslog
/var/log/auth.log
/var/log/kern.log
/var/log/messages

Опис системних журналів Linux:

 /var/log/syslog:
Цей журнал містить системні повідомлення, такі як:
Повідомлення про завантаження системи
Повідомлення служб
Повідомлення про помилки
Інформаційні повідомлення
Користується для загального аудиту та діагностики проблем.

 /var/log/auth.log:
Цей журнал містить записи про аутентифікацію та авторизацію, такі як:
Успішні та невдалі входи в систему
Зміни паролів
Спроби несанкціонованого доступу
Користується для відстеження проблем безпеки та аудиту доступу до системи.

 /var/log/kern.log:
Цей журнал містить повідомлення ядра Linux, такі як:
Повідомлення про драйвери пристроїв
Помилки ядра
Інформаційні повідомлення про ядро
Користується для діагностики проблем з апаратним забезпеченням та ядром.

 /var/log/messages:
Цей журнал містить суміш повідомлень з різних джерел, таких як:
Системні повідомлення
Повідомлення служб
Повідомлення про помилки
Інформаційні повідомлення
Цей файл журналу може бути корисним для швидкого огляду останніх подій в системі.

3. -rw------- : Describe this permission. How to add an executable flag to the file?
Права доступу "-rw-------" вказують на те, що це є права доступу до файлу для конкретного користувача. 
Тут розшифровка має такий вигляд:

"-rw": Перші три символи вказують на права для власника файлу. 
У цьому випадку "rw" означає, що власник може читати та записувати (read and write) в файл, але не може виконувати його як програму.
"-------": Решта символів вказують на відсутність прав доступу для групи користувачів та інших користувачів.
Щоб додати виконавчий прапорець (executable flag) до файлу із такими правами, можна використати команду chmod. 
support@study:~$ touch lab.txt
support@study:~$ chmod 600 lab.txt
support@study:~$ ls -l lab.txt
-rw------- 1 support support 0 Feb 20 14:12 lab.txt
support@study:~$ chmod +x lab.txt
support@study:~$ ls -l lab.txt
-rwx--x--x 1 support support 0 Feb 20 14:12 lab.txt

support@study:~$ chmod 700 lab.txt
support@study:~$ ls -l lab.txt
-rwx------ 1 support support 0 Feb 20 14:12 lab.txt

4. What is the difference between apt and dpkg?
Різниця між apt та dpkg:
apt (Advanced Packaging Tool) та dpkg (Debian Package Manager) - це два інструменти, 
що використовуються для керування пакетами в Debian та інших дистрибутивах Linux, заснованих на Debian.

dpkg:

dpkg - це більш низькорівневий інструмент, який використовується для встановлення, видалення та оновлення пакетів Debian (.deb).
dpkg працює з файлами пакетів безпосередньо, не маючи залежностей.
dpkg може бути корисним для діагностики проблем з пакетами.
apt:

apt - це більш високорівневий інструмент, який використовується для керування пакетами з використанням репозиторіїв.
apt може автоматично завантажувати та встановлювати пакети, а також вирішувати залежності.
apt використовує dpkg для фактичного встановлення, видалення та оновлення пакетів.
apt - це більш зручний інструмент для користувачів, які не хочуть працювати з dpkg безпосередньо.
Коротко:

dpkg: низькорівневий, використовується для роботи з файлами пакетів, не має залежностей.
apt: високорівневий, використовується для роботи з репозиторіями, автоматично вирішує залежності.
Використання apt та dpkg:

apt - це кращий вибір для більшості завдань, таких як:
Встановлення пакетів
Оновлення пакетів
Видалення пакетів
dpkg може бути корисним для:
Діагностики проблем з пакетами
Встановлення пакетів з невідомих джерел
Встановлення пакетів, які не доступні в репозиторіях
