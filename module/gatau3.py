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

mengetik('Tunggu Sebentar...')
mengetik('1')
mengetik('2')
mengetik('3')
mengetik('4')
mengetik('5')
mengetik('6')
mengetik('7')
mengetik('8')
mengetik('9')
mengetik('10')
mengetik('system siap')
