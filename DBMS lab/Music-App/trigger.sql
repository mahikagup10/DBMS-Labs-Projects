SET FOREIGN_KEY_CHECKS=0;
DELIMITER $$
CREATE TRIGGER check_subscrption
BEFORE INSERT
ON userAccount FOR EACH ROW
BEGIN
 DECLARE error_msg VARCHAR(255);
 declare count int;
 SET error_msg = ('Choose a valid subscripion type (1 or 2)');
 IF NEW.Subscription! = 1 AND NEW.Subscription!=2 THEN 
 SIGNAL SQLSTATE '45000'
 SET MESSAGE_TEXT=error_msg;  
 END IF;
END $$
DELIMITER ;