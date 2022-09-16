import pickle
import sklearn as sk
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from time import sleep

def prever_diabetes():
    info = {'Espessura do Sangue ou thickness': [0, '''O sangue muito espesso pode levar a coágulos sanguíneos, e o sangue muito fino pode levar a hematomas ou sangramentos fáceis. Problemas com a espessura do sangue podem ocorrer desde o nascimento ou se desenvolver mais tarde na vida. A espessura do sangue pode ser afetada por alimentos, medicamentos e várias condições médicas.

O sangue espesso pode levar a coágulos sanguíneos nas pernas, causando uma condição dolorosa e inchada chamada trombose venosa profunda. Às vezes, um pedaço de coágulo se rompe no pulmão causando dor no peito e falta de ar - uma condição com risco de vida chamada embolia pulmonar. Às vezes, o sangue espesso causa coágulos nas artérias em vez de nas veias. Um coágulo de sangue que se forma nas artérias do pescoço pode viajar para o cérebro e causar um acidente vascular cerebral. Um coágulo de sangue se formando nas artérias do coração pode resultar em um ataque cardíaco. Os coágulos sanguíneos causam problemas no órgão afetado, cortando o fluxo de oxigênio.

O sangue espesso é causado por proteínas pesadas ou por muito sangue na circulação. Muitos glóbulos vermelhos, glóbulos brancos e plaquetas resultarão em espessamento do sangue. Outra causa é um desequilíbrio no sistema de coagulação do sangue. Doenças específicas incluem lúpus, inibidores, deficiência em proteína C ou S ou antitrombina, ou mutações no Fator 5 ou protrombina. O câncer também pode causar espessamento do sangue.

Nem todos os coágulos sanguíneos são causados por sangue espesso. Coágulos sanguíneos que levam a ataques cardíacos e derrames podem ser formados quando o sangue fino entra em contato com a placa, o que desencadeia um coágulo sanguíneo. Alguns coágulos sanguíneos resultam de fluxo sanguíneo lento ou má circulação. Pessoas em um longo avião ou viagem de carro são propensas a coágulos sanguíneos se não se esticarem o suficiente, por causa do fluxo sanguíneo lento nas pernas. Pessoas obesas são propensas a coágulos sanguíneos porque seu sangue flui mais lentamente. Um batimento cardíaco irregular chamado fibrilação atrial causa coágulos sanguíneos, devido ao fluxo sanguíneo lento através do coração.'''],
            
            'Exame de Sangue na Pele ou skin': [0, '''Um teste cutâneo, também chamado de punção ou teste de arranhões, verifica reações alérgicas imediatas a até 50 substâncias diferentes de uma só vez. Este teste geralmente é feito para identificar alergias a pólen, mofo, pêlos de animais, ácaros e alimentos. Em adultos, o teste geralmente é feito no antebraço.'''],
            
            'Índice de Massa Corporal (IMC) ou bmi': [0,'''O IMC é um cálculo universal adotado pela OMS (Organização Mundial da Saúde) para classificar padrões de saúde relacionados ao peso, como desnutrição e obesidade, principalmente em populações. 
            
            No entanto, o IMC não é um índice suficiente para determinar a saúde de uma pessoa, uma vez que não leva em consideração a composição corporal do indivíduo (quantidade de massa muscular e gordura)
            
            A fórmula do IMC foi criada pelo matemático e astrônomo belga Lambert Adolphe Jacques Quételet em 1832 e recebeu originalmente o nome de "Índice de Quételet", mas foi rebatizada com o nome atual pela OMS em 1972.'''],
            
            'Nível de Insulina ou insulin': [0, '''A principal função da insulina é controlar a quantidade de glicose no sangue após a alimentação1. Ela informa as células de que a glicose deve ser absorvida. Caso isso não aconteça, a permanência de níveis elevados de glicose na corrente sanguínea pode ser altamente tóxica.
            
            A insulina é um hormônio produzido pelo pâncreas, que é responsável por transportar a glicose do sangue para o interior das células, para que seja usada como fonte de energia. A insulina é produzida principalmente após as refeições, quando a quantidade de açúcar no sangue aumenta.

Quando a produção de insulina é insuficiente ou ausente, como no diabetes, o açúcar não consegue ser levado para o interior das células e, por isso, acaba se acumulando no sangue e no resto do organismo, provocando complicações como retinopatia, insuficiência renal, ferimentos que não cicatrizam e até favorecendo o AVC, por exemplo.'''],
            
            'Concentração de Glicose ou glucose_conc': [0, '''A Concentração de Glicose no Plasma é frequentemente medida em experimentos de laboratório. Uma pessoa em jejum antes do café da manhã possui uma concentração de glicose no sangue de 80-90 mg/dL de sangue. Durante a primeira hora após uma refeição, a concentração aumenta para 120-140 mg/dL. Em seguida, os sistemas de feedback rapidamente retornam a concentração de glicose aos níveis de controle, geralmente dentro de 2 h após a última absorção de carboidratos. Por outro lado, durante a inanição (A inanição é caracterizada por um estágio de total ausência do consumo alimentar), a gliconeogênese no fígado fornece glicose.

Quando uma refeição rica em carboidratos é ingerida, a glicose no sangue causa a rápida secreção de insulina (Fig. 20.4). A insulina causa rápida absorção de glicose por quase todos os tecidos, especialmente os músculos, o fígado e os tecidos adiposos. Se os músculos não estão se exercitando, a glicose é armazenada como glicogênio muscular.'''],
            
            'Pressão Arterial Diastólica ou diastolic_bp': [0, '''A Pressão Arterial Diastólica mede a pressão nas paredes das artérias entre os Batimentos Cardíacos. A Pressão Arterial Diastólica normal é inferior a 80 mmHg.'''],
            
            'Idade ou age': [0, '''Conforme envelhecemos, constitui-se uma síndrome multidimensional envolvendo uma interação complexa dos fatores biológicos, psicológicos e sociais no curso de vida individual, que culmina com um estado de maior vulnerabilidade, associado ao maior risco de ocorrência de desfechos clínicos adversos - declínio funcional, quedas, hospitalização, institucionalização e morte.'''],
            
            'Número de Gestações ou num_preg': [0, '''o Sistema Imunológico se adapta durante a gestação. Ele muda, mas não necessariamente se torna mais fraco. Fatores hormonais também podem contribuir para a maior propensão de desenvolver infecções leves, como gripes, resfriados e infecção de urina, durante a gravidez''']}
    
    
    print('''
    
    Olá seja bem vindo ao Teste de Diabetes!
    Para fazer o teste precisaremos das seguintes informações:    
    ''')
    sleep(5)
    for i, k in enumerate(info.keys()):
        print(f'{i+1}º {k}.')
        sleep(3)
    sleep(3)
    print('''
    
    Agora você passará cada uma delas, e também receberá uma explicação da importância de cada um dos itens listados acima.
    
    podemos começar?    
    precione ENTER para prosseguir.''')
    input()
    
    # pergunta ao usuário quais são suas informações pra então fazer o teste
    for i in info.keys():
        info[i][0] = float(input(f'''
        
        
        {i}
        
        {info[i][1]}
        
        Digite a seguinte informação: {i}
        Caso seja um valor decimal, use ponto para separar e não vírgula.
        Modo errado: 0,1
        Modo certo: 0.1
        
         >>  '''))
    
    
    # verifica se o usuário digitou as informações corretamente
    print(f'''
    
    
    
    Confirme se as informações estão corretas:\n''')    
    
    for i, k in enumerate(info.keys()):
        print(f'{i+1}. {k}: {info[k][0]}')
        
    confirmar = input('''
    
    Estão todas corretas?[S/N] >>  ''').upper().strip()
    while confirmar.upper() not in ['S','N']:
        confirmar = input('''
        Erro: 
        Digite S - para confirmar que os dados estão corretos;
        digite N - para confirmar que os dados não estão corretos.
        
        Tente novamente[S/N] >>  ''').upper().strip()
    
    if confirmar == 'N':
        while confirmar == 'N':
            print('\n\n\n')
            for i, k in enumerate(info.keys()):
                print(f'{i+1}. {k}: {info[k][0]}')
            sleep(6)
            trocar = int(input('''
            
            Quais dos valores acima você deseja trocar?[1,2,3,...] >>  '''))
            while trocar not in [i+1 for i in range(len(info.keys()))]:
                for i, k in enumerate(info.keys()):
                    print(f'{i+1}. {k}: {info[k][0]}')
                trocar = int(input('''
                Erro: Digite o número referente à informação que está incorreta:

                Quais dos valores acima você deseja trocar?[1,2,3,...] >>  '''))

            keys = [i for i in info.keys()]
            confirma_troca = float(input(f'''
            Este valor realmente está incorreto?
            {keys[trocar-1]}: {info[keys[trocar-1]][0]}

            Se sim, digite o valor que irá substituí-lo;
            Se não, digite 0.
             >>  '''))

            if confirma_troca != 0:
                info[keys[trocar-1]][0] = confirma_troca
            
            print()
        
            for i, k in enumerate(info.keys()):
                print(f'{i+1}. {k}: {info[k][0]}')
                
            confirmar = input('''
            
            Ainda há alguma informação incorreta?[S/N] >>  ''').upper().strip()
            while confirmar.upper() not in ['S','N']:
                confirmar = input('''
                Erro: 
                Digite S - para confirmar ainda existem dados incorretos;
                digite N - para confirmar que todos os dados estão corretos.

                Tente novamente[S/N] >>  ''').upper().strip()
            if confirmar == 'N':
                confirmar = 'S'
    if confirmar == 'S':
        print('''
        
        
        Agora seus dados estão sendo analizados para confirmar as chances que você tem de estar com Diabetes.
        
        Analizando...''')
        sleep(6)
        
        ml_model_path = 'melhor_modelo.sav'
        accuracy = 73.59
        ml_model = pickle.load(open(ml_model_path, 'rb'))
        diagnostico = ml_model.predict(np.array([info[i][0] for i in info.keys()]).reshape(1,-1))
        
        if diagnostico[0] == 0:
            print(f'''
            Você tem {round(100 - accuracy,2)}% de chances de estar com Diabetes
            Isso é um bom sinal! Mas não leve este teste como a verdade absoluta.
            ''')
            sleep(3)
            print('''
            Este teste foi resultado de um estudo de Inteligência Artificial, ele foi feito com pouquíssimos dados, então seja lá qual foi o resultado, ele não dve ser levado a sério.
            Sua saúde é de extrema importância, procure um médico especialista para saber qual sua real situação!''')
            sleep(3)
            print('''
            
            Obrigado por participar!!''')
            
            sleep(3)
            print('Pressione ENTER para fechar o programa.')
            input()
            print('Finalizando...')
            sleep(5)
        else:
            print(f'''
            Você tem {accuracy}% de chances de estar com Diabetes
            Isso é um péssimo sinal! Mas não leve este teste como a verdade absoluta.
            ''')
            sleep(3)
            print('''
            Este teste foi resultado de um estudo de Inteligência Artificial, ele foi feito com pouquíssimos dados, então seja lá qual foi o resultado, ele não dve ser levado a sério.
            Sua saúde é de extrema importância, procure um médico especialista para saber qual sua real situação!''')
            sleep(3)
            print('''
            
            Obrigado por participar!!''')
            
            sleep(3)
            print('Pressione ENTER para fechar o programa.')
            input()
            print('Finalizando...')
            sleep(5)
            
            
prever_diabetes()