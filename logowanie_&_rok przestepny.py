Login = "admin"
Password = "lol"

proby = 3
while proby > 0:

    user_login = input("podaj login: ")
    user_password = input("podaj password: ")
    if Login == user_login and Password == user_password:
        print ("dostep przyznany")
        break
    else:
        print ("dostep nieprzyznany")
    proby = proby -1

if proby == 0:
    print ("dostep zablokowany")

#-------------------------------------------------------------

rok = int(input ("podaj rok "))

if (rok%4 == 0 and rok%100!=0) or (rok%400==0):
    print("rok_przestępny")
else:
    print("rok_nieprzestępny")


    user_login = input("podaj login: ")
    user_password = input("podaj password: ")
    if Login == user_login and Password == user_password:
         print ("dostep przyznany")
