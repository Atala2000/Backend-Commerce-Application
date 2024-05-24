# Backend E-commerce Application
This is a backend application for an e-commerce website. It is built using Django and Django Rest Framework. The application has the following features:
- User authentication
- Product management
- Order management
- Payment processing
- User profile management
- User reviews and ratings
  
## Installation
```bash
git clone 
cd backend-ecommerce
pip install -r requirements.txt
python manage.py runserver
```


## API Endpoints
- `/accounts/register/` - Register a new user
    ```json
    {
        "email": "required_field",
        "password": "required_field",
        "first_name": "optional_field",
        "last_name": "optional_field",
        "phone_no": "optional_field",
        "address": "optional_field",
    }
    ```
- `/accounts/login/` - Login a user
    ```json
    {
        "email": "test@example.com",
        "password": "testpassword"
    }
    ```
- `/accounts/logout/` - Logout a user
  - For it to work needs a user to have logged in

- `/accounts/user/` - Get the user profile
  
