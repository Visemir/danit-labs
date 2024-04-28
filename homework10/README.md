PART 1: Develop a REST API
Develop a REST API for student management in Python using the Flask library named [app.py](https://github.com/Visemir/danit-labs/blob/main/homework10/app.py), with data persistence in a students.csv file. 
The API should support GET, POST, PUT, PATCH, and DELETE requests. Each student should have fields for id, first name, last name, and age.

![](https://github.com/Visemir/danit-labs/blob/main/homework10/web1.jpg)

![](https://github.com/Visemir/danit-labs/blob/main/homework10/web2.jpg)

![](https://github.com/Visemir/danit-labs/blob/main/homework10/web3.jpg)

PART 2: Create test_requests.py
Functionalities
Create a [test_requests.py](https://github.com/Visemir/danit-labs/blob/main/homework10/test_requests.py) file to verify the created REST API. In this file, demonstrate the functionality of all methods using the requests library in the following sequence:

Retrieve all existing students (GET).
Create three students (POST).

![](https://github.com/Visemir/danit-labs/blob/main/homework10/test1.jpg)

Retrieve information about all existing students (GET).

![](https://github.com/Visemir/danit-labs/blob/main/homework10/test2.jpg)

Update the age of the second student (PATCH).
Retrieve information about the second student (GET).
Update the fist name, last name and the age of the third student (PUT).
Retrieve information about the third student (GET).
Retrieve all existing students (GET).

![](https://github.com/Visemir/danit-labs/blob/main/homework10/test3.jpg)

Delete the first user (DELETE).
Retrieve all existing students (GET).

![](https://github.com/Visemir/danit-labs/blob/main/homework10/test4.jpg)

Display the execution results in the console and write them to the [results.txt](https://github.com/Visemir/danit-labs/blob/main/homework10/results.txt) file.
