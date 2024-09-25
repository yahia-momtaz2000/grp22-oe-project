# file contains CRUD operations for Company class
# CRUD  [ Create - Read - Update - Delete  ]
# 5 main functions [ get_all_companies(),  get_company_by_id(company_id),  insert_company(company),
#                   update_company(company), delete_company(company_id) ]
from customers.company import Company
from db.db_connection_factory import DBConnectionFactory


class CompanyHandler:
    @staticmethod
    def insert_company(company):
        # 1- Create db Connection
        my_conn = DBConnectionFactory.create_connection()

        # 2- prepare sql statement
        sql_statement = ('insert into customers'
                         ' (CUSTOMER_NAME, CUSTOMER_ADDRESS, CUSTOMER_PHONE, '
                         ' CUSTOMER_CONTACT, CUSTOMER_DISCOUNT, CUSTOMER_TYPE_ID)'
                         ' values'
                         ' (%s, %s, %s, %s, %s, 1 )')

        # 3- set parameters ( data )
        values_tuple = (company.get_customer_name(), company.get_customer_address(), company.get_customer_phone(),
                        company.get_contact(), company.get_discount())

        # 4- Create cursor and execute sql statement
        my_cursor = my_conn.cursor()
        my_cursor.execute(sql_statement, values_tuple)

        # 5- commit changes
        my_conn.commit()


    @staticmethod
    def update_company(company):
        # 1- Create db Connection
        my_conn = DBConnectionFactory.create_connection()

        # 2- prepare sql statement
        sql_statement = ('Update customers'
                         ' set customer_name = %s,'
                         '     customer_address = %s,'
                         '     customer_phone = %s,'
                         '     customer_contact = %s,'
                         '     customer_discount = %s'
                         ' where customer_id = %s')

        # 3- set parameters ( data )
        values_tuple = (company.get_customer_name(), company.get_customer_address(), company.get_customer_phone(),
                        company.get_contact(), company.get_discount(), company.get_customer_id())

        # 4- Create cursor and execute sql statement
        my_cursor = my_conn.cursor()
        my_cursor.execute(sql_statement, values_tuple)

        # 5- commit changes
        my_conn.commit()



    @staticmethod
    def delete_company(company_id):
        pass

    @staticmethod
    def get_all_companies():
        pass

    @staticmethod
    def get_company_by_id():
        pass

# main program to test each function
# test insert
# my_company = Company(101, 'Herotech', '01112312', 'Alex - Eg',
#                      'Ibrahim Aly', 12)
# CompanyHandler.insert_company(my_company)


# test update
my_company = Company(3, 'Herotech - Advanced', '777-999-888', 'Assuit - Eg',
                     'Hussein Mohamed', 17)
CompanyHandler.update_company(my_company)


