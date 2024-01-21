def freq_words(str):
    
    li = str.split()
    print(li)
    d = {}

    for i in li:
        if i not in d.keys():
            d[i] = 0
        d[i] +=1
    print(d)

str = input("Enter a words of string :")
freq_words(str)