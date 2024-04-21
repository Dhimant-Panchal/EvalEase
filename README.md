# Installation & Execution

## Frontend
```
cd frontend
npm i
npm run build
npm run preview
```

## Backend
```
cd backend
pip install django
pip install djangorestframework
py manage.py runserver
```

# Usage

Access the app at `http://localhost:4173/`.

This app has an accounts system. If you wish to login, you can create accounts and change passwords on the admin page (`http://localhost:8000/admin`).
A superuser is provided; credentials `uname: Admin, pwd: Bingus123`. All accounts included in the sample db have the password `Bingus123`.