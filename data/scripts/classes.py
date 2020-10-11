import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Você efetuou o login com sucesso e o bot {self.user.name} está no ar.\nO seu id é equivalente a: '
              f'{self.user.id}.')

    async def on_message(self, message):
        #  Verifica se o author da mensagem é o próprio bot.
        if message.author == self.user:
            return

        #  Verifica se o canal da mensagem enviada é igual a: '🤖comandos', e se o attachments é diferente de zero.
        if (len(message.attachments) != 0) and (message.channel.name == '🤖comandos'):
            for attachments in message.attachments:
                if attachments.url.endswith('png') or attachments.url.endswith('jpg') or \
                   attachments.url.endswith('jpeg') or attachments.url.endswith('gif'):

                    emoji = ['✅', '❎']

                    for i in range(0, 2):
                        await message.add_reaction(emoji[i])

        #  Verifica se o nome do canal é: '🤖comandos' e se a mensagem é igual a !duvida.
        elif (message.channel.name == '🤖comandos') and (message.content == '!duvida'):
            await message.channel.send('O funcionamento é bem simples. A cada imagem enviada eu adicionarei reações'
                                       ' a elas, o avaliador de roleplay ira clicar em uma das duas e será '
                                       'contabilizada a sua contribuição com a facção. O resultado da resposta será'
                                       ' enviado para você através de mensagem privada, certifique-se de ficar '
                                       'atento a minhas mensagens. A falta de contribuição ocasionará em sapatos de'
                                       ' concreto feito sob medida e um passeio no lago.')
        else:
            return


client = MyClient()
client.run('NzM1MTg0NDk1MDQ4Nzg1OTIw.Xxcj6g.gofCZ3ZJ9aZmJf4pCIYt-YKDYIg')
