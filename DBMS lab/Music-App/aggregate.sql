-- display artist name with number of songs
select artist.ArtistName, count(*) "Number of songs"
from
song join artist ON song.ArtistID=artist.ArtistID
group by artist.ArtistName
order by count(*) desc;

-- display all songs longer than 5 mins
select song.SongName,artist.ArtistName,song.SongLength,count(*) "Number of songs longer than 5 mins"
from
song join artist on song.ArtistID=artist.ArtistID
where song.SongLength>5
group by artist.ArtistName;

--average streams for rock songs
select song.Genre, AVG(song.Streams) "Average streams for rock genre"
from song where Genre='Rock';

--Number of songs released in album per year
select album.AlbumName,album.AlbumYear,count(*) "Number of songs released"
from song join album ON song.AlbumID=album.AlbumID
group by AlbumYear
having count(*) = (select max(count) 
from (select album.AlbumYear,count(*) count 
from album
group by album.AlbumYear
)as temp
);
