def juft_toq_sonlar(sonlar):
    juft_sonlar = []
    toq_sonlar = []
    for son in sonlar:
        if son % 2 == 0:
            juft_sonlar.append(son)
        else:
            toq_sonlar.append(son)
    return juft_sonlar, toq_sonlar

def main():
    sonlar = [12, 45, 7, 23, 56, 89, 34, 21, 90, 76, 43, 98, 65, 11, 74]
    juft, toq = juft_toq_sonlar(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

    sonlar = [1, 3, 5, 7, 9]
    juft, toq = juft_toq_sonlar(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

    sonlar = [2, 4, 6, 8, 10]
    juft, toq = juft_toq_sonlar(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

    sonlar = [1, 2, 3, 4, 5]
    juft, toq = juft_toq_sonlar(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

    sonlar = [10, 20, 30, 40, 50]
    juft, toq = juft_toq_sonlar(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

    sonlar = [11, 13, 15, 17, 19]
    juft, toq = juft_toq_sonlar(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

    sonlar = [21, 23, 25, 27, 29]
    juft, toq = juft_toq_sonlar(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

    sonlar = [31, 33, 35, 37, 39]
    juft, toq = juft_toq_sonlar(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

    sonlar = [41, 43, 45, 47, 49]
    juft, toq = juft_toq_sonlar(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

    sonlar = [51, 53, 55, 57, 59]
    juft, toq = juft_toq_sonlar(sonlar)
    print("Juft sonlar:", juft)
    print("Toq sonlar:", toq)

if __name__ == "__main__":
    main()