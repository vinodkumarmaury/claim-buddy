Thought for a second


```markdown
# Patient Data Management App

A Django-based patient data management module built for the ClaimBuddy Technologies Software Engineer Intern assessment.  
Integrated with the [Stisla Admin Dashboard template](https://getstisla.com/) for a clean, responsive UI.

---



---

## 🔗 GitHub Repository

[https://github.com/your-username/patient-management](https://github.com/your-username/patient-management)

---

## 🚀 Quick Start

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/patient-management.git
   cd patient-management
````

2. **Create & activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **(Optional) Add dummy patient data**

   ```bash
   python manage.py shell
   ```

   ```python
   from patients.models import Patient
   Patient.objects.create(full_name="John Doe", age=30, gender="Male", insurance_provider="Blue Cross", policy_number="123456789")
   Patient.objects.create(full_name="Jane Smith", age=28, gender="Female", insurance_provider="Aetna", policy_number="987654321")
   # …repeat for at least 5 patients…
   exit()
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Open in browser**

   * Patient list: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   * Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## ⚙️ UI & Integration

* **Stisla Template**: Placed under `static/stisla/`.
* **Responsive Design**: Uses Stisla’s grid plus custom CSS for Excel-style tables, search bar animations, and polished pagination.
* **Templates**:

  * `patient_list.html` dynamically renders patients, includes search, pagination, and “Add Patient (Admin)” button.

---

## 📝 Notes

* Code follows Django best practices (app structure, `app_name.urls`, template inheritance).
* UI is mobile-friendly and cleanly integrated with Stisla’s components.
* Bonus features: animated search bar, zebra-striped tables, and styled pagination.

---

```
```
