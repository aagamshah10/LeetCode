SELECT sign.user_id, ROUND(AVG(if (confirm.action="confirmed",1,0)),2) as confirmation_rate
FROM Signups sign
LEFT JOIN Confirmations confirm
ON sign.user_id=confirm.user_id
GROUP BY user_id
