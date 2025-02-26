# Docker Installation

## Introduction
This guide will walk you through setting up and running the application in a Dockerized environment, ensuring a consistent and reproducible deployment process.

Using Docker, you can easily package all dependencies and configurations into a container, eliminating compatibility issues and simplifying deployment across different environments. Whether you are running the application on a local machine, staging server, or production environment, Docker provides an efficient and scalable solution.

---

## Available Docker Images

OBMS provides two public Docker images for running the application. These images are tailored for different tasks, making it easy to deploy both the core application and background processes efficiently. The `app` image is used for handling web requests, while the `worker` image is designed for background processing tasks.

| Image Name  | Purpose                           |
|-------------|-----------------------------------|
| `ghcr.io/obms-open-business-management-software/core-app`  | The main application container, handling web requests. |
| `ghcr.io/obms-open-business-management-software/core-worker` | The worker container for processing background jobs. |

By default, the `latest` tag should be used for both the `obms-open-business-management-software/core-app` and `obms-open-business-management-software/core-worker` images to ensure you’re always using the most recent version. If you require an older version, you can access previous releases by specifying their semantic version tags (e.g., `obms-open-business-management-software:v1.8.2`).

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

### Generate the Application Keys
Generate an encryption key.
```bash
./vendor/bin/sail artisan key:generate
```

Generate a keypair for Laravel Passport (needed for OAUTH clients to work).
```bash
./vendor/bin/sail artisan passport:keys
```
> **NOTE:** The keypair for Laravel Passport can be set per instance by overriding the parameters `passport.private_key` and `passport.public_key` within the admin UI.

### Migrate Database
Migrate the database schema.
```bash
./vendor/bin/sail artisan migrate --no-interaction --force
```

### Generate OAUTH Clients
Generate set of OAUTH clients needed for API authentication.
```bash
./vendor/bin/sail artisan passport:install --no-interaction
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

This will build the containers from the local Dockerfile. However, if you prefer to use the public images instead, you can modify the `docker-compose.production.yml` file to reference the appropriate image tags (e.g., `obms-open-business-management-software/core-app:latest` or a specific version).

### Generate the Application Key
Generate an application key.
```bash
docker-compose -f docker-compose.production.yml exec app php artisan key:generate
```

### Migrate Database
Migrate the database schema.
```bash
docker-compose -f docker-compose.production.yml exec app php artisan migrate --no-interaction --force
```

### Generate OAUTH Clients
Generate set of OAUTH clients needed for API authentication.
```bash
docker-compose -f docker-compose.production.yml exec app php artisan passport:install --no-interaction
```