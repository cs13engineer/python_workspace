create table InsuranceInfo(
    InsuranceID int primary key,
    InsuringCompany varchar(50) not null,
    TypeofPlan varchar(50) not null,
    StartDate date,
    EndDates date
);

create table PatientDetails(
    PatientId int primary key,
    PatientName varchar(50) not null,
    PatientAddr varchar(50) not null,
    Email varchar(50),
    Zipcode int not null,
    TelNo varchar(50),
    InsuranceId int,
    CONSTRAINT FK_PatientInsurance FOREIGN KEY (InsuranceId)
    REFERENCES InsuranceInfo(InsuranceID)
);

create table Feedbacks(
    FeedbackId int primary key,
    FeedbackOn  varchar(50) not null,
    Texts varchar(50) not null,
    Dates date,
    PatientId int,
    CONSTRAINT FK_FeedbackPatient FOREIGN KEY (PatientId)
    REFERENCES PatientDetails(PatientId)
);

create table AssetsMaster(
    AssetId int primary key,
    PartId int,
    AssetStartDate DATE,
    AssetEndDate DATE,
    DepreciationPCT varchar(50)
);


create table EquipMaint(
    AssetId int,
    MaintDate Date ,
    MaintCompany varchar(50) ,
    CompTelNo varchar(50),
    Satisfactory varchar(10) ,
    CONSTRAINT FK_EquipM FOREIGN KEY (AssetId)
    REFERENCES AssetsMaster(AssetID)
);

create table Nurses(
    NurseId int primary key,
    NurseEmpNo int not null,
    NurseName varchar(50) not null,
    NurseStation varchar(50),
    NurseTelNo varchar(50)
);

create table Doctor(
    DoctId int primary key,
    DoctName varchar(50) not null,
    DoctSpeciality varchar(50),
    DoctTelNo varchar(50),
    Doctemail varchar(50)
);

create table NursePatientDoct(
    NurseId int,
    PatientId int,
    DoctId int,
    CONSTRAINT FK_OTTN FOREIGN KEY (NurseId) REFERENCES Nurses (NurseId),
    CONSTRAINT FK_OTT FOREIGN KEY (PatientId) REFERENCES PatientDetails (PatientID),
    CONSTRAINT FK_OPTT FOREIGN KEY (DoctId) REFERENCES Doctor (DoctID)
);

create table OperationTheatre(
    OPId int primary key,
    PatientId int ,
    DoctId int,
    DateofSurgery date not null,
    FromTime varchar(20),
    ToTime varchar(20),
    CONSTRAINT FK_OT FOREIGN KEY (PatientId) REFERENCES PatientDetails (PatientID),
    CONSTRAINT FK_OPT FOREIGN KEY (DoctId) REFERENCES Doctor (DoctID)
);

create table Attendance(
    AttendanceId int primary key,
    AttendDate Date ,
    TimeofEntry varchar(20) ,
    TimeofExit varchar(20)
);

create table PatientMedicine(
    MedicineId int primary key,
    Medicine1 varchar(50) not null,
    Medicine2 varchar(50) not null,
    Medicine3 varchar(50) ,
    Medicine4 varchar(50) ,
    Medicine5 varchar(50)
);

create table Disease(
    DiseaseID int primary key,
    DiseaseDescription varchar(50) not null,
    Chronic varchar(5) not null
);

create table PatientDisease(
    PatientDiseaseId int primary key,
    PatientId int, 
    DiseaseID int, 
    DoctId int,
    StartDate date,
    EndDates date,
    MedicineId int,
    CONSTRAINT FK_DiseaseMedicine FOREIGN KEY (MedicineId)
    REFERENCES PatientMedicine(MedicineId),

    CONSTRAINT FK_DiseasePatient FOREIGN KEY (PatientId)
    REFERENCES PatientDetails(PatientId),

    CONSTRAINT FK_DiseaseId FOREIGN KEY (DiseaseID)
    REFERENCES Disease(DiseaseID),

    CONSTRAINT FK_DiseaseDoctor FOREIGN KEY (DoctId)
    REFERENCES Doctor(DoctId)
);


create table PatientPayments(
    PaymentId int primary key,
    PaymentAmount int,
    PaymentDate date,
    PatientId int,
    CONSTRAINT FK_PatientPayments FOREIGN KEY (PatientId) REFERENCES PatientDetails (PatientID)
);

create table AuditTable(
    NurseId int,
    PatientId int,
    DoctId int,
    EntryDate date,
    Operation varchar(50)
);