import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.5)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat

mengetik('MAAP NIH GABUT MAAP YA')
