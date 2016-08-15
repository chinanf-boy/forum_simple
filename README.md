# forum_simple

use PostgreSQL
----------------
CREATE TABLE messages(
  id        SERIAL PRIMARY KEY,
  subject   TEXT NOT NULL,
  sender    TEXT NOT NULL,
  reply_to  INTEGER REFERENCES messages,
  text      TEXT NOT NULL
  );
  
----------------  
use MySQl
----------------
CREATE TABLE messages(
  id        INT NOT NULL AUTO_INCREMENT,
  subject   VARCHAR(100) NOT NULL,
  sender    VARCHAR(15) NOT NULL,
  reply_to  INT,
  text      MEDIUMTEXT NOT NULL
  PRIMARY KEY(id)
  );
  
----------------  
use SQLite
----------------
carete table messages(
  id        integer primary key autoincrement,
  subject   text not null,
  sender    text not null,
  reply_to  int,
  text      text not null
  );
