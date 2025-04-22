SELECT
  order_id,
  customer_id,
  order_date
FROM {{ ref('orders') }}
