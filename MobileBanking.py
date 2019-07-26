import random
import time
import datetime
i,j=0,2
Pin=1331
ballance=50000
a = random.randint(1366, 30978)
b = random.randint(13432, 65789)

while i<j:
    user=int(input("Enter Your 4 Digit Pin : "))
    i+=1
    if user==Pin:

        print("\n\t\t\t\t\t\t\t@#@# Welcome To Mobile Banking @#@#   \n\n\t\t\t\t\t 1: Ballance Inquirey "
              " \t2: Withrawl Money \n\n\t\t\t\t\t 3: Send Money  \t4: Pay Bills \n\n\t\t\t\t\t 5: Change Pin \n")
        user1=int(input("\n\t\t\t\t\t What You Want to Do ? "))
        if user1==1:
            print('\t\t\t\t\tYour Available Ballance is : ' ,ballance ,'R')
            print('\n')
            print("By Using the Ac No#**", a)
            break

        elif user1==2:
            print("You are welcome! \n Select your account type ! \n 1 : Current Account \n 2 : Savings Account ")
            user3=int(input("Select Account Type  : "))
            if user3==1:
                print('Welcome to Current Account')

            elif user3==2:
                print('Welcome ! To Savings Account')


            else:
                print('we have only two types of accounts \n \n Please ! Select Your Account Type Again : ')
            user4=int(input("Enter Your Amount : "))
            print("PLEASE WAIT...")
            time.sleep(2)
            if user4<500:
                print("Minimum Withrawal is 500 ! Try Again ")
                break
            elif user4>50000:
                print('maximum withdrawl is 50000 ! Try Again')
                break
            else:
                print('R' , user4," Has Been Successfully Withdrawl")
                print('\n')
                print('Your Remaining Ballance is : ', ballance - user4)
                print("By Using the Ac No#**", a)
                print("Your Transaction id is #**", b)
                
                break
        elif user1==3:
            print("@@@@@@@ Available Banks are : @@@@@@@ :  \n 1 : Standard Bank  \n 2 : Absa Bank \n 3 : MCB \n 4 : Capitec Bank    ")
            user7=int(input('Enter Account No.'))
            user5=int(input("Select Bank "))
            if user5==1 or 2 or 3 or 4 :
                user6=int(input("Enter Amount:  "))
                print('\n')
                print("PLEASE WAIT...")
                time.sleep(2)
                print(user6 , "R has been Successfully Sent To Ac. No# " , user7)
                print("Your Transaction id is #**", b)
                print('\n')
                print('Your Remaining Ballance is : ',ballance-user6)
                print("By Using the Ac No#**", a)

                break
        elif user1==4:
            print("1:Electric Bill \t 2:Gas Bill \n 3:Ptcl Bill \t 4:Internet Bill \n 5:Water Bill \t 6:Utility Bill")
            user8=int(input('Select Your Bill Type : '))
            if user8==1 or 2 or 3 or 4 or 5 or 6 :
                user9=int(input("Enter Reffernce No. : "))
                print("PLEASE WAIT...")
                time.sleep(2)
                print(user9 ,"Bill has been payed Successfully")
                print('Your Remaining Ballance is : ', ballance - user9)
                print("By Using the Ac No#**", a)
                print("Your Transaction id is #**", b)
                break
        else:
            print("@@@@@@@@@@@@@@@@@@@@@@@ ALERT ! @@@@@@@@@@@@@@@@@@@@@@  ")
            print("You are Going To Change Your Pin , \n You would not be able to change it further for next 90 days . \n 1 : Do you Agree ? \n 2 : Not Agree")
            user10=int(input("Select Terms & Conditions 1st : " ))
            if user10==1:
                chng=int(input("Enter Your Old Pin : "))
                if chng==Pin:
                    new=int(input("Enter Your New Password: "))
                    print("PLEASE WAIT...")
                    time.sleep(2)
                    print("Congratulations ! Your Pin has been Changed ")
                    break
                else:
                    print("Incorrect Old Pin, You Can't Change Your Pin ")
                    break
            else:
                print("You Must Have to Agree to our Terms and Conditions ! ")
                break



    else:
        print("Incorrect Pin \n ")


print('\n')
print('\n')
print("\t\t\tDate is : ", datetime.date.today())
waqt=datetime.datetime.now()
print("\t\t\tTime is : ",waqt.hour,":",waqt.minute,":",waqt.second)





print(" ")
print("\t\t\t\t\t@#@#@#@# Thank you for using Our Online Services ,  Mr Saki @#@#@#@#")
