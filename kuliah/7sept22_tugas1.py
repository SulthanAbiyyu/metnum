import math
import pandas as pd

def nomor_satu(x, degree):
    un = []
    sn = 0
    for i in range(1, degree + 1):
        un.append((x ** (2*i - 2) / math.factorial(2 * i - 2)) * ((-1) ** (i-1)))
        sn += un[i - 1]

    return un, sn

def nomor_dua(x, degree):
    un = []
    sn = 0
    for i in range(1, degree + 1):
        un.append((x ** (1 + ((2*i) - 2))) / math.factorial(((1 + ((2*i) - 2)))) * ((-1) **(i-1)))
        sn += un[i - 1]
    
    return un, sn

if __name__ == "__main__":
    true_value_1 = math.cos(5)
    true_value_2 = math.sin(5)

    # Nomor 1
    un_1, pred_value_1 = nomor_satu(5, 10)
    galat_sebenarnya_1 = abs((pred_value_1 - true_value_1) / (true_value_1) * 100)
    un_1_df = pd.DataFrame(un_1, columns=["Un"])
    un_1_df["Sn"] = un_1_df["Un"].cumsum()

    sn_1 = un_1_df["Sn"]
    Er_1 = []
    for i in range(len(un_1_df)):
        if i == 0:
            Er_1.append(None)
        else:
            Er_1.append(abs((sn_1[i] - sn_1[i-1]) / (sn_1[i]) * 100))
    
    un_1_df["Galat Aproksimasi"] = Er_1

    # print("No. 1")
    # print(un_1_df)
    # print(f"Galat sebenarnya: {galat_sebenarnya_1}")
    # print("No. 2")

    un_2, pred_value_2 = nomor_dua(5, 10)
    galat_sebenarnya_2 = abs((pred_value_2 - true_value_2) / (true_value_2) *100)
    un_2_df = pd.DataFrame(un_2, columns=["Un"])
    un_2_df["Sn"] = un_2_df["Un"].cumsum()

    sn_2 = un_2_df["Sn"]
    Er_2 = []
    for i in range(len(un_2_df)):
        if i == 0:
            Er_2.append(None)
        else:
            Er_2.append(abs((abs(sn_2[i]) - abs(sn_2[i-1])) / abs((sn_2[i])) * 100))

    un_2_df["Galat Aproksimasi"] = Er_2
    print(sn_1)
    print((sn_1[4]))
    
    # print(un_2_df)
    # print(f"Galat sebenarnya: {galat_sebenarnya_2}")
    