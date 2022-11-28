nums = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
x = 70

also = 0
felso = len(nums) - 1
kozep = 0
counter = 0
 
while also <= felso:
 
    kozep = (felso + also) // 2
    counter += 1
    if nums[kozep] > x:
        felso = kozep - 1           
    elif nums[kozep] < x:
        also = kozep + 1
    else:
        print(f"also: {also}, felso: {felso}, lepesszam: {counter}, szam: {kozep}")
        break
            




