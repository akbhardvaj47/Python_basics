email=input(" Enter your Email : ")
c,d,k=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        c=c+1
                    elif i==i.isalpha():
                        if i==i.upper():
                            d=d+1
                    elif i==i.isdigit():
                        continue
                    elif i=="@" or i=="_" or i==".":
                        continue
                    else:
                        k=k+1
                if c>0 or d>0 or k>0:
                    print("Envalid Email 5")
                else:
                    print("Right Email : ")
            else:
                print("Enavalid Email 4")
        else:
            print("Enavalid Email 3")
    else:
        print( "Envalid Email 2")
else:
    print(" Envalid Email 1 ")