# Nginx — Load Balancing avec Docker

Un projet minimaliste pour apprendre les bases de **Nginx** en tant que **reverse proxy** et **load balancer**, orchestré avec **Docker Compose**.

## Architecture

```
                 ┌─────────────┐
  :8080    ───▶  │    Nginx    │
                 │  (port 80)  │
                 └──────┬──────┘
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
       ┌────────────┐     ┌────────────┐
       │  Backend 1 │     │  Backend 2 │
       │  (Python)  │     │  (Python)  │
       │  :8000     │     │  :8000     │
       └────────────┘     └────────────┘
```

Nginx distribue les requêtes en **round-robin** entre les deux backends Python.

## Stack

| Service    | Image / Langage    | Rôle                          |
| ---------- | ------------------ | ----------------------------- |
| `nginx`    | `nginx:latest`     | Reverse proxy & load balancer |
| `backend1` | `python:3.12-slim` | Serveur HTTP simple           |
| `backend2` | `python:3.12-slim` | Serveur HTTP simple           |

## Lancer le projet

```bash
docker compose up --build
```

Puis tester le load balancing :

```bash
curl http://localhost:8080
# → Backend Python 1

curl http://localhost:8080
# → Backend Python 2
```

Chaque requête est redirigée alternativement vers un backend différent.

## Structure du projet

```
.
├── compose.yaml              # Orchestration des services
├── nginx.conf                # Configuration Nginx (upstream + proxy_pass)
└── backend/
    ├── dockerfile            # Image Python pour les backends
    ├── server_1/server.py    # Serveur HTTP → "Backend Python 1"
    └── server_2/server.py    # Serveur HTTP → "Backend Python 2"
```

## Concepts abordés

- **Reverse proxy** — Nginx reçoit les requêtes et les transmet aux backends
- **Load balancing (round-robin)** — Répartition automatique de la charge
- **Docker Compose** — Orchestration multi-conteneurs
- **Volumes en lecture seule (`:ro`)** — Montage sécurisé de la config Nginx
