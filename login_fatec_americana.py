#login fatec americana
print('')
print('Login Fatec Americana')
print('')
print('')
print('')
print('Informe o RA e Senha')
print('')
print('')
print('')


#variável para armazenar o RA
meu_ra='0040482311005'
print('O valor do RA é:',meu_ra)
minha_senha='1234'
print('O valor da minha senha é:',minha_senha)



ra_digitado=input('\nEntre com o RA: ')

print('\nO RA informado foi:',ra_digitado)

#Vou testar se o RA digitado é igual ao definido
#Se o RA digitado for igual ao definido, testar se a senha é igual a definida

if meu_ra==ra_digitado:
    print('O RA digitado confere com o definido')
    senha_digitada=input('\nInsira a senha: ')
    print('A senha digitada foi:',senha_digitada)

    if minha_senha==senha_digitada:
        print('\nA senha digitada confere com a do usuário')
    else:
        print('\nERRO: A senha digitada está INCORRETA')
else:
    print('\nERRO: RA digitado NÃO confere com o definido')
