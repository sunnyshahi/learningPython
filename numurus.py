def numerus(val:str):
    roman = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'm': 1000
    }
    val = val.lower()
    sum = 0
    prev_num = 0
    for i in val:
        if i in roman:
            if prev_num < roman[i]:
                sum -= 2*prev_num
            sum += roman[i]
            prev_num = roman[i]
        else:
            return None
    return sum 

if __name__ == "__main__":
    print(numerus('MCIX'))