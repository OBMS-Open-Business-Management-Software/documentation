# Modules

## Introduction
Open Business Management Software (OBMS) is a free, open-source platform designed to meet diverse business automation needs. Its modular architecture allows for seamless integration of various functionalities, enabling businesses to tailor the software to their specific requirements. This document provides an overview of key modules available in OBMS, including payment gateways and product management tools.

---

## Installing Modules
OBMS modules can be installed easily using Composer, ensuring seamless integration into your system. Follow the steps below to install and manage modules within your OBMS instance.

### Prerequisites
Before installing a module, ensure that:
- You have a working OBMS installation.
- Composer is installed on your system.
- Your OBMS instance has the necessary permissions to install new packages.

### Installation Steps
Following these steps ensures a smooth installation and management process for OBMS modules. For more details, refer to the module’s official documentation.

1. **Find the Module**  
    Identify the module you want to install from the official OBMS repositories or Packagist. Each module has a unique package name that can be used for installation.

2. **Install via Composer**  
    Run the following command to install a module using Composer:  
    ```
    composer require obms/<module-name>
    ```

    For example, to install the PayPal Payment Gateway module, use:  
    ```
    composer require obms/paymentgateway-paypal
    ```

3. **Run Migrations (if required)**  
    Some modules may require database migrations. If specified in the module’s documentation, run:  
    ```
    php artisan migrate
    ```

4. **Enable the Module**  
    Depending on the module type, it may need to be activated within the OBMS admin panel or via the command line. Check the module documentation for specific activation instructions.

5. **Clear Cache**  
    After installation, clear your application cache to ensure the module loads correctly:  
    ```
    php artisan config:clear
    ```
    ```
    php artisan cache:clear
    ```

### Updating Modules
To update an installed module to the latest version, run:
```
composer update obms/<module-name>
```

For example:
```
composer update obms/paymentgateway-paypal
```

### Uninstalling Modules
If a module is no longer needed, you can remove it using Composer:
```
composer remove obms/<module-name>
```

Then, clear the cache again to finalize the removal:
```
php artisan config:clear
```
```
php artisan cache:clear
```

---

## Module Development
Developers can extend OBMS's functionality by creating custom modules. To facilitate this process, OBMS provides development tools and guidelines.

### Module SDK
The Module SDK offers a comprehensive set of tools and documentation for developing OBMS modules, such as products or payment gateways. It streamlines the development process and ensures compatibility with the OBMS core system. Developers can access the SDK and contribute to its improvement via the [GitHub repository](https://github.com/OBMS-Open-Business-Management-Software/module-sdk).

### Composer Installer
To manage module installations efficiently, OBMS utilizes a custom Composer Installer. This tool automates the installation and updating of modules, ensuring they are correctly integrated into the OBMS environment. The Composer Installer's source code and usage instructions are available on [GitHub](https://github.com/OBMS-Open-Business-Management-Software/composer-installer).

For more detailed information on module development and integration, developers are encouraged to consult the [OBMS Developer Documentation](/docs/developer_guide/intro).
