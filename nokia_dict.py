d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
for char in input().upper():
    for key, value in d.items():
        if char in value:
            index = value.index(char) + 1 #определяем, сколько нажатий нужно
            print(key * index, end='')
