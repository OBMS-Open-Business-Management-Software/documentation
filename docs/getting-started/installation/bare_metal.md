# Bare-Metal Installation

## Introduction
This method involves setting up OBMS directly on your server.

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

Generate an application key.
```bash
php artisan key:generate
```

### Migrate Database
Migrate the database schema.
```bash
php artisan migrate
```

### Deploy Workers
Please visit the [Laravel Horizon Documentation](https://laravel.com/docs/11.x/horizon#deploying-horizon) for an extensive guide on how to deploy Laravel Horizon to a server.