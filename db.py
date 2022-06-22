import mysql.connector

# your_secret_password_here
# mydb = mysql.connector.connect(host="coinsproject.cjstfzsq8whn.us-east-1.rds.amazonaws.com", user="admin",
#                                password="adminadmin",
#                                database="coins_project", port=3306)
mydb = mysql.connector.connect(host="127.0.0.1", user="root",
                               password="root",
                               database="coins_project", port=8889)
print(mydb)
# id19097948_ahmed
# id19097948_coins_project
# localhost
mycursor = mydb.cursor(buffered=True)


# Account
# 403380792977
# KMS key ID
# 65119fb3-37b2-4720-9bc0-b9ca90be2968


def insert_coin(coin_name, full_name, coin_info):
    sql = "INSERT INTO coins (coin_name,full_name, coin_info) VALUES (%s ,%s,%s)"
    val = (coin_name, full_name, coin_info)
    mycursor.execute(sql, val)

    mydb.commit()


def get_coin(coin):
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SELECT coin_info FROM coins where coin_name LIKE '% {} %'".format(coin))
    res = mycursor.fetchone()[0]
    return res

# s = 'ماهي العمله الرقميه Ontology / ONT وماهو مشروعها ومعلومات عنها'
# s = 'ما هي العملة الرقمية Ankr (ANKR) مشروعها و معلومات عنها'

# print(s.split('ما هي العملة الرقمية', 1)[1].strip().split('/', 1)[0].replace(' مشروعها و معلومات عنها', '').strip())
# print(
#     s.split('ماهي العمله الرقميه', 1)[1].strip().split('/', 1)[1].strip().replace('وماهو مشروعها ومعلومات عنها','').strip())
