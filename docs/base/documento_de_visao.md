---
id: documento_de_visao
title: Documento de Visão
---
## Introdução

<p align = "justify">
O propósito deste documento é fornecer uma visão geral sobre o projeto que será realizado na disciplina Arquitetura e Desenho de Software 2020/1, na Universidade de Brasília. Sendo assim, Nesse documento serão descritas de maneira resumida as principais funcionalidades, usabilidades, o problema que será abordado e os objetivos da equipe.
</p>

## Descrição do Problema 

<p align = "justify">
A Ilha Primeira enfrenta desafios significativos no processo de entrega de mercadorias devido à sua natureza geográfica, que requer uma travessia marítima. Atualmente, não existe um sistema integrado que gerencie o fluxo de entregas desde o continente até os destinatários na ilha, resultando em processos ineficientes e pouca visibilidade do status das entregas.
</p>

### Problema

Dificuldade em gerenciar e coordenar entregas que necessitam de travessia marítima, envolvendo múltiplos atores (entregadores terrestres e barqueiros) e pontos de transferência (portos e postos).

### Impactados

- Moradores da Ilha Primeira que precisam receber mercadorias
- Entregadores que realizam o transporte terrestre
- Barqueiros que fazem a travessia marítima
- Comerciantes e serviços de entrega que atendem a região

### Consequência

- Atrasos e incertezas nas entregas
- Falta de rastreabilidade dos pedidos
- Comunicação ineficiente entre as partes envolvidas
- Custos elevados devido à falta de otimização
- Experiência frustante para os usuários

### Solução

Desenvolver uma plataforma web que integre todos os atores do processo de entrega:
- Sistema de pedidos com rastreamento em tempo real
- Fluxo de status claro e bem definido
- Interfaces específicas para cada tipo de usuário
- Gerenciamento de portos e postos de entrega
- API REST para integrações futuras

## Objetivos

<p align = "justify">
O objetivo da equipe é desenvolver uma solução que simplifique e otimize o processo de entregas para a Ilha Primeira, oferecendo:
- Rastreabilidade completa dos pedidos
- Coordenação eficiente entre entregadores e barqueiros
- Interface intuitiva para todos os usuários
- Sistema seguro e confiável de gestão de entregas
- Base para futuras expansões e integrações
</p>

## Descrição do Usuário 

<p align = "justify">
O sistema atende três tipos principais de usuários:

1. **Moradores**
   - Pessoas que residem na Ilha Primeira
   - Necessitam receber entregas regularmente
   - Precisam de visibilidade do status de seus pedidos

2. **Entregadores**
   - Profissionais que realizam o transporte terrestre
   - Necessitam ver pedidos disponíveis
   - Precisam coordenar entregas nos portos

3. **Barqueiros**
   - Responsáveis pela travessia marítima
   - Precisam ver pedidos disponíveis nos portos
   - Necessitam registrar entregas nos postos
</p>

## Recursos do produto

### Sistema de Usuários

<p align = "justify">
O sistema suporta três tipos principais de usuários:
- **Moradores**: Podem solicitar entregas, acompanhar status e confirmar recebimento
- **Entregadores**: Podem aceitar pedidos e realizar o transporte até o porto
- **Barqueiros**: Podem aceitar pedidos no porto e realizar travessias
</p>

### Gestão de Pedidos

<p align = "justify">
O sistema oferece um fluxo completo de pedidos:
- Criação de pedidos com descrição e valor proposto
- Rastreamento em tempo real do status
- Sistema de aceitação por entregadores e barqueiros
- Confirmação de entrega em múltiplas etapas
</p>

### Portos e Postos

<p align = "justify">
Gerenciamento de locais de entrega:
- Cadastro e listagem de portos de origem
- Cadastro e listagem de postos de destino
- Associação de pedidos com portos e postos
</p>

### Sistema de Status

<p align = "justify">
Fluxo detalhado de status dos pedidos:
1. A_CONFIRMAR: Aguardando aceitação
2. ACEITO: Pedido aceito pelo entregador
3. EM_TRANSITO: Em transporte até o porto
4. NO_PORTO: Aguardando barqueiro
5. EM_TRAVESSIA: Em travessia marítima
6. NO_POSTO: Aguardando retirada
7. ENTREGUE: Entregue ao destinatário
8. CONCLUIDO: Confirmado pelo cliente
</p>

<p align = "justify">
O cliente poderá pesquisar...
</p>

## Restrições

<p align = "justify">
A aplicação não será responsável...
</p>

## Referências Bibliográficas

> Documento de visão. Disponível em https://www... Acesso em dd/MM/yyYY

> Documento de visão. Disponível em  Acesso em dd/MM/yyYY

## Versionamento
| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| DD/MM/YYYY | 1.0 | Criação do documento | XXX XXXX e ZZZ ZZZZ | 

