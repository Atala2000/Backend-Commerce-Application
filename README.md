# Backend E-commerce Application
This is a backend application for an e-commerce website. It is built using Django and Django Rest Framework. The application has the following features:
- User authentication
- Product management
- Order management
- Payment processing
- User profile management


## Requirements
- Python 3.6+
- Django 3.0+
- Django Rest Framework 3.11+
- Redis 5.0+
- Postman 7.34+ (optional)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/Backend-Commerce-Application.git
    ```

2. **Navigate to the project directory:**
    ```sh
    cd Backend-Commerce-Application
    ```

3. **Create and activate a virtual environment:**
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

4. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Apply the migrations:**
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```sh
    python manage.py runserver
    ```


## API Endpoints
### Accounts Endpoints
- `/accounts/register/` - Register a new user
  - Method: `POST`
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

## Products Endpoints
### Category View
Endpoint for listing all categories.

- **URL:** `/api/categories/`
- **Method:** `GET`
- **Permission:** Allow any user.
- **Description:** Returns a list of all categories.

### Product View
Endpoint for listing all products.

- **URL:** `/api/products/`
- **Method:** `GET`
- **Permission:** Allow any user.
- **Description:** Returns a list of all products.

### Update Product View
Endpoint for updating or deleting a product by ID. Only accessible by admin users.

- **URL:** `/api/products/<id>/`
- **Methods:** `GET`, `PUT`, `PATCH`, `DELETE`
- **Permission:** Admin users only.
- **Description:** Retrieve, update, or delete a product by its ID.

### Product Search View
Endpoint for searching products by name.

- **URL:** `/api/products/search/`
- **Method:** `GET`
- **Permission:** Allow any user.
- **Description:** Returns a list of products matching the search query. If no query is provided, returns all products.
- **Query Parameters:**
  - `q`: The search term to filter products by name.

## Authentication and Permissions

- **CSRF Protection:** Enabled by default for all views except for views that are explicitly exempted.
- **Admin Access:** Only admin users can update or delete products.

## Usage with Postman

To test the endpoints using Postman:
1. **List Categories:**
   - **URL:** `http://localhost:8000/api/categories/`
   - **Method:** `GET`

2. **List Products:**
   - **URL:** `http://localhost:8000/api/products/`
   - **Method:** `GET`

3. **Update Product (Admin only):**
   - **URL:** `http://localhost:8000/api/products/<id>/`
   - **Methods:** `GET`, `PUT`, `PATCH`, `DELETE`
   - **Headers:** Include the CSRF token in the `X-CSRFToken` header if CSRF protection is enabled.

4. **Search Products:**
   - **URL:** `http://localhost:8000/api/products/search/?q=<search_term>`
   - **Method:** `GET`

## Cart Endpoints
### View Cart
Endpoint for viewing the contents of the user's cart.
- **URL:** `/cart/`
- **Method:** `GET`
- **Permission:** Allow any user.
- **Description:** Returns the items in the user's cart.

### List Cart Items
Adding items to the cart
- **URL:** `/cart/items/`
- **Method:** `POST`
- **Permission:** Allow any user.
- **Description:** Returns a list of all items in the user's cart.

### Clear Cart
Endpoint for clearing the user's cart.
- **URL:** `/cart/clear/`
- **Method:** `POST`
- **Permission:** Allow any user.
- **Description:** Clears all items from the user's cart.

## Payment Endpoints
### Create Payment(Paypal)
Endpoint for creating a payment.
- **URL:** `/payments/process/`
- **Method:** `POST`
- **Permission:** Allow any user.
- **Description:** Creates a payment for the user's cart.
- ```json
    {
        "payment_method": "required_field",
        "total": "required_field",
        "price": "required_field",
    }
    ```

### Execute Payment
Endpoint for executing a payment.
- **URL:** `/payments/execute/`
- **Method:** `POST`
- **Permission:** Allow any user.
- **Description:** Executes a payment for the user's cart.
- ```json
    {
        "payment_method": "required_field",
        "total": "required_field",
        "price": "required_field",
    }
    ```

## Payment History Endpoints
### List Payment History
Endpoint for listing the user's payment history.
- **URL:** `/history/`
- **Method:** `GET`
- **Permission:** Logged in user.
- **Description:** Returns a list of all payments made by the user.

### Retrieve Payment History
Endpoint for retrieving a payment by ID.
- **URL:** `/history/<str:transaction_id>/`
- **Method:** `GET`
- **Permission:** Logged in user.
- **Description:** Returns a payment by its transaction ID.

## Mpesa Payment
### Initiate payment
Initiate M-Pesa Payment
- **URL:** /mpesa/
- **Method:** POST
- **Description:** This endpoint initiates a payment process using M-Pesa.
- **Name:** initiate_payment

### M-Pesa Callback
- **URL:**  /mpesa/callback/
- **Description:**  This endpoint handles the callback from M-Pesa after a payment is processed.
- **Name:** mpesa_callback

### Mpesa Order History
- **URL:**  /orders/history/
- **Method:** GET
- **Description:** This endpoint allows users to view their order history.
- **Name:**  order_history

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## Contact

For any inquiries, please contact:
[cyrilondanje@gmail.com](mailto:cyrilondanje@gmail.com).
[atalakidi@gmail.com](mailto:atalakidi@gmail.com).
