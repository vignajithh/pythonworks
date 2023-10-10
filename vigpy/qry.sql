show databases;
create database hotel;

use hotel;
create table items(id int unique,
					name varchar(150) not null,
                    category varchar(200) not null,
                    price int not null,
                    type varchar(160) not null

				 );               
	
    
-- listing all tables
show tables;

-- inserting tables

insert into items(id,name,category,price,type)
                          values(5,'noodles','nonveg',170,'chinese');
				
select name,price from items;
select * from items;

-- price below 160

select * from items where price<160;

select * from items where price>150 and price<200;

select name from items where type != "chinese";

-- agrigate functions sum() min() max() count()

select count(*) from items;

select max(price) from items;

select sum(price) from items;

-- nested querry

select * from items where price=(select max(price) from items);

select * from items where price=(select min(price) from items);

-- costly product in category nonveg

select * from items where price=(select max(price) from items where category = "nonveg");

select max(price) from items where price!=(select max(price) from items); 

select * from items where price=(select max(price) from items where price!=(select max(price) from items));

select category,count(*) from items group by(category);

-- employee id name dept salary location

-- sort records

select * from items order by price asc;


-- limit
select * from items order by price asc limit 3;

select count(*) from items where name="vegfriedrice";

select * from items;
-- update items

update items set price=180 where id=2;

-- delete
delete from items where id=2;

-- truncate items; all the datas will be removed from table

alter table items add column course enum("maincourse","starter","desserts") default "maincourse";

update items set course="starter" where id=3;