nota1 = float (input('Diigte a Nota do Aluno: '))
nota2 = float (input('Digite Segunda nota do Aluno: '))
media = (nota1 + nota1) / 2
print ('Com o Aluno Tirando {:.1f} e {:.1f}, A Média do Aluno Será {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print ('O Aluno Está em RECUPERAÇÃO')
elif media < 5:
    print ('O Aluno Está REPROVADO')
else:
    print ('O Aluno Está APROVADO')