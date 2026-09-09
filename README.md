# 🎫 TicketBuddy - Movie Ticket Booking Platform

**TicketBuddy** is a full-stack movie ticket booking web application designed to deliver seamless ticketing experiences for moviegoers and robust management tools for theater administrators.

---

## ✨ Features

### 👤 **Customer Portal**
* **Authentication**: User registration and secure JWT-based login.
* **Movie & Venue Discovery**: Browse currently showing movies across various venues and locations.
* **Search & Filters**: Search movies and venues by keywords, locations, or categories.
* **Ticket Booking**: Interactive seat selection and real-time ticket availability updates.
* **Booking History**: Track past and upcoming movie ticket reservations.

### 🛡️ **Admin Dashboard**
* **Venue Management**: Create, update, and delete theater venues and locations.
* **Movie & Show Scheduling**: Manage movie listings, showtimes, ratings, ticket pricing, and seat capacities.
* **Category Management**: Organize movies by genre/category.
* **Data Export**: Export venue booking data asynchronously as CSV reports.

### ⚙️ **Background Tasks & Automation**
* **Celery & Redis**: Asynchronous job processing for heavy operations and CSV exports.
* **Celery Beat**: Automated scheduled tasks (e.g., daily reminders, monthly activity reports).
* **MailHog Integration**: Email delivery testing for booking confirmations and automated notifications.

---

## 🛠️ Tech Stack

* **Frontend**: Vue.js 2, Vue Router, Vuex, Axios, Bootstrap 5, Bootstrap-Vue
* **Backend**: Python 3, Flask, Flask-SQLAlchemy, Flask-JWT-Extended, Flask-Caching, Marshmallow
* **Database**: SQLite
* **Queue & Cache**: Redis, Celery, Celery Beat
* **Email Testing**: MailHog

---

## 🗄️ Database Schema

The application employs the following data models:

| Entity | Fields & Keys |
| :--- | :--- |
| **`admin`** | `admin_id` (PK), `email`, `password`, `name` |
| **`customer`** | `cust_id` (PK), `email`, `password`, `name`, `address`, `phone` |
| **`category`** | `category_id` (PK), `name`, `description` |
| **`movie`** | `movie_id` (PK), `venue_id` (FK), `name`, `movie_rating`, `movie_time`, `category_id` (FK), `ticket_price`, `number_of_seats` |
| **`booking`** | `booking_id` (PK), `cust_id` (FK), `venue_id` (FK), `movie_id` (FK), `number_of_tickets` |
| **`venue`** | `venue_id` (PK), `venue_name`, `venue_state`, `venue_city` |

---

## 🔌 API Endpoints

### Common Routes
* `/register`
* `/adminmovie`
* `/exportcsvasync/<int:venue_id>`
* `/exportresult/<string:id>`

### Routes Specific to User
* `/login`
* `/updateprofile`
* `/pickvenue`
* `/pickmovie`
* `/useraddbooking/<int:movie_id_param>`
* `/search_venue_keyword/<string:keyword>`
* `/search_movie_keyword/<string:keyword>`

### Routes Specific to Admin
* `/loginadmin`
* `/admincustomers`
* `/admincategories`
* `/deletecategory/<int:category_id>`
* `/adminaddcategory`
* `/modifycategory/<int:category_id>`
* `/adminvenue`
* `/deletevenue/<int:venue_id>`
* `/adminaddvenue`
* `/modifyvenue/<int:venue_id>`
* `/deletemovie/<int:movie_id>`
* `/adminaddmovie`
* `/modifymovie/<int:movie_id>`
* `/exportcsv`

---

## 📁 Repository Structure

```text
TicketBuddy/
├── README.md              # Project documentation
└── code/
    ├── README.md          # Internal execution steps
    ├── requirements.txt   # Python backend dependencies
    ├── backend/
    │   └── app/
    │       ├── main.py          # Flask application entry point
    │       ├── routes.py        # REST API endpoints & Celery tasks
    │       ├── models.py        # Database models (Customer, Admin, Venue, Movie, Booking)
    │       ├── marsh_schema.py  # Serialization schemas
    │       ├── task.py          # Celery background job definitions
    │       ├── workers.py       # Celery worker initialization
    │       └── jobs.py          # Celery beat scheduled tasks
    └── frontend/
        ├── package.json   # Node package configuration
        └── src/           # Vue components, views, and store
```

---

## 🚀 Getting Started

### Prerequisites
Make sure you have the following installed on your system:
* **Python 3.8+**
* **Node.js 14+** & **npm**
* **Redis Server** (`redis-server`)
* **MailHog** (for local email capture)

---

### 1. Backend Setup

```bash
# Navigate to the backend directory
cd code/backend/app

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r ../../requirements.txt

# Run the Flask server
python main.py
```
The backend API will start at `http://localhost:5000`.

---

### 2. Redis & Celery Worker Setup

In a new terminal window:

```bash
# Start Redis server
redis-server

# Activate the virtual environment
cd code/backend/app
source venv/bin/activate

# Start Celery Worker & Beat
celery -A main.celery worker --loglevel=info
celery -A main.celery beat --loglevel=info
```

---

### 3. MailHog Setup (Email Testing)

In a new terminal window:
```bash
# Start MailHog
mailhog
```
Access the MailHog web interface at `http://localhost:8025` to view outgoing emails.

---

### 4. Frontend Setup

In a new terminal window:

```bash
# Navigate to the frontend directory
cd code/frontend

# Install dependencies
npm install

# Start the Vue development server
npm run serve
```
Access the web application at `http://localhost:8080`.

---