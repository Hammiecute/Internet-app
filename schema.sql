drop table if exists internet;
create table internet (
  id integer primary key autoincrement,
  user_location text not null,
  user_network text not null,
  network_use text not null,
  rating text not null
);
