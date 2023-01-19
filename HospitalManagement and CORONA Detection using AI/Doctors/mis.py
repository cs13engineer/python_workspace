from Database import connection

def test():
    print("\nTesting MIS****")

def one():
    db = connection.ConnectDB()
    dbCursor = db.cursor()

    query = """
            SELECT pt.PatientName, pd.DiseaseId FROM
            PatientDisease pd INNER JOIN PatientDetails pt ON
            pd.PatientId = pt.PatientId WHERE
            pd.DiseaseId IN ( SELECT PatientDisease.DiseaseId FROM PatientDisease GROUP BY PatientDisease.DiseaseId HAVING COUNT(PatientDisease.DiseaseId) > 1)
            ORDER BY 2;
            """
    # print(query)
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    db.close()
    print("+-------------+-----------+\n| PatientName | DiseaseId |\n+-------------+-----------+\n")
    for res in result:
        print(res[0],"\t",res[1])
    print("")


def two():
    db = connection.ConnectDB()
    dbCursor = db.cursor()

    query = """
            SELECT DISTINCT ( dd.doctname ), pd.patientname, cc.diseasedescription, cc.chronic FROM
            Doctor dd 
            INNER JOIN NursePatientDoct npd ON dd.doctid = npd.doctid 
            INNER JOIN PatientDetails pd ON pd.patientid = npd.patientid, Disease cc 
            INNER JOIN PatientDisease ps ON cc.diseaseid = ps.diseaseid
            limit 50;
            """
    # print(query)
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    db.close()
    print("+--------------+-------------+--------------------+---------+\n| doctname     | patientname | diseasedescription | chronic |\n+--------------+-------------+--------------------+---------+\n")
    for res in result:
        print(res[0],"\t",res[1],"\t\t",res[2],"\t",res[3])
    print("")


def two():
    db = connection.ConnectDB()
    dbCursor = db.cursor()

    query = """
            SELECT DISTINCT ( dd.doctname ), pd.patientname, cc.diseasedescription, cc.chronic FROM
            Doctor dd 
            INNER JOIN NursePatientDoct npd ON dd.doctid = npd.doctid 
            INNER JOIN PatientDetails pd ON pd.patientid = npd.patientid, Disease cc 
            INNER JOIN PatientDisease ps ON cc.diseaseid = ps.diseaseid
            limit 50;
            """
    # print(query)
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    db.close()
    print("+--------------+-------------+--------------------+---------+\n| doctname     | patientname | diseasedescription | chronic |\n+--------------+-------------+--------------------+---------+\n")
    for res in result:
        print(res[0],"\t",res[1],"\t\t",res[2],"\t",res[3])
    print("")



def three():
    db = connection.ConnectDB()
    dbCursor = db.cursor()

    query = """
            SELECT pp.patientid, pp.paymentdate, SUM(pp.paymentamount) totalamount FROM  PatientPayments pp 
            GROUP BY pp.paymentdate, pp.patientid;
            """
    # print(query)
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    db.close()
    print("+-----------+-------------+-------------+\n| patientid | paymentdate | totalamount |\n+-----------+-------------+-------------+")
    for res in result:
        print("\t",res[0],"\t",res[1],"\t",res[2])
    print("")


def four():
    db = connection.ConnectDB()
    dbCursor = db.cursor()

    query = """
            SELECT
                pd.patientname,
                ii.insuranceid,
                ii.insuringcompany,
                ii.startdate,
                ii.enddates
            FROM
                    PatientDetails pd
                INNER JOIN InsuranceInfo ii ON pd.insuranceid = ii.insuranceid
            GROUP BY
                pd.patientname,
                ii.insuranceid,
                ii.insuringcompany,
                ii.startdate,
                ii.enddates;
            """
    
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    db.close()
    print(
        """
    +----------------------+-------------+---------------------------+------------+------------+
    | patientname          | insuranceid | insuringcompany           | startdate  | enddates   |
    +----------------------+-------------+---------------------------+------------+------------+
        """
    )
    for res in result:
        print("\t",res[0],"\t",res[1],"\t",res[2],"\t",res[3],"\t",res[4])
    print("")


def five():
    db = connection.ConnectDB()
    dbCursor = db.cursor()

    query = """
            SELECT pd.patientname, ff.feedbackon, ff.texts, ff.dates FROM 
            Feedbacks ff INNER JOIN PatientDetails pd ON ff.patientid = pd.patientid;
        """
    
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    db.close()
    print(
        """
+-------------+---------------------+----------------------------------------+------------+
| patientname | feedbackon          | texts                                  | dates      |
+-------------+---------------------+----------------------------------------+------------+
        """
    )
    for res in result:
        print("\t",res[0],"\t",res[1],"\t",res[2],"\t",res[3])
    print("")



def six():
    db = connection.ConnectDB()
    dbCursor = db.cursor()

    query = """
            SELECT nn.nurseempno, 
            nn.nursename,  
            nn.nursestation,
            pd.patientname,
            dd.doctname
        FROM
            NursePatientDoct npd
            INNER JOIN PatientDetails pd ON npd.patientid = pd.patientid
            INNER JOIN Doctor         dd ON npd.doctid = dd.doctid
            INNER JOIN Nurses         nn ON npd.nurseid = nn.nurseid;
        """
    
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    db.close()
    print(
        """
+------------+---------------+-----------------------+-------------+--------------+
| nurseempno | nursename     | nursestation          | patientname | doctname     |
+------------+---------------+-----------------------+-------------+--------------+
        """
    )
    for res in result:
        print("\t",res[0],"\t",res[1],"\t",res[2],"\t",res[3],"\t",res[4])
    print("")

def seven():
    db = connection.ConnectDB()
    dbCursor = db.cursor()

    query = """
            SELECT
            dd.doctname,
            ot.opid,
            ot.dateofsurgery,
            ot.fromtime,
            ot.totime,
            pd.patientname
        FROM
                OperationTheatre ot
            INNER JOIN Doctor         dd ON ot.doctid = dd.doctid
            INNER JOIN PatientDetails pd ON ot.patientid = pd.patientid;
        """
    
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    db.close()
    print(
        """
+--------------+------+---------------+----------+----------+-------------+
| doctname     | opid | dateofsurgery | fromtime | totime   | patientname |
+--------------+------+---------------+----------+----------+-------------+
        """
    )
    for res in result:
        print(res[0],"\t",res[1],"\t",res[2],"\t",res[3],"\t",res[4],"\t",res[5])
    print("")


def eight():
    db = connection.ConnectDB()
    dbCursor = db.cursor()

    query = """
        SELECT
             am.assetid,
             am.assetstartdate,
             am.assetenddate,
             emt.maintcompany,
             emt.satisfactory,
             am.depreciationpct
         FROM
                  AssetsMaster am
             INNER JOIN EquipMaint emt ON am.assetid = emt.assetid;
        """
    
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    db.close()
    print(
        """
+---------+----------------+--------------+--------------+--------------+-----------------+
| assetid | assetstartdate | assetenddate | maintcompany | satisfactory | depreciationpct |
+---------+----------------+--------------+--------------+--------------+-----------------+
        """
    )
    for res in result:
        print(res[0],"\t\t",res[1],"\t",res[2],"\t",res[3],"\t",res[4],"\t",res[5])
    print("")


def nine():
    db = connection.ConnectDB()
    dbCursor = db.cursor()

    query = """
        SELECT
            pd.patientname,
            dd.diseasedescription,
            dd.chronic,
            ps.startdate,
            ps.enddates
        FROM
                 PatientDetails pd
            INNER JOIN PatientDisease ps ON pd.patientid = ps.patientid
            INNER JOIN Disease        dd ON ps.diseaseid = dd.diseaseid;
        """
    
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    db.close()
    print(
        """
+-------------+--------------------+---------+------------+------------+
| patientname | diseasedescription | chronic | startdate  | enddates   |
+-------------+--------------------+---------+------------+------------+
        """
    )
    for res in result:
        print(res[0],"\t",res[1],"\t",res[2],"\t",res[3],"\t",res[4])
    print("")

def ten():
    db = connection.ConnectDB()
    dbCursor = db.cursor()

    query = """
        SELECT
             am.assetid,
             am.assetstartdate,
             am.assetenddate,
             am.depreciationpct
         FROM
             AssetsMaster am
         GROUP BY
             am.assetid,
             am.assetstartdate,
             am.assetenddate,
             am.depreciationpct;
        """
    
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    db.close()
    print(
        """
+---------+----------------+--------------+-----------------+
| assetid | assetstartdate | assetenddate | depreciationpct |
+---------+----------------+--------------+-----------------+
        """
    )
    for res in result:
        print(res[0],"\t\t",res[1],"\t",res[2],"\t",res[3])
    print("")