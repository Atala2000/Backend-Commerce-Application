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
- `/accounts/login/` - Login a user
  : Request: POST
    : Body: 
    ```json
    {
        "email": "test@example.com",
        "password": "testpassword"
    }
    ```
- `/accounts/logout/` - Logout a user
  
- `/accounts/user/` - Get the user profile
