def main():
    #Get the mass of the object
    get_mass = int(input("M: "))

    #Calculate the energy of the object
    joules = calculate_energy(get_mass)

    #Print the result
    print(f"E: {joules}")

def calculate_energy(mass):
    C = 300000
    return mass * C ** 2

main()

