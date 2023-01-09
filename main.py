import time

def ger_perguntas():
    for asr in perguntas:
        time.sleep(2.5)
        print(asr)
        
perguntas = [
    
('Você está em um quarto escuro, O luar brilha através da janela.'),
('Há OURO no canto, junto com uma PÁ e uma CORDA.'),
('Há uma PORTA para o LESTE.'),
('O que deseja fazer?'),
(input('Opções de jogo: PEGAR OURO, PEGAR PÁ, PEGAR CORDA.'))
]



ger_perguntas()


