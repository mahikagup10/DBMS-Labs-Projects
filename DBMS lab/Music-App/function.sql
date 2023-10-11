DELIMITER $$ 
CREATE FUNCTION checkSubscription(userID INTEGER) 
RETURNS varchar(20) 
DETERMINISTIC 
BEGIN 
DECLARE curr_date DATE;
DECLARE u_date DATE;
DECLARE msg varchar(20);
DECLARE c INTEGER;
DECLARE days INTEGER;
SET days = 365;
SET curr_date = sysdate();
SET u_date = (SELECT DateSubscribed from userAccount WHERE userAccount.UserID=userID); 
SET c = (datediff(curr_date,u_date));
IF c>days THEN 
SET msg = "Subscription expired"; 
ELSE SET msg = "Subscription valid"; 
END IF; 
RETURN msg; 
END $$
DELIMITER ;

SELECT userAccount.UserID, userAccount.Subscription, userAccount.DateSubscribed, checkSubscription(userAccount.UserID) from userAccount;

