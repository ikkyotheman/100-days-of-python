def calculate_love_score(first_name, second_name):
   true = "TRUE"
   love = "LOVE"
   true_letters = []
   love_letters = []
   for letter in true:
      if letter in first_name:
         true_letters.append(letter)
   for u in true:
      if u in second_name:
         true_letters.append(u)
   for o in love:
      if o in first_name:
         love_letters.append(o)
   for y in love:
      if y in second_name:
         love_letters.append(y)
   count_t = true_letters.count("T")
   count_r = true_letters.count("R")
   count_u = true_letters.count("U")
   count_e = true_letters.count("E")
   count_l = love_letters.count("L")
   count_o = love_letters.count("O")
   count_v = love_letters.count("V")
   count_ee = love_letters.count("E")
   print(f"T occurs {count_t} times")
   print(f"R occurs {count_r} times")
   print(f"U occurs {count_u} times")
   print(f"E occurs {count_e} times")
   true_total = count_t + count_r + count_u + count_e
   text_true = str(true_total)
   print(f"Total = {true_total}")
   print()
   print(f"L occurs {count_l} times")
   print(f"O occurs {count_o} times")
   print(f"V occurs {count_v} times")
   print(f"E occurs {count_ee} times")
   love_total = count_l + count_o + count_v + count_ee
   text_love = str(love_total)
   print(f"Total = {love_total}")
   total = text_true + text_love
   print(f"love score = {total}")

first_name = input("What's the first person's name?").upper()
second_name = input("What's the other person's name?").upper()
calculate_love_score(first_name, second_name)

