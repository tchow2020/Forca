import time
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_questions(count):
    for teste, asr in enumerate(perguntas):
        if teste == count:
            time.sleep(2.5)
            print(asr[0])
            res = input('\n> ')
            vall = similarity(res, asr[1])
            if vall < 0.8:
                print('Tente novamente!')
                return get_questions(count)
            count += 1

perguntas = [
    ('Você está em um quarto escuro, O luar brilha através da janela, "olhe ao seu redor" para ver oque tem no local.', 'olhando ao meu redor'),
    ('Há OURO no canto, junto com uma PÁ e uma CORDA.\nO que deseja fazer?', 'pegar ouro'),
    ('Pegou!', 'pegar pá'),
    ('Pegou!', 'pegar corda'),
    ('Pegou!\n\nHá uma PORTA para o LESTE.', 'abrir porta'),
    ('A porta abriu\n\nA LUA PÁLIDA SORRI PARA VOCÊ. \nVocê está em uma floresta. Existem caminhos para o NORTE, OESTE, e LESTE. \nQual caminho você quer seguir?', 'norte'),
    ('A LUA PÁLIDA SORRI PARA VOCÊ. \nVocê seguiu pelo caminho do NORTE, olhe em sua volta.', 'olhando ao meu redor'),
    ('Você percebe que há uma PLACA, um caminho que está obstruído e um poço, o que você quer fazer? ', 'olhar poço'),
    ('Você encontra um caderno ao lado do poço, e se aproximando você ouve sons vindos de seu interior.\npegar caderno?', 'pegando caderno'),
    ('Lendo o caderno você encontra uma localização e seguindo você se depara com um carro velho já a muito tempo abandonado. \nvasculhe o carro e veja se tem algo útil pra você', 'olhando o carro'),
    ('Você encontra uma CHAVE')
]

get_questions(0)