create database imdb;
use imdb;

create table language(
 id int auto_increment primary key,
 name varchar(200) not null unique

);
insert into language(name) values("malayalam"),("english"),("hindi"),("tamil");


select * from language;

create table movies(
 id int auto_increment primary key,
 name varchar(200) not null unique,
 year varchar(200) not null,
 language_id int not null,
 foreign key(language_id)references language(id) on delete no action

);

insert into movies(name,year,language_id) values("pathuthalla","2023",4);
select * from movies;

select movies.name,movies.year,language.name from movies,language where movies.language_id=language.id;

-- print malayalm movies
select movies.name from movies,language where movies.language_id=language.id and language.name="malayalam";

create table reviews(
 id int auto_increment primary key,
 comment varchar(200) not null,
 rating int check(rating<6),
 user varchar(200) not null,
 movie_id int,
 foreign key(movie_id) references movies(id) on delete no action

);
select * from reviews;
insert into reviews(comment,rating,user,movie_id) values("awsome","14","vig",5);
-- inner join intersection matchimng 
select movies.name,reviews.comment,reviews.rating,reviews.user from movies inner join reviews on movies.id=reviews.movie_id;
-- left join left all record and right matching records
select movies.name,reviews.comment,reviews.rating,reviews.user from movies left join reviews on movies.id=reviews.movie_id;
-- right join right all recors and left matching records
select movies.name,reviews.comment,reviews.rating,reviews.user from movies right join reviews on movies.id=reviews.movie_id;