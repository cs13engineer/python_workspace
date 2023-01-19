mysql> select * from PatientMedicine;
+------------+---------------+-------------+------------+---------------+----------------+
| MedicineId | Medicine1     | Medicine2   | Medicine3  | Medicine4     | Medicine5      |
+------------+---------------+-------------+------------+---------------+----------------+
|        200 | Augmentin 625 | Dolo 650    | Dytor 10   | Renolog       | Roxid          |
|        201 | Ketorol-DT    | Aspirin     | Sinarest   | Susten SR     | Ursocol 300    |
|        202 | Udiliv 150    | Fluka 150   | Flexon     | Glycomet GP   | Ganon Total    |
|        203 | Hifenac P     | Heptral 400 | Intdral 10 | Libraxz       | Intralase 200  |
|        204 | Liofen 10     | Meftal SPAS | Monocef    | Mucaine Gel   | Udiliv 200     |
|        205 | Augmentin 250 | Meftal SPAS | Dytor 10   | Renolog       | Mucaine Gel    |
|        206 | Mintope Forte | Norflox     | Nexpro     | Ondem Syrup   | Omez           |
|        207 | Ornof         | Primolut-N  | Pantop 40  | Qutipin       | Qutan 25       |
|        208 | Qure 500      | Razo D      | Rebagen    | Stugeron      | Sibelium       |
|        209 | Susten SR     | Telma 40    | Trajenta   | Renolog       | Telvas         |
|        210 | Tonact        | Ultraset    | Udapa      | Urifast Syrup | Roxid          |
|        211 | Augmentin 625 | Urikind K   | Voliobio   | Valium 5mg    | Vertistar MD   |
|        212 | Warf          | Dolo 650    | Wincold    | Xone          | Xycal M        |
|        213 | Xtralite      | Yutopar     | YashCold   | Zerodol       | Zenflox        |
|        214 | Zifi 200      | Avil        | Atarax 25  | Alprax        | Betbesol       |
|        215 | Betamil       | Balcof      | Cefix 200  | Renolog       | Roxid          |
|        216 | Crocin ADV    | Ciplox      | Diane 35   | Drotin        | Evion LC       |
|        217 | Econorm       | Enzar Forte | Flagyl 400 | Fucibet       | Grenil         |
|        218 | Gemcal        | Hepakind    | Lokip 10   | Xewllog       | Loxid          |
|        219 | Histafree     | Hifrenac    | Imol Plus  | Ibset         | Ivera Solution |
|        220 | Januvia 50    | Jalra M     | Ketorol DT | Kenacart      | Lonazep        |
|        221 | Levocet       | Lysoflam    | Meprate 50 | Morr F        | Nexito Plus    |
|        222 | Nicip         | Nikroran    | Ovral L    | Omez          | Roxid          |
|        223 | Ondem         | Dolo 650    | Dytor 10   | Oxdetol       | Primolut N     |
|        224 | Predmet       | Qustain     | Rexidin M  | Solvin        | Taxim          |
+------------+---------------+-------------+------------+---------------+----------------+
25 rows in set (0.00 sec)

mysql> insert into PatientDisease values(150,35,93,4,'2016-01-01','2016-01-10',200);
ease values(151,36,104,2,'2016-01-20','2016-01-25',201);
insert into PatientDisease values(152,37,105,21,'2016-02-01','2016-02-20',201);
insert into PatientDisease values(153,40,107,16,'2016-03-15','2016-04-15',203);
insert into PatientDisease values(154,50,107,16,'2016-03-25','2016-03-30',204);
insert into PatientDisease values(155,51,92,17,'2016-04-15','2016-04-20',205);
insert into PatientDisease values(156,38,92,22,'2016-07-05','2016-07-15',206);
insert into PatientDisease values(157,49,99,15,'2016-08-17','2016-08-25',207);
insert into PatientDisease values(158,53,106,12,'2016-08-25','2016-09-05',208);
insert into PatientDisease values(159,39,94,1,'2016-10-05','2016-10-25',209);
insert iQuery OK, 1 row affected (0.08 sec)

mysql> insert into PatientDisease values(151,36,104,2,'2016-01-20','2016-01-25',201);
nto PatientDisease values(160,41,111,11,'2016-11-08','2016-11-18',210);
insert into PatientDisease values(161,54,94,1,'2016-12-01','2016-12-21',211);
insert into PatientDisease values(162,45,112,22,'2017-01-01','2017-02-01',212);
insert into PatientDisease values(163,55,99,15,'2017-02-16','2017-03-11',213);
insert into PatientDisease values(164,56,102,21,'2017-03-21','2017-03-30',214);
insert into PatientDisease values(165,57,94,2,'2017-04-01','2017-04-30',215);
insert into PatientDisease values(166,42,96,9,'2017-06-05','2017-06-18',216);
insert into PatientDisease values(167,35,100,5,'2017-07-16','2017-07-25',217);
insert into PatientDiseaseQuery OK, 1 row affected (0.06 sec)

mysql> insert into PatientDisease values(152,37,105,21,'2016-02-01','2016-02-20',201);
 values(168,46,94,1,'2017-09-05','2017-09-22',218);
insert into PatientDisease values(169,47,99,15,'2017-10-01','2017-10-12',219);
insert into PatientDisease values(170,48,100,5,'2017-10-01','2017-10-13',210);
insert into PatientDisease values(171,43,106,12,'2017-11-01','2017-11-11',211);
insert into PatientDisease values(172,45,96,9,'2018-01-11','2018-01-20',212);
insert into PatientDisease values(173,44,94,7,'2018-01-11','2018-01-20',213);
insert into PatientDisease values(174,38,106,12,'2018-01-15','2018-01-20',214);Query OK, 1 row affected (0.10 sec)

mysql> insert into PatientDisease values(153,40,107,16,'2016-03-15','2016-04-15',203);
Query OK, 1 row affected (0.06 sec)

mysql> insert into PatientDisease values(154,50,107,16,'2016-03-25','2016-03-30',204);
Query OK, 1 row affected (0.10 sec)

mysql> insert into PatientDisease values(155,51,92,17,'2016-04-15','2016-04-20',205);
Query OK, 1 row affected (0.06 sec)

mysql> insert into PatientDisease values(156,38,92,22,'2016-07-05','2016-07-15',206);
Query OK, 1 row affected (0.07 sec)

mysql> insert into PatientDisease values(157,49,99,15,'2016-08-17','2016-08-25',207);
Query OK, 1 row affected (0.10 sec)

mysql> insert into PatientDisease values(158,53,106,12,'2016-08-25','2016-09-05',208);
Query OK, 1 row affected (0.10 sec)

mysql> insert into PatientDisease values(159,39,94,1,'2016-10-05','2016-10-25',209);
Query OK, 1 row affected (0.10 sec)

mysql> insert into PatientDisease values(160,41,111,11,'2016-11-08','2016-11-18',210);
Query OK, 1 row affected (0.10 sec)

mysql> insert into PatientDisease values(161,54,94,1,'2016-12-01','2016-12-21',211);
Query OK, 1 row affected (0.19 sec)

mysql> insert into PatientDisease values(162,45,112,22,'2017-01-01','2017-02-01',212);
Query OK, 1 row affected (0.07 sec)

mysql> insert into PatientDisease values(163,55,99,15,'2017-02-16','2017-03-11',213);
Query OK, 1 row affected (0.13 sec)

mysql> insert into PatientDisease values(164,56,102,21,'2017-03-21','2017-03-30',214);
Query OK, 1 row affected (0.10 sec)

mysql> insert into PatientDisease values(165,57,94,2,'2017-04-01','2017-04-30',215);
Query OK, 1 row affected (0.07 sec)

mysql> insert into PatientDisease values(166,42,96,9,'2017-06-05','2017-06-18',216);
Query OK, 1 row affected (0.07 sec)

mysql> insert into PatientDisease values(167,35,100,5,'2017-07-16','2017-07-25',217);
Query OK, 1 row affected (0.10 sec)

mysql> insert into PatientDisease values(168,46,94,1,'2017-09-05','2017-09-22',218);
Query OK, 1 row affected (0.10 sec)

mysql> insert into PatientDisease values(169,47,99,15,'2017-10-01','2017-10-12',219);
Query OK, 1 row affected (0.11 sec)

mysql> insert into PatientDisease values(170,48,100,5,'2017-10-01','2017-10-13',210);
Query OK, 1 row affected (1.34 sec)

mysql> insert into PatientDisease values(171,43,106,12,'2017-11-01','2017-11-11',211);
Query OK, 1 row affected (0.14 sec)

mysql> insert into PatientDisease values(172,45,96,9,'2018-01-11','2018-01-20',212);
Query OK, 1 row affected (0.09 sec)

mysql> insert into PatientDisease values(173,44,94,7,'2018-01-11','2018-01-20',213);
Query OK, 1 row affected (0.09 sec)

mysql> insert into PatientDisease values(174,38,106,12,'2018-01-15','2018-01-20',214);
Query OK, 1 row affected (0.24 sec)

mysql> select * from PatientDisease; 
+------------------+-----------+-----------+--------+------------+------------+------------+
| PatientDiseaseId | PatientId | DiseaseID | DoctId | StartDate  | EndDates   | MedicineId |
+------------------+-----------+-----------+--------+------------+------------+------------+
|              150 |        35 |        93 |      4 | 2016-01-01 | 2016-01-10 |        200 |
|              151 |        36 |       104 |      2 | 2016-01-20 | 2016-01-25 |        201 |
|              152 |        37 |       105 |     21 | 2016-02-01 | 2016-02-20 |        201 |
|              153 |        40 |       107 |     16 | 2016-03-15 | 2016-04-15 |        203 |
|              154 |        50 |       107 |     16 | 2016-03-25 | 2016-03-30 |        204 |
|              155 |        51 |        92 |     17 | 2016-04-15 | 2016-04-20 |        205 |
|              156 |        38 |        92 |     22 | 2016-07-05 | 2016-07-15 |        206 |
|              157 |        49 |        99 |     15 | 2016-08-17 | 2016-08-25 |        207 |
|              158 |        53 |       106 |     12 | 2016-08-25 | 2016-09-05 |        208 |
|              159 |        39 |        94 |      1 | 2016-10-05 | 2016-10-25 |        209 |
|              160 |        41 |       111 |     11 | 2016-11-08 | 2016-11-18 |        210 |
|              161 |        54 |        94 |      1 | 2016-12-01 | 2016-12-21 |        211 |
|              162 |        45 |       112 |     22 | 2017-01-01 | 2017-02-01 |        212 |
|              163 |        55 |        99 |     15 | 2017-02-16 | 2017-03-11 |        213 |
|              164 |        56 |       102 |     21 | 2017-03-21 | 2017-03-30 |        214 |
|              165 |        57 |        94 |      2 | 2017-04-01 | 2017-04-30 |        215 |
|              166 |        42 |        96 |      9 | 2017-06-05 | 2017-06-18 |        216 |
|              167 |        35 |       100 |      5 | 2017-07-16 | 2017-07-25 |        217 |
|              168 |        46 |        94 |      1 | 2017-09-05 | 2017-09-22 |        218 |
|              169 |        47 |        99 |     15 | 2017-10-01 | 2017-10-12 |        219 |
|              170 |        48 |       100 |      5 | 2017-10-01 | 2017-10-13 |        210 |
|              171 |        43 |       106 |     12 | 2017-11-01 | 2017-11-11 |        211 |
|              172 |        45 |        96 |      9 | 2018-01-11 | 2018-01-20 |        212 |
|              173 |        44 |        94 |      7 | 2018-01-11 | 2018-01-20 |        213 |
|              174 |        38 |       106 |     12 | 2018-01-15 | 2018-01-20 |        214 |
+------------------+-----------+-----------+--------+------------+------------+------------+
25 rows in set (0.00 sec)

mysql> insert into AssetsMaster values(10001,15,'2021-11-22','2022-01-02',10);
ues(10002,16,'2021-11-21','2022-02-21',15);
insert into AssetsMaster values(10003,17,'2021-10-22','2022-01-02',13);
insert into AssetsMaster values(10004,18,'2021-10-12','2022-01-05',11);
insert into AssetsMaster values(10005,19,'2021-10-20','2022-01-21',16);
insert into AssetsMaster values(10006,20,'2021-09-15','2022-01-23',12);
insert into AssetsMaster values(10007,21,'2021-11-02','2022-03-25',18);
insert into AssetsMaster values(10008,22,'2021-10-29','2022-03-12',15);
insert into AssetsMaster values(10009,23,'2021-10-03','2022-03-02',20);
insert into AssetsMaster values(10010,24,'2021-10-04','2022-03-04',10);
insert into AssetsMaster values(10011,25,'2021-10-05','2022-03-05',20);
insert iQuery OK, 1 row affected (0.09 sec)

mysql> insert into AssetsMaster values(10002,16,'2021-11-21','2022-02-21',15);
nto AssetsMaster values(10012,26,'2021-10-06','2022-03-06',20);
insert into AssetsMaster values(10013,27,'2021-10-10','2022-03-13',13);
insert into AssetsMaster values(10014,28,'2021-10-11','2022-03-14',12);
insert into AssetsMaster values(10015,29,'2021-12-22','2022-04-20',14);
insert into AssetsMaster values(10016,30,'2021-12-23','2022-04-21',10);
insert into AssetsMaster values(10017,31,'2021-12-24','2022-04-22',14);
insert into AssetsMaster values(10018,32,'2021-12-25','2022-04-23',15);
insert into AssetsMaster values(10019,33,'2021-12-26','2022-04-24',16);
insert into AssetsMaster values(10020,34,'2021-12-27','2022-04-25',11);
insert intQuery OK, 1 row affected (0.06 sec)

mysql> insert into AssetsMaster values(10003,17,'2021-10-22','2022-01-02',13);
o AssetsMaster values(10021,35,'2021-12-28','2022-04-26',12);
insert into AssetsMaster values(10022,36,'2021-12-29','2022-04-27',16);
insert into AssetsMaster values(10023,37,'2021-12-30','2022-05-02',20);
insert into AssetsMaster values(10024,38,'2021-12-02','2022-05-05',21);
insert into AssetsMaster values(10025,39,'2021-12-03','2022-05-07',22);Query OK, 1 row affected (1.16 sec)

mysql> insert into AssetsMaster values(10004,18,'2021-10-12','2022-01-05',11);
Query OK, 1 row affected (0.10 sec)

mysql> insert into AssetsMaster values(10005,19,'2021-10-20','2022-01-21',16);
Query OK, 1 row affected (0.10 sec)

mysql> insert into AssetsMaster values(10006,20,'2021-09-15','2022-01-23',12);
Query OK, 1 row affected (0.12 sec)

mysql> insert into AssetsMaster values(10007,21,'2021-11-02','2022-03-25',18);
Query OK, 1 row affected (0.12 sec)

mysql> insert into AssetsMaster values(10008,22,'2021-10-29','2022-03-12',15);
Query OK, 1 row affected (0.10 sec)

mysql> insert into AssetsMaster values(10009,23,'2021-10-03','2022-03-02',20);
Query OK, 1 row affected (0.10 sec)

mysql> insert into AssetsMaster values(10010,24,'2021-10-04','2022-03-04',10);
Query OK, 1 row affected (0.10 sec)

mysql> insert into AssetsMaster values(10011,25,'2021-10-05','2022-03-05',20);
Query OK, 1 row affected (0.10 sec)

mysql> insert into AssetsMaster values(10012,26,'2021-10-06','2022-03-06',20);
Query OK, 1 row affected (0.10 sec)

mysql> insert into AssetsMaster values(10013,27,'2021-10-10','2022-03-13',13);
Query OK, 1 row affected (0.10 sec)

mysql> insert into AssetsMaster values(10014,28,'2021-10-11','2022-03-14',12);
Query OK, 1 row affected (0.11 sec)

mysql> insert into AssetsMaster values(10015,29,'2021-12-22','2022-04-20',14);
Query OK, 1 row affected (0.10 sec)

mysql> insert into AssetsMaster values(10016,30,'2021-12-23','2022-04-21',10);
Query OK, 1 row affected (0.06 sec)

mysql> insert into AssetsMaster values(10017,31,'2021-12-24','2022-04-22',14);
Query OK, 1 row affected (0.09 sec)

mysql> insert into AssetsMaster values(10018,32,'2021-12-25','2022-04-23',15);
Query OK, 1 row affected (0.07 sec)

mysql> insert into AssetsMaster values(10019,33,'2021-12-26','2022-04-24',16);
Query OK, 1 row affected (0.08 sec)

mysql> insert into AssetsMaster values(10020,34,'2021-12-27','2022-04-25',11);
Query OK, 1 row affected (0.10 sec)

mysql> insert into AssetsMaster values(10021,35,'2021-12-28','2022-04-26',12);
Query OK, 1 row affected (0.06 sec)

mysql> insert into AssetsMaster values(10022,36,'2021-12-29','2022-04-27',16);
Query OK, 1 row affected (0.10 sec)

mysql> insert into AssetsMaster values(10023,37,'2021-12-30','2022-05-02',20);
Query OK, 1 row affected (0.14 sec)

mysql> insert into AssetsMaster values(10024,38,'2021-12-02','2022-05-05',21);
Query OK, 1 row affected (0.33 sec)

mysql> insert into AssetsMaster values(10025,39,'2021-12-03','2022-05-07',22);
Query OK, 1 row affected (0.10 sec)

mysql> select * from AssetsMaster;
+---------+--------+----------------+--------------+-----------------+
| AssetId | PartId | AssetStartDate | AssetEndDate | DepreciationPCT |
+---------+--------+----------------+--------------+-----------------+
|   10001 |     15 | 2021-11-22     | 2022-01-02   | 10              |
|   10002 |     16 | 2021-11-21     | 2022-02-21   | 15              |
|   10003 |     17 | 2021-10-22     | 2022-01-02   | 13              |
|   10004 |     18 | 2021-10-12     | 2022-01-05   | 11              |
|   10005 |     19 | 2021-10-20     | 2022-01-21   | 16              |
|   10006 |     20 | 2021-09-15     | 2022-01-23   | 12              |
|   10007 |     21 | 2021-11-02     | 2022-03-25   | 18              |
|   10008 |     22 | 2021-10-29     | 2022-03-12   | 15              |
|   10009 |     23 | 2021-10-03     | 2022-03-02   | 20              |
|   10010 |     24 | 2021-10-04     | 2022-03-04   | 10              |
|   10011 |     25 | 2021-10-05     | 2022-03-05   | 20              |
|   10012 |     26 | 2021-10-06     | 2022-03-06   | 20              |
|   10013 |     27 | 2021-10-10     | 2022-03-13   | 13              |
|   10014 |     28 | 2021-10-11     | 2022-03-14   | 12              |
|   10015 |     29 | 2021-12-22     | 2022-04-20   | 14              |
|   10016 |     30 | 2021-12-23     | 2022-04-21   | 10              |
|   10017 |     31 | 2021-12-24     | 2022-04-22   | 14              |
|   10018 |     32 | 2021-12-25     | 2022-04-23   | 15              |
|   10019 |     33 | 2021-12-26     | 2022-04-24   | 16              |
|   10020 |     34 | 2021-12-27     | 2022-04-25   | 11              |
|   10021 |     35 | 2021-12-28     | 2022-04-26   | 12              |
|   10022 |     36 | 2021-12-29     | 2022-04-27   | 16              |
|   10023 |     37 | 2021-12-30     | 2022-05-02   | 20              |
|   10024 |     38 | 2021-12-02     | 2022-05-05   | 21              |
|   10025 |     39 | 2021-12-03     | 2022-05-07   | 22              |
+---------+--------+----------------+--------------+-----------------+
25 rows in set (0.00 sec)

mysql> insert into EquipMaint values(10001,'2021-11-22','Cascade','503-595-1720','Y');
nt values(10002,'2021-10-21','Cascade','503-595-1720','Y');
insert into EquipMaint values(10003,'2021-10-22','Cascade','503-595-1720','N');
insert into EquipMaint values(10004,'2021-10-12','Novartis','403-201-1230','Y');
insert into EquipMaint values(10005,'2021-10-20','Novartis','403-201-1230','N');
insert into EquipMaint values(10007,'2021-11-02','Medtronic','600-301-1200','Y');
insert into EquipMaint values(10008,'2021-10-29','Medtronic','600-301-1200','N');
insert into EquipMaint values(10009,'2021-10-03','Medtronic','600-301-1200','Y');
insert into EquipMaint values(10010,'2021-10-04','Baxer','700-301-1200','Y');
insert into EquipMaint vQuery OK, 1 row affected (0.07 sec)

mysql> insert into EquipMaint values(10002,'2021-10-21','Cascade','503-595-1720','Y');
alues(10011,'2021-10-05','Baxer','700-301-1200','Y');
insert into EquipMaint values(10012,'2021-10-06','Baxer','700-301-1200','Y');
insert into EquipMaint values(10013,'2021-10-10','Baxer','700-301-1200','N');
insert into EquipMaint values(10014,'2021-10-11','Danaher','800-301-1200','Y');
insert into EquipMaint values(10015,'2021-12-22','Danaher','800-301-1200','Y');
insert into EquipMaint values(10016,'2021-12-23','Danaher','800-301-1200','N');
insert into EquipMaint values(10017,'2021-12-24','Danaher','800-301-1200','Y');
insert into EquipMaint values(10018,'2021-12-25','3M Company','910-301-1200','N');
insert into EquipMaint values(10019,'2021-12-25','3M Company','910-301-1200','Y');
insert into EquipMaint values(10020,'2021-12-27','3M Company','910-301-1200','Y');
insert into EquipMaint values(10021,'2021-12-28','3M Company','910-301-1200','N');
insert into EquipMaint values(10022,'2021-12-29','Siemens','560-301-2200','Y');
insert into EquipMaint values(10023,'2021-12-30','Siemens','560-301-2200','Y');
insert into EquipMaint values(10024,'2021-12-02','Siemens','560-301-2200','Y');
insert into EquipMaint values(10025,'2021-12-03','Siemens','560-301-2200','N');
insert into EquipMaint values(10006,'2021-09-09','Novartis','403-201-1230','N');Query OK, 1 row affected (0.22 sec)

mysql> insert into EquipMaint values(10003,'2021-10-22','Cascade','503-595-1720','N');
Query OK, 1 row affected (0.07 sec)

mysql> insert into EquipMaint values(10004,'2021-10-12','Novartis','403-201-1230','Y');
Query OK, 1 row affected (0.08 sec)

mysql> insert into EquipMaint values(10005,'2021-10-20','Novartis','403-201-1230','N');
Query OK, 1 row affected (0.06 sec)

mysql> insert into EquipMaint values(10007,'2021-11-02','Medtronic','600-301-1200','Y');
Query OK, 1 row affected (0.10 sec)

mysql> insert into EquipMaint values(10008,'2021-10-29','Medtronic','600-301-1200','N');
Query OK, 1 row affected (0.10 sec)

mysql> insert into EquipMaint values(10009,'2021-10-03','Medtronic','600-301-1200','Y');
Query OK, 1 row affected (1.15 sec)

mysql> insert into EquipMaint values(10010,'2021-10-04','Baxer','700-301-1200','Y');
Query OK, 1 row affected (0.06 sec)

mysql> insert into EquipMaint values(10011,'2021-10-05','Baxer','700-301-1200','Y');
Query OK, 1 row affected (0.06 sec)

mysql> insert into EquipMaint values(10012,'2021-10-06','Baxer','700-301-1200','Y');
Query OK, 1 row affected (0.10 sec)

mysql> insert into EquipMaint values(10013,'2021-10-10','Baxer','700-301-1200','N');
Query OK, 1 row affected (0.10 sec)

mysql> insert into EquipMaint values(10014,'2021-10-11','Danaher','800-301-1200','Y');
Query OK, 1 row affected (0.10 sec)

mysql> insert into EquipMaint values(10015,'2021-12-22','Danaher','800-301-1200','Y');
Query OK, 1 row affected (0.10 sec)

mysql> insert into EquipMaint values(10016,'2021-12-23','Danaher','800-301-1200','N');
Query OK, 1 row affected (0.10 sec)

mysql> insert into EquipMaint values(10017,'2021-12-24','Danaher','800-301-1200','Y');
Query OK, 1 row affected (0.11 sec)

mysql> insert into EquipMaint values(10018,'2021-12-25','3M Company','910-301-1200','N');
Query OK, 1 row affected (0.10 sec)

mysql> insert into EquipMaint values(10019,'2021-12-25','3M Company','910-301-1200','Y');
Query OK, 1 row affected (0.10 sec)

mysql> insert into EquipMaint values(10020,'2021-12-27','3M Company','910-301-1200','Y');
Query OK, 1 row affected (0.10 sec)

mysql> insert into EquipMaint values(10021,'2021-12-28','3M Company','910-301-1200','N');
Query OK, 1 row affected (0.11 sec)

mysql> insert into EquipMaint values(10022,'2021-12-29','Siemens','560-301-2200','Y');
Query OK, 1 row affected (0.13 sec)

mysql> insert into EquipMaint values(10023,'2021-12-30','Siemens','560-301-2200','Y');
Query OK, 1 row affected (0.18 sec)

mysql> insert into EquipMaint values(10024,'2021-12-02','Siemens','560-301-2200','Y');
Query OK, 1 row affected (0.14 sec)

mysql> insert into EquipMaint values(10025,'2021-12-03','Siemens','560-301-2200','N');
Query OK, 1 row affected (0.14 sec)

mysql> insert into EquipMaint values(10006,'2021-09-09','Novartis','403-201-1230','N');
Query OK, 1 row affected (0.17 sec)

mysql> select * from EquipMaint;
+---------+------------+--------------+--------------+--------------+
| AssetId | MaintDate  | MaintCompany | CompTelNo    | Satisfactory |
+---------+------------+--------------+--------------+--------------+
|   10001 | 2021-11-22 | Cascade      | 503-595-1720 | Y            |
|   10002 | 2021-10-21 | Cascade      | 503-595-1720 | Y            |
|   10003 | 2021-10-22 | Cascade      | 503-595-1720 | N            |
|   10004 | 2021-10-12 | Novartis     | 403-201-1230 | Y            |
|   10005 | 2021-10-20 | Novartis     | 403-201-1230 | N            |
|   10007 | 2021-11-02 | Medtronic    | 600-301-1200 | Y            |
|   10008 | 2021-10-29 | Medtronic    | 600-301-1200 | N            |
|   10009 | 2021-10-03 | Medtronic    | 600-301-1200 | Y            |
|   10010 | 2021-10-04 | Baxer        | 700-301-1200 | Y            |
|   10011 | 2021-10-05 | Baxer        | 700-301-1200 | Y            |
|   10012 | 2021-10-06 | Baxer        | 700-301-1200 | Y            |
|   10013 | 2021-10-10 | Baxer        | 700-301-1200 | N            |
|   10014 | 2021-10-11 | Danaher      | 800-301-1200 | Y            |
|   10015 | 2021-12-22 | Danaher      | 800-301-1200 | Y            |
|   10016 | 2021-12-23 | Danaher      | 800-301-1200 | N            |
|   10017 | 2021-12-24 | Danaher      | 800-301-1200 | Y            |
|   10018 | 2021-12-25 | 3M Company   | 910-301-1200 | N            |
|   10019 | 2021-12-25 | 3M Company   | 910-301-1200 | Y            |
|   10020 | 2021-12-27 | 3M Company   | 910-301-1200 | Y            |
|   10021 | 2021-12-28 | 3M Company   | 910-301-1200 | N            |
|   10022 | 2021-12-29 | Siemens      | 560-301-2200 | Y            |
|   10023 | 2021-12-30 | Siemens      | 560-301-2200 | Y            |
|   10024 | 2021-12-02 | Siemens      | 560-301-2200 | Y            |
|   10025 | 2021-12-03 | Siemens      | 560-301-2200 | N            |
|   10006 | 2021-09-09 | Novartis     | 403-201-1230 | N            |
+---------+------------+--------------+--------------+--------------+
25 rows in set (0.00 sec)

mysql> insert into Attendance values(350,'2016-01-01','09:00AM','06:00PM');
51,'2016-01-01','12:30PM','21:30PM');
insert into Attendance values(352,'2016-01-01','01:00PM','22:00PM');
insert into Attendance values(353,'2016-01-01','09:00AM','06:00PM');
insert into Attendance values(354,'2016-01-01','12:30PM','21:30PM');
insert into Attendance values(355,'2016-01-01','01:00AM','22:00PM');
insert into Attendance values(356,'2016-01-01','03:00PM','24:00AM');
insert into Attendance values(357,'2016-01-01','18:00PM','03:00AM');
insert into Attendance values(358,'2016-01-01','09:00AM','06:00PM');
insert into Attendance values(359,'2016-01-02','09:00AM','06:00PM');
insert intQuery OK, 1 row affected (0.07 sec)

mysql> insert into Attendance values(351,'2016-01-01','12:30PM','21:30PM');
o Attendance values(360,'2016-01-02','01:00PM','22:00PM');
insert into Attendance values(361,'2016-01-02','01:00PM','22:00PM');
insert into Attendance values(362,'2016-01-02','03:00PM','24:00AM');
insert into Attendance values(363,'2016-01-02','03:00PM','24:00AM');
insert into Attendance values(364,'2016-01-03','03:00PM','24:00AM');
insert into Attendance values(365,'2016-01-03','18:00PM','03:00AM');
insert into Attendance values(366,'2016-01-03','01:00PM','22:00PM');
insert into Attendance values(367,'2016-01-03','03:00PM','24:00AM');
insert into Attendance values(368,'2016-01-04','09:00AM','06:00PM');
insert into Attendance values(369,'2016-01-05','8:00PM','03:00AM');
insert into Attendance values(370,'2016-01-05','12:30PM','21:30PM');
inQuery OK, 1 row affected (0.08 sec)

mysql> insert into Attendance values(352,'2016-01-01','01:00PM','22:00PM');
sert into Attendance values(371,'2016-01-05','12:30PM','21:30PM');
insert into Attendance values(372,'2016-01-06','01:00PM','22:00PM');
insert into Attendance values(373,'2016-01-06','03:00PM','24:00AM');
insert into Attendance values(374,'2016-01-07','09:00AM','06:00PM');Query OK, 1 row affected (0.11 sec)

mysql> insert into Attendance values(353,'2016-01-01','09:00AM','06:00PM');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Attendance values(354,'2016-01-01','12:30PM','21:30PM');
Query OK, 1 row affected (0.12 sec)

mysql> insert into Attendance values(355,'2016-01-01','01:00AM','22:00PM');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Attendance values(356,'2016-01-01','03:00PM','24:00AM');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Attendance values(357,'2016-01-01','18:00PM','03:00AM');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Attendance values(358,'2016-01-01','09:00AM','06:00PM');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Attendance values(359,'2016-01-02','09:00AM','06:00PM');
Query OK, 1 row affected (0.61 sec)

mysql> insert into Attendance values(360,'2016-01-02','01:00PM','22:00PM');
Query OK, 1 row affected (0.66 sec)

mysql> insert into Attendance values(361,'2016-01-02','01:00PM','22:00PM');
Query OK, 1 row affected (0.07 sec)

mysql> insert into Attendance values(362,'2016-01-02','03:00PM','24:00AM');
Query OK, 1 row affected (0.07 sec)

mysql> insert into Attendance values(363,'2016-01-02','03:00PM','24:00AM');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Attendance values(364,'2016-01-03','03:00PM','24:00AM');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Attendance values(365,'2016-01-03','18:00PM','03:00AM');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Attendance values(366,'2016-01-03','01:00PM','22:00PM');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Attendance values(367,'2016-01-03','03:00PM','24:00AM');
Query OK, 1 row affected (0.09 sec)

mysql> insert into Attendance values(368,'2016-01-04','09:00AM','06:00PM');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Attendance values(369,'2016-01-05','8:00PM','03:00AM');
Query OK, 1 row affected (0.11 sec)

mysql> insert into Attendance values(370,'2016-01-05','12:30PM','21:30PM');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Attendance values(371,'2016-01-05','12:30PM','21:30PM');
Query OK, 1 row affected (0.12 sec)

mysql> insert into Attendance values(372,'2016-01-06','01:00PM','22:00PM');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Attendance values(373,'2016-01-06','03:00PM','24:00AM');
Query OK, 1 row affected (0.13 sec)

mysql> insert into Attendance values(374,'2016-01-07','09:00AM','06:00PM');
Query OK, 1 row affected (0.06 sec)

mysql> select * from Attendance;
+--------------+------------+-------------+------------+
| AttendanceId | AttendDate | TimeofEntry | TimeofExit |
+--------------+------------+-------------+------------+
|          350 | 2016-01-01 | 09:00AM     | 06:00PM    |
|          351 | 2016-01-01 | 12:30PM     | 21:30PM    |
|          352 | 2016-01-01 | 01:00PM     | 22:00PM    |
|          353 | 2016-01-01 | 09:00AM     | 06:00PM    |
|          354 | 2016-01-01 | 12:30PM     | 21:30PM    |
|          355 | 2016-01-01 | 01:00AM     | 22:00PM    |
|          356 | 2016-01-01 | 03:00PM     | 24:00AM    |
|          357 | 2016-01-01 | 18:00PM     | 03:00AM    |
|          358 | 2016-01-01 | 09:00AM     | 06:00PM    |
|          359 | 2016-01-02 | 09:00AM     | 06:00PM    |
|          360 | 2016-01-02 | 01:00PM     | 22:00PM    |
|          361 | 2016-01-02 | 01:00PM     | 22:00PM    |
|          362 | 2016-01-02 | 03:00PM     | 24:00AM    |
|          363 | 2016-01-02 | 03:00PM     | 24:00AM    |
|          364 | 2016-01-03 | 03:00PM     | 24:00AM    |
|          365 | 2016-01-03 | 18:00PM     | 03:00AM    |
|          366 | 2016-01-03 | 01:00PM     | 22:00PM    |
|          367 | 2016-01-03 | 03:00PM     | 24:00AM    |
|          368 | 2016-01-04 | 09:00AM     | 06:00PM    |
|          369 | 2016-01-05 | 8:00PM      | 03:00AM    |
|          370 | 2016-01-05 | 12:30PM     | 21:30PM    |
|          371 | 2016-01-05 | 12:30PM     | 21:30PM    |
|          372 | 2016-01-06 | 01:00PM     | 22:00PM    |
|          373 | 2016-01-06 | 03:00PM     | 24:00AM    |
|          374 | 2016-01-07 | 09:00AM     | 06:00PM    |
+--------------+------------+-------------+------------+
25 rows in set (0.00 sec)

mysql> insert into OperationTheatre values(601,35,1,'2021-11-11','6:45 am','12:00 pm');
onTheatre values(602,36,2,'2021-11-12','9:45 am','1:00 pm');
insert into OperationTheatre values(603,37,3,'2021-11-15','6:00 pm','8:00 pm');
insert into OperationTheatre values(604,38,4,'2021-11-16','6:45 pm','9:00 pm');
insert into OperationTheatre values(605,39,5,'2021-11-20','5:20 pm','9:00 pm');
insert into OperationTheatre values(606,40,6,'2021-11-22','9:00 am','12:00 pm');
insert into OperationTheatre values(607,41,7,'2021-11-25','6:15 pm','2:00 am');
insert into OperationTheatre values(608,42,8,'2021-11-27','4:00 pm','11:00 pm');
insert into OperationTheatre values(609,43,9,'2021-11-29','5:00 am','11:00 am');
insert into OperationTheatre values(610,44,10,'2021-11-30','3:25 pm','9:00 pm');
insert into OperationTheatre values(611,45,11,'2021-12-01','2:00 pm','5:00 pm');
insert into OperationTheatre values(612,46,12,'2021-12-02','2:10 pm','12:00 am');
insert into OperationTheatre values(613,47,13,'2021-12-04','2:15 pm','7:00 pm');
insert into OperationTheatre values(614,48,14,'2021Query OK, 1 row affected (0.11 sec)

mysql> insert into OperationTheatre values(602,36,2,'2021-11-12','9:45 am','1:00 pm');
-12-10','2:20 pm','4:00 pm');
insert into OperationTheatre values(615,49,15,'2021-12-12','2:45 pm','6:00 pm');
insert into OperationTheatre values(616,50,16,'2021-12-13','3:15 pm','7:00 pm');
insert into OperationTheatre values(617,51,17,'2021-12-24','2:15 pm','7:00 pm');
insert into OperationTheatre values(618,52,18,'2021-12-24','7:15 pm','9:00 pm');
insert into OperationTheatre values(619,53,19,'2022-12-04','4:15 pm','9:00 pm');
insert into OperationTheatre values(620,54,20,'2022-01-12','7:15 pm','10:00 pm');
insert into OperationTheatre values(621,55,21,'2022-01-14','10:15 pm','1:00 am');
iQuery OK, 1 row affected (0.07 sec)

mysql> insert into OperationTheatre values(603,37,3,'2021-11-15','6:00 pm','8:00 pm');
nsert into OperationTheatre values(622,56,22,'2022-01-24','4:15 pm','10:00 pm');
insert into OperationTheatre values(623,57,23,'2022-01-26','9:15 pm','12:00 am');
insert into OperationTheatre values(624,58,24,'2022-03-24','4:15 pm','9:00 pm');
insert into OperationTheatre values(625,59,25,'2022-03-14','10:25 am','9:00 pm');Query OK, 1 row affected (0.10 sec)

mysql> insert into OperationTheatre values(604,38,4,'2021-11-16','6:45 pm','9:00 pm');
Query OK, 1 row affected (0.06 sec)

mysql> insert into OperationTheatre values(605,39,5,'2021-11-20','5:20 pm','9:00 pm');
Query OK, 1 row affected (0.24 sec)

mysql> insert into OperationTheatre values(606,40,6,'2021-11-22','9:00 am','12:00 pm');
Query OK, 1 row affected (0.80 sec)

mysql> insert into OperationTheatre values(607,41,7,'2021-11-25','6:15 pm','2:00 am');
Query OK, 1 row affected (0.22 sec)

mysql> insert into OperationTheatre values(608,42,8,'2021-11-27','4:00 pm','11:00 pm');
Query OK, 1 row affected (0.13 sec)

mysql> insert into OperationTheatre values(609,43,9,'2021-11-29','5:00 am','11:00 am');
Query OK, 1 row affected (0.09 sec)

mysql> insert into OperationTheatre values(610,44,10,'2021-11-30','3:25 pm','9:00 pm');
Query OK, 1 row affected (0.14 sec)

mysql> insert into OperationTheatre values(611,45,11,'2021-12-01','2:00 pm','5:00 pm');
Query OK, 1 row affected (0.97 sec)

mysql> insert into OperationTheatre values(612,46,12,'2021-12-02','2:10 pm','12:00 am');
Query OK, 1 row affected (0.14 sec)

mysql> insert into OperationTheatre values(613,47,13,'2021-12-04','2:15 pm','7:00 pm');
Query OK, 1 row affected (0.14 sec)

mysql> insert into OperationTheatre values(614,48,14,'2021-12-10','2:20 pm','4:00 pm');
Query OK, 1 row affected (0.09 sec)

mysql> insert into OperationTheatre values(615,49,15,'2021-12-12','2:45 pm','6:00 pm');
Query OK, 1 row affected (0.09 sec)

mysql> insert into OperationTheatre values(616,50,16,'2021-12-13','3:15 pm','7:00 pm');
Query OK, 1 row affected (0.09 sec)

mysql> insert into OperationTheatre values(617,51,17,'2021-12-24','2:15 pm','7:00 pm');
Query OK, 1 row affected (0.10 sec)

mysql> insert into OperationTheatre values(618,52,18,'2021-12-24','7:15 pm','9:00 pm');
Query OK, 1 row affected (0.13 sec)

mysql> insert into OperationTheatre values(619,53,19,'2022-12-04','4:15 pm','9:00 pm');
Query OK, 1 row affected (0.08 sec)

mysql> insert into OperationTheatre values(620,54,20,'2022-01-12','7:15 pm','10:00 pm');
Query OK, 1 row affected (0.10 sec)

mysql> insert into OperationTheatre values(621,55,21,'2022-01-14','10:15 pm','1:00 am');
Query OK, 1 row affected (0.08 sec)

mysql> insert into OperationTheatre values(622,56,22,'2022-01-24','4:15 pm','10:00 pm');
Query OK, 1 row affected (0.14 sec)

mysql> insert into OperationTheatre values(623,57,23,'2022-01-26','9:15 pm','12:00 am');
Query OK, 1 row affected (0.09 sec)

mysql> insert into OperationTheatre values(624,58,24,'2022-03-24','4:15 pm','9:00 pm');
Query OK, 1 row affected (0.09 sec)

mysql> insert into OperationTheatre values(625,59,25,'2022-03-14','10:25 am','9:00 pm');
Query OK, 1 row affected (0.07 sec)

mysql> select * from Nurses;
+---------+------------+---------------+-----------------------+-------------+
| NurseId | NurseEmpNo | NurseName     | NurseStation          | NurseTelNo  |
+---------+------------+---------------+-----------------------+-------------+
|     300 |       1000 | Debrah Lewis  | OPD                   | 9000543622  |
|     301 |       1001 | Gabriela      | IP                    | 9975344356  |
|     302 |       1002 | Maggie        | OT                    | 7999853654  |
|     303 |       1003 | Melissa       | OT                    | 9000056436  |
|     304 |       1004 | Hilma         | OT                    | 8000955463  |
|     305 |       1005 | Dicko         | IP                    | 8887764535  |
|     306 |       1006 | Fatoumata     | IP                    | 9000065432  |
|     307 |       1007 | Annette       | MRD                   | 9998885436  |
|     308 |       1008 | Sally         | MRD                   | 9225439876  |
|     309 |       1009 | Pairman       | Pharmacy              | 8874445327  |
|     310 |       1010 | Platel        | OPD                   | 8856437066  |
|     311 |       1011 | Claudine      | Pharmacy              | 563849654   |
|     312 |       1012 | Tekla         | MRD                   | 9112307653  |
|     313 |       1013 | Shipahu       | IP                    | 7765111096  |
|     314 |       1014 | Natangwe      | OPD                   | 9888334526  |
|     315 |       1015 | Teja          | Pharmacy              | 8332100953  |
|     316 |       1016 | Skodic        | IP                    | 8854398753  |
|     317 |       1017 | Zaksek        | Rehabilitation centre | 66670531124 |
|     318 |       1018 | Mary          | IP                    | 9004537528  |
|     319 |       1019 | Agholor       | OT                    | 9332105363  |
|     320 |       1020 | Edidong       | Rehabilitation centre | 6064283654  |
|     321 |       1021 | Asanga        | OT                    | 6362187537  |
|     322 |       1022 | Yoko Shimpuku | Rehabilitation centre | 6361072584  |
|     323 |       1023 | Albertha      | Pharmacy              | 8553676516  |
|     324 |       1024 | Freeman       | OT                    | 8970024365  |
|    1010 |       2211 | Nurse One     | Basr                  | 2342342341  |
|    2022 |      99889 | Nurse Nurse   | BASE                  | 1230891239  |
+---------+------------+---------------+-----------------------+-------------+
27 rows in set (0.00 sec)

mysql> INSERT INTO PatientPayments VALUES (801,10000,'2016-01-10',35);
802,16000,'2016-01-25',36);
INSERT INTO PatientPayments VALUES (803,98700,'2016-02-20',37);
INSERT INTO PatientPayments VALUES (804,45600,'2016-07-15',38);
INSERT INTO PatientPayments VALUES (805,32900,'2016-10-25',39);
INSERT INTO PatientPayments VALUES (806,80700,'2016-04-15',40);
INSERT INTO PatientPayments VALUES (807,54000,'2016-11-18',41);
INSERT INTO PatientPayments VALUES (808,43790,'2017-06-18',42);
INSERT INTO PatientPayments VALUES (809,76800,'2017-11-11',43);
INSERT INTO PatientPayments VALUES (810,27900,'2018-01-20',44);
INSERT INTQuery OK, 1 row affected (0.07 sec)

mysql> INSERT INTO PatientPayments VALUES (802,16000,'2016-01-25',36);
O PatientPayments VALUES (811,67090,'2017-02-01',45);
INSERT INTO PatientPayments VALUES (812,47800,'2017-09-22',46);
INSERT INTO PatientPayments VALUES (813,39000,'2017-10-12',47);
INSERT INTO PatientPayments VALUES (814,72980,'2017-10-13',48);
INSERT INTO PatientPayments VALUES (815,58900,'2016-08-25',49);
INSERT INTO PatientPayments VALUES (816,87600,'2016-03-30',50);
INSERT INTO PatientPayments VALUES (817,23450,'2016-04-20',51);
INSERT INTO PatientPayments VALUES (818,91000,'2016-07-05',53);
INSERT INTO PatientPayments VALUES (819,32400,'2016-12-21',54);
INSERT INTO PatientPayments VALUES (820,25700,'2017-03-11',55);
INSERT INTO PatientPayments VALUES (821,19000,'2017-03-30',56);
INSERTQuery OK, 1 row affected (0.07 sec)

mysql> INSERT INTO PatientPayments VALUES (803,98700,'2016-02-20',37);
 INTO PatientPayments VALUES (822,78000,'2017-04-30',57);
INSERT INTO PatientPayments VALUES (823,43900,'2018-01-20',38);
INSERT INTO PatientPayments VALUES (824,49200,'2018-01-20',45);
INSERT INTO PatientPayments VALUES (825,49200,'2017-07-25',35);Query OK, 1 row affected (0.11 sec)

mysql> INSERT INTO PatientPayments VALUES (804,45600,'2016-07-15',38);
Query OK, 1 row affected (0.10 sec)

mysql> INSERT INTO PatientPayments VALUES (805,32900,'2016-10-25',39);
Query OK, 1 row affected (0.09 sec)

mysql> INSERT INTO PatientPayments VALUES (806,80700,'2016-04-15',40);
Query OK, 1 row affected (0.10 sec)

mysql> INSERT INTO PatientPayments VALUES (807,54000,'2016-11-18',41);
Query OK, 1 row affected (0.58 sec)

mysql> INSERT INTO PatientPayments VALUES (808,43790,'2017-06-18',42);
Query OK, 1 row affected (0.78 sec)

mysql> INSERT INTO PatientPayments VALUES (809,76800,'2017-11-11',43);
Query OK, 1 row affected (0.13 sec)

mysql> INSERT INTO PatientPayments VALUES (810,27900,'2018-01-20',44);
Query OK, 1 row affected (0.07 sec)

mysql> INSERT INTO PatientPayments VALUES (811,67090,'2017-02-01',45);
Query OK, 1 row affected (0.07 sec)

mysql> INSERT INTO PatientPayments VALUES (812,47800,'2017-09-22',46);
Query OK, 1 row affected (0.10 sec)

mysql> INSERT INTO PatientPayments VALUES (813,39000,'2017-10-12',47);
Query OK, 1 row affected (0.10 sec)

mysql> INSERT INTO PatientPayments VALUES (814,72980,'2017-10-13',48);
Query OK, 1 row affected (0.10 sec)

mysql> INSERT INTO PatientPayments VALUES (815,58900,'2016-08-25',49);
Query OK, 1 row affected (0.10 sec)

mysql> INSERT INTO PatientPayments VALUES (816,87600,'2016-03-30',50);
Query OK, 1 row affected (0.10 sec)

mysql> INSERT INTO PatientPayments VALUES (817,23450,'2016-04-20',51);
Query OK, 1 row affected (0.10 sec)

mysql> INSERT INTO PatientPayments VALUES (818,91000,'2016-07-05',53);
Query OK, 1 row affected (0.10 sec)

mysql> INSERT INTO PatientPayments VALUES (819,32400,'2016-12-21',54);
Query OK, 1 row affected (0.07 sec)

mysql> INSERT INTO PatientPayments VALUES (820,25700,'2017-03-11',55);
Query OK, 1 row affected (0.11 sec)

mysql> INSERT INTO PatientPayments VALUES (821,19000,'2017-03-30',56);
Query OK, 1 row affected (0.14 sec)

mysql> INSERT INTO PatientPayments VALUES (822,78000,'2017-04-30',57);
Query OK, 1 row affected (0.14 sec)

mysql> INSERT INTO PatientPayments VALUES (823,43900,'2018-01-20',38);
Query OK, 1 row affected (0.09 sec)

mysql> INSERT INTO PatientPayments VALUES (824,49200,'2018-01-20',45);
Query OK, 1 row affected (0.09 sec)

mysql> INSERT INTO PatientPayments VALUES (825,49200,'2017-07-25',35);
Query OK, 1 row affected (0.07 sec)

mysql> select * from PatientPayments;
+-----------+---------------+-------------+-----------+
| PaymentId | PaymentAmount | PaymentDate | PatientId |
+-----------+---------------+-------------+-----------+
|       801 |         10000 | 2016-01-10  |        35 |
|       802 |         16000 | 2016-01-25  |        36 |
|       803 |         98700 | 2016-02-20  |        37 |
|       804 |         45600 | 2016-07-15  |        38 |
|       805 |         32900 | 2016-10-25  |        39 |
|       806 |         80700 | 2016-04-15  |        40 |
|       807 |         54000 | 2016-11-18  |        41 |
|       808 |         43790 | 2017-06-18  |        42 |
|       809 |         76800 | 2017-11-11  |        43 |
|       810 |         27900 | 2018-01-20  |        44 |
|       811 |         67090 | 2017-02-01  |        45 |
|       812 |         47800 | 2017-09-22  |        46 |
|       813 |         39000 | 2017-10-12  |        47 |
|       814 |         72980 | 2017-10-13  |        48 |
|       815 |         58900 | 2016-08-25  |        49 |
|       816 |         87600 | 2016-03-30  |        50 |
|       817 |         23450 | 2016-04-20  |        51 |
|       818 |         91000 | 2016-07-05  |        53 |
|       819 |         32400 | 2016-12-21  |        54 |
|       820 |         25700 | 2017-03-11  |        55 |
|       821 |         19000 | 2017-03-30  |        56 |
|       822 |         78000 | 2017-04-30  |        57 |
|       823 |         43900 | 2018-01-20  |        38 |
|       824 |         49200 | 2018-01-20  |        45 |
|       825 |         49200 | 2017-07-25  |        35 |
+-----------+---------------+-------------+-----------+
25 rows in set (0.00 sec)

mysql> desc create table AuditTable(
    -> 
    -> sa
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'create table AuditTable(

sa' at line 1
mysql> create table AuditTable(
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> desc AuditTable;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| NurseId   | int         | YES  |     | NULL    |       |
| PatientId | int         | YES  |     | NULL    |       |
| DoctId    | int         | YES  |     | NULL    |       |
| EntryDate | date        | YES  |     | NULL    |       |
| Operation | varchar(50) | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

mysql> CREATE OR REPLACE TRIGGER NursePatientDoctTrigger
    ->   before insert or update or delete
    ->   ON NursePatientDoct
    ->   for each row
    ->   enable
    ->   begin
    -> if inserting then
    ->  insert into AuditTable(NurseId,PatientId,DoctId,EntryDate,Operation)values(:NEW.NurseId,:NEW.PatientId,:NEW.DoctId,sysdate,'Insert');
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'TRIGGER NursePatientDoctTrigger
  before insert or update or delete
  ON NursePa' at line 1
mysql> ELSIF deleting then
    ->  insert into AuditTable(NurseId,PatientId,DoctId,EntryDate,Operation)values(:old.NurseId,:old.PatientId,:old.DoctId,sysdate,'Delete');
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ELSIF deleting then
 insert into AuditTable(NurseId,PatientId,DoctId,EntryDate,O' at line 1
mysql> ELSIF updating then 
    ->  insert into AuditTable(NurseId,PatientId,DoctId,EntryDate,Operation)values(:old.NurseId,:old.PatientId,:old.DoctId,sysdate,'update');
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ELSIF updating then 
 insert into AuditTable(NurseId,PatientId,DoctId,EntryDate,' at line 1
mysql> ELSE 
    ->     DBMS_OUTPUT.PUT_LINE('This code is not reachable.');
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ELSE 
    DBMS_OUTPUT.PUT_LINE('This code is not reachable.')' at line 1
mysql>  end if ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'end if' at line 1
mysql> end;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'end' at line 1
mysql> /
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '/' at line 1
mysql> 
mysql> 
mysql> 
mysql> 
mysql> 
mysql> 
mysql> 
mysql> 
mysql> 
mysql> 
mysql> 
mysql> 
mysql> 
mysql> SELECT
    ->     pd.patientname,
    ->     ps.diseaseid,
    ->     COUNT(ps.diseaseid) countofdisease
    -> FROM
    ->          patientdetails pd
    ->     INNER JOIN patientdisease ps ON pd.patientid = ps.patientid
    -> GROUP BY
    ->     pd.patientname,
    ->     ps.diseaseid
    -> HAVING
    ->     COUNT(ps.diseaseid) > 1;
ERROR 1146 (42S02): Table 'Capstone.patientdetails' doesn't exist
mysql> SELECT     pd.patientname,     ps.diseaseid,     COUNT(ps.diseaseid) countofdisease FROM          patientdetails pd     INNER JOIN patientdisease ps ON pd.patientid = ps.patientid GROUP BY     pd.patientname,     ps.diseaseid HAVING     COUNT(ps.diseaseid) > 1;
ERROR 1146 (42S02): Table 'Capstone.patientdetails' doesn't exist
mysql> desc PatientDetails;
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| PatientId   | int         | NO   | PRI | NULL    |       |
| PatientName | varchar(50) | NO   |     | NULL    |       |
| PatientAddr | varchar(50) | NO   |     | NULL    |       |
| Email       | varchar(50) | YES  |     | NULL    |       |
| Zipcode     | int         | NO   |     | NULL    |       |
| TelNo       | varchar(50) | YES  |     | NULL    |       |
| InsuranceId | int         | YES  | MUL | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
7 rows in set (0.00 sec)

mysql> show tables;
+--------------------+
| Tables_in_Capstone |
+--------------------+
| AssetsMaster       |
| Attendance         |
| AuditTable         |
| Disease            |
| Doctor             |
| EquipMaint         |
| Feedbacks          |
| InsuranceInfo      |
| NursePatientDoct   |
| Nurses             |
| OperationTheatre   |
| PatientDetails     |
| PatientDisease     |
| PatientMedicine    |
| PatientPayments    |
| ambulance          |
| canteen            |
+--------------------+
17 rows in set (0.00 sec)

mysql> desc Disease;
+--------------------+-------------+------+-----+---------+-------+
| Field              | Type        | Null | Key | Default | Extra |
+--------------------+-------------+------+-----+---------+-------+
| DiseaseID          | int         | NO   | PRI | NULL    |       |
| DiseaseDescription | varchar(50) | NO   |     | NULL    |       |
| Chronic            | varchar(5)  | NO   |     | NULL    |       |
+--------------------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

mysql> desc PatientDisease;
+------------------+------+------+-----+---------+-------+
| Field            | Type | Null | Key | Default | Extra |
+------------------+------+------+-----+---------+-------+
| PatientDiseaseId | int  | NO   | PRI | NULL    |       |
| PatientId        | int  | YES  | MUL | NULL    |       |
| DiseaseID        | int  | YES  | MUL | NULL    |       |
| DoctId           | int  | YES  | MUL | NULL    |       |
| StartDate        | date | YES  |     | NULL    |       |
| EndDates         | date | YES  |     | NULL    |       |
| MedicineId       | int  | YES  | MUL | NULL    |       |
+------------------+------+------+-----+---------+-------+
7 rows in set (0.00 sec)

mysql> SELECT
    ->     pd.PatientName,
    ->     ps.DiseaseID,
    ->     COUNT(ps.DiseaseID) countofdisease
    -> FROM
    ->          Patientdetails pd
    ->     INNER JOIN PatientDisease ps ON pd.PatientId = ps.PatientId
    -> GROUP BY
    ->     pd.PatientName,
    ->     ps.DiseaseID
    -> HAVING
    ->     COUNT(ps.DiseaseID) > 1;
ERROR 1146 (42S02): Table 'Capstone.Patientdetails' doesn't exist
mysql> SELECT
    ->     pd.PatientName,
    ->     ps.DiseaseID,
    ->     COUNT(ps.DiseaseID) countofdisease
    -> FROM
    ->          PatientDetails pd
    ->     INNER JOIN PatientDisease ps ON pd.PatientId = ps.PatientId
    -> GROUP BY
    ->     pd.PatientName,
    ->     ps.DiseaseID
    -> HAVING
    ->     COUNT(ps.DiseaseID) > 1;
Empty set (0.00 sec)

mysql> select * from PatientDisease;
+------------------+-----------+-----------+--------+------------+------------+------------+
| PatientDiseaseId | PatientId | DiseaseID | DoctId | StartDate  | EndDates   | MedicineId |
+------------------+-----------+-----------+--------+------------+------------+------------+
|              150 |        35 |        93 |      4 | 2016-01-01 | 2016-01-10 |        200 |
|              151 |        36 |       104 |      2 | 2016-01-20 | 2016-01-25 |        201 |
|              152 |        37 |       105 |     21 | 2016-02-01 | 2016-02-20 |        201 |
|              153 |        40 |       107 |     16 | 2016-03-15 | 2016-04-15 |        203 |
|              154 |        50 |       107 |     16 | 2016-03-25 | 2016-03-30 |        204 |
|              155 |        51 |        92 |     17 | 2016-04-15 | 2016-04-20 |        205 |
|              156 |        38 |        92 |     22 | 2016-07-05 | 2016-07-15 |        206 |
|              157 |        49 |        99 |     15 | 2016-08-17 | 2016-08-25 |        207 |
|              158 |        53 |       106 |     12 | 2016-08-25 | 2016-09-05 |        208 |
|              159 |        39 |        94 |      1 | 2016-10-05 | 2016-10-25 |        209 |
|              160 |        41 |       111 |     11 | 2016-11-08 | 2016-11-18 |        210 |
|              161 |        54 |        94 |      1 | 2016-12-01 | 2016-12-21 |        211 |
|              162 |        45 |       112 |     22 | 2017-01-01 | 2017-02-01 |        212 |
|              163 |        55 |        99 |     15 | 2017-02-16 | 2017-03-11 |        213 |
|              164 |        56 |       102 |     21 | 2017-03-21 | 2017-03-30 |        214 |
|              165 |        57 |        94 |      2 | 2017-04-01 | 2017-04-30 |        215 |
|              166 |        42 |        96 |      9 | 2017-06-05 | 2017-06-18 |        216 |
|              167 |        35 |       100 |      5 | 2017-07-16 | 2017-07-25 |        217 |
|              168 |        46 |        94 |      1 | 2017-09-05 | 2017-09-22 |        218 |
|              169 |        47 |        99 |     15 | 2017-10-01 | 2017-10-12 |        219 |
|              170 |        48 |       100 |      5 | 2017-10-01 | 2017-10-13 |        210 |
|              171 |        43 |       106 |     12 | 2017-11-01 | 2017-11-11 |        211 |
|              172 |        45 |        96 |      9 | 2018-01-11 | 2018-01-20 |        212 |
|              173 |        44 |        94 |      7 | 2018-01-11 | 2018-01-20 |        213 |
|              174 |        38 |       106 |     12 | 2018-01-15 | 2018-01-20 |        214 |
+------------------+-----------+-----------+--------+------------+------------+------------+