def beda_maju(f, x0, h):
    return (f(x0+h)-f(x0))/h

def beda_mundur(f, x0, h):
    return (f(x0)-f(x0-h))/h

def beda_tengah(f, x0, h):
    return (f(x0+h)-f(x0-h))/(2*h)

def turunan_kedua(f, x0, h):
    return (f(x0 + h) - 2 * f(x0) + f(x0-h))/h ** 2

def f(x):
    return 0.1 * x ** 4 + 0.2 * x ** 3 + 0.4 * x ** 2 + 0.5 * x + 1

if __name__ == "__main__":
    x0 = 0
    metode = [beda_maju, beda_mundur, beda_tengah, turunan_kedua]
    nama_metode = ['beda_maju', 'beda_mundur', 'beda_tengah', 'turunan_kedua']
    for nama, m in zip(nama_metode, metode):
        print(f"Menggunakan Metode {nama}")
        for k in range(5):
            h = 10 ** -k
            print(f"h: {h}\t\t|\t\thasil: {m(f, x0, h)}")