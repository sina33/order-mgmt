# Order Management System
This is a Django REST Framework application for managing orders with Role-Based Access Control (RBAC) using custom permissions and PostgreSQL as the database. The application supports two user types: admins and customers, with specific permissions for each.

### Project Structure
Project consists of configuration files (`order_management`) and orders app directory (`orders`). dependencies includes Django, Django REST Framework and `psycopg2-binary`.

### Features
Admins: Can view, edit, delete, and filter all orders.  
Customers: Can create, view, edit, and delete their own orders; cannot access other customers orders.  

### Setup Instructions
install dependencies    
`pip install -r requirements.txt`  
configure postgreSQL  
create a database named `order_management`. Update `order_management/settings.py` with your database credentials
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'order_management',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```  

Apply migrations  
`python ./manage.py makemigrations`   
`python ./manage.py migrate`  

Create a superuser (admin):  
`python manage.py createsuperuser`  

then run the server   
`python ./manage.py runserver`  

### Endpoints
using these endpoints you can create, list, edit and delete orders:
- `/api/orders/` GET - list orders
- `/api/orders/` POST - create order
- `/api/orders/<id>` GET - orer details
- `/api/orders/<id>` PUT - update order
- `/api/orders/<id>` DELETE - delete order

### Tests
execute the following command to run test cases  
`python ./manage.py test`