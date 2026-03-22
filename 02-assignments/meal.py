def main():
    #Prompt user for the time
    time = input("What is the time? ")

    #Convert time from 24-hour format to float using convert function
    t = convert(time)

    #Logic
    if 7 <= t <= 8:
        print(f"breakfast time")

    elif 12 <= t <= 13:
        print(f"lunch time")

    elif 18 <= t <= 19:
        print(f"dinner time")



#Define convert function
def convert(time):
    time = time.strip().lower()

    #check if 12 hour format
    if "a.m." in time or "p.m." in time:
        period = "a.m." if "a.m." in time else "p.m."
        time = time.replace("a.m.", "").replace("p.m.", "").strip()

        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

        #Convert hours based on period
        if period == "a.m.":
            if hours == 12:
                hours = 0
        
        else: #p.m.
            if hours != 12:
                hours += 12

    else:
        #24 hour format
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

    return hours + (minutes / 60)

if __name__ == "__main__":
    main()