import pandas as pd

servidor_a = pd.Series([100, 102, 98, 101, 99])
servidor_b = pd.Series([70, 130, 90, 110, 100])

print(f"Media dos servidores:\n A: {servidor_a.mean()},\n B: {servidor_b.mean()}")

amp_a = servidor_a.max() - servidor_a.min()
amp_b = servidor_b.max() - servidor_b.min()
print(f"Amplitude dos servidores:\n A: {amp_a},\n B:{amp_b}")

print(f"Desvio Padrao Populacional dos servidores:\n A: {servidor_a.std(ddof=0)},\n B {servidor_b.std(ddof=0)}")
