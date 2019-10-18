

def hitung_impuls(gayaimpulsif, perubahanwaktu) :
    impuls = gayaimpulsif * perubahanwaktu
    print(f'gayaimpulsif = {gayaimpulsif / 10}newton dikenai sebuah perubahanwaktu  = {perubahanwaktu / 60}menit')
    print(f'sehingga impuls = {impuls} Ns')
    return impuls

# gayaimpulsif
# perubahanwaktu
impuls = hitung_impuls(20, 0.5)

def hitung_momentum(massa, kecepatan) :
    momentum = massa * kecepatan
    print(f'massa = {massa / 1} Kg dikenai sebuah kecepatan = {1 / 60} m/s')
    print(f'sehingga momentum = {momentum} kg m/s')

# massa
# kecepatan
momentum = hitung_momentum(1000, 10)

def hitung_percepatan(kecepatan, waktu) :
    percepatan = kecepatan / waktu
    print(f'kecepatan = {1 / 60} m/s dengan waktu = {waktu / 60} menit')
    print(f'sehingga percepatan = {percepatan} m/s ** 2')

# kecepatan
# waktu
percepatan = hitung_percepatan(100 , 4)