# e-Gyan LMS – Online Learning Management System

> **A comprehensive web-based Learning Management System developed as a major project during professional Python Full Stack with Django training.**

**e-Gyan LMS** is a web-based Learning Management System designed to provide a centralized digital platform for managing online learning activities, student information, study materials, communication, feedback, enquiries, and academic interactions.

The project is inspired by the requirements of a distance-learning environment and focuses on providing students and administrators with a structured, secure, and user-friendly platform for managing educational resources and services.

> 🚧 **Project Status:** Work in Progress — actively under development and enhancement.

---

## 📌 Project Overview

Traditional distance education can involve challenges such as delayed access to learning materials, limited communication, manual record management, and difficulty in tracking academic interactions.

The **e-Gyan LMS** aims to address these challenges by bringing important academic and administrative activities into a single web application.

The system provides separate functionalities for **students and administrators**, allowing authorized users to access services according to their roles.

The project follows a modular architecture so that different educational operations can be managed independently while working together as a unified LMS.

---

## 🎯 Objectives

The major objectives of the project are:

* Provide a centralized platform for online learning and academic services.
* Manage student information efficiently.
* Provide secure user authentication and role-based access.
* Allow students to access course-wise and subject-wise study materials.
* Provide discussion and doubt-clearing functionality.
* Manage student complaints and feedback.
* Publish important academic news and announcements.
* Handle enquiries submitted by users.
* Maintain structured academic and administrative records.
* Integrate communication services such as email and SMS.
* Provide a scalable foundation for future LMS enhancements.

---

## 🚀 Key Features

### 🔐 Authentication & Login Management

* Secure login functionality.
* Role-based access for different users.
* Separate student and administrator functionality.
* Session-based user management.
* Logout functionality.
* Password management.

### 👨‍🎓 Student Information Management

* Maintain student profiles and academic information.
* Manage details such as roll number, name, program, branch, year, contact information, etc.
* Centralized student record management.

### 📚 Study Material Management

* Upload and manage learning materials.
* Organize materials according to:

  * Program
  * Branch
  * Year
  * Subject
* Provide students with access to relevant study resources.

### 💬 Discussion Forum

* Students can post questions.
* Students can participate by answering questions.
* Supports academic discussions and doubt clarification.

### 📝 Complaint Management

* Students can submit complaints.
* Administrators can view submitted complaints.
* Complaint resolution can be managed from the administrative side.

### ⭐ Feedback Management

* Students can submit feedback.
* Administrators can review feedback through the management panel.

### 📢 News & Announcement Management

* Administrators can publish important news and announcements.
* Published information can be displayed to students/users.

### 📩 Enquiry Management

* Users can submit enquiries through the system.
* Enquiries are available to administrators for further processing.

### 📧 Email Integration

* Supports system-generated email communication for relevant activities such as student registration.

### 📱 SMS Integration

* Designed to support system-generated SMS notifications for relevant enquiry-related activities.

---

## 🛠️ Technology Stack

| Technology           | Purpose                    |
| -------------------- | -------------------------- |
| **Python**           | Backend programming        |
| **Django**           | Web application framework  |
| **HTML5**            | Page structure             |
| **CSS3**             | Styling and layout         |
| **JavaScript**       | Client-side functionality  |
| **Bootstrap**        | Responsive UI design       |
| **SQLite3**          | Database                   |
| **Django Templates** | Dynamic frontend rendering |
| **VS Code**          | Development environment    |

The project synopsis specifies Python with Django for coding, HTML/CSS/JavaScript/Bootstrap for interface development, and SQLite3 as the database.

---

## 🏗️ Project Architecture

The project is organized into multiple Django applications/modules to keep different functional areas separated and maintainable.

```text
e-Gyan-LMS/
│
├── adminapp/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── ...
│
├── studentapp/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── ...
│
├── mainapp/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── ...
│
├── elms/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── media/
│   └── ...
│
├── manage.py
├── db.sqlite3
└── README.md
```

> **Note:** The project structure may evolve as development continues and additional features/modules are implemented.

---

## 🧩 Major Modules

The system is divided into multiple functional modules:

```text
e-Gyan LMS
│
├── Student Information System
├── Login Management System
├── Discussion Forum Management
├── Complaint Management System
├── Feedback Management System
├── News Management
├── Enquiry Management
├── Study Material Management
├── Email Integration
└── SMS API Integration
```

These modules are part of the project's defined functional scope.

---

## 🗄️ Database Design

The project uses a relational database structure to manage different types of academic and application data.

Major entities include:

* Student
* Login
* Enquiry
* Question
* Answer
* Response
* News
* Program
* Branch
* Year
* Study Material

The database design supports relationships between students, academic information, discussion activities, responses, news, and learning materials.

---

## 🔒 Security & Access Management

The application incorporates user authentication and session-based access management to ensure that users can access functionalities according to their roles.

Key areas include:

* Authentication
* Authorization
* Session management
* Role-based access
* Logout management
* Password management
* Controlled access to administrative functionality

---

## 📱 Responsive Interface

The frontend is developed using **HTML5, CSS3, JavaScript and Bootstrap**, allowing the application interface to be structured in a responsive and user-friendly manner across different screen sizes.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sandeepshahu33/NOU-eGyan-LMS.git
```

### 2. Navigate to the Project

```bash
cd NOU-eGyan-LMS
```

### 3. Create a Virtual Environment

```bash
python -m venv myenv
```

### 4. Activate Virtual Environment

**Windows:**

```bash
myenv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🔄 Development Workflow

The project is being developed using an iterative approach where modules and functionalities are implemented, tested, refined, and integrated progressively.

```text
Requirement Analysis
        ↓
System Design
        ↓
Database Design
        ↓
Django Development
        ↓
Frontend Integration
        ↓
Testing & Debugging
        ↓
Feature Enhancement
        ↓
Deployment
```

The project synopsis identifies requirement analysis, system design, coding, testing, and implementation as major software development phases.

---

## 🧪 Testing

Testing is performed throughout development to verify:

* Authentication and authorization flow.
* Form validation.
* Database operations.
* CRUD functionality.
* Session handling.
* Module-level functionality.
* Frontend-backend integration.
* Responsive user interface.
* Error handling and debugging.

---

## 🔮 Future Scope

The system is designed with scope for further enhancement and deployment.

Potential future improvements include:

* Deployment on a production web server.
* Dedicated Android/mobile application.
* Additional communication and notification features.
* Advanced student progress tracking.
* Enhanced assessment and evaluation features.
* Additional LMS modules and integrations.

The original project scope also identifies developing a dedicated web server deployment and an Android application as future possibilities.

---

## 📈 Project Status

| Area                  | Status            |
| --------------------- | ----------------- |
| Project Foundation    | ✅ Completed       |
| Django Setup          | ✅ Completed       |
| Core Modules          | 🚧 In Development |
| Frontend Integration  | 🚧 In Development |
| Database Integration  | 🚧 In Development |
| Testing               | 🔄 Ongoing        |
| Additional Features   | 🔄 Ongoing        |
| Production Deployment | ⏳ Planned         |

---

## 👨‍💻 Developer

**Sandeep Kumar**

**B.Tech Computer Science (AI & ML)**
Python Full Stack Developer | Django Developer

### Technical Skills

```text
Python • Django • HTML5 • CSS3 • JavaScript
Bootstrap • MySQL/SQLite • Git • GitHub
```

---

## 📚 Project Type

**Major Project / Professional Training Project**

**Domain:** Education Technology / E-Learning

**Backend:** Python + Django

**Frontend:** HTML5 + CSS3 + JavaScript + Bootstrap

**Database:** SQLite3

**Development Environment:** Visual Studio Code

---

## 📄 License

This project is developed for **educational and professional training purposes**.

---

⭐ **If you find this project useful, consider giving the repository a star.**
