# Ex. 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# Atividade extra: fazer para as outras unidades de médias.
measure = float(input('Digite uma medida em metros: '))

# km hm dam m dm cm mm
km = measure / 1000
hm = measure / 100
dam = measure / 10
dm = measure * 10
cm = measure * 100
mm = measure * 1000

print(f'A medida de {measure}m corresponde a: \n{km:.4f}km, \n{hm:.3f}hm, \n{dam:.0f}dam, \n{dm:.0f}dm, \n{cm:.0f}cm e \n{mm:.0f}mm.')
