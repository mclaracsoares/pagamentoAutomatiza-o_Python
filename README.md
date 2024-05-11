# pagamentoAutomatizacao_Python

Este é um script de automação desenvolvido em Python usando a biblioteca PyAutoGUI e Pandas para automatizar o processo de pagamento de boletos através de um site institucional e o envio do boleto por email.

### Autor

Maria Clara C Soares
Linkedin: https://www.linkedin.com/in/maria-clara-soares-88b311271/

### Pré-requisitos
Python 3.x instalado.

Um navegador web instalado e configurado (o script usa o Microsoft Edge).

Bibliotecas PyAutoGUI e pandas instaladas (instale-as via pip se ainda não estiverem instaladas: pip install pyautogui pandas).

### Instruções de Uso

1. Abra o arquivo do script em uma IDE Python.

2. Edite o script para incluir suas informações de login, senha, link do site da instituição, email destinatário e outras informações específicas, conforme necessário.

3. Certifique-se de que as coordenadas dos cliques e movimentos do mouse estão corretas para o seu ambiente. Você tem que ajustá-las conforme necessário para corresponder à interface do site e do seu navegador.

4. Salve o arquivo após fazer as edições necessárias.

5. Execute o script Python.

### Arquivo Posição.py

Disponibilizei esse arquivo para você conseguir pegar a posição da tela necessaria para os ajustes.

Como funciona?

Você vai executar o arquivo Posição.py (na mesma pasta do main.py). Você terá 5 segundos para colocar seu mouse na posição da tela que voce quer que o programa clique. Após os 5 segundos, será printado no terminal da sua IDE uma coordenada (x = algum numero, y = outro numero). Pronto, agora é so substituir no código original.

### Como instalar as bibliotecas e o pip (direto no terminal)

1. Verifique se o Python está instalado

python --version

Se o Python estiver instalado, você verá a versão instalada. Se não estiver instalado, você precisará instalá-lo primeiro.

2. Baixe o script de instalação do pip: Você pode baixar o script de instalação do pip diretamente do site oficial. Para fazer isso, você pode usar curl (para sistemas Unix-like) ou wget. Execute o seguinte comando no terminal:

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
ou
wget https://bootstrap.pypa.io/get-pip.py

3. Instale o pip: Agora que o script está instalado, você pode executá-lo usando o Python. No terminal, execute o seguinte comando:

python get-pip.py

4. Verifique a instalação: Após a instalação, você pode verificar se o pip foi instalado corretamente digitando o seguinte comando no terminal:

pip --version

Se tudo ocorreu bem, exibirá a versão do pip instalada.

5. Já com o python e pip instalados e funcionando bem, abra o términal pip se ainda não estiverem instaladas e digite:

pip install pyautogui pandas

### Como instalar as bibliotecas (direto no VS Code)

1. abra o terminal

2. Selecione o Command Prompt

3. digite:

pip install pyautogui pandas

### Notas Importantes

É necessario ajustar as coordenadas da tela, tendo em vista que a posição muda de máquina para máquina.

Segurança: Este script contém informações sensíveis como seu login, senha e informações financeiras. Certifique-se de que está executando-o em um ambiente seguro e de confiança.

Depuração: Caso ocorram erros durante a execução do script, verifique as mensagens de erro no console Python e revise o código para identificar e corrigir possíveis problemas ou entre em contato comigo.

Atualizações: Este script pode precisar de ajustes periódicos, especialmente se houver alterações na interface do site da instituição ou no processo de pagamento de boletos.

### Aviso Legal

Este script é fornecido apenas para fins educacionais e de demonstração. O uso deste script é de responsabilidade exclusiva do usuário. Não nos responsabilizamos por quaisquer danos ou consequências decorrentes do uso deste script.
