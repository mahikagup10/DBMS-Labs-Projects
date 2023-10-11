-- union
-- songs released after 2000, rock genre

SELECT song.AlbumID,song.Genre from song 
union 
SELECT album.AlbumID,album.Genre from album 
where album.AlbumYear>2000;

-- union all 
SELECT AlbumID,Genre from song 
union all
SELECT AlbumID,Genre album where album.AlbumYear>2000;

-- intersect
-- artists who have followers
SELECT ArtistName from artist
where ArtistID IN (SELECT ArtistID from follows);


-- except
-- artists who dont have Followers
SELECT ArtistName from artist
where ArtistID NOT IN (SELECT ArtistID from follows);
