
def segitiga_siku(n):
    for row in range(0, n):
        for col in range(0, row + 1):
            print("* ", end="")
        print()

def segitiga_siku_kebalik(n):
    for row in range(0, n):
        for col in range(0, n - row):
            print("* ", end="")
        print()

if __name__ == '__main__':
    segitiga_siku(5)