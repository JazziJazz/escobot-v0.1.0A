import discord
import asyncio

list_of_messages = []


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Você efetuou o login com sucesso e o bot {self.user.name} está no ar.\nO seu id é equivalente a: '
              f'{self.user.id}.')

    async def on_message(self, message):
        global list_of_messages

        #  Verifica se o author da mensagem é o próprio bot.
        if message.author == self.user:
            return

        #  Verifica se o canal da mensagem enviada é igual a: '🤖comandos', e se o attachments é diferente de zero.
        #  Se attachments for diferente de zero, significa que a mensagem é um arquívo.
        if message.attachments and (message.channel.name == '🤖comandos'):
            emojis_to_add = ['✅', '❎']
            for i in range(0, 2):
                await message.add_reaction(emojis_to_add[i])

            list_of_messages.append(message)
            return

        #  Verifica se o nome do canal é: '🤖comandos' e também se o conteúdo da mensagem é: '!duvida'.
        if (message.channel.name == '🤖comandos') and (message.content == '!duvida'):
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
            return await message.channel.send(embed=embed)
        return

    async def on_reaction_add(self, reaction, user):
        # Se o autor da reação for o próprio bot, então a chamada da função é completamente desconsiderada.
        if user.id == self.user.id:
            return

        global list_of_messages

        #  A variável channel contém a classe MyClient e um método de classe chamado get channel, que pega o ID do
        #  channel. O ID passado é o de 'bot-comandos', portanto só deverá funcionar aqui.
        channel = MyClient.get_channel(self, 698932745841279050)
        list_of_roles = []

        for roles in user.roles:
            list_of_roles.append(roles.name)

        #  Se a reação for igual a '✅' e o usuário tiver a role 'catcrew', então ele executará o bloco de instrução.
        if 'catcrewww' in list_of_roles:
            if reaction.emoji == '✅':
                await channel.send('É doidão, deu certo.')
            else:
                pass
        else:
            #  Esperará um segundo e meio, então para cada mensagem enviada, se algum membro sem o cargo 'catcrew'
            #  reagir a mensagem, então a reação dessa mensagem será removida.
            await asyncio.sleep(1.5)
            for messages in list_of_messages:
                await messages.remove_reaction(reaction.emoji, user)

            message = list_of_messages[0].author
            embed = discord.Embed(title='**Você está de palhaçada comigo? Seu _filho da puta_.**',
                                  description='Você **não é um avaliador de roleplay**. Você tá _consumindo meu poder'
                                              ' de processamento atoa?_ Mas é um desgraçado mesmo.\n\nSe você continuar'
                                              ' com essa grande merda eu vou banir você do servidor, e você vai para '
                                              'puta que pariu, **seu merda**. Se você continuar com isso eu vou '
                                              'tomar minhas **providências** e você **vai tomar no cu**.',
                                  color=0xf5cc00)
            embed.set_thumbnail(url=self.user.avatar_url)
            return await message.send(embed=embed)


client = MyClient()
client.run('')
