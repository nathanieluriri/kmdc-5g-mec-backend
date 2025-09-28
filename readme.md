

# KMDC Private 5G & MEC Mining Operations Platform – Backend

## Overview

This backend powers the **Kaduna Mining Development Company (KMDC) Private 5G and Multi-access Edge Computing (MEC) Mining Operations Platform**.
It provides secure APIs, real-time data streams, and predictive analytics for worker safety, equipment monitoring, and operational efficiency across KMDC’s mining sites.

Core functions include:

* Private 5G network & MEC node management
* IoT sensor data ingestion & processing
* Safety alerts and worker health monitoring
* Remote control sessions for heavy equipment
* Predictive maintenance and work order management
* Network KPI and satellite backhaul monitoring

---

## Key Features

| Feature                      | Description                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------ |
| **Real-Time Monitoring**     | GPS tracking of vehicles and workers, vitals monitoring, environmental sensors |
| **Remote Equipment Control** | Ultra-low latency (<20 ms) control sessions with live video feeds              |
| **Predictive Maintenance**   | ML-powered failure predictions and automated work orders                       |
| **Safety Management**        | Automated alerts with 5-second delivery guarantees                             |
| **Secure Access**            | OAuth 2.0 with role-based access control (RBAC)                                |
| **Network KPIs**             | Private 5G/MEC and satellite performance metrics                               |

---

## Repository Structure

```
kmdc-5g-mec-backend/
├── .github/                 # GitHub-specific configs
│   └── workflows/           # CI/CD workflows (build, test, deploy)
├── api/                     # API routes
│   └── v1/                  # Version 1 REST endpoints
├── core/                    # Core application logic & utilities
├── email_templates/         # Predefined email templates for notifications
├── repositories/            # Data access layer (DB CRUD operations)
├── schemas/                 # Pydantic schemas / request-response models
├── services/                # Business logic services used by endpoints
├── security/                # Auth, permissions, and security utilities
├── tests/                   # Unit and integration tests
├── .env                     # Environment variables (local dev)
├── .gitignore               # Git ignore file
├── deploy.sh                # Deployment script
├── docker-compose.yml       # Local Docker stack
├── Dockerfile               # Container build instructions
├── main.py                  # App entry point
├── readme.md                # Project README
├── requirements.txt         # Python dependencies
└── seed.py                  # Data seeding script (initial data population)

```

---

## Getting Started

### Prerequisites

* **Docker & Docker Compose** (local dev)
* **Python 3.9+**
* Access credentials for 5G equipment and MEC nodes

### Local Development

1. Clone this repository:

   ```bash
   git clone https://github.com/kmdc/kmdc-5g-mec-backend.git
   cd kmdc-5g-mec-backend
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt (Optional as it will still be installed with commands written from docker)
  
   ```
3. Copy environment variables:

   ```bash
   cp .env.example .env
   ```
4. Start services:

   ```bash

   docker compose up -d --build

   ```
5. Access the local API:

   ```
   http://localhost:8000/api/v1
   ```
6. API docs (Swagger/OpenAPI):

   ```
   http://localhost:8000/docs
   ```


---

## Authentication & Authorization

* **OAuth 2.0 Bearer Tokens**
  Every request must include:

  ```
  Authorization: Bearer <access_token>
  ```

* Obtain token:

  ```http
  POST /api/v1/auth/token
  Content-Type: application/json

  {
    "username": "operator@kdmc.com",
    "password": "secure_password",
    "grant_type": "password"
  }
  ```

* Roles & permissions:

  | Role             | Scope                                                  |
  | ---------------- | ------------------------------------------------------ |
  | Remote Engineer  | Full system access incl. remote control, video feeds   |
  | Safety Officer   | Sensor monitoring, worker tracking, incident reporting |
  | Maintenance Tech | Equipment health, predictive maintenance               |
  | Operator Viewer  | Read-only dashboards                                   |

---

## Base URLs

| Environment    | URL                               |
| -------------- | --------------------------------- |
| Production API | `https://api.kdmc.mining.local`   |
| Edge MEC API   | `https://edge.kdmc.mining.local`  |
| WebSocket      | `wss://kdmc.mining.local/ws`      |
| Video CDN      | `https://video.kdmc.mining.local` |

Standard Request headers:



| Header         | Example Value      | Description                                                         |
| -------------- | ------------------ | ------------------------------------------------------------------- |
| `Content-Type` | `application/json` | Specifies the media type of the request body (JSON payload).        |
| `Accept`       | `application/json` | Tells the server which response formats are acceptable (JSON here). |



Standard Response Headers:


| Header                  | Example Value                   | Description                                                        |
| ----------------------- | ------------------------------- | ------------------------------------------------------------------ |
| `Connection`            | `keep-alive`                    | Indicates that the server will keep the connection open for reuse. |
| `Content-Length`        | `58`                            | Size of the response body in bytes.                                |
| `Content-Type`          | `application/json`              | MIME type of the response content.                                 |
| `Date`                  | `Sun, 28 Sep 2025 22:51:15 GMT` | Date and time when the response was sent.                          |
| `Server`                | `nginx/1.26.3 (Ubuntu)`         | Web server software handling the request.                          |
| `X-Process-Time`        | `0.005338191986083984`          | Time taken by the backend to process the request (in seconds).     |
| `X-RateLimit-Limit`     | `60`                            | Maximum requests allowed per time window.                          |
| `X-RateLimit-Remaining` | `59`                            | Remaining requests in the current time window.                     |
| `X-RateLimit-Reset`     | `60`                            | Time in seconds until the rate limit resets.                       |
| `X-User-Id`             | `68d9bbd1c193e004331fd882`      | Authenticated user’s ID for this request.                          |
| `X-User-Type`           | `member/admin/annonymous`                        | Role or type of the authenticated user.                            |


---

## Core API Endpoints (Examples)

### Asset Management

* **Vehicles:** `GET /api/v1/assets/vehicles`
* **Equipment Status:** `GET /api/v1/assets/equipment/{equipment_id}`
* **Container Tracking:** `GET /api/v1/assets/containers/track`

### Safety & Environment

* **Worker Locations & Vitals:** `GET /api/v1/safety/workers`
* **Environmental Sensors:** `GET /api/v1/safety/environmental/sensors`
* **Create Safety Alert:** `POST /api/v1/safety/alerts`

### Remote Control

* **Initiate Session:** `POST /api/v1/remote-control/sessions`
* **Send Command:** `POST /api/v1/remote-control/sessions/{session_id}/commands`

### Predictive Maintenance

* **Analyze Equipment:** `POST /api/v1/predictive/equipment/analyze`
* **Create Work Order:** `POST /api/v1/maintenance/work-orders`

### Network Monitoring

* **Network KPIs:** `GET /api/v1/network/kpis`
* **Satellite Status:** `GET /api/v1/network/satellite/status`

---

## WebSocket Streams

| Stream        | URL                                    | Purpose                      |
| ------------- | -------------------------------------- | ---------------------------- |
| **Sensors**   | `wss://kdmc.mining.local/ws/sensors`   | Real-time IoT sensor updates |
| **Alerts**    | `wss://kdmc.mining.local/ws/alerts`    | Critical safety alerts       |
| **Telemetry** | `wss://kdmc.mining.local/ws/telemetry` | Equipment telemetry          |

Authenticate immediately after connecting:

```json
{ "type": "auth", "token": "Bearer eyJhbGciOiJSUzI1NiIs..." }
```

---

## Data Models

### **Common Response Envelope**

All API responses (success or error) follow the same envelope:

```json
{
  "status_code": <HTTP status code>,
  "data": { /* payload or null on error */ },
  "detail": <additional detail about the request/response>
}
```

**Example (404 Not Found):**

```json
{
  "status_code": 404,
  "data": null,
  "detail": "Agent not found"
}
```

**Common Response Headers:**

| Header                  | Example Value                   | Description                                                        |
| ----------------------- | ------------------------------- | ------------------------------------------------------------------ |
| `Connection`            | `keep-alive`                    | Indicates that the server will keep the connection open for reuse. |
| `Content-Length`        | `58`                            | Size of the response body in bytes.                                |
| `Content-Type`          | `application/json`              | MIME type of the response content.                                 |
| `Date`                  | `Sun, 28 Sep 2025 22:51:15 GMT` | Date and time when the response was sent.                          |
| `Server`                | `nginx/1.26.3 (Ubuntu)`         | Web server software handling the request.                          |
| `X-Process-Time`        | `0.005338191986083984`          | Time taken by the backend to process the request (in seconds).     |
| `X-RateLimit-Limit`     | `60`                            | Maximum requests allowed per time window.                          |
| `X-RateLimit-Remaining` | `59`                            | Remaining requests in the current time window.                     |
| `X-RateLimit-Reset`     | `60`                            | Time in seconds until the rate limit resets.                       |
| `X-User-Id`             | `68d9bbd1c193e004331fd882`      | Authenticated user’s ID for this request.                          |
| `X-User-Type`           | `member`                        | Role or type of the authenticated user.                            |


* **Location Object**:

  ```json
  {
    "coordinates": { "lat": -1.234567, "lng": 36.123456, "altitude_m": 1589.5, "accuracy_m": 1.0 },
    "zone": "pit-north-2",
    "level": "surface"
  }
  ```

* **Alert Severity Levels**: Critical (<5 s), High (<30 s), Medium (<5 min), Low (<30 min)

---

## Error Handling & Rate Limits


### **Standard Error**

```json
{
  "status_code": 404,
  "data": null,
  "detail": "Equipment not found"
}
```

Common codes: `400 INVALID_REQUEST`, `401 UNAUTHORIZED`, `403 FORBIDDEN`, `404 RESOURCE_NOT_FOUND`, `429 RATE_LIMIT_EXCEEDED`, `500 INTERNAL_ERROR`

Rate limit headers:

X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 950


---

## Contributing

1. Fork & branch (`feature/my-change`)
2. Implement changes + tests
3. Open pull request

---

## License

This backend is proprietary to **Kaduna Mining Development Company (KMDC)**.
All rights reserved.

---

### TL;DR

This backend is the real-time nerve center of KMDC’s mining operations: it connects sensors, workers, and equipment over Private 5G + MEC, and exposes secure APIs for monitoring, control, and predictive analytics.

