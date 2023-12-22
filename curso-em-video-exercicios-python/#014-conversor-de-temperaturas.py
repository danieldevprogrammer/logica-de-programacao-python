# Ex. 014 - Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

temperatureCelsius = float(input('Informe a temperatura em °C: '))

temperatureFahrenheit = ((9 * temperatureCelsius) / 5) + 32

print(
    f'A temperatura de {temperatureCelsius:.2f}°C corresponde a {temperatureFahrenheit:.2f}°F!')
