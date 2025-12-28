def main():
    pin = 7868
    tries=0
    while tries<3:
        user = get_pin()
        if user == pin:
            print("___________________________")
            print("*ACCESS GRANTED|BALNCE:40$")
            print("____________________________")
            break 
        if user != pin:
            print("INVALID")
            tries+=1
    if tries==3:
        print("############################")
        print("*ACCOUNT HAS BEEN LOCKED")
        print("##############################")


def get_pin():
    while True:
        try:
            x = input("PIN:")
            if len(x)== 4 and x.isdigit():
                return int(x)
            else:
                pass
        except ValueError:
            pass        


if __name__ == "__main__":
    main()