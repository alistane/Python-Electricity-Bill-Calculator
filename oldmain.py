# prompt the user if he already knows how much wattage does he have 

ac_wattage = 0
laundry_wattage = 0
ref_wattage = 0
tv_wattage = 0
li_wattage = 0
Oven_wattage = 0

total_wattage = 0

def calculate_wattage():
    global ac_wattage, laundry_wattage, ref_wattage, tv_wattage , li_wattage , Oven_wattage
    # formula of wattage = (Amps) x (volts)
    num_of_devices = int(input("how many ac's do you have?"))
    if num_of_devices == 1:
        ac_amps = int(input("Enter how many apms your ac uses"))
        ac_volts = int(input("Enter how many volts your ac uses"))
        wattage = ac_amps * ac_volts
        ac_wattage += wattage
    elif num_of_devices >= 2:
        print('We are in baby')
        for i in range(0,num_of_devices):
            ac_amps = int(input(f"Enter how many apms your ac{i+1} uses"))
            ac_volts = int(input(f"Enter how many volts your ac{i+1} uses"))
            wattage = ac_amps * ac_volts
            ac_wattage += wattage
    print(f"Your ac wattage is  : {ac_wattage} Watts")

    num_of_devices = int(input("how many laundry machines do you have?"))
    if num_of_devices == 1:
        laundry_amps = int(input("Enter how many apms your machine uses"))
        laundry_volts = int(input("Enter how many volts your machine uses"))
        wattage = laundry_amps * laundry_volts
        laundry_wattage += wattage
    elif num_of_devices >= 2:
        print('We are in baby')
        for i in range(0, num_of_devices):
            laundry_amps = int(input(f"Enter how many apms your machine {i + 1} uses"))
            laundry_volts = int(input(f"Enter how many volts your machine {i + 1} uses"))
            wattage = laundry_amps * laundry_volts
            laundry_wattage += wattage
    print(f"Your total laundry machine(s) wattage is : {laundry_wattage} Watts")


    num_of_devices = int(input("how many refrigerators do you have?"))
    if num_of_devices == 1:
        ref_amps = int(input("Enter how many apms your machine uses"))
        ref_volts = int(input("Enter how many volts your machine uses"))
        wattage = ref_amps * ref_volts
        ref_wattage += wattage
    elif num_of_devices >= 2:
        print('We are in baby')
        for i in range(0, num_of_devices):
            ref_amps = int(input(f"Enter how many apms your machine {i + 1} uses"))
            ref_volts = int(input(f"Enter how many volts your machine {i + 1} uses"))
            wattage = ref_amps * ref_volts
            ref_wattage += wattage
    print(f"Your total refrigerator(s) wattage is : {ref_wattage} Watts")

    num_of_devices = int(input("how many tvs do you have?"))
    if num_of_devices == 1:
        tv_amps = int(input("Enter how many apms your machine uses"))
        tv_volts = int(input("Enter how many volts your machine uses"))
        wattage = tv_amps * tv_volts
        tv_wattage += wattage
    elif num_of_devices >= 2:
        print('We are in baby')
        for i in range(0, num_of_devices):
            tv_amps = int(input(f"Enter how many apms your machine {i + 1} uses"))
            tv_volts = int(input(f"Enter how many volts your machine {i + 1} uses"))
            wattage = tv_amps * tv_volts
            tv_wattage += wattage
    print(f"Your total tv(s) wattage is : {tv_wattage} Watts")

    num_of_devices = int(input("how many lights do you have?"))
    if num_of_devices == 1:
        li_amps = int(input("Enter how many apms your bulb uses"))
        li_volts = int(input("Enter how many volts your bulb uses"))
        wattage = li_amps * li_volts
        li_wattage += wattage
    elif num_of_devices >= 2:
        print('We are in baby')
        for i in range(0, num_of_devices):
            li_amps = int(input(f"Enter how many apms your bulb {i + 1} uses"))
            li_volts = int(input(f"Enter how many volts your bulb {i + 1} uses"))
            wattage = li_amps * li_volts
            li_wattage += wattage
    print(f"Your total light(s) wattage is : {li_wattage} Watts")

    num_of_devices = int(input("how many ovens do you have?"))
    if num_of_devices == 1:
        ov_amps = int(input("Enter how many apms your oven uses"))
        ov_volts = int(input("Enter how many volts your oven uses"))
        wattage = ov_amps * ov_volts
        li_wattage += wattage
    elif num_of_devices >= 2:
        print('We are in baby')
        for i in range(0, num_of_devices):
            ov_amps = int(input(f"Enter how many apms your bulb {i + 1} uses"))
            ov_volts = int(input(f"Enter how many volts your bulb {i + 1} uses"))
            wattage = ov_amps * ov_volts
            Oven_wattage += wattage
    print(f"Your total oven(s) wattage is : {Oven_wattage} Watts")
    total_wattage = ac_wattage + laundry_wattage + ref_wattage + tv_wattage + li_wattage + Oven_wattage
    print(f"your total wattage is {total_wattage}")
    print("------------- Now that we have all the wattages we need lets move forward !")

def prompt():
    user_prompt = input('Hi Welcome! Do you know wattage of your appliances (AC(s),laundry machines,refrigerators,TVs,Lighting and ovens?) Press Y for yes and press N for no').capitalize()
    if user_prompt == 'Y':
        print("Good")
    elif user_prompt == 'N':
        print("alright lets calculate it right away!")
        # call a separate method which will first calculate the wattages and then return 
        calculate_wattage()
prompt()