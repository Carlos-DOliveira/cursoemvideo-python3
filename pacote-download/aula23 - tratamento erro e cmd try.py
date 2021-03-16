try:  # para tentar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: # mostrar o erro
    print(f'Problema encontrado foi {erro.__class__}')


        ##### PODE TER VÁRIOS EXCEPT DENTRO DO TRY
#except TypeError:
#    BLOCO
#except ValueError:
#    BLOCO
#except OSError:
#    BLOCO


else:  # caso de certo
    print(f'O resultado {r:.1f}')
finally:    # sempre vai aparecer
    print('Volte sempre! Muito obrigado')