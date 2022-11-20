with open("hazi.txt", encoding="utf-8") as f:
    with open("ki.txt", "w", encoding="utf-8") as ki:
        counter = 0
        for line in f.readlines():
            if line.strip():
                counter += 1
                for char in line:
                    if char.isalpha():
                        if counter % 3 == 0:
                            ki.write(char)
                if counter % 3 == 0:
                    ki.write("\n")