# order-mgmt
Order Management System using Django

### setup and run
to setup the project run the following command in the root directory  
`python ./manage.py migrate`  
this will create database and tables required for the application  
then run the server   
`python ./manage.py runserver`  
using these endpoints you can create, list, edit and delete orders:
- /api/orders/ GET - list orders
- /api/orders/ POST - create order
- /api/orders/<id> GET - orer details
- /api/orders/<id> PUT - update order
- /api/orders/<id> DELETE - delete order

execute the following command to run test cases  
`python ./manage.py test`