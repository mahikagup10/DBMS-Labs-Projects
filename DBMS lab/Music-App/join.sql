-- display artists and albums released by them after year 2000
SELECT artist.ArtistName,album.AlbumName FROM
artist 
join releases ON artist.ArtistID=releases.ArtistID
join
album ON album.AlbumID=releases.AlbumID
where album.AlbumYear>2000;

-- display artist and album for each song
SELECT song.SongName,album.AlbumName,artist.ArtistName
FROM
song join album ON song.AlbumID = album.AlbumID
join releases ON releases.AlbumID = album.AlbumID
join artist ON artist.ArtistID=releases.ArtistID;


-- display all playlists made by users
SELECT userAccount.UserID,playlist.PlaylistName
from
userAccount join playlist ON userAccount.UserID=playlist.UserID;


-- display all rock songs and the song's artist
SELECT song.SongName,artist.ArtistName,song.Genre
from 
song join artist ON song.ArtistID=artist.ArtistID
where song.genre = 'Rock';