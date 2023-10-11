import mysql.connector

mydb = mysql.connector.connect(host="localhost",user = "root",password="",database = "MUSIC_APP_PROJECT")
c=mydb.cursor()

def create_table_album():
    c.execute("CREATE TABLE IF NOT EXISTS album(AlbumID INTEGER PRIMARY KEY,AlbumName VARCHAR(100),AlbumYear INTEGER,Genre VARCHAR(20))")

def create_table_artist():
    c.execute("CREATE TABLE IF NOT EXISTS artist(ArtistID INTEGER PRIMARY KEY,ArtistName VARCHAR(100))")

def create_table_song():
    c.execute("CREATE TABLE IF NOT EXISTS song(SongID INTEGER,ArtistID INTEGER REFERENCES artist(ArtistID) ON DELETE CASCADE,AlbumID INTEGER REFERENCES album(AlbumID) ON DELETE CASCADE,Streams INTEGER DEFAULT 0,SongName VARCHAR(100),SongLength FLOAT(3)Genre VARCHAR(100),PRIMARY KEY(SongID))")

def create_table_user():
    c.execute("CREATE TABLE IF NOT EXISTS user(UserID INTEGER,Email VARCHAR(100) UNIQUE,UserPassword VARCHAR(20) NOT NULL,Dob DATE,Gender VARCHAR(3), Subscription INTEGER,DateSubscribed DATE,PRIMARY KEY (UserID))")


def add_data_album(AlbumID,AlbumName,AlbumYear,Genre):
    c.execute("INSERT INTO album(AlbumID,AlbumName,AlbumYear,Genre) VALUES (%s,%s,%s,%s)",(AlbumID,AlbumName,AlbumYear,Genre))
    mydb.commit()

def add_data_artist(ArtistID,ArtistName):
    c.execute("INSERT INTO artist(ArtistID,ArtistName) VALUES (%s,%s)",(ArtistID,ArtistName))
    mydb.commit()

def add_data_song(SongID,ArtistID,AlbumID,Streams,SongName,SongLength,Genre):
    c.execute("INSERT INTO song(SongID,ArtistID,AlbumID,Streams,SongName,SongLength,Genre) VALUES (%s,%s,%s,%s,%s,%s,%s)",(SongID,ArtistID,AlbumID,Streams,SongName,SongLength,Genre))
    mydb.commit()

def add_data_user(UserID,Email,UserPassword,Dob,Gender,Subscription,DateSubscribed):
    c.execute("INSERT INTO userAccount(UserID,Email,UserPassword,Dob,Gender,Subscription,DateSubscribed) VALUES (%s,%s,%s,%s,%s,%s,%s)",(UserID,Email,UserPassword,Dob,Gender,Subscription,DateSubscribed))
    mydb.commit()


def view_albums():
    c.execute("SELECT * FROM album")
    data = c.fetchall()
    return data

def view_artists():
    c.execute("SELECT * FROM artist")
    data = c.fetchall()
    return data

def view_songs():
    c.execute("SELECT * FROM song")
    data = c.fetchall()
    return data

def view_users():
    c.execute("SELECT * FROM userAccount")
    data = c.fetchall()
    return data

def view_only_album():
    c.execute('SELECT AlbumName FROM album')
    data = c.fetchall()
    return data

def view_only_artist():
    c.execute('SELECT ArtistName FROM artist')
    data = c.fetchall()
    return data

def view_only_song():
    c.execute('SELECT SongName FROM song')
    data = c.fetchall()
    return data

def view_only_user():
    c.execute('SELECT UserID FROM userAccount')
    data = c.fetchall()
    return data

def get_albums(AlbumName):
    c.execute('SELECT * FROM album WHERE AlbumName ="{}"'.format(AlbumName))
    data = c.fetchall()
    return data

def get_artists(ArtistName):
    c.execute('SELECT * FROM artist WHERE ArtistName ="{}"'.format(ArtistName))
    data = c.fetchall()
    return data

def get_songs(SongName):
    c.execute('SELECT * FROM song WHERE SongName ="{}"'.format(SongName))
    data = c.fetchall()
    return data

def get_users(UserID):
    c.execute('SELECT * FROM userAccount WHERE UserID ="{}"'.format(UserID))
    data = c.fetchall()
    return data

def edit_album(newAlbumID,newAlbumName,newAlbumYear,newGenre,AlbumID,AlbumName,AlbumYear,Genre):
        c.execute("UPDATE album SET AlbumID=%s, AlbumName=%s, AlbumYear=%s, Genre=%s WHERE AlbumID=%s and AlbumName=%s and AlbumYear=%s and Genre=%s", (newAlbumID,newAlbumName,newAlbumYear,newGenre, AlbumID,AlbumName,AlbumYear,Genre))
        mydb.commit()
        c.execute("SELECT AlbumName from album")
        data = c.fetchall()
        return data

def edit_artist(newArtistID,newArtistName,ArtistID,ArtistName):
        c.execute("UPDATE artist SET ArtistID=%s, ArtistName=%s WHERE AlbumID=%s and ArtistName=%s", (newArtistID,newArtistName, ArtistID,ArtistName))
        mydb.commit()
        c.execute("SELECT ArtistName from artist")
        data = c.fetchall()
        return data

def edit_song(newSongID,newArtistID,newAlbumID,newStreams,newSongName,newSongLength,newGenre,SongID,ArtistID,AlbumID,Streams,SongName,SongLength,Genre):
        c.execute("UPDATE song SET SongID=%s,ArtistID=%s,AlbumID=%s,Streams=%s,SongName=%s,SongLength=%s,Genre=%s WHERE SongID=%s and ArtistID=%s and AlbumID=%s and Streams=%s and SongName=%s and SongLength=%s and Genre=%s", (newSongID,newArtistID,newAlbumID,newStreams,newSongName,newSongLength,newGenre,SongID,ArtistID,AlbumID,Streams,SongName,SongLength,Genre))
        mydb.commit()
        c.execute("SELECT SongNaame from song")
        data = c.fetchall()
        return data

def edit_user(newUserID,newEmail,newUserPassword,newDob,newGender,newSubscription,newDateSubscribed,UserID,Email,UserPassword,Dob,Gender,Subscription,DateSubscribed):
        c.execute("UPDATE album SET UserID=%s,Email=%s,UserPassword=%s,Dob=%s,Gender=%s,Subscription=%s,DateSubscribed=%s WHERE UserID=%s and Email=%s and UserPassword=%s and Dob=%s and Gender=%s and Subscription=%s and DateSubscribed=%s", (newUserID,newEmail,newUserPassword,newDob,newGender,newSubscription,newDateSubscribed,UserID,Email,UserPassword,Dob,Gender,Subscription,DateSubscribed))
        mydb.commit()
        c.execute("SELECT UserID from userAccount")
        data = c.fetchall()
        return data

def delete_data_album(AlbumName):
    c.execute('SET FOREIGN_KEY_CHECKS=0')
    c.execute('DELETE FROM album WHERE AlbumName="{}"'.format(AlbumName))
    mydb.commit()

def delete_data_artist(ArtistName):
    c.execute('SET FOREIGN_KEY_CHECKS=0')
    c.execute('DELETE FROM artist WHERE ArtistName="{}"'.format(ArtistName))
    mydb.commit()

def delete_data_song(SongName):
    c.execute('SET FOREIGN_KEY_CHECKS=0')
    c.execute('DELETE FROM song WHERE SongName="{}"'.format(SongName))
    mydb.commit()

def delete_data_user(UserID):
    c.execute('SET FOREIGN_KEY_CHECKS=0')
    c.execute('DELETE FROM userAccount WHERE UserID="{}"'.format(UserID))
    mydb.commit()

def execute_query(query):
    str(query).replace(";", '')

    if "create" in str(query).lower():
        c.execute(query)
        mydb.commit()

    elif "read" or '*' in str(query).lower():
        c.execute(query)
        res = c.fetchall()
        return res,c.description

    elif "update" in str(query).lower():
        c.execute(query)
        mydb.commit()

    elif "delete" in str(query).lower():
        c.execute(query)
        mydb.commit()