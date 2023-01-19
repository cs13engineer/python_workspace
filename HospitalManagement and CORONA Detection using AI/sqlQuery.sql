


select * from PatientDisease; 

select * from PatientMedicine;


select * from Feedbacks;


select * from AssetsMaster;


select * from EquipMaint;

select * from Attendance;



select * from OperationTheatre;

select * from Nurses;







select * from PatientPayments;


create table AuditTable(
NurseId number(5),
PatientId number(5),
DoctId number(5),
EntryDate date,
Operation varchar2(50)
);

CREATE OR REPLACE TRIGGER NursePatientDoctTrigger
  before insert or update or delete
  ON NursePatientDoct
  for each row
  enable
  begin
if inserting then
 insert into AuditTable(NurseId,PatientId,DoctId,EntryDate,Operation)values(:NEW.NurseId,:NEW.PatientId,:NEW.DoctId,sysdate,'Insert');
ELSIF deleting then
 insert into AuditTable(NurseId,PatientId,DoctId,EntryDate,Operation)values(:old.NurseId,:old.PatientId,:old.DoctId,sysdate,'Delete');
ELSIF updating then 
 insert into AuditTable(NurseId,PatientId,DoctId,EntryDate,Operation)values(:old.NurseId,:old.PatientId,:old.DoctId,sysdate,'update');
ELSE 
    DBMS_OUTPUT.PUT_LINE('This code is not reachable.');
 end if ;
end;
/





--1
SELECT
    pd.PatientName,
    ps.DiseaseID,
    COUNT(ps.DiseaseID) countofdisease
FROM
         PatientDetails pd
    INNER JOIN PatientDisease ps ON pd.PatientId = ps.PatientId
GROUP BY
    pd.PatientName,
    ps.DiseaseID
HAVING
    COUNT(ps.DiseaseID) > 1;

--2

SELECT DISTINCT
    ( dd.doctname ),
    pd.patientname,
    cc.diseasedescription,
    cc.chronic
FROM
         doctor dd
    INNER JOIN nursepatientdoct npd ON dd.doctid = npd.doctid
    INNER JOIN patientdetails   pd ON pd.patientid = npd.patientid, disease cc
    INNER JOIN patientdisease   ps ON cc.diseaseid = ps.diseaseid;


--3

SELECT
    patientpayments.paymentdate,
    patientpayments.patientid,
    SUM(patientpayments.paymentamount) totalamount
FROM
    patientpayments
GROUP BY
    patientpayments.paymentdate,
    patientpayments.patientid;
	
--4	
SELECT
    pd.patientname,
    ii.insuranceid,
    ii.insuringcompany,
    ii.startdate,
    ii.enddates
FROM
         patientdetails pd
    INNER JOIN insuranceinfo ii ON pd.insuranceid = ii.insuranceid
GROUP BY
    pd.patientname,
    ii.insuranceid,
    ii.insuringcompany,
    ii.startdate,
    ii.enddates;
	
--5

SELECT
    pd.patientname,
    ff.feedbackon,
    ff.texts,
    ff.dates
FROM
         feedbacks ff
    INNER JOIN patientdetails pd ON ff.patientid = pd.patientid;
	
	
--6

SELECT
    nn.nurseempno,
    nn.nursename,
    nn.nursestation,
    pd.patientname,
    dd.doctname
FROM
         nursepatientdoct npd
    INNER JOIN patientdetails pd ON npd.patientid = pd.patientid
    INNER JOIN doctor         dd ON npd.doctid = dd.doctid
    INNER JOIN nurses         nn ON npd.nurseid = nn.nurseid;
	
	
--7

SELECT
    dd.doctname,
    ot.opid,
    ot.dateofsurgery,
    ot.fromtime,
    ot.totime,
    pd.patientname
FROM
         operationtheatre ot
    INNER JOIN doctor         dd ON ot.doctid = dd.doctid
    INNER JOIN patientdetails pd ON ot.patientid = pd.patientid;


--8

SELECT
    am.assetid,
    am.assetstartdate,
    am.assetenddate,
    emt.maintcompany,
    emt.satisfactory,
    am.depreciationpct
FROM
         assetsmaster am
    INNER JOIN equipmaint emt ON am.assetid = emt.assetid;
	
--9

SELECT
    pd.patientname,
    dd.diseasedescription,
    dd.chronic,
    ps.startdate,
    ps.enddates
FROM
         patientdetails pd
    INNER JOIN patientdisease ps ON pd.patientid = ps.patientid
    INNER JOIN disease        dd ON ps.diseaseid = dd.diseaseid;
	
--10
SELECT
    am.assetid,
    am.assetstartdate,
    am.assetenddate,
    am.depreciationpct
FROM
    assetsmaster am
GROUP BY
    am.assetid,
    am.assetstartdate,
    am.assetenddate,
    am.depreciationpct;





select * from PatientDetails where PatientId in ( select ps.PatientId from PatientDetails ps, PatientDisease pd where ps.PatientId = pd.PatientId group by pd.PatientId having count(ps.DiseaseID)>1);


select * from PatientDetails where PatientId in ( select ps.PatientId from PatientDetails ps, PatientDisease pd where pd.DiseaseID = pd.DiseaseID group by pd.PatientId having count(pd.PatientId)>1);

select * from PatientDetails where PatientId in(select PatientId from PatientDisease where DiseaseID in (select DiseaseId from PatientDisease group by DiseaseId having count(DiseaseId)>1));
+-----------+
| PatientId |
+-----------+
|        40 |
|        50 |
|        51 |
|        38 |
|        49 |
|        53 |
|        39 |
|        54 |
|        55 |
|        57 |
|        42 |
|        35 |
|        46 |
|        47 |
|        48 |
|        43 |
|        45 |
|        44 |
|        38 |
+-----------+