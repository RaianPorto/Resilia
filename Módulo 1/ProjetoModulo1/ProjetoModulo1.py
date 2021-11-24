###########################################################################################################
def fimDoJogo():
    print('\nFinalizando Jogo...\n')
    print('\nFINALIZADO!\n')
    exit()
###########################################################################################################

###########################################################################################################
def menuPrincipal():
    print('''
    MENU PRINCIPAL
    ==========================

        [1] - Iniciar jogo
        [2] - Sobre o jogo
        [0] - Sair do Jogo

    ==========================
    ''')

    opcaoEscolhida = input('Informe a opção desejada: ')

    if opcaoEscolhida == '0':
        fimDoJogo()
    elif opcaoEscolhida == '1':
        print('\nINICIANDO JOGO...\n')
        inicioDoJogo()
    elif opcaoEscolhida == '2':
        print('''
        
        SOBRE O JOGO:
        =====================================================================================================

        Jogo em estilo RPG de quiz inspirado na área de Softskills.
        Jogo criado por Raian Porto para projeto de fim de módulo 1 do curso de analista de Dados da Resilia.

        AUXILIARES DO PROJETO:
        =====================================================================================================

        - Bruna Pereira
        - Jonatas Carvalho
        - Nathaly Cavalvante

        SUBMENU SOBRE O JOGO
        =====================================================================================================

        [1] - Voltar para o menu principal
        [2] - Finalizar jogo

        ''')

        subMenuOpcao = input('Informa a opção desejada: ')
        
        if subMenuOpcao == '1':
            menuPrincipal()
        elif subMenuOpcao == '2':
            fimDoJogo()
        else:
            print('Opção inválida!')
            subMenuOpcao = input('Informe a opção desejada: ')
    else:
        print('Você informou uma opção inválida. Escolha um número entre os indicados abaixo!')
###########################################################################################################

###########################################################################################################
def escolhaDePersonagem():
    print('''
    Escolha o personagem que você quer ajudar a alcançar o conhecimento de Pitão!

        [1] - Procastinadora Bru
        [2] - Eterno Aprendiz Jonas
        [3] - Ocupada Nat
        [0] - Voltar para o menu principal
    ''')

    personagemEscolhido = input('Informe o personagem: ')

    if personagemEscolhido == '1':
        jogandoComBru()
    elif personagemEscolhido == '2':
        jogandoComJonas()
    elif personagemEscolhido == '3':
        jogandoComNat()
    elif personagemEscolhido == '0':
        print('\nVoltando para o menu principal!\n')
        menuPrincipal()
    else:
        print('Personagem inválido! Informe um personagem válido.')
        escolhaDePersonagem()
###########################################################################################################

###########################################################################################################
def inicioDoJogo():
    print('''
    [datadeIniciodocurso] de [mesdeInicio] de 2021

    Quatro jovens buscam o mesmo objetivo: Alcançar o grande conhecimento de Pitão!
    
    Mas para atingir esse objetivo cada um deles enfretam diferentes problemas pessoais e precisarão da sua ajuda para conquistar o poder de Pitão.

    Bru - Aquela pessoa que sempre tem o hábito de deixar tudo para última hora. Uma procrastinadora nata para tudo que deveria levar mais à sério.
    Jonas - Jovem com dificuldade de concentração e sem foco para o aprendizado.
    Nat - Uma mulher independente, ocupada que precisa se disciplinar e conciliar trabalho e estudo.
    ''')

    personagem = escolhaDePersonagem()
    return personagem
###########################################################################################################

###########################################################################################################
def gameOver(perdedor):

    if perdedor == 'B':
        print('\nZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZz...\n')
        print('\nParece que a preguiça foi maior que a vontade de Bru aprender Pitão. Acabou procrastinando!\n')
        print('Gostaria de tentar de novo?')
        resposta = input('Sim ou Não?')
        if resposta == 'Não' or resposta == 'não' or resposta == 'nao' or resposta == 'n' or resposta == 'N':
            print('\nVoltando para a seleção de personagens...\n')
            escolhaDePersonagem()
        else:
            print('Vamos tentar ajudar Bru mais uma vez!')
            jogandoComBru()
    elif perdedor == 'J':
        print('\nPéssima escolha!\n')
        print('\nO vício no Free Fire foi mais alto e Jonas desviou sua atenção para o que não deveria.\n')
        print('Gostaria de tentar de novo?')
        resposta = input('Sim ou Não?')
        if resposta == 'Não' or resposta == 'não' or resposta == 'nao' or resposta == 'n' or resposta == 'N':
            print('Voltando para a seleção de personagens...')
            escolhaDePersonagem()
        else:
            print('Vamos tentar ajudar Jonas mais uma vez!')
            jogandoComJonas()
    else:
        print('Triiiiiiiiim... Seu tempo acabou!')
        print('Você não ajudou Nat a gerir seu tempo da melhor forma.')
        print('Gostaria de tentar de novo?')
        resposta = input('Sim ou Não?')
        if resposta == 'Não' or resposta == 'não' or resposta == 'nao' or resposta == 'n' or resposta == 'N':
            print('Voltando para a seleção de personagens...')
            escolhaDePersonagem()
        else:
            print('Vamos tentar ajudar Nat mais uma vez!')
            jogandoComNat()
###########################################################################################################

###########################################################################################################
def jogandoComBru():
    print('''
    Espero que tenha trazido um guindaste porque Bru está com a preguiça do tamanho de um mamute e só assim você irá conseguir retirar Bru da cama.

    Está pronto(a)? Espero que sim, vamos lá!

    ---------- FASE 1 - O INÍCIO DO PROJETO

        Bru posssui um projeto para entregar em uma sexta-feira, ela tem total ciencia da importância do projeto e apenas 5 dias para chegar o dia da entrega, mas para conseguir entrega-lo a tempo ela precisa encarar a procrastinação. Na noite passada Bru havia ido para uma festa mesmo sabendo que teria uma semana cheia. Ela sabe que tem que usar a semana para trabalhar no projeto logo cedo.

    [1] - Acordar bem cedo
    [2] - Dormir até tarde
    [3] - Se lamentar por ter ido para a festa.

    ''')

    resposta = input('O que Bru deve fazer? ')

    while resposta:
        if resposta == '1':
            print('''
            Bru acordou cedo, preparou o café e pensou em assistir uma série enquanto comia. Seria uma boa idéia?
            
            [1] - Assitir uma série enquanto come
            [2] - Comer sem distrações
            [3] - Deixar de tomar café para iniciar o projeto
            
            ''')

            resposta = input('O que Bru deve fazer? ')

            while resposta:
                if resposta == '1':
                    gameOver('B')
                elif resposta == '2':
                    print('''
                    Bru tomou seu café e imediatamente deu inicio ao seu projeto. Ela planejou minuciosamente tudo o que deverá fazer nos proximos dias para conseguir entregar o projeto a tempo. Por volta de 11:30h já havia produzido mais que o suficiente para um dia e pensa em parar pela tarde e voltar a adiantar o projeto pela noite. Porem, no fim da tarde, seu namorado liga convidando Bru para jantar.

                    [1] - Bru aceita o convite
                    [2] - Bru explica que precisa se dedicar ao projeto e tentar combinar com ele depois da entrega do projeto 
                    [3] - Bru recusa o convite e termina o namoro porque seu namorado não deveria fazer esse convite logo agora. Total falta de compreensão!

                    ''')

                    resposta = input('O que Bru deve fazer?')
                    while resposta:
                        if resposta == '1':
                            gameOver('B')
                        elif resposta == '2':
                            print('''
                            Seu namorado entendeu a situação e foi até a casa de Bru preparar um jantar para tentar ajudar e levou um presente. Bru abriu o presente e viu que era um livro. Enquanto seu namorado preparava a janta.

                            [1] - Enquanto ele prepara a janta, Bru trabalha ainda mais no projeto para adiantar
                            [2] - Bru vai para a cozinha e ajuda seu namorado com a janta
                            [3] - Bru espera seu namorado terminar a janta para que ele ajude no projeto tambem

                            ''')

                            resposta = input('O que Bru deve fazer?')

                            while resposta:
                                if resposta == '1':
                                    print('''
                                    Enquanto Bru estava trabalhando no projeto seu celular toca. Era uma notificação do instagram. Raí havia marcado Bru em uma publicação de sorteio.

                                    [1] - Participar tambem porque se tratava de sorteio de pote tupperware
                                    [2] - Ignorar já que estava tendo sorte no amor, no jogo ia ser azar.
                                    [3] - Desligar o celular para não ter distrações.

                                    ''')

                                    resposta = input('O que Bru deve fazer?')
                                    while resposta:
                                        if resposta == '1':
                                            gameOver('B')
                                        elif resposta == '2':
                                            gameOver('B')
                                        elif resposta == '3':
                                            print('''
                                            Faltando apenas 2 dias para a entrega do projeto e agora sem distrações Bru começa a trabalhar no projeto e alguns minutos depois percebe que precisa de ajuda para resolver um erro que apareceu no seu código.

                                            [1] - Apaga tudo e começa tudo de novo.
                                            [2] - Chuta o balde e desiste de tudo aquilo.
                                            [3] - Ligar para sua amigona de trabalho Marisa e pedir ajuda.

                                            ''')

                                            resposta = input('O que Bru deve fazer?')
                                            while resposta:
                                                if resposta == '1':
                                                    gameOver('B')
                                                elif resposta == '2':
                                                    gameOver('B')
                                                elif resposta == '3':
                                                    print('''
                                                    FASE 2 - A CONSEQUÊNCIA DA PROCRASTINAÇÃO

                                                    No dia seguinte, a campanhia toca e quando ela vai abrir a porta se depara com sua amiga Marisa segurando um pote de sorvete. Lembrou que havia a convidado para almoçar em sua casa e ajudar com o erro no projeto.
                                                    No momento, Bru torceu para que dentro do pote não houvesse sorvete e sim feijão pois não havia preparado nada para o almoço.
                                                    Marisa imediatamente a cumprimenta e alerta Bru de que havia trazido a sobremesa.
                                                    
                                                    [1] - Mostrar o código para Marisa dar uma olhada enquanto Bru faz o almoço
                                                    [2] - Deixar Marisa olhando o código enquanto ela vai para a cozinha comer o sorvete todo sozinha
                                                    [3] - Pedir o almoço no ifood e acompanhar a análise do código junto com Marisa.

                                                    ''')

                                                    resposta = input('O que Bru deve fazer?')

                                                    while resposta:
                                                        if resposta == '1':
                                                            print('''
                                                            Perdido um dia procurando o erro Marisa percebe que faltou um fechar um parentese na função print.

                                                            [1] - Bru perde a cabeça e joga o PC longe
                                                            [2] - Bru chora por ter perdido tempo por causa de um detalhe
                                                            [3] - Bru agradece Marisa, se despede e volta a trabalhar no projeto.

                                                            ''')

                                                            resposta = input('O que Bru deve fazer?')

                                                            while resposta:
                                                                if resposta == '1':
                                                                    gameOver('B')
                                                                elif resposta == '2':
                                                                    gameOver('B')
                                                                elif resposta == '3':
                                                                    print('''
                                                                    Em um momento de reflexão, Bru olha para a mesa e vê o livro que havia ganhado de presente do seu namorado e que está louca para ler mesmo sabendo que não pode perder o foco e a data da entrega está cada vez mais proxima.

                                                                    [1] - Ler um pouco do livro para relaxar
                                                                    [2] - Jogar o livro longe
                                                                    [3] - Pegar o livro, guardar para não se render e voltar ao projeto

                                                                    ''')

                                                                    resposta = input('O que Bru deve fazer?')

                                                                    while resposta:
                                                                        if resposta == '1':
                                                                            gameOver('B')
                                                                        elif resposta == '2':
                                                                            gameOver('B')
                                                                        elif resposta == '3':
                                                                            print('''
                                                                            FASE 3 - O dia da entrega

                                                                            No dia da entrega Bru conseguiu terminar o projeto mas não se sente segura pois percebe que se não houvesse enrolado tanto e deixado de fazer coisas não tão importantes teria tempo para possíveis imprevistos. Ela ainda possui algumas horas para finalizar o projeto já que a entrega é até o fim da noite.

                                                                            [1] - Revisar todo o projeto, ver se existem possíveis falhas e corrigi-las
                                                                            [2] - Deixar como está e torcer para dar tudo certo
                                                                            [3] - Pensar: Na minha máquina funciona

                                                                            ''')

                                                                            resposta = input('O que Bru deve fazer?')
                                                                            
                                                                            while resposta:
                                                                                if resposta == '1':
                                                                                    print('PARABÉNS! VOCÊ CONSEGUIU VENCER A PROCRASTINAÇÃO!')
                                                                                    menuPrincipal()
                                                                                elif resposta == '2':
                                                                                    gameOver('B')
                                                                                elif resposta == '3':
                                                                                    gameOver('B')
                                                                                else:
                                                                                    print('Opcão inválida! Informe uma opção válida.')
                                                                                    resposta = input('O que Bru vai fazer?')
                                                                        else:
                                                                            print('Opcão inválida! Informe uma opção válida.')
                                                                            resposta = input('O que Bru vai fazer?')
                                                                else:
                                                                    print('Opcão inválida! Informe uma opção válida.')
                                                                    resposta = input('O que Bru vai fazer?')
                                                        elif resposta == '2':
                                                            gameOver('B')
                                                        elif resposta == '3':
                                                            gameOver('B')
                                                        else:
                                                            print('Opcão inválida! Informe uma opção válida.')
                                                            resposta = input('O que Bru vai fazer?')
                                                else:
                                                    print('Opcão inválida! Informe uma opção válida.')
                                                    resposta = input('O que Bru vai fazer?')
                                        else:
                                            print('Opcão inválida! Informe uma opção válida.')
                                            resposta = input('O que Bru vai fazer?')
                                elif resposta == '2':
                                    gameOver('B')
                                elif resposta == '3':
                                    gameOver('B')
                                else:
                                    print('Opcão inválida! Informe uma opção válida.')
                                    resposta = input('O que Bru vai fazer?')
                        elif resposta == '3':
                            gameOver('B')
                        else:
                            print('Opcão inválida! Informe uma opção válida.')
                            resposta = input('O que Bru vai fazer?')
                elif resposta == '3':
                    gameOver('B')
                else:
                    print('Opcão inválida! Informe uma opção válida.')
                    resposta = input('O que Bru vai fazer?')
        elif resposta == '2':
            gameOver('B')
        elif resposta == '3':
            gameOver('B')
        else:
            print('Opcão inválida! Informe uma opção válida.')
            resposta = input('O que Bru vai fazer?')
###########################################################################################################

###########################################################################################################
def jogandoComJonas():
    print('Então você prefere ajudar o Jonas e guia-lo pelo caminho do aprendizado?')
    print('Tudo bem, boa sorte, você vai precisar!')

    print('FASE 1 - O MOTIVO DO APRENDIZADO')

    print('''
    Jonas irá realizar uma prova de Pitão no próximo fim de semana e precisar aprender tudo o que puder até o dia da prova. Porem, ele possui uma grande dificuldade de aprendizado devido a diversos fatores. 

    [1] - Pensar em fazer a prova na cara e na coragem.
    [2] - Buscar uma orientação sobre o assunto com a conselheira Taís.
    [3] - Fazer a prova por experiência e tentar novamente outro ano.
    ''')

    resposta = input('O que Jonas vai fazer?')

    while resposta:
        if resposta == '1':
            gameOver('J')
        elif resposta == '2':
            print('''
            Jonas procurou Taís para saber o que ele precisa fazer para conseguir se preparar e entender de maneira rápida e produtiva todo o conteudo necessario de Pitão. Enquanto Taís explica, Jonas não para de mexer no celular e logo Taís demonstra uma raiva porque Taís é dessas, adora que as pessoas falem no olho da pessoa.

            [1] - Jonas mostra um meme para Taís
            [2] - Jonas nem liga porque escuta com os ouvidos
            [3] - Jonas percebe que deixou Taís desconfortável e dedica sua atenção a ela.

            ''')
            resposta = input('O que Jonas vai fazer?')

            while resposta:
                if resposta == '1':
                    gameOver('J')
                elif resposta == '2':
                    gameOver('J')
                elif resposta == '3':
                    print('''
                    Tais então, pergunta para Jonas se ele sabe o que uma pessoa que possui dificuldade de aprendizado possui

                    [1] - Jonas explica que é uma pessoa que possui uma maneira diferente de aprender, devido a um barreira que pode ser cultural, cognitiva ou emocional.
                    [2] - Jonas diz que são pessoas ignorantes.
                    [3] - Jonas diz que são pessoas que não possui os mesmos recursos que outros
                    ''')

                    resposta = input('O que Jonas vai fazer?')

                    while resposta:
                        if resposta == '1':
                            print('''
                            Taís confirma a resposta de Jonas informando que ele tem dificuldade de aprendizagem.

                            [1] - Jonas mantem a calma pois está diante da pessoa que pode resolver esse problema num estalar de dedos... quase, a conselheira Taís. 
                            [2] - Jonas começa a chorar
                            [3] - Jonas entra em desespero
                            ''')

                            resposta = input('O que Jonas vai fazer?')

                            while resposta:
                                if resposta == '1':
                                    print('''
                                    Tais orienta Jonas a se desligar um pouco do celular, pelo menos até a prova, e encontrar com a Sábia Marisa em sua casa as 20:40h pois ela pode orienta-lo sobre o caminho mais adequado para aprender Pitão de maneira simples.

                                    [1] - Jonas segue o conselho de Taís e desliga o celular ali mesmo em sua frente e vai atrás de Marisa
                                    [2] - Fica olhando para o celular se imaginando sem ele com a música My Heart Will Go On do tocando em sua cabeça
                                    [3] - Continua chorando
                                    ''')

                                    resposta = input('O que Jonas vai fazer?')

                                    while resposta:
                                        if resposta == '1':
                                            print('''
                                            A caminho do encontro com Marisa, Jonas encontra seu amigo Bebêzorde que o chama para jogar um Free Fire.

                                            [1] - Jonas explica que não pode no momento porque precisa estudar para uma prova
                                            [2] - Jonas vira a cara e sai correndo para longe porque a tentação de jogar um FF é forte
                                            [3] - Jonas vai, claro!
                                            ''')

                                            resposta = input('O que Jonas vai fazer?')

                                            while resposta:
                                                if resposta == '1':
                                                    print('''
                                                    FASE 2 - Inovando no aprendizado

                                                    Ao chegar a casa de Marisa, ela atende a porta com um pote de feijão na mão, ou será sorvete? Enfim, ela diz que estava a sua espera há 1h e o convida para entrar.

                                                    [1] - Olha para tras e fica se imaginando jogando FF com Bebêzorde.
                                                    [2] - Fica olhando para o pote tentando ver se era sorvete ou feijão.
                                                    [3] - Jonas explica para Marisa que estava 5 minutos adiantado do horário que Taís havia dito e entra.

                                                    ''')

                                                    resposta = input('O que Jonas vai fazer?')

                                                    while resposta:
                                                        if resposta == '1':
                                                            gameOver('J')
                                                        elif resposta == '2':
                                                            gameOver('J')
                                                        elif resposta == '3':
                                                            print('''
                                                            Marisa então diz que Taís vive no horário de verão, aplica um método inovador que só ela sabe e ordena que Jonas treine aquele método ate a hora da prova.

                                                            [1] - Jonas se distrai com o cachorrinho de Marisa, até porque ninguem resiste a um cachorrinho(Não é, Gabriel Oliveira?)
                                                            [2] - Jonas treina o método incansavelmente conforme sua mestra tinha ordenado
                                                            [3] - Jonas continua tentando adivinhar o que tinha no pote.
                                                            ''')

                                                            resposta = input('O que Jonas vai fazer?')

                                                            while resposta:
                                                                if resposta == '1':
                                                                    gameOver('J')
                                                                elif resposta == '2':
                                                                    print('''
                                                                    ÚLTIMA FASE - 
                                                                    Enfim, o dia da prova chegou e Jonas está nervoso. Entra na sala escolhe o melhor lugar, se acomoda na carteira mas começa a se distrair com uma borboleta que entrou na sala.
                                                                    
                                                                    [1] - Continua olhando a borboleta
                                                                    [2] - Fica com medo da prova e sai correndo da sala.
                                                                    [3] - Mantem a calma, principalmente, o foco e lembra dos grandes ensinamentos da Sábia Marisa.

                                                                    ''')

                                                                    resposta = input('O que Jonas vai fazer?')

                                                                    while resposta:
                                                                        if resposta == '1':
                                                                            gameOver('J')
                                                                        elif resposta == '2':
                                                                            gameOver('J')
                                                                        elif resposta == '3':
                                                                            print('''
                                                                            PARABÉNS!
                                                                            Você passou pelas adversidades do aprendizado e mesmo com tantas distrações a sua volta manteve o foco e conseguiu aprender tudo o que precisa para a prova de Pitão e tirou nota... 10!
                                                                            ''')
                                                                            menuPrincipal()
                                                                        else:
                                                                            print('Opcão inválida! Informe uma opção válida.')
                                                                            resposta = input('O que Jonas vai fazer?')

                                                                elif resposta == '3':
                                                                    gameOver('J')
                                                                else:
                                                                    print('Opcão inválida! Informe uma opção válida.')
                                                                    resposta = input('O que Jonas vai fazer?')
                                                        else:
                                                            print('Opcão inválida! Informe uma opção válida.')
                                                            resposta = input('O que Jonas vai fazer?')
                                                elif resposta == '2':
                                                    gameOver('J')
                                                elif resposta == '3':
                                                    gameOver('J')
                                                else:
                                                    print('Opcão inválida! Informe uma opção válida.')
                                                    resposta = input('O que Jonas vai fazer?')
                                        elif resposta == '2':
                                            gameOver('J')
                                        elif resposta == '3':
                                            gameOver('J')
                                        else:
                                            print('Opcão inválida! Informe uma opção válida.')
                                            resposta = input('O que Jonas vai fazer?')

                                elif resposta == '2':
                                    gameOver('J')
                                elif resposta == '3':
                                    gameOver('J')
                                else:
                                    print('Opcão inválida! Informe uma opção válida.')
                                    resposta = input('O que Jonas vai fazer?')
                        elif resposta == '2':
                            gameOver('J')
                        elif resposta == '3':
                            gameOver('J')
                        else:
                            print('Opcão inválida! Informe uma opção válida.')
                            resposta = input('O que Jonas vai fazer?')
                else:
                    print('Opcão inválida! Informe uma opção válida.')
                    resposta = input('O que Jonas vai fazer?')
        elif resposta == '3':
            gameOver('J')
        else:
            print('Opcão inválida! Informe uma opção válida.')
            resposta = input('O que Jonas vai fazer?')
###########################################################################################################

###########################################################################################################
def jogandoComNat():
    print('Como diria Cazuza: O tempo não para, então corre para ajudar a Nat antes que o tempo acabe!')

    print('''
    FASE 1 - DELEGANDO AS TAREFAS

    Nat é uma moça que possui uma rotina muito corrida e precisa se organizar melhor para aproveitar seu tempo e cumprir com todos os seus a fazeres. Ela trabalha 8h por dia de segunda a sexta e estuda de segunda a quinta de 18h as 21h. Com tudo isso, ela precisa criar uma aprensentação para o seu fim de môdulo do curso sobre Pitão e possui apenas 3 dias para a apresentação.

    Nat tem que se organizar e estar pronta para apresentar seu trabalho final.

    [1] - Pagar alguem para fazer
    [2] - Fazer como o Zeca pagodinho e deixar a vida levar
    [3] - Gerir bem o seu tempo
    
    ''')

    resposta = input('O que Nat vai fazer?')

    while resposta:
        if resposta == '1':
            gameOver('N')
        elif resposta == '2':
            gameOver('N')
        elif resposta == '3': # CAMINHO MAIS CORRETO
            print('''
            Certo, agora Nat precisa separar melhor o seu tempo e conseguir trabalhar na apresentação.

            [1] - Faltar o trabalho para focar na apresentação.
            [2] - Deixar para fazer durante as aulas do curso.
            [3] - Rever suas prioridades.
            ''')

            resposta = input('O que Nat vai fazer?')

            while resposta:
                if resposta == '1':
                    gameOver('N')
                elif resposta == '2':
                    gameOver('N')
                elif resposta == '3': # CAMINHO MAIS CORRETO
                    print('''
                    Após estabelecer suas prioridades Nat precisa organiza-las para poder se guiar.

                    [1] - Procurar a conselheira Taís, pois ela possui o segredo para este caminho.
                    [2] - Tentar focar na apresantação só quando tiver um tempo livre.
                    [3] - Deixar de dormir para trabalhar nos slides.
                    ''')

                    resposta = input('O que Nat vai fazer?')

                    while resposta:
                        if resposta == '1': # CAMINHO MAIS CORRETO
                            print('''
                            A conselheira Tais orienta Nat a organizar suas tarefas para se guiar e entrega para ela uma ferramenta poderosa chamada Trello.

                            [1] - Nat prefere criar um passo a passo no grupo solitário do whats
                            [2] - Não usa nada disso pois sua mente é um excelente organizador
                            [3] - Usa a poderosa ferramenta Trello
                            
                            ''')

                            resposta = input('O que Nat vai fazer?')

                            while resposta:
                                if resposta == '1':
                                    gameOver('N')
                                elif resposta == '2':
                                    gameOver('N')
                                elif resposta == '3': # CAMINHO MAIS CORRETO

                                    print('''
                                    Conselheira Tais percebe ainda que Nat possui muito pouco tempo para trabalhar na sua aprensentação e orienta Nat a usar uma ferramenta mágica do tempo chamada Pomodoro.

                                    [1] - Não se acha digna de tamanho poder
                                    [2] - Tentar usar a ferramenta
                                    [3] - Ser pessimista e dizer que isso não funcionaria para ela mesmo sem dar uma chance
                                
                                    ''')

                                    resposta = input('O que Nat vai fazer?')
                                    
                                    while resposta:
                                        if resposta == '1':
                                            gameOver('N')
                                        elif resposta == '2': # FIM DA FASE 1 <---------------------------------------
                                            print('''
                                            Prioridades priorizadas, ajuda solicitada, ferramentas poderosas em mãos agora o que resta é começar a criar a apresentação. Para isso Nat sabe que precisa obter o conhecimento de Pitão.

                                            [1] - Tenta estudar sozinha mesmo sabendo que não tem tempo.
                                            [2] - Sobe o monte e vai atrás da Sábia Marisa, grande conhecedora dos ensinamentos de Pitão, para obter dicas.
                                            [3] - Acha que não vai entender e nem pede ajuda.

                                            ''')

                                            resposta = input('O que Nat vai fazer?')

                                            while resposta:
                                                if resposta == '1':
                                                    gameOver('N')
                                                elif resposta == '2':

                                                    print('''
                                                    FASE 2 - Entendendo Pitão

                                                    Ao chegar no monte, Nat se depara com a sábia Marisa em cima de uma rocha comendo seu revigoroso miojo com tempero verde.

                                                    [1] - Explica a Marisa que precisa de dicas sobre Pitão para colocar na sua apresentação
                                                    [2] - Desmaia porque o monte era muito alto
                                                    [3] - Pede um pouco do miojo para Marisa

                                                    ''')

                                                    resposta = input('O que Nat vai fazer?')

                                                    while resposta:
                                                        if resposta == '1':

                                                            print('''
                                                            Marisa diz que é sabia e não milagrosa e poderá passar apenas o básico de Pitão para Nat.

                                                            [1] - Começa a reclamar porque subiu o monte a toa
                                                            [2] - Toma o miojo de Marisa
                                                            [3] - Nat aceita pois foi para isso que subiu o monte.
                                                            
                                                            ''')

                                                            resposta = input('O que Nat vai fazer?')

                                                            while resposta:
                                                                if resposta == '1':
                                                                    gameOver('N')
                                                                elif resposta == '2':
                                                                    gameOver('N')
                                                                elif resposta == '3':
                                                                    print('''
                                                                    Marisa então entrega a Nat o super manual resilia e a alerta para usar com sabedoria.
                                                                    
                                                                    [1] - Usa o manual como apoio para descer o monte. 
                                                                    [2] - Nat entra em desespero e acha que não vai conseguir entender
                                                                    [3] - Nat lê o manual enquanto desce o monte e aplica o que acha importante na sua apresentação.

                                                                    ''')

                                                                    resposta = input('O que Nat vai fazer?')

                                                                    while resposta:
                                                                        if resposta == '1':
                                                                            gameOver('N')
                                                                        elif resposta == '2':
                                                                            gameOver('N')
                                                                        elif resposta == '3':
                                                                            print('''FASE 3 - O DIA DA APRESENTAÇÃO

                                                                            Nat conseguiu criar a apresentação e o que resta agora é se organizar para estar na hora para a apresentação. Nat sabe que existem outros coleguinhas para apresentar.

                                                                            [1] - Falar como se não houvesse amanhã
                                                                            [2] - Treinar o tempo de apresentação
                                                                            [3] - Quem liga para os outros coleguinhas?
                                                                            ''')

                                                                            resposta = input('O que Nat vai fazer?')
                                                                            
                                                                            while resposta:
                                                                                if resposta == '1':
                                                                                    print('Gastou tanto tempo para chegar no final e perceber que não geriu seu tempo da melhor forma!')
                                                                                    gameOver('N')
                                                                                elif resposta == '2':
                                                                                    print('\nPARABÉNS! VOCE CONSEGUIU BEM A TEMPO!')
                                                                                    print('Não existe melhor gestor(a) de tempo que você!\n')
                                                                                    menuPrincipal()
                                                                                elif resposta == '3':
                                                                                    print('Gastou tanto tempo para chegar no final e perceber que não geriu seu tempo da melhor forma!')
                                                                                    gameOver('N')
                                                                                else:
                                                                                    print('Opcão inválida! Informe uma opção válida.')
                                                                                    resposta = input('O que Nat vai fazer?')
                                                                        else:
                                                                            print(resposta)
                                                                            print('Opcão inválida! Informe uma opção válida.')
                                                                            resposta = input('O que Nat vai fazer?')
                                                                else:
                                                                    print('Opcão inválida! Informe uma opção válida.')
                                                                    resposta = input('O que Nat vai fazer?')
                                                        elif resposta == '2':
                                                            gameOver('N')
                                                        elif resposta == '3':
                                                            gameOver('N')
                                                        else:
                                                            print('Opcão inválida! Informe uma opção válida.')
                                                            resposta = input('O que Nat vai fazer?')
                                                elif resposta == '3':
                                                    gameOver('N')
                                                else:
                                                    print('Opcão inválida! Informe uma opção válida.')
                                                    resposta = input('O que Nat vai fazer?')
                                        elif resposta == '3':
                                            gameOver('N')
                                        else:
                                            print('Opcão inválida! Informe uma opção válida.')
                                            resposta = input('O que Nat vai fazer?')
                                else:
                                    print('Opcão inválida! Informe uma opção válida.')
                                    resposta = input('O que Nat vai fazer?')
                        elif resposta == '2':
                            gameOver('N')
                        elif resposta == '3': 
                            gameOver('N')
                        else:
                            print('Opcão inválida! Informe uma opção válida.')
                            resposta = input('O que Nat vai fazer?')
                    else:
                        print('Opcão inválida! Informe uma opção válida.')
                        resposta = input('O que Nat vai fazer?')
        else:
            print('Opcão inválida! Informe uma opção válida.')
            resposta = input('O que Nat vai fazer?')
###########################################################################################################


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('                                                   Bem vindos(as) ao jogo                                                ')
print('                                                   - EM BUSCA DE PITÃO -                                                 ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('INTRODUÇÃO')
print('Jovens com diferentes personalidades mais algo muito em comum, a enorme vontade de adquirir o conhecimento de Pitão. Porém, querer não é o suficiente. Vamos ajudar essas almas perdidas a obter o conhecimento e se tornarem os maiores especialistas em Pitão?')

menuPrincipal()

# RECURSOS USADOS:

# Variáveis
# Estruturas condicionais
# Estruturas de repetição
# Operadores lógicos
# Funções
# Formatação de String