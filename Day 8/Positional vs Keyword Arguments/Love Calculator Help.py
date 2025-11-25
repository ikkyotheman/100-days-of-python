def calculate_love_score(first_name, second_name):
    combined = (first_name + second_name).replace(" ", "").upper()
    true = "TRUE"
    love = "LOVE"
    count_t = combined.count("T")
    count_r = combined.count("R")
    count_u = combined.count("U")
    count_e_true = combined.count("E")
    count_l = combined.count("L")
    count_o = combined.count("O")
    count_v = combined.count("V")
    count_e_love = combined.count("E")
    print(f"T occurs {count_t} times")
    print(f"R occurs {count_r} times")
    print(f"U occurs {count_u} times")
    print(f"E occurs {count_e_true} times")
    true_total = count_t + count_r + count_u + count_e_true
    print(f"Total: {true_total}")
    print(f"L occurs {count_l} times")
    print(f"O occurs {count_o} times")
    print(f"V occurs {count_v} times")
    print(f"E occurs {count_e_love} times")
    love_total = count_l + count_o + count_v + count_e_love
    print(f"Total: {love_total}")
    total = str(true_total) + str(love_total)
    print(f"Total: {total}")
first_name = input("What's the first person's name?").upper()
second_name = input("What's the other person's name?").upper()
calculate_love_score(first_name, second_name)

