SELECT 
  c.login,
  COUNT(o.id) AS "ordersInDelivery"
FROM "Couriers" c
LEFT JOIN "Orders" o ON c.id = o."courierId" AND o."inDelivery" = true
GROUP BY c.login
ORDER BY "ordersInDelivery" DESC;