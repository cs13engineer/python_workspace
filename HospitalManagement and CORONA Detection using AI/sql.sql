-- ambulance
create table ambulance(
  vanNumber varchar(20) primary key,
  ambulanceType ENUM('Equiped','Unequiped'),
  driverName varchar(40),
  driverContact int,
  associateHospitalName varchar(50)  
);

create table canteen(
    canteenName varchar(40),
    canteenOwnerName varchar(40),
    address varchar(50)
);