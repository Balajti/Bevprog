def isPali(s):
    s.lower()
    s_new = ""
    osszetett = ["cs", "dz", "gy", "ly", "ny", "sz", "ty", "zs"]
    for i in range(0, len(s)):
        if s[i].isalpha():
            if "dzs" in s:
                if i + 3 == len(s)-1 or i + 2 == len(s)-1 or i + 1 == len(s)-1 or i == len(s)-1 : 
                    if f"{s[i]}{s[i + 1]}{s[i + 2]}" == "dzs":
                        s_new = f"{s_new}{s[i]}{s[i + 1]}{s[i + 2]}"
                        i += 2
            if i == len(s)-1:
                if f"{s[i]}{s[i + 1]}" in osszetett:
                    s_new = f"{s_new}{s[i]}{s[i + 1]}"
                    i += 1
                else:
                    s_new = f"{s_new}{s[i]}"    
    print(s_new)
            
    
    
if __name__ == "__main__":
    s = input("Enter a sentence or a word \t")
    isPali(s)