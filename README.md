# Python Client-Server with Sockets

This project is an implementation of client-server communication using sockets in Python. The main goal is to deepen understanding of fundamental networking concepts and their practical application in software environments.

## Project Purpose

As part of my self-taught learning in networks, infrastructure, and programming, I built this tool to better understand how network connections are managed, how concurrency is handled, and how data is serialized in real time.

## Technical Features
  - Real-Time Communication: TCP sockets for message exchange between multiple clients and a central server.
  - Concurrency Handling: The server uses the threading library to manage multiple simultaneous connections asynchronously.
  - Basic Security: Includes a simple access control list (ACL) to block specific IP addresses.
  - Data Serialization: Structured data exchange using JSON format.
  - Logging System: Detailed event and message logging to separate files (server.log and client.log) for both client and server.
  - Containerization: The server is ready to be deployed with Docker, improving portability.

## Repository Structure
  - server.py: Server logic that listens for incoming connections and manages a thread per client.
  - client.py: Terminal interface for users to send messages to the server.
  - Dockerfile: Configuration to package the server application.
  - .gitignore: Configuration to prevent log files (.log) from being committed.

## Usage Instructions
### Local Run
  1. Start the server:
  ```bash
  python server.py
  ```
  2. Start one or more clients:
  ```bash
  python client.py
  ```

### Run with Docker

If you prefer containers, you can build and run the server image:

```bash
docker build -t python-server .
docker run -p 5500:5500 python-server
```

## Next Improvements (Roadmap)
  - SSL/TLS Encryption: Add a security layer so messages do not travel in plain text.
  - Database Persistence: Store message history in a database instead of only text files.
  - CI/CD Pipeline: Set up a GitHub Actions workflow to validate the code and build the Docker image automatically.
  - User Interface: Build a small GUI or web app for the client.
  - Environment Variables: Manage settings like host and port via .env files.