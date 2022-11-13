# HrManager

HrManager is a  Django application that helps us to manage certain aspects of the HR (human resource) department of a company, it is not so detailed, but still, it does have 
useful features.

# Installation

To lunch this project, you can use below command to user docker
> docker-compose up --build 

# Employee Fields : 

* first name 
* last name
* birth day
* national_id
* username
* passwords 

# End points :

0) django-admin panel : first, you need to create a super-user through the terminal and then login to Django-admin from this endpoint: http://localhost:8000/admin



1) for accessing different parts of the project you need to be authenticated , so you can get your access token of already created user 
    from this endpoint and then use it as a header request  :   access token ===>>> http://localhost:8000/auth/jwt/create
    

1) through this enpoint (only Hr_manager ) , submit email and automatically an email will be sent to the user,
    the email contain unique link which will be expire in 1 hour and the client could use it for the rest of hiring process.
    endpoint ===>>> http://localhost:8000/user 

2) Hr_Manager and PayRoll_Manager both have permissions to see the list of employees and their salaries 
  through this endpoint ===>>> http://localhost:8000/manager/Employees/
  
3) just by adding an id at the end of previous endpoint you will get access(if you are authenticated as hr_manager or payroll_manager) to an specific employee profile 
  endpoint : http://localhost:8000/manager/Employees/employee_id 
  
4) a PayRoll_Manager has permission to change the salaries too, endpoint : http://localhost/manager/Employees/employee_id/salaries

5) a Hr_Manager has permission to edit profiles of add employees , endpoint http://localhost/manager/Employees/employee_id 

6) every type of employee have access to their profile with this endpoint : http://localhost/manager/profile 

watch out : you have to be authenticated by your token

