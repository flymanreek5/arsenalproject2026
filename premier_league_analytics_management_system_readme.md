# ⚽ Premier League Analytics & Management System (PL-AMS)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-2.4.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![React](https://img.shields.io/badge/react-18.2+-61DAFB.svg)

A full-stack sports analytics, fixture tracking, and league management platform built for the English Premier League. PL-AMS ingests real-time match telemetry, calculates advanced metrics (such as Expected Goals $xG$ and Expected Assists $xA$), and provides an interactive dashboard for fans, analysts, and fantasy managers.

---

## 📋 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#-api-endpoints)
- [Data Models & Metrics](#-data-models--metrics)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

* **Live Match Center:** Real-time scoreboards, match events (goals, cards, substitutions), and live commentary powered by WebSockets.
* **Dynamic League Table:** Automated standings updates calculating Points ($P$), Goal Difference ($GD$), Goals For ($GF$), Goals Against ($GA$), and form streaks.
* **Advanced Analytics Engine:** Deep-dive statistical breakdowns including:
  * Expected Goals ($xG$) & Expected Goals on Target ($xGOT$)
  * Progressive Passes & Carries
  * Shot Maps & Pitch Heatmaps
* **Player & Club Profiles:** Historical performance data, injury reports, transfer rumors, and contract details for all 20 Premier League clubs.
* **FPL (Fantasy Premier League) Assistant:** Form-vs-fixture difficulty ratings (FDR) and algorithmic captaincy/transfer recommendations.

---

## 🛠 Tech Stack

**Backend:**
* **Framework:** FastAPI (Python 3.11+)
* **Database:** PostgreSQL 15 (with TimescaleDB for time-series match events)
* **Caching & Pub/Sub:** Redis
* **Task Queue:** Celery (for scheduled data scraping and post-match aggregations)

**Frontend:**
* **Framework:** React 18 (TypeScript)
* **Styling:** Tailwind CSS
* **Data Visualization:** D3.js & Recharts (for pitch maps and statistical charts)

**DevOps & Infrastructure:**
* **Containerization:** Docker & Docker Compose
* **CI/CD:** GitHub Actions

---

## 🏗 System Architecture

```text
[External Sports Data APIs]
           │
           ▼
   [Celery Workers] ──► [Redis Cache / PubSub]
           │                      │
           ▼                      ▼
    [PostgreSQL DB] ◄────► [FastAPI Backend]
                                  │
                                  ▼
                         [React Web Client]
```

---

## 🚀 Getting Started

### Prerequisites
Ensure you have the following installed on your local machine:
* [Docker](https://docs.docker.com/get-docker/) & Docker Compose
* [Node.js](https://nodejs.org/) (v18+ for local frontend development)
* [Python](https://www.python.org/) (v3.11+ for local backend development)
* An API key from a supported football data provider (e.g., Football-Data.org, API-Football, or Sportmonks).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/premier-league-ams.git
   cd premier-league-ams
   ```

2. **Configure Environment Variables:**
   Copy the example environment file and add your API keys and database credentials.
   ```bash
   cp .env.example .env
   ```
   *Required variables in `.env`:*
   ```env
   DATABASE_URL=postgresql://pl_user:pl_password@db:5432/premier_league
   REDIS_URL=redis://redis:6379/0
   FOOTBALL_API_KEY=your_api_key_here
   SECRET_KEY=your_jwt_secret_key
   ```

3. **Spin up the containers:**
   ```bash
   docker-compose up --build -d
   ```

4. **Run database migrations & seed initial season data:**
   ```bash
   docker-compose exec backend alembic upgrade head
   docker-compose exec backend python scripts/seed_clubs_and_players.py
   ```

5. **Access the application:**
   * **Frontend Dashboard:** `http://localhost:3000`
   * **API Documentation (Swagger UI):** `http://localhost:8000/docs`

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/v1/standings` | Retrieve the current Premier League table. |
| `GET` | `/api/v1/fixtures` | Get fixtures filtered by gameweek, club, or date. |
| `GET` | `/api/v1/matches/{match_id}` | Detailed match stats, lineups, and $xG$ timeline. |
| `GET` | `/api/v1/players/{player_id}` | Player season totals, per-90 metrics, and heatmaps. |
| `WS` | `/ws/live-scores` | WebSocket stream for real-time match updates. |

---

## 📊 Data Models & Metrics

The analytics engine calculates custom efficiency metrics to evaluate team and player performance beyond basic box scores:

* **Goal Efficiency ($GE$):** Measures clinical finishing relative to chance quality:
  $$GE = \text{Goals Scored} - xG$$
* **Points Per Game ($PPG$):**
  $$PPG = \frac{\text{Total Points}}{\text{Matches Played}}$$

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/ExpectedThreatModel`).
3. Commit your changes (`git commit -m 'Add Expected Threat (xT) calculation'`).
4. Push to the branch (`git push origin feature/ExpectedThreatModel`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.