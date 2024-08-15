# Capstone-Project

# Little Lemon

## Overview

Little Lemon is a web application for managing a restaurant's menu and table bookings. It provides APIs for performing CRUD operations on menu items and booking tables on specific dates. The application uses Django and Django REST Framework, with Djoser for user authentication and MySQL as the database backend.

## Features

- **Menu API:**
  - View a list of menu items.
  - Retrieve details of a single menu item.
  - Create, update, and delete menu items.

- **Booking API:**
  - Book a table for a specific date.
  - Manage existing bookings.

- **Authentication:**
  - User registration and login using Djoser and token authentication.

## Technologies Used

- **Backend Framework:** Django, Django REST Framework
- **Authentication:** Djoser
- **Database:** MySQL
- **Other Tools:** mysqlclient


### Prerequisites

1. **Python**: Ensure that Python 3.x is installed on your machine. You can download it from [python.org](https://www.python.org/).

2. **MySQL**: Ensure that MySQL is installed and running. You can download it from [mysql.com](https://dev.mysql.com/downloads/) Ensure also to create the database specified in the settings.py file on your local machine.

3. **Git**: Ensure that Git is installed for cloning the repository. You can download it from [git-scm.com](https://git-scm.com/).

**Clone the repository:**

   ```bash
   git clone https://github.com/aikay2/Capstone-project.git
   ```

### Menu API Endpoints

- **List menu items:** `GET /menu/`
- **Retrieve a menu item:** `GET /menu/<id>/`
- **Create a menu item:** `POST /menu/`
- **Update a menu item:** `PUT /menu/<id>/`
- **Delete a menu item:** `DELETE /menu/<id>/`

### Booking API Endpoints

- **List bookings:** `GET /restaurant/booking/tables/`
- **Retrieve a booking:** `GET /restaurant/booking/tables/<id>/`
- **Book a table:** `POST /restaurant/booking/tables/`
- **Update a booking:** `PUT /restaurant/booking/tables/<id>/`
- **Delete a booking:** `DELETE /restaurant/booking/tables/<id>/`

### Authentication Endpoints

- **Register:** `POST /auth/users/`
- **Login:** `POST /auth/token/login/`
- **Logout:** `POST /auth/token/logout/`

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Special thanks to the developers of Django and the Django REST Framework.
- Inspiration for this project came from real-world restaurant management systems.

