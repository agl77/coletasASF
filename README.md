# coletasASF

Coleta de temperatura e umidade de uma caixa de abelha sem ferrão Mandaçaia MQQ, melipona quadrifasciata quadrifasciata.

![Abelha Mandaçaia MQQ](images/foto_abelha_grama.jpg)

## Descrição

Este projeto se refere à coleta de dados de temperatura e umidade em uma caixa de abelha sem ferrão Mandaçaia MQQ, utilizando um coletor de dados. A coleta foi realizada no período de 15 de fevereiro de 2022 a 10 de março de 2023.

### Caixa modular modelo INPA

A coleta de dados foi realizada em uma caixa modular modelo INPA. A caixa é dividida em módulos, sendo o módulo de ninho, o módulo de sobre-ninho e o módulo de melgueira. A imagem abaixo ilustra a estrutura da caixa:

![Caixa modular modelo INPA](images/Inpa_vazada.png)

### Coletor de dados

O coletor de dados foi construído utilizando um microcontrolador ESP8266 (Esp D1 Mini) e um sensor SHTC3. A montagem do coletor é mostrada na imagem abaixo:

![Sensor conectado no Esp D1 mini](images/d1Sensor.png)

O módulo coletor foi acoplado entre a tampa e o módulo mais alto da caixa, conforme a imagem abaixo:

![Montagem do coletor](images/Montagem_coletor.png)

### Arquivo de dados

Os dados coletados foram armazenados inicialmente no SGBD InfluxDB. No entanto, devido a um problema no cartão de memória da Raspberry Pi onde os dados estavam armazenados, a recuperação dos dados tornou-se difícil. Como solução, optou-se por substituir o InfluxDB pelo PostgreSQL. Após a recuperação bem-sucedida dos dados armazenados no InfluxDB, os dados foram inseridos no PostgreSQL. O arquivo resultante, 2011_02_15-2023_03_10.csv, contém as informações coletadas nos sensores "external" e "caixa01".

O dataset possui um total de 1.335.098 linhas com as coletas dos sensores "teste", "Caixa03" e "testePy". Caso esses dados sejam removidos, o arquivo contém 1.333.962 linhas.

Os equipamentos de teste mencionados, "Caixa03" e "testePy", foram utilizados durante o desenvolvimento do código e seus dados não são reais.

