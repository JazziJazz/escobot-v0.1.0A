import discord
import asyncio


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

            emoji = ['✅', '❎']

            for attachments in message.attachments:
                if attachments.url.endswith('png') or attachments.url.endswith('jpg') or \
                   attachments.url.endswith('jpeg') or attachments.url.endswith('gif'):

                    for i in range(0, 2):
                        await message.add_reaction(emoji[i])

            def check(reaction, user):
                return user == message.author and reaction.emoji == '✅'

            try:
                reaction, user = await client.wait_for('add_reaction', timeout=10.0, check=check)
            except asyncio.TimeoutError:
                await message.remove_reaction(emoji[0], self.user)
            else:
                await message.remove_reaction(emoji[1])
        #  Verifica se o nome do canal é: '🤖comandos' e se a mensagem é igual a !duvida.
        elif (message.channel.name == '🤖comandos') and (message.content == '!duvida'):
            embed = discord.Embed(title='Está com dúvida sobre a avaliação de roleplay?',
                                  description='`Etapa número um:`\nAo enviar suas imagens para avaliação, eu irei '
                                              'adicionar duas reações em cada uma delas, uma é positiva e outra é negat'
                                              'iva, _*não clique*_ em nenhuma delas, são de uso exclusivo do avaliador,'
                                              ' sua reação só vai **dificultar** o meu serviço aqui.\n\n`Etapa número '
                                              'dois:`\nQuando o avaliador clicar na reação, irei enviar uma mensagem '
                                              'para você no privado, com o código a ser postado no fórum e contabiliza'
                                              'rei o seu progresso dentro da facção. Tudo é feito de forma automática,'
                                              ' afim de automatizar ao máximo o processo de avaliação, você também '
                                              'pode consultar a sua posição no ranking dos membros que mais postaram'
                                              ' essa semana ou mês, basta digitar _**!ranking**_ em qualquer channel '
                                              'deste servidor.',
                                  color=0xf5cc00)
            embed.set_thumbnail(url=self.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            return


client = MyClient()
client.run('NzM1MTg0NDk1MDQ4Nzg1OTIw.Xxcj6g.yKkfE65khz7iS8SAbtL3i75nWBk')
