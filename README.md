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

##  Project Setup

Follow these steps to set up and run the service locally:

1️ **Clone the repository:**
```bash
git clone <your-repo-url>
cd scheduler_service

2. python -m venv venv
3. venv\Scripts\activate
4. pip install -r requirements.txt
5. uvicorn app.main:app --reload


## Scalability Overview (One-Pager)
This microservice is designed to scale horizontally and handle high workloads:

1️ Horizontal Scaling
Deploy multiple FastAPI instances behind a load balancer (e.g., NGINX, AWS ALB).

Each instance is stateless and can serve any request.

2️ Centralized Database
Migrate from SQLite to PostgreSQL/MySQL for concurrency.

Use connection pooling for efficient DB access.

Optionally add read replicas to distribute read load.

3️ Distributed Job Scheduling
Use APScheduler’s SQLAlchemyJobStore for shared scheduling state.

Alternatively, integrate Celery with Redis/RabbitMQ to distribute job execution across workers.

4️ API Rate Limiting and Security
Protect APIs with API key or JWT authentication.

Enforce rate limits per client.

Serve over HTTPS in production.

5️ Observability
Integrate structured logging (Loguru) and monitoring (Prometheus + Grafana).

Use centralized log aggregation for traceability.

6️ Containerization and Deployment
Package as Docker containers.

Orchestrate with Kubernetes for auto-scaling and failover.

🛡 API Management
Interactive Docs: FastAPI generates OpenAPI schema and Swagger UI at /docs.

Client SDKs: OpenAPI spec can be used to auto-generate client libraries.

Validation: All input data is validated using Pydantic.

Error Handling: Consistent JSON error responses with clear messages.
