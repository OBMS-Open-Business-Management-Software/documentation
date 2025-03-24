# Kubernetes Installation

## Introduction
If you want to deploy OBMS on Kubernetes, you can easily integrate it using the [public Docker images](/docs/getting-started/installation/docker/#available-docker-images) along with the Laravel Helm Chart. This allows you to leverage Kubernetes’ scalability and management features while using the OBMS Docker images (`ghcr.io/obms-open-business-management-software/core-app` and `ghcr.io/obms-open-business-management-software/core-worker`). Below are the steps to deploy OBMS on Kubernetes using Helm.

---

## Step-by-Step

### Create the Environment Secret
Begin by creating a `secret.yaml` file to specify the contents of the `.env` file within the new containers:

```yaml
---
kind: Secret
apiVersion: v1
metadata:
  name: obms-env-secret
stringData:
  .env: |
    APP_NAME=OBMS
    APP_THEME=aurora
    APP_ENV=production
    APP_KEY=
    APP_DEBUG=false
    APP_URL=http://localhost

    LOG_CHANNEL=stack
    LOG_DEPRECATIONS_CHANNEL=null
    LOG_LEVEL=debug

    DB_CONNECTION=mysql
    DB_HOST=mysql
    DB_PORT=3306
    DB_DATABASE=laravel
    DB_USERNAME=sail
    DB_PASSWORD=password

    BROADCAST_DRIVER=log
    CACHE_DRIVER=file
    FILESYSTEM_DRIVER=local
    QUEUE_CONNECTION=sync
    SESSION_DRIVER=file
    SESSION_LIFETIME=120

    MEMCACHED_HOST=127.0.0.1

    REDIS_HOST=redis
    REDIS_PASSWORD=null
    REDIS_PORT=6379

    MAIL_MAILER=smtp
    MAIL_HOST=mailhog
    MAIL_PORT=1025
    MAIL_USERNAME=null
    MAIL_PASSWORD=null
    MAIL_ENCRYPTION=null
    MAIL_FROM_ADDRESS=null
    MAIL_FROM_NAME="${APP_NAME}"
    MAIL_SUPPORT_ADDRESS=hi@obms.one
    MAIL_SUPPORT_NAME=Test

    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    AWS_DEFAULT_REGION=us-east-1
    AWS_BUCKET=
    AWS_USE_PATH_STYLE_ENDPOINT=false

    PUSHER_APP_ID=
    PUSHER_APP_KEY=
    PUSHER_APP_SECRET=
    PUSHER_APP_CLUSTER=mt1

    MIX_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
    MIX_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"
```

Note that you are required to at least modify the parameters for the `DB`, `REDIS` and `MAIL` connections. Also, we advise to set an `APP_KEY` and modify the `APP_URL` to ensure proper data encryption and user redirects. If you want to generate an `APP_KEY` using a `bash` command you can do so by utilizing the `openssl` utility:
```bash
echo "APP_KEY=base64:$(openssl rand -base64 32)"
```

These values will be used to configure the main instance of the application. Some may be overridden by the dynamic parameterization utility of OBMS. After modifying the file accordingly, run the following command to publish the new secret to the Kubernetes cluster:
```bash
kubectl apply -f secret.yaml
```

### Add the Helm Chart Repository
Continue by adding the [Laravel Helm Chart](https://github.com/renoki-co/charts) repository to your Helm setup:
```bash
helm repo add renoki-co https://renoki.co/charts
```
```bash
helm repo update
```

### Configure the values-*.yaml Files
Create a `values-app.yaml` and `values-worker.yaml` file to specify the OBMS Docker images for the Laravel Helm chart. You need to define both the main application image (`ghcr.io/obms-open-business-management-software/core-app`) and the worker image (`ghcr.io/obms-open-business-management-software/core-worker`). Here's an example app configuration:
```yaml
app:
  image:
    repository: ghcr.io/obms-open-business-management-software/core-app
    pullPolicy: Always
    tag: latest
  envSecretName: obms-env-secret
```

For the worker an additional modification of the start command is needed. Here's an example worker configuration:
```yaml
app:
  image:
    repository: ghcr.io/obms-open-business-management-software/core-worker
    pullPolicy: Always
    tag: latest
  command: php artisan horizon
  envSecretName: obms-env-secret
```

These YAML files specify that both the app and worker containers will use the `latest` tags for the images. You can adjust the tag field if you need to use a specific version.

### Deploy Using Helm
Now, use the Helm chart to deploy OBMS on Kubernetes. Run the following command to install the Laravel chart with your custom `values-*.yaml` configuration:
```bash
helm install obms renoki-co/laravel -f values-app.yaml
```
```bash
helm install obms renoki-co/laravel-worker -f values-worker.yaml
```

This will deploy OBMS using the Docker images specified in the `values-*.yaml` file. It will configure the necessary Kubernetes resources like deployments, services, and persistent volumes.

### Generate the Application Key
Generate an application key.
```bash
kubectl exec -it laravel -- php artisan key:generate
```

### Migrate Database
Migrate the database schema.
```bash
kubectl exec -it laravel -- php artisan migrate --no-interaction --force
```

### Generate OAUTH Clients
Generate set of OAUTH clients needed for API authentication.
```bash
kubectl exec -it laravel -- php artisan passport:install --no-interaction
```

### Accessing the Application
Once deployed, you can access the application based on how your Kubernetes cluster is configured. This may include exposing the application via a load balancer or using `kubectl port-forward` for local access. 

For a detailed overview of the available Helm chart options please consult the respective [documentation](https://github.com/renoki-co/charts/blob/master/charts/laravel/values.yaml).