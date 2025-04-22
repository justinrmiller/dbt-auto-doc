# DBT Project Summary Document

## Overview

This document provides a comprehensive summary of the DBT setup for the project, which is organized into three main components: **staging models**, **marts**, and **seeds**. The staging models are responsible for transforming raw data into a more usable format, the marts consolidate and enrich this data for analytical purposes, and the seeds provide static data inputs.

## Seed Files Description

1. **customers.csv**: Contains customer information with fields such as `customer_id`, `first_name`, `last_name`, and `email`. This data is used to identify and describe customers in the system.

2. **order_items.csv**: Details each item within an order, including `order_item_id`, `order_id`, `product_id`, and `quantity`. This data is crucial for understanding the composition of each order.

3. **orders.csv**: Provides order-level data with fields like `order_id`, `customer_id`, and `order_date`. This seed is used to track orders placed by customers.

4. **products.csv**: Contains product information, including `product_id`, `product_name`, `category`, and `price`. This data helps in identifying products and their attributes.

## Staging Models Summary

| Staging Model     | Source Table | Key Fields Extracted                |
|-------------------|--------------|-------------------------------------|
| stg_customers     | customers    | customer_id, first_name, last_name, email |
| stg_order_items   | order_items  | order_item_id, order_id, product_id, quantity |
| stg_orders        | orders       | order_id, customer_id, order_date   |
| stg_products      | products     | product_id, product_name, category, price |

## Mart Models Description

### fact_orders.sql

The `fact_orders` model aggregates data from various staging models to provide a comprehensive view of orders. It performs the following joins:

- **Join with `stg_orders`**: To get order-level details such as `order_id` and `order_date`.
- **Join with `stg_customers`**: To associate each order with customer details like `customer_id`, `first_name`, and `last_name`.
- **Join with `stg_order_items`**: To include item-level details such as `quantity`.
- **Join with `stg_products`**: To enrich the data with product information like `product_name`, `category`, and `price`.

**Calculated Fields**:
- `total_price`: Calculated as the product of `quantity` and `price` for each order item.

## Data Lineage Diagram

```
customers.csv --> stg_customers
order_items.csv --> stg_order_items
orders.csv --> stg_orders
products.csv --> stg_products

stg_customers --> fact_orders
stg_order_items --> fact_orders
stg_orders --> fact_orders
stg_products --> fact_orders
```

## Conclusion

The DBT setup is well-structured, with a clear separation between staging and mart layers, which enhances data transformation and analysis. The use of seed files for static data inputs is a good practice, ensuring that reference data is easily maintainable and version-controlled. The calculated fields in the mart models provide valuable insights, such as the `total_price` in `fact_orders`, which is crucial for business analysis. Overall, the architecture is robust and follows best practices for data modeling and transformation.