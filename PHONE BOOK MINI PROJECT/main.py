import sys
import cx_Oracle
from PySide2 import *
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMessageBox
from geopy.geocoders import Nominatim


import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

# from PySide2.QtWidgets import
from ui_contact import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.home_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        )
        self.ui.insert_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.insert)
        )
        self.ui.update_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.update)
        )
        self.ui.delete_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.delete_2)
        )
        self.ui.search_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search)
        )

        self.ui.search_2.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.single_search)
        )
        self.ui.search_all.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.all_search)
        )
        self.ui.restore_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        )
        # self.ui.logout.clicked.connect(
        #     lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.login_page)
        # )
        self.ui.check.clicked.connect(self.check_display)
        self.ui.logout.clicked.connect(self.back)
        self.ui.home_show.clicked.connect(self.home_show)

        self.ui.i_add.clicked.connect(self.add_data)

        self.ui.d_search.clicked.connect(self.delete_show)

        self.ui.d_delete_btn.clicked.connect(self.delete_confirm)

        self.ui.u_search_btn_3.clicked.connect(self.update_show)

        self.ui.u_update_btn_3.clicked.connect(self.update_confirm)

        self.ui.search_all.clicked.connect(self.search_all_show)

        self.ui.single_search_btn.clicked.connect(self.search_single_show)

        self.ui.login_btn_3.clicked.connect(self.login)

        self.ui.i_clear_btn.clicked.connect(self.insert_clear)

        self.ui.u_clear_btn_3.clicked.connect(self.update_clear)

        self.ui.restore.clicked.connect(self.restore_data)

        self.ui.p_delete.clicked.connect(self.permanent_delete_confirm)

        self.ui.r_show.clicked.connect(self.r_display)

        self.ui.tableWidget_9.setColumnWidth(0, 100)
        self.ui.tableWidget_9.setColumnWidth(1, 250)
        self.ui.tableWidget_9.setColumnWidth(2, 250)
        self.ui.tableWidget_9.setColumnWidth(3, 200)
        self.ui.tableWidget_9.setColumnWidth(4, 200)
        self.ui.tableWidget_9.setColumnWidth(5, 150)
        self.ui.tableWidget_9.setColumnWidth(6, 150)
        self.ui.tableWidget_9.setColumnWidth(7, 100)
        self.ui.tableWidget_9.setColumnWidth(8, 200)
        self.ui.tableWidget_9.setColumnWidth(9, 150)
        self.ui.tableWidget_9.setColumnWidth(10, 150)
        self.ui.tableWidget_9.setColumnWidth(11, 150)
        self.ui.tableWidget_9.setColumnWidth(12, 150)
        self.ui.tableWidget_9.setColumnWidth(13, 150)
        self.ui.tableWidget_9.setColumnWidth(14, 150)
        self.ui.tableWidget_9.setColumnWidth(15, 150)
        self.ui.tableWidget_9.setColumnWidth(16, 150)

        self.ui.tableWidget_3.setColumnWidth(0, 100)
        self.ui.tableWidget_3.setColumnWidth(1, 250)
        self.ui.tableWidget_3.setColumnWidth(2, 250)
        self.ui.tableWidget_3.setColumnWidth(3, 200)
        self.ui.tableWidget_3.setColumnWidth(4, 200)
        self.ui.tableWidget_3.setColumnWidth(5, 150)
        self.ui.tableWidget_3.setColumnWidth(6, 150)
        self.ui.tableWidget_3.setColumnWidth(7, 100)
        self.ui.tableWidget_3.setColumnWidth(8, 200)
        self.ui.tableWidget_3.setColumnWidth(9, 150)
        self.ui.tableWidget_3.setColumnWidth(10, 150)
        self.ui.tableWidget_3.setColumnWidth(11, 150)
        self.ui.tableWidget_3.setColumnWidth(12, 150)
        self.ui.tableWidget_3.setColumnWidth(13, 150)
        self.ui.tableWidget_3.setColumnWidth(14, 150)
        self.ui.tableWidget_3.setColumnWidth(15, 150)
        self.ui.tableWidget_3.setColumnWidth(16, 150)

        self.ui.tableWidget_4.setColumnWidth(0, 100)
        self.ui.tableWidget_4.setColumnWidth(1, 250)
        self.ui.tableWidget_4.setColumnWidth(2, 250)
        self.ui.tableWidget_4.setColumnWidth(3, 200)
        self.ui.tableWidget_4.setColumnWidth(4, 200)
        self.ui.tableWidget_4.setColumnWidth(5, 150)
        self.ui.tableWidget_4.setColumnWidth(6, 150)
        self.ui.tableWidget_4.setColumnWidth(7, 100)
        self.ui.tableWidget_4.setColumnWidth(8, 200)
        self.ui.tableWidget_4.setColumnWidth(9, 150)
        self.ui.tableWidget_4.setColumnWidth(10, 150)
        self.ui.tableWidget_4.setColumnWidth(11, 150)
        self.ui.tableWidget_4.setColumnWidth(12, 150)
        self.ui.tableWidget_4.setColumnWidth(13, 150)
        self.ui.tableWidget_4.setColumnWidth(14, 150)
        self.ui.tableWidget_4.setColumnWidth(15, 150)
        self.ui.tableWidget_4.setColumnWidth(16, 150)

        self.ui.tableWidget_6.setColumnWidth(0, 100)
        self.ui.tableWidget_6.setColumnWidth(1, 250)
        self.ui.tableWidget_6.setColumnWidth(2, 250)
        self.ui.tableWidget_6.setColumnWidth(3, 200)
        self.ui.tableWidget_6.setColumnWidth(4, 200)
        self.ui.tableWidget_6.setColumnWidth(5, 150)
        self.ui.tableWidget_6.setColumnWidth(6, 150)
        self.ui.tableWidget_6.setColumnWidth(7, 100)
        self.ui.tableWidget_6.setColumnWidth(8, 200)
        self.ui.tableWidget_6.setColumnWidth(9, 150)
        self.ui.tableWidget_6.setColumnWidth(10, 150)
        self.ui.tableWidget_6.setColumnWidth(11, 150)
        self.ui.tableWidget_6.setColumnWidth(12, 150)
        self.ui.tableWidget_6.setColumnWidth(13, 200)
        self.ui.tableWidget_6.setColumnWidth(14, 200)
        self.ui.tableWidget_6.setColumnWidth(15, 200)
        self.ui.tableWidget_6.setColumnWidth(16, 200)

        self.ui.tableWidget_7.setColumnWidth(0, 100)
        self.ui.tableWidget_7.setColumnWidth(1, 250)
        self.ui.tableWidget_7.setColumnWidth(2, 200)
        self.ui.tableWidget_7.setColumnWidth(3, 250)
        self.ui.tableWidget_7.setColumnWidth(4, 200)
        self.ui.tableWidget_7.setColumnWidth(5, 150)
        self.ui.tableWidget_7.setColumnWidth(6, 150)
        self.ui.tableWidget_7.setColumnWidth(7, 100)
        self.ui.tableWidget_7.setColumnWidth(8, 200)
        self.ui.tableWidget_7.setColumnWidth(9, 150)
        self.ui.tableWidget_7.setColumnWidth(10, 150)
        self.ui.tableWidget_7.setColumnWidth(11, 150)
        self.ui.tableWidget_7.setColumnWidth(12, 150)
        self.ui.tableWidget_7.setColumnWidth(13, 150)
        self.ui.tableWidget_7.setColumnWidth(14, 150)
        self.ui.tableWidget_7.setColumnWidth(15, 150)
        self.ui.tableWidget_7.setColumnWidth(16, 150)

        self.ui.tableWidget_8.setColumnWidth(0, 100)
        self.ui.tableWidget_8.setColumnWidth(1, 250)
        self.ui.tableWidget_8.setColumnWidth(2, 250)
        self.ui.tableWidget_8.setColumnWidth(3, 200)
        self.ui.tableWidget_8.setColumnWidth(4, 200)
        self.ui.tableWidget_8.setColumnWidth(5, 150)
        self.ui.tableWidget_8.setColumnWidth(6, 150)
        self.ui.tableWidget_8.setColumnWidth(7, 100)
        self.ui.tableWidget_8.setColumnWidth(8, 200)
        self.ui.tableWidget_8.setColumnWidth(9, 150)
        self.ui.tableWidget_8.setColumnWidth(10, 150)
        self.ui.tableWidget_8.setColumnWidth(11, 150)
        self.ui.tableWidget_8.setColumnWidth(12, 150)
        self.ui.tableWidget_8.setColumnWidth(13, 150)
        self.ui.tableWidget_8.setColumnWidth(14, 150)
        self.ui.tableWidget_8.setColumnWidth(15, 150)
        self.ui.tableWidget_8.setColumnWidth(16, 150)

        self.show()

    def login(self):
        user = "user"
        passw = "phonebook@1234"
        user_text = self.ui.user_login.text()
        pass_text = self.ui.password_login.text()
        if user_text == user and pass_text == passw:
            self.ui.login_btn_3.clicked.connect(
                lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.main_page)
            )
        else:
            self.message("Invaild User/password")

    def back(self):
        self.ui.logout.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.login_page)
        )

    def message(self, text):
        QMessageBox.warning(self, "Warning", f"{text}")

    def information(self, text):
        QMessageBox.information(self, "Information", f"{text}")

    def SQL_insert(self, query):
        try:
            con = cx_Oracle.connect("contact_management/user123@localhost")
            cursor = con.cursor()
            cursor.execute(query)
            con.commit()
            print("Record inserted successfully")

        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)

        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

    def SQL_delete(self, query):
        try:
            con = cx_Oracle.connect("contact_management/user123@localhost")
            cursor = con.cursor()
            cursor.execute(query)
            con.commit()
            print("Record deleted successfully")

        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)

        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

    def SQL_retrive(self, query):
        try:
            con = cx_Oracle.connect("contact_management/user123@localhost")
            cur = con.cursor()
            print(con.version)

            cur.execute(query)
            rows = cur.fetchall()
            return rows
        except cx_Oracle.DatabaseError as er:
            print("There is an error in the Oracle database:", er)

        finally:
            if cur:
                cur.close()
            if con:
                con.close()

    def SQL_update(self, query):
        try:
            con = cx_Oracle.connect("contact_management/user123@localhost")
            cursor = con.cursor()
            cursor.execute(query)
            con.commit()
            print("Record updated successfully")

        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)

        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

    def contact_id(self):
        rows = self.SQL_retrive("select * from contact")
        r_rows = self.SQL_retrive("select c_id from RESTORE")
        ls1 = []
        for tup in r_rows:
            ls1.append(tup[0])
        ls = [100]
        for tup in rows:
            ls.append(tup[0])
        max_id = max(ls) + 1
        while True:
            if max_id in ls1:
                max_id += 1
            else:
                break
        return max_id

    def return_phno(self):
        phno = []
        rows = self.SQL_retrive("select * from contact")
        for tup in rows:
            phno.append(tup[3])
        return phno

    def add_data(self):
        # print("add")
        max_id = 100

        c_id = self.contact_id()
        print(c_id)
        name = self.ui.i_name.text()
        phno_value = self.ui.comboBox.currentText()
        phno = self.ui.i_phno.text()
        email = self.ui.i_email.text()
        relationship = self.ui.i_relationship.currentText()
        types = self.ui.i_type.currentText()
        dob = self.ui.i_dob.text()
        hno = self.ui.i_hno.text()
        hname = self.ui.i_hname.text()
        area = self.ui.i_area.text()
        # city = self.ui.i_city.text()
        # state = self.ui.i_state.text()
        pincode = self.ui.i_pincode.text()
        lst = self.return_phno()
        new_phno = phno[1:]
        if new_phno in lst:
            self.message("already exist")
        else:
            try:
                number = ph.parse(phno)
                time_zone = timezone.time_zones_for_number(number)
                print(time_zone)
                company = carrier.name_for_number(number, "en")
                country = geocoder.description_for_number(number, "en")
                code = phno[0:3]
                if len(company) == 0:
                    company = "N/A"
                    if code == "+91":
                        if country in ["Mumbai", "New Delhi"]:
                            company = "MTNL"
                        else:
                            company = "BSNL"
                print(company)

                geolocator = Nominatim(user_agent="geoapiExcercises")
                code = pincode
                location = geolocator.geocode(code)
                d = list(location)[0].split(",")
                print(d)
                district = d[1]
                state = d[2]
                print(district, state)
                if time_zone[0] == "Etc/Unknown":
                    self.message("Invalid phno")
                else:
                    z_rows = self.SQL_retrive(
                        f"select * from zipcode where PINCODE = '{pincode}'"
                    )
                    print(z_rows, "<---------------------")
                    if len(z_rows) == 0:
                        self.SQL_insert(
                            f"insert into zipcode values('{district}','{state}','{pincode}')"
                        )
                    self.SQL_insert(
                        f"insert into contact values({c_id},'{name}','{email}',{phno},'{relationship}','{types}','{dob}','{pincode}')"
                    )
                    self.SQL_insert(
                        f"insert into ADDRESS_1 values({c_id},'{hno}','{hname}','{area}','{pincode}')"
                    )

                    self.SQL_insert(
                        f"insert into details values({c_id},{phno},'{time_zone[0]}','{company}','{country}','{phno_value}')"
                    )
                    self.information("inserted successfully")
            except:
                self.message("Invalid phno / Invalid pincode / slow internet")

        self.insert_show()

    def insert_show(self):
        rows = self.SQL_retrive(
            "select c.c_id,c.name,c.email,c.phno,c.RELATIONSHIP,c.type,c.dob,a.hno,a.hname,a.area,z.city,z.state,c.pincode,d.ZONE,d.COMPANY,d.LOCATION,d.PHNO_TYPE from DETAILS d,contact c,address_1 a,zipcode z where c.pincode=z.pincode and a.c_id=c.c_id and d.c_id=c.c_id "
        )
        rowcount = len(rows)
        self.ui.tableWidget_9.setRowCount(rowcount)
        tablerow = 0
        rows.sort(key=lambda lst: lst[0], reverse=True)

        for tup in rows:
            i = 0
            for col in tup:
                self.ui.tableWidget_9.setItem(
                    tablerow, i, QtWidgets.QTableWidgetItem(str(tup[i]))
                )
                i += 1
            tablerow += 1

    def search_all_show(self):
        # print(c_id)
        rows = self.SQL_retrive(
            f"select c.c_id,c.name,c.email,c.phno,c.RELATIONSHIP,c.type,c.dob,a.hno,a.hname,a.area,z.city,z.state,c.pincode,d.zone,d.company,d.location,d.phno_type from contact c,address_1 a,zipcode z,DETAILS d where c.pincode=z.pincode and a.c_id=c.c_id and d.c_id=c.c_id"
        )

        rowcount = len(rows)
        self.ui.tableWidget_3.setRowCount(rowcount)
        tablerow = 0
        rows.sort(key=lambda lst: lst[0], reverse=False)

        for tup in rows:
            i = 0
            for col in tup:
                self.ui.tableWidget_3.setItem(
                    tablerow, i, QtWidgets.QTableWidgetItem(str(tup[i]))
                )
                i += 1
            tablerow += 1

    def home_show(self):
        # print(c_id)
        type_ = self.ui.home_combo.currentText()
        rows = self.SQL_retrive(
            f"select c.c_id,c.name,c.email,c.phno,c.RELATIONSHIP,c.type,c.dob,a.hno,a.hname,a.area,z.city,z.state,c.pincode,d.ZONE,d.COMPANY,d.LOCATION,d.PHNO_TYPE from DETAILS d,contact c,address_1 a,zipcode z where c.pincode=z.pincode and a.c_id=c.c_id and d.c_id=c.c_id and d.PHNO_TYPE='{type_}' "
        )
        rowcount = len(rows)
        self.ui.tableWidget_6.setRowCount(rowcount)
        tablerow = 0
        rows.sort(key=lambda lst: lst[0], reverse=False)

        for tup in rows:
            i = 0
            for col in tup:
                self.ui.tableWidget_6.setItem(
                    tablerow, i, QtWidgets.QTableWidgetItem(str(tup[i]))
                )
                i += 1
            tablerow += 1

    def r_display(self):
        rows = self.SQL_retrive(f"select * from RESTORE ")
        rowcount = len(rows)
        self.ui.tableWidget_7.setRowCount(rowcount)
        tablerow = 0
        rows.sort(key=lambda lst: lst[0], reverse=False)

        for tup in rows:
            i = 0
            for col in tup:
                self.ui.tableWidget_7.setItem(
                    tablerow, i, QtWidgets.QTableWidgetItem(str(tup[i]))
                )
                i += 1
            tablerow += 1

    def search_single_show(self):
        # print(c_id)
        item = self.ui.single_search_item.currentText()
        value = self.ui.single_search_value.text()
        lst = self.SQL_retrive(f"select c.name,c.phno from contact c ")
        n = []
        p = []
        for tup in lst:
            n.append(tup[0])
            p.append(tup[1])

        if item == "Name":
            value = self.ui.single_search_value.text()
            if value in n:
                query = f"select c.c_id,c.name,c.email,c.phno,c.RELATIONSHIP,c.type,c.dob,a.hno,a.hname,a.area,z.city,z.state,c.pincode,d.zone,d.company,d.location,d.phno_type from contact c,address_1 a,zipcode z,DETAILS d where c.pincode=z.pincode and a.c_id=c.c_id and c.c_id=d.c_id and c.name='{value}'"
            else:
                self.message(f"{value} not found")
        else:
            value = self.ui.single_search_value.text()
            if value in p and value.isdigit():
                query = f"select c.c_id,c.name,c.email,c.phno,c.RELATIONSHIP,c.type,c.dob,a.hno,a.hname,a.area,z.city,z.state,c.pincode,d.zone,d.company,d.location,d.phno_type from contact c,address_1 a,zipcode z,DETAILS d where c.pincode=z.pincode and a.c_id=c.c_id and c.c_id=d.c_id and c.phno={value}"
            else:
                self.message(f"{value} not found")
        rows = self.SQL_retrive(query)
        if len(rows) == 0:
            self.message("")
        rowcount = len(rows)
        self.ui.tableWidget_4.setRowCount(rowcount)
        tablerow = 0
        rows.sort(key=lambda lst: lst[0], reverse=False)

        for tup in rows:
            i = 0
            for col in tup:
                self.ui.tableWidget_4.setItem(
                    tablerow, i, QtWidgets.QTableWidgetItem(str(tup[i]))
                )
                i += 1
            tablerow += 1

    def delete_show(self):
        item = self.ui.d_search_item.currentText()
        value = self.ui.d_search_value.text()
        lst = self.SQL_retrive(f"select c.c_id,c.phno from contact c ")
        c = []
        p = []
        for tup in lst:
            c.append(tup[0])
            p.append(tup[1])
        if int(value) in c or value in p:
            if item == "C_id":
                value = self.ui.d_search_value.text()
                if value.isdigit():
                    query = f"select c.c_id,c.name,c.email,c.phno,c.RELATIONSHIP,c.type,c.dob,a.hno,a.hname,a.area,z.city,z.state,c.pincode,d.ZONE,d.COMPANY,d.location,d.PHNO_TYPE from DETAILS d,contact c,address_1 a,zipcode z where c.pincode=z.pincode and a.c_id=c.c_id and d.c_id=c.c_id and c.c_id={int(value)} "
                else:
                    self.message("invalid input")
            else:
                value = self.ui.d_search_value.text()
                if value.isdigit():
                    query = f"select c.c_id,c.name,c.email,c.phno,c.RELATIONSHIP,c.type,c.dob,a.hno,a.hname,a.area,z.city,z.state,c.pincode,d.ZONE,d.COMPANY,d.location,d.PHNO_TYPE from DETAILS d,contact c,address_1 a,zipcode z where c.pincode=z.pincode and a.c_id=c.c_id and d.c_id=c.c_id and d.PHNO={value} "
                else:
                    self.message("invalid input")
            rows = self.SQL_retrive(query)

            rowcount = len(rows)
            self.ui.tableWidget_8.setRowCount(rowcount)
            tablerow = 0
            rows.sort(key=lambda lst: lst[0], reverse=False)

            for tup in rows:
                i = 0
                for col in tup:
                    self.ui.tableWidget_8.setItem(
                        tablerow, i, QtWidgets.QTableWidgetItem(str(tup[i]))
                    )
                    i += 1
                tablerow += 1
        else:
            self.message("Search not found")

    def delete_confirm(self):
        item = self.ui.d_search_item.currentText()

        if item == "C_id":
            value = self.ui.d_search_value.text()
            # self.SQL_delete(f"delete from contact where c_id={int(value)}")
            rows = self.SQL_retrive(
                f"select c.c_id,c.name,c.email,c.phno,c.RELATIONSHIP,c.type,c.dob,c.pincode,a.hno,a.hname,a.area,z.city,z.state,d.ZONE,d.COMPANY,d.location,d.PHNO_TYPE from DETAILS d,contact c,address_1 a,zipcode z where c.pincode=z.pincode and a.c_id=c.c_id and d.c_id=c.c_id and c.c_id = {int(value)}"
            )
            self.SQL_delete(f"delete from contact where c_id = {int(value)}")
            # self.message("Deleted Successfully")
            i = 1
        else:
            value = self.ui.d_search_value.text()
            rows = self.SQL_retrive(
                f"select c.c_id,c.name,c.email,c.phno,c.RELATIONSHIP,c.type,c.dob,c.pincode,a.hno,a.hname,a.area,z.city,z.state,d.ZONE,d.COMPANY,d.location,d.PHNO_TYPE from DETAILS d,contact c,address_1 a,zipcode z where c.pincode=z.pincode and a.c_id=c.c_id and d.c_id=c.c_id and c.phno = {int(value)}"
            )
            self.SQL_delete(f"delete from contact where PHNO = {int(value)}")
            # self.message("Deleted Successfully")
            i = 1

        if len(rows) == 0:
            self.message("Record not found")
        else:
            self.message("Deleted Successfully")
            c_id = rows[0][0]
            name = rows[0][1]
            email = rows[0][2]
            phno = rows[0][3]
            relationship = rows[0][4]
            type_ = rows[0][5]
            dob = rows[0][6]
            pincode = rows[0][7]
            hno = rows[0][8]
            hname = rows[0][9]
            area = rows[0][10]
            city = rows[0][11]
            state = rows[0][12]
            zone = rows[0][13]
            company = rows[0][14]
            location = rows[0][15]
            phno_type = rows[0][16]

            self.SQL_insert(
                f"insert into RESTORE values({c_id},'{name}',{phno},'{email}','{relationship}','{type_}','{dob}','{hno}','{hname}','{area}','{city}','{state}',{pincode},'{zone}','{company}','{location}','{phno_type}')"
            )
            # if
            self.ui.tableWidget_8.setRowCount(0)
            # self.delete_show()

    def restore_data(self):
        item = self.ui.d_search_item.currentText()
        if item == "C_id":
            value = self.ui.d_search_value.text()
            rows = self.SQL_retrive(f"select * from RESTORE where c_id = {int(value)}")
            self.SQL_delete(f"delete from RESTORE  where c_id = {int(value)}")
        else:
            value = self.ui.d_search_value.text()
            rows = self.SQL_retrive(
                f"select * from RESTORE where P_L_NUMBER = {int(value)}"
            )
            self.SQL_delete(f"delete from RESTORE where P_L_NUMBER = {int(value)}")
        if len(rows) == 0:
            self.message("No records found")
        else:
            c_id = rows[0][0]
            name = rows[0][1]
            email = rows[0][3]
            phno = rows[0][2]
            relationship = rows[0][4]
            type_ = rows[0][5]
            dob = rows[0][6]
            pincode = rows[0][12]
            hno = rows[0][7]
            hname = rows[0][8]
            area = rows[0][9]
            city = rows[0][10]
            state = rows[0][11]
            zone = rows[0][13]
            company = rows[0][14]
            location = rows[0][15]
            phno_type = rows[0][16]

            self.SQL_insert(
                f"insert into contact values({c_id},'{name}','{email}',{phno},'{relationship}','{type_}','{dob}','{pincode}')"
            )
            self.SQL_insert(
                f"insert into ADDRESS_1 values({c_id},'{hno}','{hname}','{area}','{pincode}')"
            )
            self.SQL_insert(
                f"insert into details values({c_id},{phno},'{zone}','{company}','{location}','{phno_type}')"
            )
            self.message(f"restored successfully {phno}")
            self.delete_show()

    def permanent_delete_confirm(self):
        item = self.ui.d_search_item.currentText()

        if item == "C_id":
            value = self.ui.d_search_value.text()
            rows = self.SQL_retrive(f"select * from RESTORE where c_id = {int(value)}")
            if len(rows) == 0:
                self.message("Deleted Record not found")
            else:
                self.SQL_delete(f"delete from RESTORE  where c_id = {int(value)}")
                self.message(f"deleted permanently {value}")
        else:
            value = self.ui.d_search_value.text()
            rows = self.SQL_retrive(
                f"select * from RESTORE where P_L_NUMBER = {int(value)}"
            )
            if len(rows) == 0:
                self.message("Deleted Record not found")
            else:
                self.SQL_delete(f"delete from RESTORE where P_L_NUMBER = {int(value)}")
                self.message(f"deleted permanently {value}")
        # self.message(f"deleted permanently {value}")

    def update_show(self):
        phno = self.ui.u_search_bar_3.text()
        lst = self.SQL_retrive(f"select c.phno from contact c ")
        p = []
        for tup in lst:
            p.append(tup[0])
        if phno in p:
            rows = self.SQL_retrive(
                f"select c.c_id,c.name,c.email,c.phno,c.RELATIONSHIP,c.type,c.dob,a.hno,a.hname,a.area,z.city,z.state,c.pincode from contact c,address_1 a,zipcode z where c.pincode=z.pincode and a.c_id=c.c_id and c.phno={phno}"
            )
            self.ui.u_name_3.setText(rows[0][1])
            self.ui.u_email_3.setText(rows[0][2])
            self.ui.u_phno_3.setText(str(rows[0][3]))
            self.ui.u_relationship_3.setText(rows[0][4])
            self.ui.u_type_3.setText(rows[0][5])
            self.ui.u_dob_3.setText(rows[0][6])
            self.ui.u_hno_3.setText(str(rows[0][7]))
            self.ui.u_hname_3.setText(rows[0][8])
            self.ui.u_area_3.setText(rows[0][9])
            self.ui.u_city_3.setText(rows[0][10])
            self.ui.u_state_3.setText(rows[0][11])
            self.ui.u_pincode_3.setText(rows[0][12])
        else:
            self.message("search not found")

    def update_confirm(self):
        phno = self.ui.u_search_bar_3.text()
        item = self.ui.update_combo.currentText()

        if item == "Name":
            value = self.ui.update_item.text()
            self.SQL_update(f"update contact set name='{value}' where PHNO={int(phno)}")

        elif item == "Email":
            value = self.ui.update_item.text()
            self.SQL_update(
                f"update contact set email='{value}' where PHNO={int(phno)}"
            )

        elif item == "HouseNo":
            value = self.ui.update_item.text()
            c_id = self.SQL_retrive(
                f"select c_id from CONTACT where PHNO = {int(phno)} "
            )
            self.SQL_update(
                f"update ADDRESS_1 set hno='{value}' where c_id = {int(c_id[0][0])}"
            )

        elif item == "HouseName":
            value = self.ui.update_item.text()
            c_id = self.SQL_retrive(
                f"select c_id from CONTACT where PHNO = {int(phno)} "
            )
            self.SQL_update(
                f"update ADDRESS_1 set hname='{value}' where c_id = {int(c_id[0][0])}"
            )

        else:
            value = self.ui.update_item.text()
            c_id = self.SQL_retrive(
                f"select c_id from CONTACT where PHNO = {int(phno)} "
            )
            self.SQL_update(
                f"update ADDRESS_1 set area='{value}' where c_id = {int(c_id[0][0])}"
            )
        self.information("Updated successfully")

    def check_display(self):
        phno = self.ui.i_phno.text()

        z_rows = self.SQL_retrive(f"select * from DETAILS where PHNO = '{int(phno)}'")
        print(z_rows)
        self.ui.time_zone.setText(str(z_rows[0][2]))
        self.ui.company.setText(str(z_rows[0][3]))
        self.ui.location.setText(str(z_rows[0][4]))

    def insert_clear(self):
        self.ui.i_name.clear()
        self.ui.i_email.clear()
        self.ui.i_phno.clear()
        self.ui.i_hno.clear()
        self.ui.i_hname.clear()
        self.ui.i_area.clear()
        self.ui.i_city.clear()
        self.ui.i_state.clear()
        self.ui.i_pincode.clear()

    def update_clear(self):
        self.ui.u_name_3.clear()
        self.ui.u_email_3.clear()
        self.ui.u_phno_3.clear()
        self.ui.u_hno_3.clear()
        self.ui.u_hname_3.clear()
        self.ui.u_area_3.clear()
        self.ui.u_city_3.clear()
        self.ui.u_state_3.clear()
        self.ui.u_pincode_3.clear()
        self.ui.u_search_bar_3.clear()

        self.ui.u_name_3.setText("N/A")
        self.ui.u_email_3.setText("N/A")
        self.ui.u_phno_3.setText("N/A")
        self.ui.u_hno_3.setText("N/A")
        self.ui.u_hname_3.setText("N/A")
        self.ui.u_area_3.setText("N/A")
        self.ui.u_city_3.setText("N/A")
        self.ui.u_state_3.setText("N/A")
        self.ui.u_relationship_3.setText("N/A")
        self.ui.u_type_3.setText("N/A")
        self.ui.u_dob_3.setText("N/A")
        self.ui.u_pincode_3.setText("N/A")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = MainWindow()
    sys.exit(app.exec_())
