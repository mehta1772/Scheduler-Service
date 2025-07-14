# Scheduler Microservice

A production-grade microservice for scheduling jobs with configurable intervals and persistence. This service provides RESTful APIs for job creation, retrieval, and listing.

---

##  Features

 **Job Scheduling:**  
Create jobs with cron-like schedules (e.g., every Monday at 9 AM).

 **API Endpoints:**
- `POST /jobs` – Create a new job.
- `GET /jobs` – List all jobs.
- `GET /jobs/{id}` – Retrieve job details.

 **Persistence:**
- Jobs stored in a relational database (SQLite for demonstration, easily replaceable with PostgreSQL/MySQL).

 **Background Execution:**
- Jobs run automatically using APScheduler.

 **Interactive API Documentation:**
- Swagger UI available at `/docs`.

---

## 🚀 Project Setup

Follow these steps to set up and run the service locally:

1️⃣ **Clone the repository:**
```bash
git clone <your-repo-url>
cd scheduler_service
