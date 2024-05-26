# Backend E-commerce Application
This is a backend application for an e-commerce website. It is built using Django and Django Rest Framework. The application has the following features:
- User authentication
- Product management
- Order management
- Payment processing
- User profile management
- User reviews and ratings


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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## Contact

For any inquiries, please contact [cyrilondanje@gmail.com](mailto:cyrilondanje@gmail.com).
