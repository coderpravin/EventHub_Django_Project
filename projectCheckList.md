# 🚀 EventHub - Project Checklist

## 📌 1. Project Setup
- [✅] Project requirements finalized
- [✅] Virtual environment created (named venv)
- [✅] Django installed
- [✅] Django REST Framework installed
- [✅] Django project created (named 'eventHub')
- [✅] Git repository initialized
- [✅] .gitignore configured
- [✅] requirements.txt created

## 🏗️ 2. Project Architecture
- [✅] Project folder structure created
- [✅] Django apps created (named 'events')
- [✅] settings.py configured
- [✅] urls.py configured
- [✅] middleware.py file created in events app
- [✅] Custom middleware implemented and tested
- [✅] Environment variables configured

## 🗄️ 3. Database
- [✅] Database configured
- [✅] Models created ('Event' and 'Reservation')
- [✅] Relationships defined ('Reservation' --> 'Event' using ForeignKey)
- [✅] Migrations created
- [✅] Migrations applied
- [✅] Database tested


## 🎟️ 4. Event Management

#  🟣 FBV — Function-Based Views ⚙️ 
- [✅] Create event API
- [✅] Get all events API
- [✅] Get event by ID API
- [✅] Update event API
- [✅] Delete event API

## 🟣 6. CBV — Class-Based Views (Events)⚙️
- [✅] Create event API
- [✅] Get all events API
- [✅] Get event by ID API
- [✅] Update event API
- [✅] Delete event API
- [✅] DefaultRouter implemented
- [✅] URL routing using basename
- [✅] Automatic CRUD operations using ModelViewSet
- [✅] Filter events by status — ?status=upcoming
- [✅] Filter events by Venue — ?status=kolhapur

#  🟣 7. CBV — Class-Based Views (Reservations)⚙️
- [✅] Create All Reservations
- [✅] Get Single Reservation
- [✅] Get All Reservation
- [✅] Filter Reservation by events_id
- [✅] Cancel Reservation API
- [✅] Restore available seats after cancellation


## 📚 8. Documentation
- [✅] screenshotInfo.md created
- [✅] projectCheckList.md created
- [✅] screenshots folder created
- [✅] README.md file created


## 🎯 9. Final Verification
- [✅] Application runs successfully
- [✅] All APIs tested
- [✅] All tests passing
- [✅] Git commits completed
- [✅] Project ready for demonstration