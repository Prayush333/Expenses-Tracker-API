# Django Expense Tracker API

This is a RESTful API for tracking personal expenses and income, built as part of an internship task. It includes user authentication using JWT tokens. Regular users can manage their own data, and superusers can manage all records.

---

##  Features

- User registration and login with JWT
- Personal income/expense tracking
- Automatic tax calculation (flat or percentage)
- Complete CRUD operations
- Paginated API responses
- Role-based access (user vs superuser)

---

##  Technologies Used

- Python 3.8+
- Django
- Django REST Framework
- Simple JWT (`djangorestframework-simplejwt`)
- SQLite (development database)

---

##  Setup Instructions (using bash)

# 1. Clone the repository
git clone https://github.com/Prayush333/Expenses-Tracker-API.git
cd Expenses-Tracker-API

# 2. Create virtual environment

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create a superuser (optional)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver

