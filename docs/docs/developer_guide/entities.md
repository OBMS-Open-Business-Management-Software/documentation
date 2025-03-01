# Entities

## Introduction  
This section provides an overview of the relationships and structure within the OBMS database. 

---

## Entity Relationship Diagram
The Entity Relationship Diagram (ERD) is an essential tool for understanding how data is organized and interconnected within the system. This diagram helps developers, administrators, and other stakeholders visualize the core entities and their relationships to ensure efficient data management.

Below is the Entity Relationship Diagram for OBMS, showing the primary entities and their connections within the system.

![ERD Diagram](https://api.getobms.com/erd-latest.svg)

---

## Download
You can download the ERD diagram for offline use by clicking one of the links below:

<a href="https://api.getobms.com/erd-latest.svg" target="_blank" download>Download ERD Diagram (SVG)</a><br />
<a href="https://api.getobms.com/erd-latest.pdf" target="_blank" download>Download ERD Diagram (PDF)</a>

---

## Regenerating the ERD Diagram  

To regenerate the Entity Relationship Diagram (ERD) for OBMS, you can use the `generate:erd` Artisan command. This command will automatically generate the ERD based on your current database schema.

```bash
php artisan generate:erd
```

For more details on customizing the generation process or to explore additional options, refer to the [Laravel ER Diagram Generator documentation](https://github.com/beyondcode/laravel-er-diagram-generator).