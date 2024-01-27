def calculate_slices_of_pizzas(individuals):
    ls= 8
    ms = 6
    rs = 4
    ss = 1

    lps = individuals // ls
    mps = (individuals % ls) // ms
    rps = ((individuals % ls) % ms) // rs
    sps = (((individuals % ls) % ms) % rs) // ss

    print("Number of individuals: ",individuals)
    print("Number of Large Pizzas: ",lps)
    print("Number of Medium Pizzas: ",mps)
    print("Number of Regular Pizzas: ",rps)
    print("Number of Small Pizzas: ",sps)

calculate_slices_of_pizzas(100)