DELIMITER &&  
CREATE PROCEDURE display_max_streams (INOUT maxStreams varchar(40))  
BEGIN  
    SELECT SongName INTO maxStreams FROM song where Streams= (SELECT MAX(Streams) from song);
END &&  
DELIMITER ;

SET @M="";
CALL display_max_streams(@M);
SELECT @M;





