import random

def primary():
    # print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = len(quotes)
    rnd1 = random.randint(0,last)
    rnd2 = random.randint(0,last)
    print(quotes[rnd1], end="")
    print(quotes[rnd2])

    f = open("quotes.txt",'w')    
    quotes.append('This is awesome\n')
    f.writelines(quotes)
    f.close()

if __name__ == "__main__":
    primary()
