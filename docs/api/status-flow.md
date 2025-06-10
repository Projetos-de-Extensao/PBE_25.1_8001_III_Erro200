# Fluxo de Status dos Pedidos

O sistema possui um fluxo bem definido de status para cada pedido, garantindo o rastreamento correto da entrega em cada etapa.

## Estados Possíveis

1. **A_CONFIRMAR**
   - Estado inicial quando o pedido é criado
   - O pedido está disponível para aceitação por um entregador

2. **ACEITO**
   - O entregador aceitou o pedido
   - Aguardando início do transporte

3. **EM_TRANSITO**
   - Entregador está transportando o pedido até o porto
   - Iniciado após o entregador confirmar o início do transporte

4. **NO_PORTO**
   - Pedido foi entregue ao porto
   - Disponível para aceitação por um barqueiro

5. **EM_TRAVESSIA**
   - Barqueiro está realizando a travessia do pedido
   - Iniciado após o barqueiro aceitar a travessia

6. **NO_POSTO**
   - Pedido chegou ao posto de destino
   - Aguardando retirada pelo cliente

7. **ENTREGUE**
   - Cliente recebeu o pedido
   - Aguardando confirmação final do cliente

8. **CONCLUIDO**
   - Estado final do pedido
   - Cliente confirmou o recebimento

## Transições de Status

### Ações do Entregador
- `A_CONFIRMAR` → `ACEITO` (via aceitar_entrega)
- `ACEITO` → `EM_TRANSITO` (via iniciar_transporte)
- `EM_TRANSITO` → `NO_PORTO` (via entregar_no_porto)

### Ações do Barqueiro
- `NO_PORTO` → `EM_TRAVESSIA` (via aceitar_travessia)
- `EM_TRAVESSIA` → `ENTREGUE` (via marcar_entregue)

### Ações do Cliente
- `ENTREGUE` → `CONCLUIDO` (via marcar_concluido)

## Regras de Negócio

1. **Restrições de Usuário**
   - Apenas entregadores podem aceitar e transportar pedidos
   - Apenas barqueiros podem realizar travessias
   - Apenas o cliente que criou o pedido pode marcá-lo como concluído

2. **Ordem dos Status**
   - Os status devem seguir a ordem definida
   - Não é possível pular etapas
   - Um pedido não pode voltar a um status anterior

3. **Visibilidade**
   - Entregadores veem pedidos em `A_CONFIRMAR` e seus próprios pedidos aceitos
   - Barqueiros veem pedidos em `NO_PORTO` e seus próprios pedidos em travessia
   - Clientes veem apenas seus próprios pedidos
   - Administradores veem todos os pedidos
