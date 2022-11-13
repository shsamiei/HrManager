# HrManager

HrManager is a  Django application that helps us to manage certain aspects of the HR (human resource) department of a company, it is not so detailed, but still, it does have 
useful features.

### Django-admin-login
for login Django-admin panel you need to create `superuser`, otherwise you can not access the panel.

----

### Installation

-use `docker compose build` to get the images ready to create containers.<br/><br/>
-then you should use `docker-compose up` to aggregates the output of each container

----
### API endpoints :

#### GET
`All of employees` http://localhost:8000/manager/Employees/ <br/><br/>
`Specific employee with id`  http://localhost:8000/manager/Employees/employee_id <br/><br/>
`An employee profile` http://localhost/manager/profile <br/><br/>
`see all the salaries of an employee`http://localhost/manager/Employees/employee_id/salaries <br/><br/>
`see all the users` http://localhost:8000/user <br/><br/>

>watch out : you have to have appropriate permissions to access data - first get access token
----
#### AUTHENTICATION
`access token using user` http://localhost:8000/auth/jwt/create<br/><br/>
`refreshing access token `  http://localhost:8000/auth/jwt/refresh/


----

#### POST
>`creating user by email` http://localhost:8000/user<br/><br/>
>`creating an employee` http://127.0.0.1:8000/manager/accounts/create/uuid<br/>
 you will get your unique link when HrManager submit your email first <br/><br/>
`create new salary (assign to an employee)` http://localhost/manager/Employees/employee_id/salaries <br/>



