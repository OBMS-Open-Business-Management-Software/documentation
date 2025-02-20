# Docker Installation

## Introduction
This guide will walk you through setting up and running the application in a Dockerized environment, ensuring a consistent and reproducible deployment process.

Using Docker, you can easily package all dependencies and configurations into a container, eliminating compatibility issues and simplifying deployment across different environments. Whether you are running the application on a local machine, staging server, or production environment, Docker provides an efficient and scalable solution.

---

## Step-by-Step (Development)
This will create containers referencing the local version of the application. **Do not use in production**, as it may lead to instability or unintended changes. Always use properly built and tested images for deployment.

### Clone Repository
Clone the GIT repository of the OBMS core application to the machine.
```bash
git clone https://github.com/OBMS-Open-Business-Management-Software/core.git
```

### Install Dependencies
Install the Composer dependencies.
```bash
composer install
```

Install the NodeJS package dependencies.
```bash
npm install
```

### Configure Environment
Copy and modify the environment variables.

```bash
cp .env.example .env
```

> **NOTE:** If needed, an external database and redis cache connection can be provided. By default the Laravel Sail containers will be used.

### Start the Containers
Start the docker containers.
```bash
./vendor/bin/sail up -d
```

### Generate the Application Key
Generate an application key.
```bash
./vendor/bin/sail artisan key:generate
```

### Migrate Database
Migrate the database schema.
```bash
./vendor/bin/sail artisan migrate
```

---

## Step-by-Step (Production)
This will build and deploy stable, production-ready Docker images. Ensure that all images have been thoroughly tested and validated before deployment. Only use properly built and verified images in a production environment to guarantee stability, security, and performance. Using untested or improperly configured containers in production can lead to unexpected behavior, downtime, and potential security vulnerabilities. Always follow best practices for Docker image creation, versioning, and deployment when working in production.

### Clone Repository
Clone the GIT repository of the OBMS core application to the machine.
```bash
git clone https://github.com/OBMS-Open-Business-Management-Software/core.git
```

### Install Dependencies
Install the Composer dependencies.
```bash
composer install
```

Install the NodeJS package dependencies.
```bash
npm install
```

### Configure Environment
Copy and modify the environment variables.

```bash
cp .env.example .env
```
> **NOTE:** If needed, an external database and redis cache connection can be provided. By default the bundled containers will be used.

### Start the Containers
Start the docker containers.
```bash
docker-compose -f docker-compose.production.yml up -d
```

### Generate the Application Key
Generate an application key.
```bash
docker-compose -f docker-compose.production.yml exec app php artisan key:generate
```

### Migrate Database
Migrate the database schema.
```bash
docker-compose -f docker-compose.production.yml exec app php artisan migrate
```