SELECT
  o.order_id,
  o.order_date,
  c.customer_id,
  c.first_name,
  c.last_name,
  p.product_name,
  p.category,
  oi.quantity,
  p.price,
  (oi.quantity * p.price) AS total_price
FROM {{ ref('stg_orders') }} o
JOIN {{ ref('stg_customers') }} c ON o.customer_id = c.customer_id
JOIN {{ ref('stg_order_items') }} oi ON o.order_id = oi.order_id
JOIN {{ ref('stg_products') }} p ON oi.product_id = p.product_id
