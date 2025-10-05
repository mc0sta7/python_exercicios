"""
frase = 'Socorram-me, subi no ônibus em Marrocos'
frase2 = frase[::-1]
if frase2 == frase:
    print('Palindromo')
else:
    print('Não é Palindromo')
"""
frase = 'Socorram-me, subi no ônibus em Marrocos'
frase_lower = frase.lower()
frase_sem_espacos = frase_lower.strip(" -")
print(frase_sem_espacos)