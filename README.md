# Django Quora-Style Q&A Web App

This Django project replicates the core functionality of a Q&A website inspired by Quora. It enables user authentication, question posting, answering, and liking answers. The emphasis is on functionality over design as per the assignment requirement.

## 🔧 Features Implemented

- **User Registration and Login**: Users can register, log in, and log out using Django's built-in authentication system.
- **Post Questions**: Logged-in users can post questions via a form.
- **View All Questions**: All users can see a list of questions posted by others.
- **Answer Questions**: Logged-in users can submit answers to existing questions.
- **Like Answers**: Logged-in users can like answers posted by others.
- **Logout**: Users can log out from the site.


## 🚀 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone  https://github.com/prasanjit-jena/Quora-clone.git

2. **Create and Activate a Virtual Environment**
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

3. **Install Dependencies**
pip install -r requirements.txt

4. **Run Migrations and Migrate**
python manage.py makemigrations
python manage.py migrate

5.**Create Superuser (Optional)**
python manage.py createsuperuser

6.**Start the Development Server**
python manage.py runserver
Access the App Open http://127.0.0.1:8000/ in your browser.
