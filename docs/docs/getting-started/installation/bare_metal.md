# Bare-Metal Installation

## Introduction
This guide will walk you through setting up the application directly on your machine, without containerization, ensuring full control over the environment and resource allocation.

Running on bare metal allows for direct hardware access, optimized performance, and customization tailored to your infrastructure needs. This method is ideal for scenarios where virtualization overhead must be minimized or when deploying on dedicated hardware.

---

## Step-by-Step
### Clone Repository
Clone the GIT repository of the OBMS core application to the machine.
```bash
git clone https://github.com/OBMS-Open-Business-Management-Software/core.git
```

### Configure Webserver
Please visit the [Laravel Documentation](https://laravel.com/docs/11.x/deployment) for an extensive guide on how to deploy Laravel applications to a webserver.

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
Copy and modify the environment variables. A valid database and redis cache connection need to be provided.
```bash
cp .env.example .env
```

### Generate the Application Keys
Generate an encryption key.
```bash
php artisan key:generate
```

Generate a keypair for Laravel Passport (needed for OAUTH clients to work).
```bash
php artisan passport:keys
```
> **NOTE:** The keypair for Laravel Passport can be set per instance by overriding the parameters `passport.private_key` and `passport.public_key` within the admin UI.

### Migrate Database
Migrate the database schema.
```bash
php artisan migrate --no-interaction --force
```

### Generate OAUTH Clients
Generate set of OAUTH clients needed for API authentication.
```bash
php artisan passport:install --no-interaction
```

### Deploy Workers
Please visit the [Laravel Horizon Documentation](https://laravel.com/docs/11.x/horizon#deploying-horizon) for an extensive guide on how to deploy Laravel Horizon to a server.