# prompt the user if he already knows how much wattage does he have


items = ["ACs","laundry_machines","Computers","Refrigerators","Tvs","Lights","Ovens"]
total_wattage = 0
num_of_devices = 0
def calculate_wattage():
    global total_wattage, num_of_devices
    for item in items:
        num_of_devices = int(input(f"Enter how many {item}(s) you have"))
        if num_of_devices == 1:
            item_amps = float(input(f"Enter amps your {item} uses:  "))
            item_volts = float(input(f"Enter volts your {item} uses: "))
            wattage  = item_amps * item_volts
            total_wattage += wattage
        elif num_of_devices >= 2:
            for i in range(0,num_of_devices):
                item_amps = float(input(f"Enter amps your {item} {i+1} uses:  "))
                item_volts = float(input(f"Enter volts your {item} {i+1} uses: "))
                wattage = item_amps * item_volts
                total_wattage += wattage
        elif num_of_devices == 0:
            continue
    print(f"so your total wattage is {total_wattage}Watts")
    print("------------- Now that we have all the wattages we need lets move forward !")
    return total_wattage

def main_solution(watts,unit_price):
    usage = 0
    for item in items:
        item_usage = int(input(f"Enter all {item}(s) sum up hours of usage monthly"))
        usage+=item_usage
    print(f"so your total usage is {usage}")
    k_watt_hrs = watts* usage / 1000
    cost = k_watt_hrs * unit_price
    return cost

def prompt():
    print("Hi Welcome to Electricity Bill Calculator! Lets get started calculating your appliances wattage.\n Remember this program gives a rough estimate. Alright Lets start ")
    unit_price = float(input("First of all, what is unit price of electricity in your country? Just give numbers "))
    print("Alright lets calculate wattage.")
    # call a separate method which will first calculate the wattages and then return
    method_wattage = calculate_wattage()
    cost = main_solution(method_wattage,unit_price)
    print(f"You estimated bill : {cost}")


prompt()