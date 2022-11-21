def isPali(str):
    s = str.lower()
    s_new = []
    i = 0
    osszetett = ["cs", "dz", "gy", "ly", "ny", "sz", "ty", "zs"]
    while i < len(s):
        if s[i].isalpha():
            if i != len(s)-1 :
                if f"{s[i]}{s[i + 1]}" in osszetett:
                    s_new.append(f"{s[i]}{s[i + 1]}")
                    i += 1
                else:
                    s_new.append(f"{s[i]}")
            elif i <= len(s) - 2:
                if f"{s[i]}{s[i + 1]}{s[i + 2]}" == "dzs":
                    s_new.append(f"{s[i]}{s[i + 1]}{s[i + 2]}")
                    i += 2
                else:
                    s_new.append(f"{s[i]}")
            else:
                s_new.append(f"{s[i]}")
        i += 1
    s_new_rev = s_new[::-1]
    new = ''.join([elem for elem in s_new])
    new_rev = ''.join([elem for elem in s_new_rev]) 
    return new == new_rev
if __name__ == "__main__":
    s = input("Enter a sentence or a word: ")
    if isPali(s):
        print("Palindrom")
    else:
        print("nem palindrom")