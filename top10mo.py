import time

print('     Top 10 primeiras coisas com a mo    ')

eu = input('\033[35;41mOlá! Para continuar digite: "oimoanoite": \033[0m')

while True:
    if eu == 'oimoanoite':
        escolha = input('\033[32;45mDe 1 a 10 escolha qual lembrança deseja: \033[0m')
        while escolha == '0123456789':
            print('Ok, aqui está uma novidade na vida de Hiago com você\033[0m')
        if escolha == '1':
            print('\033[31mPrimeira vez tomando banho com alguém\033[0m')
        elif escolha == '2':
            print('\033[32mViajem de casal para praia\033[0m')
        elif escolha == '3':
            print('\033[33mJantar romântico (até jantar normal ;( )\033[0m')
        elif escolha == '4':
            print('\033[34mFalar "eu te amo" ao mesmo tempo durante o sexo (conexão <3)\033[0m')
        elif escolha == '5':
            print('\033[35mCuidar de alguém dodói\033[0m')
        elif escolha == '6':
            print('\033[36mEscapar de uma tentativa de assalto\033[0m')
        elif escolha == '7':
            print('\033[90mLevar pra "cama" quando se conheceu\033[0m')
        elif escolha == '8':
            print('\033[1;31;43mIr á um show sertanejo e de pagode\033[0m')
        elif escolha == '9':
            print('\033[4;34mIr a um zoológico em casal\033[0m')
        elif escolha == '10':
            print('\033[32;46mChurrasco com os sogros\033[0m')
        elif escolha == '11':
            print('\033[7;35mIr ao motel rsrsrsrsrs\033[0m')
        elif escolha == '12':
            print('\033[4;35mDar uma aliança de compromisso\033[0m')
        elif escolha == '13':
            print('\033[33;42mFechar um casamento (2)\033[0m')
        elif escolha == '14':
            print('\033[7;36mCancelar um casamento (2)\033[0m')
        else:
            print('\033[100mDigite um número de 1 ~ 10\033[0m')
            
        time.sleep(2)
    else:
        print('Errado.')
