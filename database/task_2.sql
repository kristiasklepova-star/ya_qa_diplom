SELECT 
  track,
  CASE
    WHEN finished = true THEN 2
    WHEN cancelled = true THEN -1
    WHEN "inDelivery" = true THEN 1
    ELSE 0
  END AS status
FROM "Orders"
ORDER BY track;
/* В случае если для тестирования требуется полноценная проверка статусов и подробный вывод всех значений можно использовать следующий запрос:
SELECT 
  track,
  finished,
  cancelled,
  "inDelivery",
  CASE
    WHEN finished = true THEN 2
    WHEN cancelled = true THEN -1
    WHEN "inDelivery" = true THEN 1
    ELSE 0
  END AS status,
  CASE
    WHEN finished = true THEN 'Завершен'
    WHEN cancelled = true THEN 'Отменен'
    WHEN "inDelivery" = true THEN 'В доставке'
    ELSE 'Новый'
  END AS status_name
FROM "Orders"
ORDER BY track;
*/