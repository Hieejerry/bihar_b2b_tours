# Uruvela Journeys

A single-page B2B lead-generation website for travel agents and tour operators arranging Bihar itineraries.

## Run locally

```powershell
cd D:\study\bihar_b2b_tours
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. Manage enquiries at `http://127.0.0.1:8000/admin/`.

## Enable Hostinger Webmail notifications

Copy `.env.example` to a new `.env` file in the project root. Replace only
`EMAIL_HOST_PASSWORD` with the password for `Operations@uruvelajourneys.com`,
then restart the Django server. The password stays on this computer and is not
tracked by Git.

## Before launch

Use `.env.example` as a reference and set the listed values in your deployment platform's environment settings (or your local shell). Set a secure `DJANGO_SECRET_KEY`, your real `SALES_EMAIL`, email provider credentials, and allowed domain names. The local default prints email messages to the terminal.
