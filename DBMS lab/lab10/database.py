import mysql.connector

mydb = mysql.connector.connect(host="localhost",user = "root",password="",database = "Railway2")
c=mydb.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS train_243(train_no INT, train_name TEXT, train_type TEXT, source TEXT, destination TEXT, availability TEXT)")

def add_data(train_no,train_name,train_type,source,destination,availabilty):
    c.execute("INSERT INTO train_243(train_no,train_name,train_type,source,destination,availability) VALUES (%s,%s,%s,%s,%s,%s)",(train_no,train_name,train_type,source,destination,availabilty))
    mydb.commit()

def view_trains():
    c.execute("SELECT * FROM train_243")
    data = c.fetchall()
    return data

def view_only_train():
    c.execute('SELECT train_name FROM train_243')
    data = c.fetchall()
    return data

def get_trains(train_name):
    c.execute('SELECT * FROM train_243 WHERE train_name ="{}"'.format(train_name))
    data = c.fetchall()
    return data

def edit_train(new_train_no, new_train_name, new_train_type, new_source, new_destination, new_availability, train_no, train_name, train_type, source, destination, availability):
        c.execute("UPDATE train_243 SET train_no=%s, train_name=%s, train_type=%s, source=%s, destination=%s, availability=%s WHERE train_no=%s and train_name=%s and train_type=%s and source=%s and destination=%s and availability=%s", (new_train_no, new_train_name, new_train_type, new_source, new_destination, new_availability, train_no, train_name, train_type, source, destination, availability))
        mydb.commit()
        c.execute("SELECT train_name from train_243")
        data = c.fetchall()
        return data

def delete_data(train_name):
    c.execute('SET FOREIGN_KEY_CHECKS=0')
    c.execute('DELETE FROM train_243 WHERE train_name="{}"'.format(train_name))
    mydb.commit()

def execute_query(query):
    str(query).replace(";", '')

    if "create" in str(query).lower():
        c.execute(query)
        mydb.commit()

    elif "read" or '*' in str(query).lower():
        c.execute(query)
        res = c.fetchall()
        return res,c.description

    elif "update" in str(query).lower():
        c.execute(query)
        mydb.commit()

    elif "delete" in str(query).lower():
        c.execute(query)
        mydb.commit()