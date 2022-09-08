import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def nomor_satu(x, degree):
    un = []
    sn = 0
    for i in range(1, degree + 1):
        un.append((x ** (2*i - 2) / math.factorial(2 * i - 2))
                  * ((-1) ** (i-1)))
        sn += un[i - 1]

    return un, sn


def nomor_dua(x, degree):
    un = []
    sn = 0
    for i in range(1, degree + 1):
        un.append((x ** (1 + ((2*i) - 2))) /
                  math.factorial(((1 + ((2*i) - 2)))) * ((-1) ** (i-1)))
        sn += un[i - 1]

    return un, sn


if __name__ == "__main__":
    true_value_1 = math.cos(5)
    true_value_2 = math.sin(5)
    degree = 100

    # Nomor 1
    un_1, pred_value_1 = nomor_satu(5, degree)
    galat_sebenarnya_1 = abs(
        (pred_value_1 - true_value_1) / (true_value_1) * 100)
    un_1_df = pd.DataFrame(un_1, columns=["Un"])
    un_1_df["Sn"] = un_1_df["Un"].cumsum()

    sn_1 = un_1_df["Sn"]
    Er_1 = []
    kurva_galat_sebenarnya_1 = []
    for i in range(len(un_1_df)):
        if i == 0:
            kurva_galat_sebenarnya_1.append(
                abs((sn_1[i] - true_value_1)/true_value_1 * 100))
            Er_1.append(None)
        else:
            kurva_galat_sebenarnya_1.append(
                abs((sn_1[i] - true_value_1)/true_value_1 * 100))
            Er_1.append(abs((sn_1[i] - sn_1[i-1]) / (sn_1[i]) * 100))

    un_1_df["Galat Aproksimasi"] = Er_1

    print("No. 1")
    print(un_1_df)
    print(f"Nilai sebenarnya: {true_value_1}")
    print(f"Nilai hampiran: {pred_value_1}")
    print(f"Galat sebenarnya: {galat_sebenarnya_1}\n")

    # No. 2
    print("No. 2")
    un_2, pred_value_2 = nomor_dua(5, degree)
    galat_sebenarnya_2 = abs(
        (pred_value_2 - true_value_2) / (true_value_2) * 100)
    un_2_df = pd.DataFrame(un_2, columns=["Un"])
    un_2_df["Sn"] = un_2_df["Un"].cumsum()

    sn_2 = un_2_df["Sn"]
    Er_2 = []
    kurva_galat_sebenarnya_2 = []
    for i in range(len(un_2_df)):
        if i == 0:
            kurva_galat_sebenarnya_2.append(
                abs((sn_2[i] - true_value_1)/true_value_1 * 100))
            Er_2.append(None)
        else:
            kurva_galat_sebenarnya_2.append(
                abs((sn_2[i] - true_value_1)/true_value_1 * 100))
            Er_2.append(
                abs((sn_2[i] - sn_2[i-1]) / (sn_2[i]) * 100))

    un_2_df["Galat Aproksimasi"] = Er_2
    print(un_2_df)
    print(f"Nilai sebenarnya: {true_value_2}")
    print(f"Nilai hampiran: {pred_value_2}")
    print(f"Galat sebenarnya: {galat_sebenarnya_2}")

    # Plotting
    fig, ax = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle("Latihan Soal Bab Aproksimasi Galat", fontsize=20)

    ax[0, 0].title.set_text("Fungsi Cosinus dan Aproksimasinya")
    ax[0, 0].plot(un_1_df["Sn"], label="Aproksimasi")
    ax[0, 0].plot([true_value_1] * degree, label="Cosinus")
    ax[0, 0].legend()

    ax[0, 1].title.set_text("Galat Aproksimasi No. 1")
    sns.lineplot(data=un_1_df, x=un_1_df.index,
                 y="Galat Aproksimasi", ax=ax[0, 1])
    ax[0, 2].title.set_text("Kurva Galat Sebenarnya No. 1")
    sns.lineplot(data=un_1_df, x=un_1_df.index,
                 y=kurva_galat_sebenarnya_1, ax=ax[0, 2])

    ax[1, 0].title.set_text("Fungsi Sinus dan Aproksimasinya")
    ax[1, 0].plot(un_2_df["Sn"], label="Aproksimasi")
    ax[1, 0].plot([true_value_2] * degree, label="Sinus")
    ax[1, 0].legend()

    ax[1, 1].title.set_text("Galat Aproksimasi No. 2")
    sns.lineplot(data=un_2_df, x=un_2_df.index,
                 y="Galat Aproksimasi", ax=ax[1, 1])
    ax[1, 2].title.set_text("Kurva Galat Sebenarnya No. 2")
    sns.lineplot(data=un_2_df, x=un_2_df.index,
                 y=kurva_galat_sebenarnya_2, ax=ax[1, 2])

    plt.show()
