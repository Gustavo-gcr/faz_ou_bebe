import streamlit as st
import random

# --- LISTA DE DESAFIOS E PERGUNTAS (COMPLETA) ---
DESAFIOS_E_PERGUNTAS = [
    "Você faria um ménage com alguém aqui? Se sim, diga com quem, ou beba 2 shots.",
    "Se ninguém fosse comprometido, você toparia um sexo geral com todos aqui ou beba sua bebida toda.",
    "Qual a posição sexual que você mais gosta? Responda ou beba 1 shot.",
    "Conte sobre a transa mais estranha que já teve ou beba 2 shots.",
    "Você transaria com a pessoa à sua direita? Responda sinceramente ou beba 1 shot.",
    "Qual foi o lugar mais inusitado em que você transou? Conte ou beba 2 shots.",
    "Já ficou com mais de uma pessoa na mesma noite? Diga quem ou beba 2 shots.",
    "Beije a pessoa à sua esquerda na boca ou beba 2 shots.",
    "Você faria sexo casual com alguém desta roda? Responda ou beba 1 shot.",
    "Mostre a última nude que enviou (sem rosto) ou beba 3 shots.",
    "Conte sua maior fantasia sexual ou beba 2 shots.",
    "Você já traiu alguém? Conte como foi ou beba 2 shots.",
    "Faça um striptease de 15 segundos ou beba 2 shots.",
    "Diga qual é o nome da última pessoa que você stalkeou no Instagram ou beba 1 shot.",
    "Diga quem aqui você beijaria agora ou beba 1 shot.",
    "Você toparia beijar duas pessoas seguidas do jogo? Faça ou beba 2 shots.",
    "Qual foi o maior fetiche que você já realizou? Conte ou beba 2 shots.",
    "Você já transou em um lugar público? Diga qual ou beba 2 shots.",
    "Já enviou nude para alguém errado? Conte a história ou beba 2 shots.",
    "Qual é a parte do seu corpo mais erógena? Responda ou beba 1 shot.",
    "Diga quem é a pessoa mais sexy desta roda ou beba 1 shot.",
    "Você teria um caso com alguém comprometido? Responda ou beba 2 shots.",
    "Já ficou com alguém do mesmo sexo? Conte ou beba 1 shot.",
    "Qual foi a experiência sexual mais constrangedora da sua vida? Responda ou beba 2 shots.",
    "Mostre o histórico do seu navegador ou beba 2 shots.",
    "Já transou sem camisinha? Responda ou beba 1 shot.",
    "Você toparia mandar um áudio gemendo para alguém da sua lista de contatos? Faça ou beba 3 shots.",
    "Qual foi o maior tempo que você já ficou sem transar? Responda ou beba 1 shot.",
    "Você já mandou nude em troca de outra? Conte ou beba 2 shots.",
    "Se tivesse que dormir com alguém da roda hoje, quem seria? Responda ou beba 2 shots.",
    "Já filmou ou tirou fotos transando? Responda ou beba 2 shots.",
    "Qual a maior quantidade de vezes que você transou na mesma noite? Responda ou beba 1 shot.",
    "Já usou brinquedos sexuais? Diga qual ou beba 1 shot.",
    "Você faria um sexo a três hoje? Responda ou beba 2 shots.",
    "Diga o nome da pessoa mais gostosa que você já pegou ou beba 2 shots.",
    "Você já fingiu orgasmo? Conte como foi ou beba 1 shot.",
    "Você transaria por dinheiro? Responda ou beba 2 shots.",
    "Quem aqui você levaria para um motel agora? Responda ou beba 1 shot.",
    "Já ficou com ex de amigo? Responda ou beba 2 shots.",
    "Diga qual foi a pior transa da sua vida ou beba 2 shots.",
    "Mostre a foto mais picante que tem no celular ou beba 2 shots.",
    "Já mandou mensagem para a pessoa errada falando de sexo? Conte ou beba 1 shot.",
    "Quem aqui você deixaria te amarrar na cama? Responda ou beba 2 shots.",
    "Você já pensou em alguém da roda enquanto se masturbava? Responda ou beba 2 shots.",
    "Já fez sexo sem querer que descobrissem? Conte ou beba 1 shot.",
    "Qual foi a vez que você mais bebeu e acabou transando? Responda ou beba 2 shots.",
    "Você faria sexo com alguém aqui só por diversão? Responda ou beba 1 shot.",
    "Mostre sua última conversa no direct ou beba 1 shot.",
    "Já ficou com alguém mais velho(a) que você por mais de 10 anos? Responda ou beba 2 shots.",
    "Já transou ouvindo música estranha? Conte qual ou beba 1 shot.",

    "Descreva em detalhes o que você faria na cama com a pessoa à sua direita. Seja explícito(a). Ou beba 2 shots.",
    "Faça uma demonstração, usando as mãos em um copo, de como você faz um boquete/sexo oral. Ou beba 2 shots.",
    "Qual foi o som mais estranho que você já fez durante o sexo? Tente reproduzi-lo ou beba 2 shots.",
    "Diga qual pessoa na roda você escolheria para uma noite de sexo selvagem e por quê. Beba 1 shot.",
    "Mostre ao grupo o tipo de pornô que você assiste. Abra um site e mostre a página inicial. Ou beba 3 shots.",
    "Tire uma peça de roupa íntima (cueca ou sutiã) e pendure em algum lugar visível da sala. Faça ou beba 3 shots.",
    "Dê um beijo molhado no pescoço de alguém escolhido pelo grupo por 10 segundos. Faça ou beba 2 shots.",
    "Qual o número exato de parceiros sexuais que você já teve? Responda ou vire sua bebida.",
    "Se você pudesse ter um fetiche realizado agora com alguém da roda, qual seria e com quem? Responda ou beba 2 shots.",
    "Envie uma mensagem para o último contato com quem você flertou: 'Estou te querendo agora'. Mostre o print ou beba 3 shots.",
    "Faça a posição sexual 'frango assado' por 15 segundos ou beba 2 shots.",
    "Qual a sua opinião sincera sobre sexo anal (dar e/ou receber)? Responda ou beba 1 shot.",
    "Escolha alguém para te vendar. Essa pessoa deve então te dar de comer ou beber algo usando apenas a boca dela. Façam ou ambos bebem 2 shots.",
    "Descreva o cheiro de sexo para você ou beba 1 shot.",
    "Quem na roda parece ter mais 'pinta' de quem curte BDSM (bondage, dominação, submissão)? Responda ou beba 2 shots.",
    "Grave um áudio de 10 segundos gemendo e envie para o terceiro contato do seu WhatsApp. Faça ou beba 3 shots.",
    "Tente colocar dois dedos inteiros na boca e mantê-los por 10 segundos ou beba 1 shot.",
    "Você já participou de um sexo em grupo (ménage ou mais)? Conte como foi ou beba 2 shots.",
    "Passe gelo em uma parte do corpo da pessoa à sua esquerda (barriga, costas, pescoço) até derreter. Faça ou beba 2 shots.",
    "Qual foi a coisa mais broxante que já te disseram na 'hora H'? Conte ou beba 2 shots.",
    "Faça uma performance de strip-tease sensual de 30 segundos, tirando pelo menos uma peça de roupa. Faça ou beba 2 shots.",
    "Classifique o desempenho sexual de seu último parceiro(a) de 0 a 10, em voz alta. Beba 1 shot.",
    "Deixe a pessoa à sua direita dar um chupão no seu pescoço. Faça ou beba 3 shots.",
    "Você já gozou tão alto que um vizinho poderia ter ouvido? Responda ou beba 2 shots.",
    "Qual o seu recorde de orgasmos em um único dia? Responda ou beba 1 shot.",
    "Dê uma lambida do queixo ao pescoço da pessoa que você acha mais cheirosa na roda. Faça ou beba 2 shots.",
    "Mande uma foto da sua boca para o primeiro contato dos seus stories e diga 'pensando no que essa boca pode fazer'. Beba 3 shots.",
    "Desabotoe a calça e mostre um pedaço da sua roupa íntima para o grupo por 5 segundos. Faça ou beba 2 shots.",
    "Você prefere uma transa longa e romântica ou uma rapidinha selvagem? Responda ou beba 1 shot.",
    "Fale a palavra 'pau' ou 'buceta' no diminutivo e no aumentativo de forma bem sensual. Faça ou beba 1 shot.",
    "Qual o lugar mais arriscado em que você já se masturbou? Conte ou beba 2 shots.",
    "Escolha alguém para te usar como 'descanso de pé' por uma rodada. Faça ou beba 2 shots.",
    "Você já engoliu ou deixou engolirem? Responda ou beba 2 shots.",
    "Reencene a sua posição favorita do Kama Sutra com um parceiro imaginário (ou com uma almofada). Faça ou beba 2 shots.",
    "Qual amigo(a) do seu parceiro(a) você pegaria sem pensar duas vezes? Responda ou beba 2 shots.",
    "Deixe o grupo escolher uma categoria de pornografia para você pesquisar no seu celular. Mostre o primeiro vídeo que aparecer. Beba 3 shots.",
    "Dê um beijo na parte interna da coxa de alguém da roda. Faça ou beba 3 shots.",
    "Qual a coisa mais estranha que já te pediram para fazer na cama? Responda ou beba 2 shots.",
    "Qual pessoa da roda você acha que faria um vídeo pornô amador melhor? Responda ou beba 1 shot.",
    "Coloque a mão por dentro da sua calça e finja que está se tocando por 10 segundos, com direito a expressões faciais. Faça ou beba 2 shots.",
    "Você já fez 'golden shower' ou 'chuva dourada'? Responda ou beba 3 shots.",
    "Tire a camisa e deixe a pessoa à sua direita desenhar algo na sua barriga ou costas. Fique assim até o fim do jogo. Beba 2 shots.",
    "Descreva o gosto do sêmen/fluido vaginal para você ou beba 2 shots.",
    "Qual o maior número de vezes que você transou em um único dia? Responda ou beba 1 shot.",
    "Faça a sua melhor imitação de um(a) ator/atriz pornô gemendo ou beba 2 shots.",
    "Qual o seu fetiche mais secreto, aquele que você tem vergonha de admitir? Conte ou beba 2 shots.",
    "Dê uma mordida sensual no ombro da pessoa que está há duas posições de você. Faça ou beba 2 shots.",
    "Se você fosse um brinquedo sexual, qual seria e por quê? Responda ou beba 1 shot.",
    "Poste um emoji de diabinho (😈) no story de 3 ex-parceiros. Mostre que fez ou beba 3 shots.",
    "Escolha alguém da roda. Vocês devem ficar se encarando, olho no olho, a 10cm de distância, por 30 segundos, sem rir. Quem rir primeiro, bebe 2 shots.",
    "Dê um beijo de língua de 20 segundos na pessoa que você acha mais atraente na roda ou beba 3 shots.",
    "Deixe a pessoa à sua direita te dar um tapa na bunda, com força. Ou beba 2 shots.",
    "Qual o seu recorde de masturbação em um único dia? Responda ou beba 1 shot.",
    "Tire uma peça de roupa e jogue assim até o final da rodada, ou beba 2 shots.",
    "Mande uma mensagem para seu/sua ex dizendo 'Ainda penso em você'. Mostre o print ou beba 3 shots.",
    "Quem da roda parece ser o pior de cama? Responda ou beba 2 shots.",
    "Faça uma dança sensual no colo de alguém escolhido pelo grupo por 30 segundos ou beba 2 shots.",
    "Descreva o pênis/vagina ideal para você ou beba 1 shot.",
    "Já gozou pensando em alguém desta roda? Diga quem ou beba 2 shots.",
    "Lamba o pescoço da pessoa à sua frente ou beba 2 shots.",
    "Qual foi o maior número de pessoas com quem você transou em 24 horas? Responda ou beba 2 shots.",
    "Deixe o grupo escolher uma foto sua para postar no seu story por 10 minutos ou beba 3 shots.",
    "Troque de blusa com a pessoa do sexo oposto mais próxima ou beba 2 shots.",
    "Se você pudesse ter um caso de uma noite com um famoso(a), quem seria? Responda ou beba 1 shot.",
    "Diga qual a sua posição sexual menos favorita e por quê ou beba 1 shot.",
    "Dê um selinho em todas as pessoas da roda ou beba sua bebida toda.",
    "Já fez sexo anal? Gostou? Responda ou beba 2 shots.",
    "Abra o Instagram e mande um 'oi sumido(a)' para a 5ª pessoa que aparecer nos seus contatos. Faça ou beba 2 shots.",
    "Qual a coisa mais nojenta que você já fez na cama? Conte ou beba 2 shots.",
    "Fale o nome de alguém que você se arrepende profundamente de ter beijado ou beba 1 shot.",
    "Tire o sutiã/cueca por baixo da roupa sem ir ao banheiro ou beba 2 shots.",
    "Quem da roda tem mais cara de quem curte uma boa sacanagem? Responda ou beba 1 shot.",
    "Se seu corpo falasse, o que ele diria sobre a sua vida sexual? Responda ou beba 1 shot.",
    "Deixe alguém da roda escrever uma palavra na sua testa com caneta. Fique até o fim do jogo ou beba 2 shots.",
    "Você já brochou ou teve dificuldade de lubrificação com alguém? Conte ou beba 2 shots.",
    "Morda o lábio inferior da pessoa à sua esquerda de forma sensual ou beba 1 shot.",
    "Classifique todos na roda do mais ao menos provável de você ter um caso. Responda ou beba 2 shots.",
    "Qual foi a coisa mais ilegal que você já fez? Conte ou beba 2 shots.",
    "Deixe a roda escolher um contato do seu celular para você ligar e cantar 'Parabéns pra Você'. Faça ou beba 3 shots.",
    "Você já ejaculou/gozou 'sem querer' em um lugar inapropriado? Conte ou beba 2 shots.",
    "Qual a sua opinião sincera sobre o desempenho sexual do seu último parceiro(a)? Responda ou beba 2 shots.",
    "Faça a sua melhor cara de orgasmo ou beba 1 shot.",
    "Qual amigo(a) seu você pegaria se tivesse a chance? Responda ou beba 2 shots.",
    "Rebole por 20 segundos ao som de uma música escolhida pelo grupo ou beba 2 shots.",
    "Mostre as 3 últimas pessoas que você pesquisou no Instagram ou beba 1 shot.",
    "Diga uma fantasia sexual que você tem vergonha de admitir ou beba 2 shots.",
    "Dê um gole da sua bebida diretamente na boca de outra pessoa ou beba 1 shot.",
    "Se você pudesse ler a mente de alguém na roda por 1 minuto, quem seria e por quê? Responda ou beba 1 shot.",
    "Poste um story com a legenda 'procurando um amor'. Deixe por 15 minutos ou beba 3 shots.",
    "Quem aqui tem o melhor corpo? Responda ou beba 1 shot.",
    "Você já fez algo por dinheiro que se arrepende? Conte ou beba 2 shots.",
    "Imite a posição sexual que você mais odeia ou beba 1 shot.",
    "Qual foi o sonho mais erótico que você já teve? Descreva ou beba 2 shots.",
    "Sussurre algo picante no ouvido da pessoa à sua direita ou beba 1 shot.",
    "Qual foi a cantada mais brega que você já usou e funcionou? Responda ou beba 1 shot.",
    "Deixe alguém desenhar um pinto no seu braço com caneta ou beba 2 shots.",
    "Você já beijou alguém do mesmo sexo em uma festa só pela zoeira? Conte ou beba 1 shot.",
    "Qual a coisa mais pervertida que você já pesquisou na aba anônima? Responda ou beba 2 shots.",
    "Dê um beijo no local do corpo que a pessoa à sua esquerda escolher (exceto partes íntimas) ou beba 2 shots.",
    "Já fez sexo virtual? Conte como foi ou beba 2 shots.",
    "Fale em voz alta o nome da última pessoa que te mandou nude ou beba 2 shots.",
    "Você perdoaria uma traição? Responda ou beba 1 shot.",
    "Tente seduzir um objeto inanimado na sala por 30 segundos ou beba 2 shots.",
    "Quem da roda você acha que seria o mais 'selvagem' na cama? Responda ou beba 1 shot.",
    "Qual foi o elogio mais safado que você já recebeu? Conte ou beba 1 shot.",
    "Mande uma mensagem para sua mãe dizendo 'descobri uma coisa chocante'. Não responda por 10 minutos. Ou beba 3 shots.",
    "Já ficou com duas pessoas que eram amigas entre si? Conte a história ou beba 2 shots.",
    "Qual cheiro mais te excita em uma pessoa? Responda ou beba 1 shot.",
    "Faça 10 polichinelos falando algo safado a cada pulo ou beba 1 shot.",
    "Se você fosse um animal na cama, qual seria? Responda ou beba 1 shot.",
    "Quem aqui tem mais cara de quem gosta de ser dominado(a)? Responda ou beba 1 shot.",
    "Já participou de um 'dark room' ou cabine de sexo? Conte como foi ou beba 2 shots.",
    "Coloque um cubo de gelo na sua calça e deixe derreter ou beba 2 shots.",
    "Diga em voz alta quanto você daria de 0 a 10 para o beijo da última pessoa que você ficou. Beba 1 shot.",
    "Se sua vida sexual fosse um filme, qual seria o título? Responda ou beba 1 shot.",
    "Dê uma mordida (de leve!) na orelha da pessoa que você acha mais cheirosa na roda ou beba 1 shot.",
    "Já quebrou algo durante uma transa? Conte ou beba 2 shots.",
    "Qual a idade da pessoa mais velha e mais nova que você já ficou? Responda ou beba 1 shot.",
    "Deixe o grupo fazer uma pergunta de 'sim' ou 'não' que você é obrigado a responder. Beba 2 shots se não quiser.",
    "Se você pudesse apagar uma experiência sexual da sua memória, qual seria? Responda ou beba 2 shots.",
    "Descreva seu gemido ou beba 2 shots.",
    "Qual a parte do corpo de alguém do sexo oposto (ou do mesmo) que você repara primeiro? Beba 1 shot.",
    "Qual a coisa mais louca que você já fez por amor ou tesão? Conte ou beba 2 shots.",
    "Tire uma selfie fazendo uma cara sexy e poste no seu feed. Deixe por 5 minutos ou beba 3 shots.",
    "Você prefere sexo com pegada ou mais romântico? Responda ou beba 1 shot.",
    "Quem aqui você acha que beija mal? Responda ou beba 2 shots.",
    "Qual foi o maior 'mico' que você já pagou tentando flertar com alguém? Conte ou beba 1 shot.",
    "Já gemeu o nome errado durante o sexo? Conte ou beba 3 shots.",
    "Beije o umbigo de alguém da roda ou beba 2 shots.",
    "Qual foi o seu primeiro pensamento ao acordar hoje de manhã? Responda sinceramente ou beba 1 shot.",
    "Qual o seu tipo de pornô favorito? Responda ou beba 1 shot.",
    "Já fez algo que seus pais te deserdariam se soubessem? Conte ou beba 2 shots.",
    "Mande um áudio para o segundo contato do seu WhatsApp dizendo 'Estou com fogo'. Faça ou beba 3 shots.",
    "Diga algo que te brocha instantaneamente ou beba 1 shot.",
    "Use uma venda nos olhos pela próxima rodada ou beba 2 shots.",
    "Já usou comida durante o sexo? O quê e como? Conte ou beba 1 shot.",
    "Quem da roda parece ter o gosto musical mais duvidoso? Responda ou beba 1 shot.",
    "Faça massagem nos ombros da pessoa à sua direita por 1 minuto ou beba 1 shot.",
    "Você já foi pego(a) no ato? Conte como foi ou beba 2 shots.",
    "Se todos na roda estivessem solteiros, quem formaria o casal mais bonito? Responda ou beba 1 shot.",
    "Qual a sua opinião sobre 'chifre trocado não dói'? Responda ou beba 1 shot.",
    "Deixe uma pessoa da roda escolher uma música para você dançar por 30 segundos. Dance ou beba 2 shots.",
    "Qual o lugar mais estranho que você já se masturbou? Conte ou beba 2 shots.",
    "Você prefere luz acesa ou apagada? Responda ou beba 1 shot.",
    "Quem aqui tem mais chances de ser preso(a)? Por quê? Responda ou beba 1 shot.",
    "Deixe a pessoa à sua esquerda passar gelo nas suas costas ou beba 2 shots.",
    "Qual foi a maior vergonha que seus pais já te fizeram passar? Conte ou beba 1 shot.",
    "Você já sentiu atração por algum professor(a)? Conte ou beba 1 shot.",
    "Fale com sotaque de outro estado até a sua próxima vez de jogar ou beba 2 shots.",
    "Você já vomitou por beber demais? Conte a história ou beba 1 shot.",
    "Qual o seu maior 'turn on' (o que mais te excita)? Responda ou beba 1 shot.",
    "Finja que está tendo um orgasmo barulhento agora ou beba 2 shots.",
    "Escolha duas pessoas na roda que deveriam se beijar. Se elas não o fizerem, você bebe 2 shots.",
    "Mostre o tempo de uso do seu celular hoje ou beba 1 shot.",
    "Você já pagou por sexo ou foi pago por ele? Responda ou beba 2 shots.",
    "Imite alguém da roda e os outros têm que adivinhar quem é. Faça ou beba 2 shots.",
    "Qual foi o último filme adulto que você assistiu? Responda ou beba 1 shot.",
    "Diga um segredo que você nunca contou a ninguém da roda ou beba 2 shots.",
    "Deixe o grupo te fazer uma pergunta de verdade ou desafio. Cumpra ou beba 3 shots.",
    "Coma ou beba algo sem usar as mãos ou beba 1 shot.",
    "Você já se apaixonou por alguém que não deveria? Conte ou beba 2 shots.",
    "Ligue para uma pizzaria e tente flertar com o atendente. Faça ou beba 3 shots.",
    "Qual o apelido mais vergonhoso que você já teve? Responda ou beba 1 shot.",
    "Já fingiu estar doente para não sair com alguém? Conte ou beba 1 shot.",
    "Dê um beijo triplo com outras duas pessoas da roda. Façam ou todos os três bebem 2 shots.",
    "Qual a coisa mais idiota que você já fez por estar bêbado(a)? Conte ou beba 2 shots.",
    "Você já stalkeou um ex e descobriu algo que não deveria? Conte ou beba 2 shots.",
    "Fique de quatro e uive para a lua por 10 segundos ou beba 1 shot.",
    "Você prefere dominar ou ser dominado(a)? Responda ou beba 1 shot.",
    "Qual a sua música favorita para transar? Responda ou beba 1 shot.",
    "Descreva o último orgasmo que você teve em uma palavra ou beba 1 shot.",
    "Deixe a pessoa à sua direita postar um status em seu nome no WhatsApp. Deixe por 30 minutos ou beba 3 shots.",
    "Quem aqui tem o sorriso mais bonito? Responda ou beba 1 shot.",
    "Já usou algemas ou foi amarrado(a) na cama? Responda ou beba 1 shot.",
    "Se você pudesse trocar de corpo com alguém da roda por um dia, quem seria e o que faria? Beba 2 shots.",
    "Cante o refrão de uma música bem brega em voz alta ou beba 1 shot.",
    "Você já fez xixi na piscina? Responda ou beba 1 shot.",
    "Qual o cheiro de uma pessoa que mais te atrai? Responda ou beba 1 shot.",
    "Se você tivesse que beijar alguém do mesmo sexo na roda, quem seria? Responda ou beba 2 shots.",
    "Qual a mentira mais recente que você contou? Responda ou beba 1 shot.",
    "Tire uma foto fazendo careta e envie para o primeiro contato da sua lista de amigos próximos no Instagram. Beba 2 shots.",
    "Você já foi expulso de algum lugar? Conte o motivo ou beba 2 shots.",
    "Deixe a pessoa da sua frente cheirar seu cabelo ou beba 1 shot.",
    "Qual foi a sua pior experiência com bebida? Conte ou beba 1 shot.",
    "Se você pudesse fazer uma pergunta para o ex de alguém da roda, o que perguntaria e para o ex de quem? Beba 2 shots.",
    "Fale por 1 minuto sobre um assunto que você odeia como se o amasse. Faça ou beba 2 shots.",
    "Já se arrependeu de ter transado com alguém no dia seguinte? Conte ou beba 2 shots.",
    "Qual o seu guilty pleasure (prazer culposo) inconfessável? Responda ou beba 1 shot.",
    "Beije o joelho da pessoa à sua esquerda ou beba 1 shot.",
    "Quem aqui você acha que é virgem (ou foi o último a perder)? Responda ou beba 2 shots.",
    "Se sua vida sexual fosse uma nota de 0 a 10, qual seria hoje? Responda ou beba 1 shot.",
    "Mande uma mensagem para um amigo aleatório: 'Preciso te confessar uma coisa...'. Não diga mais nada. Faça ou beba 2 shots.",
    "Qual foi o maior vexame que você já passou em público? Conte ou beba 2 shots.",
    "Você tem alguma pinta ou marca de nascença em um lugar escondido? Mostre (se possível) ou descreva. Beba 1 shot.",
    "Tente fazer um truque de mágica. Se falhar, beba 2 shots.",
    "Qual a coisa mais infantil que você ainda faz? Responda ou beba 1 shot.",
    "Escolha alguém para ser seu 'servo' até sua próxima rodada (pegar bebida, etc.). Faça ou beba 2 shots.",
    "Já ficou com alguém muito mais feio(a) que você só por carência? Responda ou beba 2 shots.",
    "Deixe alguém da roda te maquiar (mesmo que seja só um batom borrado). Fique assim por 3 rodadas ou beba 2 shots.",
    "Qual a sua maior insegurança física? Responda ou beba 1 shot.",
    "Qual foi a última vez que você chorou e por quê? Responda ou beba 1 shot.",
    "Dê um beijo esquimó (esfregar as pontas dos narizes) na pessoa à sua frente ou beba 1 shot.",
    "Se você fosse obrigado a deletar um aplicativo do seu celular agora, qual seria? Delete ou beba 2 shots.",
    "Você já peidou durante o sexo? Conte como disfarçou (ou não). Beba 2 shots.",
    "Quem da roda parece ser o mais fiel em um relacionamento? Responda ou beba 1 shot.",
    "Faça uma imitação de um animal por 20 segundos ou beba 1 shot.",
    "Qual o seu palpite sobre o número de parceiros sexuais da pessoa à sua direita? Responda ou beba 2 shots.",
    "Você já sonhou que estava traindo seu parceiro(a)? Conte ou beba 1 shot.",
    "Permita que o grupo veja suas 5 últimas fotos tiradas com o celular ou beba 2 shots.",
    "Se você pudesse ter um superpoder sexual, qual seria? Responda ou beba 1 shot.",
    "Dê um abraço de urso bem apertado em alguém da roda por 15 segundos ou beba 1 shot.",
    "Qual a combinação de comida mais estranha que você gosta? Responda ou beba 1 shot.",
    "Fique sem falar até a sua próxima rodada. Se falar, bebe 2 shots.",
    "Você já saiu com alguém que conheceu em um aplicativo de namoro? Conte ou beba 1 shot.",
    "Qual o filme que mais te excitou? Responda ou beba 1 shot.",
    "Quem da roda tem o pior gosto para se vestir? Responda ou beba 2 shots.",
    "Faça um brinde à pessoa que você considera mais parceira na roda. Beba 1 shot junto com ela.",
    "Qual a sua memória mais feliz da infância? Conte ou beba 1 shot.",
    "Se você só pudesse salvar uma pessoa da roda em um apocalipse zumbi, quem seria? Beba 1 shot.",
    "Dê sua bebida para a pessoa à sua esquerda e pegue a dela. Jogue com o copo trocado por uma rodada.",
    "Qual o seu maior medo? Responda ou beba 2 shots.",
    "Se você tivesse um vibrador, que nome daria a ele? Responda ou beba 1 shot.",
    "Faça a 'dança da minhoca' no chão por 10 segundos ou beba 2 shots.",
    "Qual foi a coisa mais romântica que já fizeram por você? Conte ou beba 1 shot.",
    "Quem aqui tem mais probabilidade de se tornar um meme? Responda ou beba 1 shot.",
    "Tente equilibrar um copo na sua cabeça por 20 segundos. Se cair, beba 2 shots.",
    "Você já foi em uma praia de nudismo? Conte ou beba 1 shot.",
    "Diga 'eu te amo' para a pessoa à sua frente olhando nos olhos dela, sem rir. Se rir, beba 2 shots.",
    "Qual a pior coisa que você já comeu na vida? Responda ou beba 1 shot.",
    "Escolha alguém para beber um shot com você, sem motivo. Apenas pela companhia.",
    "Qual foi a sua primeira impressão sobre mim (a pessoa à sua direita)? Responda ou beba 1 shot.",
    "Deixe a pessoa à sua esquerda fazer uma trança ou um penteado ridículo no seu cabelo. Beba 2 shots.",
    "Você já leu o diário de alguém ou mexeu no celular escondido? Responda ou beba 2 shots.",
    "Qual a sua celebrity crush inusitada (alguém que a maioria não acha atraente)? Beba 1 shot.",
    "Encha a boca com bebida e tente cantar uma música. Se cuspir, bebe mais. Beba 2 shots.",
    "Qual foi a última mentira que você contou para seus pais? Responda ou beba 1 shot.",
    "Quem da roda seria o melhor em um filme pornô? Responda ou beba 2 shots.",
    "Deixe uma pessoa do grupo te dar um apelido. Ele valerá até o fim do jogo. Beba 2 shots.",
    "Qual a parte do seu próprio corpo que você mais gosta? Responda ou beba 1 shot.",
    "Se o apocalipse fosse amanhã, qual seria a última coisa que você faria? Responda ou beba 1 shot.",
    "Faça o som do seu animal favorito por 15 segundos ou beba 1 shot.",
    "Você já roubou algo, mesmo que pequeno? Conte o que foi ou beba 2 shots.",
    "Quem aqui você chamaria para te ajudar a esconder um corpo? Responda ou beba 1 shot.",
    "Tire o sapato e a meia de um dos pés e fique assim por 3 rodadas ou beba 2 shots.",
    "Qual a coisa mais vergonhosa que tem no seu quarto agora? Responda ou beba 1 shot.",
    "Crie uma regra para o jogo. Quem quebrar a regra, bebe. A regra vale por 5 rodadas.",
    "Dê um beijo na testa da pessoa mais alta da roda ou beba 1 shot.",
    "Qual o seu maior arrependimento na vida até agora? Responda ou beba 2 shots.",
    "Se você fosse um sabor de pizza, qual seria e por quê? Responda ou beba 1 shot.",
    "Declare-se para alguém da roda de forma dramática, como em uma novela. Faça ou beba 2 shots.",
    "Se todos fossem sabores de sorvete, quem seria baunilha (básico)? Responda ou beba 2 shots.",
    "Você já ficou com algum parente distante em uma festa de família? Responda ou beba 3 shots.",
    "Tente lamber o próprio cotovelo. Se não conseguir, beba 1 shot.",
    "Qual foi o motivo mais idiota pelo qual você já brigou com alguém? Conte ou beba 1 shot.",
    "Abrace a pessoa à sua esquerda por trás (abraço de conchinha) por 20 segundos. Faça ou beba 2 shots.",
    "Beije a boca de duas pessoas na roda, uma seguida da outra. Faça ou beba 2 shots.",
    "Todos na roda devem beijar a pessoa à sua direita na bochecha. Faça ou beba 1 shot.",
    "Passe a mão na bunda da pessoa ao seu lado (direita ou esquerda, sua escolha). Faça ou beba 1 shot.",
    "Lamba a boca da pessoa à sua frente por 5 segundos. Faça ou beba 2 shots.",
    "Beije o peito da pessoa ao seu lado (por cima ou por baixo da roupa, sua escolha). Faça ou beba 2 shots.",
    "Lamba a parte de baixo de um órgão sexual de alguém que você escolher na roda (se for homem, testículos; se mulher, vagina/clitóris, por cima da roupa). Faça ou beba 3 shots.",
    "Faça 30 segundos de 'dirty dancing' (dança muito sensual) no colo de alguém escolhido pelo grupo. Faça ou beba 2 shots.",
    "Tire o sutiã/cueca por baixo da roupa e mostre ao grupo a peça íntima. Beba 2 shots se não puder fazer.",
    "Dê um chupão (chupada/mordida) no pescoço de alguém na roda que você ache atraente. Faça ou beba 3 shots.",
    "Peça para alguém da roda lamber o gelo do seu umbigo. Ambos fazem ou bebem 2 shots.",
    "Troque uma peça de roupa íntima (cueca/calcinha) com alguém do sexo oposto. Usem as peças trocadas até o próximo desafio ou bebam 3 shots.",
    "Grave um vídeo de 10 segundos de si mesmo fazendo uma posição sexual do Kamasutra (pode ser com um travesseiro). Mostre ao grupo ou beba 3 shots.",
    "Vire um shot na boca da pessoa à sua frente (ou na boca de quem ela escolher). Façam ou ambos bebem 2 shots.",
    "Deixe a pessoa à sua direita dar um tapa forte na sua bunda. Aceite ou beba 2 shots.",
    "Beije a parte interna da coxa da pessoa à sua esquerda. Faça ou beba 2 shots.",
    "Tire uma selfie erótica (pode ser por cima da roupa, insinuando algo) e envie para a primeira pessoa que aparecer no seu Instagram Direct. Mostre o print ou beba 3 shots.",
    "Fique de joelhos e faça o som e a expressão de um animal sexualmente excitado por 15 segundos. Faça ou beba 1 shot.",
    "Use um cubo de gelo para deslizar pela sua nuca e descer até sua cintura, sem usar as mãos, fazendo um gemido dramático. Faça ou beba 2 shots.",
    "Permita que a pessoa que acabou de jogar escreva uma fantasia sexual (com caneta atóxica) na sua testa. Mantenha até o final do jogo ou beba 2 shots.",
    "Dê um beijo de cinema (longo e com pegada) em alguém da roda que você ainda não beijou (se houver). Faça ou beba 3 shots.",
    "Faça uma performance sensual de 10 segundos em torno de uma garrafa/objeto no chão. Faça ou beba 1 shot.",
    "Deixe a pessoa à sua esquerda cheirar sua axila. Se ela fizer careta, ela bebe 1 shot, se não, você bebe 1 shot. Façam ou ambos bebem 2 shots.",
    "Descreva em detalhes o que você faria com a língua na pessoa à sua direita, sem encostar nela. Faça ou beba 2 shots.",
    "Pegue no peito e aperte sensualmente por 20 segundos ou beba 3 shots.",
    "Dê um beijo de lingua na pessoa que você acha mais atraente na roda. Faça ou beba 3 shots.",
    "Fique na sua posição sexual favorita (pode ser imaginaria) por 30 segundos. Faça ou beba 2 shots.",
    "Crie uma 'coleira' usando um pedaço de roupa e use-a na pessoa à sua frente. Puxe-a suavemente até que ela beba um shot. Façam ou ambos bebem 3 shots.",
    "Passe o seu dedo na boca de alguém na roda (que você escolher) e depois no órgão sexual da mesma pessoa (por cima da roupa). Faça ou beba 3 shots."
]


st.set_page_config(page_title="Faz ou Bebe 😈", page_icon="🍻", layout="centered")


# --- INICIALIZAÇÃO DO ESTADO DA SESSÃO ---

if 'jogadores' not in st.session_state:
    st.session_state.jogadores = []
if 'jogo_iniciado' not in st.session_state:
    st.session_state.jogo_iniciado = False
if 'jogador_atual' not in st.session_state:
    st.session_state.jogador_atual = None
if 'carta_atual' not in st.session_state:
    st.session_state.carta_atual = ""
# NOVO/CORRIGIDO: Lista de desafios restantes no jogo.
# Cria uma cópia da lista original para garantir que as cartas não se repitam.
if 'desafios_restantes' not in st.session_state:
    st.session_state.desafios_restantes = list(DESAFIOS_E_PERGUNTAS)


# --- INTERFACE DO USUÁRIO (UI) ---

st.title("🍻 Faz ou Bebe - A Vingança 😈")
st.markdown("### Prepare-se para revelações, desafios e muitas risadas.")

# --- TELA DE CADASTRO DE JOGADORES ---
if not st.session_state.jogo_iniciado:
    st.header("👤 Quem vai jogar?")

    # Usar um formulário melhora a experiência de adicionar jogadores
    with st.form(key="form_jogadores", clear_on_submit=True):
        nome_jogador = st.text_input("Nome do Jogador", placeholder="Digite um nome...")
        submitted = st.form_submit_button("Adicionar Jogador")
        if submitted and nome_jogador:
            if nome_jogador not in st.session_state.jogadores:
                st.session_state.jogadores.append(nome_jogador)
            else:
                st.warning("Esse jogador já está na lista!")

    # Mostra os jogadores já adicionados
    if st.session_state.jogadores:
        st.write("Jogadores na mesa:")
        # Exibe os jogadores em colunas para melhor visualização
        cols = st.columns(len(st.session_state.jogadores))
        for i, jogador in enumerate(st.session_state.jogadores):
            with cols[i]:
                st.success(f"**{jogador}**")

    # Botão para começar o jogo
    if len(st.session_state.jogadores) >= 2:
        if st.button("▶️ Começar o Jogo!", type="primary"):
            st.session_state.jogo_iniciado = True
            st.rerun() # Força o recarregamento da página para a tela do jogo
    else:
        st.info("Adicione pelo menos 2 jogadores para começar.")


# --- TELA PRINCIPAL DO JOGO ---
else:
    st.header("🔥 A Roleta da Verdade (e da Cachaça)!")
    
    # Adicionando um aviso de quantas cartas restam
    st.info(f"Cartas disponíveis: **{len(st.session_state.desafios_restantes)}**")

    # Verifica se ainda há cartas para jogar
    if not st.session_state.desafios_restantes:
        st.error("🎉 O jogo acabou! Todas as cartas foram sorteadas! 🎉")
        st.session_state.carta_atual = "Fim de Jogo! Reinicie para jogar de novo."
    else:
        # Botão principal para sortear jogador e gerar a carta
        if st.button("🎰 Sortear Próxima Vítima!", type="primary", use_container_width=True):
            with st.spinner("Sorteando um alvo..."):
                # Sorteia um jogador (pode repetir, o que é o normal para "roleta")
                st.session_state.jogador_atual = random.choice(st.session_state.jogadores)
                
                # Sorteia o ÍNDICE da carta na lista de restantes
                indice_sorteado = random.randrange(len(st.session_state.desafios_restantes))
                
                # Pega a carta
                carta = st.session_state.desafios_restantes[indice_sorteado]
                st.session_state.carta_atual = carta
                
                # REMOVE a carta sorteada da lista para que não seja sorteada novamente
                st.session_state.desafios_restantes.pop(indice_sorteado)
                
                st.rerun() # Atualiza a tela após o sorteio
            
    # Exibe o jogador e a carta sorteada
    if st.session_state.jogador_atual:
        st.markdown(f"## A vez é de: **{st.session_state.jogador_atual}**")
        
        # Container estilizado para a carta
        with st.container(border=True):
            st.markdown(f"<p style='text-align: center; font-size: 22px; font-weight: bold;'>{st.session_state.carta_atual}</p>", unsafe_allow_html=True)
        
        st.markdown("---")
        st.warning("Lembre-se: se não fizer ou não responder... BEBA! 🍻")

    # Botão para reiniciar o jogo na barra lateral
    if st.sidebar.button("🔄 Reiniciar Jogo"):
        # Limpa todos os dados da sessão para começar do zero
        for key in st.session_state.keys():
            del st.session_state[key]
        # CORRIGIDO: O st.rerun() deve estar indentado corretamente dentro do if
        st.rerun()