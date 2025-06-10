---
id: brainstorm
title: Brainstorm
---
 
## Introdução
<p align = "justify">
O brainstorm é uma técnica de elicitação de requisitos que consiste em reunir a equipe e discutir sobre diversos tópicos gerais do projeto apresentados no documento problema de negócio. No brainstorm o diálogo é incentivado e críticas são evitadas para permitir que todos colaborem com suas próprias ideias.
</p>
 
## Metodologia
<p align = "justify">
A equipe se reuniu para debater ideias gerais sobre o projeto via..., começou .... e terminou..., onde o XXXX XXXX foi o moderador, direcionando a equipe com questões pré-elaboradas, e transcrevendo as respostas para o documento.
</p>
 
## Brainstorm
 
## Versão 1.0
 
## Perguntas
 
### 1. Qual o objetivo principal da aplicação?
 
<p align = "justify">

<b>Bryan</b> -  Deve ser uma plataforma onde qualquer pessoa possa solicitar embarcações sob demanda para transporte de pequenas cargas, reduzindo o tempo de espera e melhorando a conectividade entre a Ilha de Primeira e o continente.
</p>
 
<b>Breno</b> -  A plataforma deve fornecer soluções inovadoras para otimizar a logística, incluindo entregas rápidas e eficientes, usando de embarcações ecológicas para reduzir impactos ambientais.

<b>Guilherme</b> - O objetivo da aplicação é integrar tecnologias de mobilidade marítima e logística inteligente, proporcionando um sistema de transporte seguro, ágil e sustentável para os moradores e visitantes da Ilha de Primeira.
 
<b>João</b> - O principal objetivo da aplicação é a criação de um ecossistema de transporte eficiente e conectado, utilizando monitoramento em tempo real.
 
<b>Gustavo</b> -  A plataforma deve gerenciar todo o processo logístico, desde a solicitação de transporte até a entrega de mercadorias, garantindo um fluxo contínuo e confiável entre a ilha e o continente.

</p>
 
---
 
### 2. Como será o processo de registro e autenticação dos usuários?
 
<p align = "justify">
<b>Bryan</b> - O usuário poderá se registrar escolhendo seu tipo (MORADOR, ENTREGADOR ou BARQUEIRO) e receberá um token JWT para autenticação.
 
<b>Breno</b> - O registro deve incluir validações específicas para cada tipo de usuário, garantindo a segurança do sistema.
 
<b>Guilherme</b> - A autenticação será baseada em tokens JWT, permitindo acesso seguro à API.

<b>João</b> - O sistema deve validar as permissões específicas de cada tipo de usuário.
 
<b>Gustavo</b> - Os tokens devem ter expiração e o sistema deve implementar refresh tokens.
 
---
 
### 3. Como será o fluxo de um pedido no sistema?
 
<p align = "justify">
<b>Bryan</b> - O pedido inicia com o morador criando uma solicitação com descrição e valor proposto.
</p>
 
<p align = "justify">
<b>Breno</b> - Entregadores podem aceitar pedidos e iniciar o transporte até o porto.
</p>
 
<b>Guilherme</b> - No porto, barqueiros podem aceitar a travessia até o posto de destino.
 
<b>João</b> - O sistema rastreia cada etapa do pedido através de status bem definidos.
 
<b>Gustavo</b> - O fluxo termina com a confirmação do morador após receber o pedido.

 
---
 
### 4. Como será gerenciado o sistema de portos e postos?

<p align = "justify">
<b>Bryan</b> - O sistema manterá um registro de todos os portos de origem e postos de destino.
 
<b>Breno</b> - Cada pedido será associado a um porto de origem e um posto de destino específico.
 
<b>João</b> - A interface mostrará quais pedidos estão em cada porto/posto.

<b>Guilherme</b> - Os barqueiros poderão ver todos os pedidos disponíveis em um porto específico.
 
<b>Gustavo</b> - O sistema registrará o momento exato de chegada e saída em cada local.
 
---
 
### 5. Como será implementada a segurança e rastreabilidade?
<p align = "justify">
<b>Bryan</b> - Cada ação no sistema será registrada com timestamp e usuário responsável.

<b>Breno</b> - O sistema implementará diferentes níveis de permissão para cada tipo de usuário.

<b>João</b> - Todas as transições de status serão validadas e registradas.
</p>
 
### 6. Quais informações serão disponibilizadas para cada tipo de usuário?
<p align = "justify">
   <b>Bryan</b> - Moradores verão seus próprios pedidos e seu histórico completo.
   
   <b>Breno</b> - Entregadores verão pedidos disponíveis e os que estão transportando.

   <b>Guilherme</b> - Barqueiros verão pedidos no porto e em travessia.
   
   <b>João</b> - Todos os usuários terão acesso ao histórico de suas próprias operações.
   
   <b>Gustavo</b> - O sistema fornecerá estatísticas e métricas relevantes para cada tipo de usuário.
   
</p>
 
### Requisitos elicitados
 
|ID|Descrição|
|----|-------------|
|BS01| O cliente...|
|BS02| O cliente...|
|BS03| O cliente...|
|BS04| O cliente...|
|BS05| O cliente...|
|BS06| O cliente...|
|BS07| O cliente...|
|BS08| O cliente...|
|BS09| O cliente...|
|BS10| O produto...|
|BS11| O produto...|
|BS12| O produto...|
|BS13| O produto...|
|BS14| O produto...|
|BS15| O produto...|
 
## Conclusão
<p align = "justify">
Através da aplicação da técnica, foi possível elicitar alguns dos primeiros requisitos do projeto.
</p>
## Referências Bibliográficas
 
> BARBOSA, S. D. J; DA SILVA, B. S. Interação humano-computador. Elsevier, 2010.
 
 
## Autor(es)
| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| DD/MM/YYYY | 1.0 | Criação do documento | XXX XXXX, XXXX XXXX, YYY YYYY e ZZZ XXXX |
