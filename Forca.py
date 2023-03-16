"""Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade 
  para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
  na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver
  na palavra secreta; exiba *.
  Faça a contagem de tentativas do seu usuário.
"""
palavra_secreta = 'Vanessa da Mata'.lower()
letras_acertadas = ''

while True:
  print('dica:um cantor(a) famoso(a)')
  letra_digitada = str(input('Digite uma letra: '))

  if len(letra_digitada) > 1:
    print('Digite apenas uma letra!')
    continue

  if letra_digitada in palavra_secreta:
    letras_acertadas += letra_digitada

  palavra_formada = ''
  for letra_secreta in palavra_secreta:
    if letra_secreta in letras_acertadas:
      palavra_formada += letra_secreta
    elif letra_secreta == ' ':
      palavra_formada += ' '
    else:
      palavra_formada += '*'

  palavra_secreta_formatada = palavra_formada.replace(' ', '')  
  print(f'A palavra secreta é {palavra_formada}\nA palavra secreta tem {len(palavra_secreta_formatada)} caracteres')

  if palavra_formada == palavra_secreta:
    print('Você Ganhou, meus parabéns!')
    break
