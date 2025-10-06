frase = 'a grama é amarga'

frase_lower = frase.lower()

frase_sem_barras = frase_lower.replace(' ','')
frase_sem_travessao = frase_sem_barras.replace('-','')
frase_sem_virgulas = frase_sem_travessao.replace(',','')
frase_sem_ponto_final = frase_sem_virgulas.replace('.','')
frase_sem_exclamacao = frase_sem_ponto_final.replace('!','')
frase_sem_interrogacao = frase_sem_exclamacao.replace('?','')
frase_sem_dois_pontos = frase_sem_interrogacao.replace(':','')
frase_sem_ponto_e_virgula = frase_sem_dois_pontos.replace(';','')
frase_sem_underline = frase_sem_ponto_e_virgula.replace('_','')

frase_sem_acento_a_circunflexo = frase_sem_ponto_e_virgula.replace('â','')
frase_sem_acento_e_circunflexo = frase_sem_acento_a_circunflexo.replace('ê','')
frase_sem_acento_i_circunflexo = frase_sem_acento_e_circunflexo.replace('î','')
frase_sem_acento_o_circunflexo = frase_sem_acento_i_circunflexo.replace('ô','')
frase_sem_acento_u_circunflexo = frase_sem_acento_o_circunflexo.replace('û','')

frase_sem_acento_a_agudo = frase_sem_acento_u_circunflexo.replace('á','')
frase_sem_acento_e_agudo = frase_sem_acento_a_agudo.replace('é','')
frase_sem_acento_i_agudo = frase_sem_acento_e_agudo.replace('í','')
frase_sem_acento_o_agudo = frase_sem_acento_i_agudo.replace('ó','')
frase_sem_acento_u_agudo = frase_sem_acento_o_agudo.replace('ú','')

frase_sem_tio_a = frase_sem_acento_u_agudo.replace('ã','')
frase_sem_tio_o = frase_sem_tio_a.replace('õ','')

frase_sem_crase_a = frase_sem_tio_o.replace('à','')
frase_sem_crase_e = frase_sem_crase_a.replace('è','')
frase_sem_crase_i = frase_sem_crase_e.replace('ì','')
frase_sem_crase_o = frase_sem_crase_i.replace('ò','')
frase_sem_crase_u = frase_sem_crase_o.replace('ù','')

frase1 = frase_sem_acento_u_circunflexo
frase2 = frase1[::-1]

if frase2 == frase1:
    print('É palíndromo')
else:
    print('Não é palíndromo')