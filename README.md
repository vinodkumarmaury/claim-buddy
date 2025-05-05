
---

# 🏥 Patient Management System — README

A Django web app to view paginated and searchable patient records with a responsive UI using the Stisla admin template.

## 🔧 How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/claim-buddy.git
   cd patient-management
   ```

2. Create and activate virtual environment:

   ```bash
   python -m venv venv
   # Windows: venv\Scripts\activate
   # macOS/Linux: source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5.  Create superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open in browser:

   * Main App: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   * Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)



---


