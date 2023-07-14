# coletasASF

Coleta de temperatura e umidade de uma caixa de abelha sem ferrão Mandaçaia MQQ, melipona quadrifasciata quadrifasciata.
O arquivo teve que ser compactado para o GitHub permitir o Upload.

## Descrição

Foram coletados dados de sensores de temperatura e umidade instalados em uma caixa de ASF mandaçaia, tanto internos quanto externos, durante o período iniciado em 15 de fevereiro de 2022 e finalizado em 10 de março de 2023. Inicialmente, os dados eram armazenados no SGBD InfluxDB. Entretanto, um problema ocorreu com o cartão de memória da Raspberry Pi onde os dados estavam armazenados, o que tornou difícil a extração desses dados. Como solução, optou-se por substituir o SGBD InfluxDB pelo PostgreSQL. Após algum tempo, foi obtido êxito na recuperação dos dados armazenados no InfluxDB e esses dados foram inseridos no PostgreSQL, totalizando o período de coletas citado no início do parágrafo.

Esta coleta foi realizada nos sensores chamados "external" e "caixa01". Além desses dados, houve a inserção dos dados de equipamentos de testes chamados "Caixa03" e "testePy". O dataset possui um total de 1.335.098 linhas com as coletas dos sensores "teste", "Caixa03" e "testePy", e 1.333.962 linhas se esses dados forem removidos.

Esses equipamentos de teste foram utilizados durante o desenvolvimento do código, e seus dados não são reais.

