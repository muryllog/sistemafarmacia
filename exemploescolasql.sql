create table clientes(
nome varchar(80)not null,
cpf varchar(14) primary key,
telefone varchar(11) not null,
email varchar(100) not null
);

create table medicamentos(
id_med serial primary key,
nome varchar(80)not null,
fabricante varchar (80) not null,
preco real not null,
validade date not null
);


