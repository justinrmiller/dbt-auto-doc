# DBT Project Summary Document

## 1. Overview of the DBT Structure

This DBT project is organized into three main components: **staging models**, **marts**, and **seeds**. 

- **Staging Models**: These models are responsible for transforming raw data from source tables into a more refined format, which is then used by the mart models.
- **Marts**: These models aggregate and join data from the staging models to create fact tables that are used for analysis and reporting.
- **Seeds**: These are static CSV files that are loaded into the database and used as source tables for the staging models.

## 2. Description of Each Seed File

- **customers.csv**: Contains customer information with fields such as `customer_id`, `first_name`, `last_name`, and `email`.
- **order_items.csv**: Contains details of each order item, including `order_item_id`, `order_id`, `product_id`, and `quantity`.
- **orders.csv**: Contains order information with fields like `order_id`, `customer_id`, and `order_date`.
- **products.csv**: Contains product details, including `product_id`, `product_name`, `category`, and `price`.

## 3. Table Summarizing Staging Models

| Staging Model     | Source Table | Key Fields Extracted                |
|-------------------|--------------|-------------------------------------|
| `stg_customers`   | `customers`  | `customer_id`, `first_name`, `last_name`, `email` |
| `stg_order_items` | `order_items`| `order_item_id`, `order_id`, `product_id`, `quantity` |
| `stg_orders`      | `orders`     | `order_id`, `customer_id`, `order_date` |
| `stg_products`    | `products`   | `product_id`, `product_name`, `category`, `price` |

## 4. Description of Each Mart Model

- **fact_orders.sql**: This mart model aggregates data from the staging models to create a comprehensive fact table for orders. It performs the following joins:
  - Joins `stg_orders` with `stg_customers` on `customer_id`.
  - Joins `stg_orders` with `stg_order_items` on `order_id`.
  - Joins `stg_order_items` with `stg_products` on `product_id`.
  
  The model also calculates a new field `total_price` as the product of `quantity` and `price`.

## 5. Data Lineage Diagram

```
customers.csv --> stg_customers
order_items.csv --> stg_order_items
orders.csv --> stg_orders
products.csv --> stg_products

stg_customers
    |
    +--> fact_orders
stg_order_items
    |
    +--> fact_orders
stg_orders
    |
    +--> fact_orders
stg_products
    |
    +--> fact_orders
```

## 6. Conclusion

This DBT setup demonstrates several good practices in data engineering:

- **Modular Design**: The separation of staging and mart models allows for clear data transformation steps and easier maintenance.
- **Reusability**: Staging models are designed to be reusable, providing a clean and consistent interface for downstream models.
- **Calculated Fields**: The use of calculated fields in the mart models, such as `total_price`, adds value by providing ready-to-use metrics for analysis.

Overall, this DBT project is well-structured, making it both scalable and easy to understand for both technical and business stakeholders.