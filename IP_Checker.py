def IP_Check(IP):
    while True:
        try:
            if ((int(IP[0]) >= 0 and int(IP[0]) < 256) and
            (int(IP[1]) >= 0 and int(IP[1]) < 256) and
            (int(IP[2]) >= 0 and int(IP[2]) < 256) and
            (int(IP[3]) >= 0 and int(IP[3]) < 256)):
                print(user_IP + " is a valid IP Address")
                break
            else:
                print(user_IP + " is not a valid IP Address")
                break
        except (IndexError, ValueError):
            print(user_IP + " is not a valid IP Address")
            break

def IP_split(IP):
    split_IP = IP.split(".")
    if len(split_IP) > 4:
        print(user_IP + " is not a valid IP Address")
        return True
    IP_Check(split_IP)

while True:

    user_IP = input("Enter IP Address (Type x to End): ")
    if user_IP == "x" or user_IP == "X":
        print("Thank you for using my program.")
        break
    elif user_IP.isalpha() == True:
        print(user_IP + " is not a valid IP Address")
        continue
    else:
        IP_split(user_IP)


