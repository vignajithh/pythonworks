use cakehut;
create table cake(
  id int auto_increment primary key,
  name varchar(200) not null

);

insert into cake(name) values('white forest'),('blueberry'),('white chocoberry cake'),('blueberry cheese cake'),('vancho cake'),('peanut butter cake'),('black forest cake');

select * from cake;

create table cakevarient(
  id int auto_increment primary key,
    weight enum('1kg','2kg','3kg','4kg','5kg') default '1kg',
    price int not null,
    flavour varchar(200) not null,
    shape enum('round','rectangle','square','heart') default 'round',
    cake_id int,
    foreign key(cake_id) references cake(id) on delete cascade,
    unique(weight,price,flavour,shape)
    
);


insert into cakevarient(weight,price,flavour,cake_id) values ("1kg",700,"white forest",1);
select * from cakevarient;

select cake.name,cakevarient.weight,cakevarient.price from cake,cakevarient where cake.id=cakevarient.cake_id;

-- select 1kg cakenames

