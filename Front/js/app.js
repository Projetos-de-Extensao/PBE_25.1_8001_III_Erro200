// Application Logic

// UI Navigation
function showLoginForm() {
    document.getElementById('loginForm').style.display = 'block';
    document.getElementById('registerForm').style.display = 'none';
    document.getElementById('dashboard').style.display = 'none';
}

function showRegisterForm() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('registerForm').style.display = 'block';
    document.getElementById('dashboard').style.display = 'none';
}

function showDashboard() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('registerForm').style.display = 'none';
    document.getElementById('dashboard').style.display = 'block';
    
    const userType = localStorage.getItem('userType');
    const userFullName = localStorage.getItem('userFullName');
    
    document.getElementById('userInfo').textContent = `${userFullName} (${userType})`;
    
    hideAllViews();
    loadUserView(userType);
}

function hideAllViews() {
    document.getElementById('moradorView').style.display = 'none';
    document.getElementById('entregadorView').style.display = 'none';
    document.getElementById('barqueiroView').style.display = 'none';
}

// View Loading
async function loadUserView(userType) {
    switch(userType) {
        case 'MORADOR':
            document.getElementById('moradorView').style.display = 'block';
            await loadMoradorView();
            break;
        case 'ENTREGADOR':
            document.getElementById('entregadorView').style.display = 'block';
            await loadEntregadorView();
            break;
        case 'BARQUEIRO':
            document.getElementById('barqueiroView').style.display = 'block';
            await loadBarqueiroView();
            break;
    }
}

// Pedido Management
function showNewPedidoForm() {
    document.getElementById('newPedidoForm').style.display = 'block';
    loadPortosAndPostos();
}

async function loadPortosAndPostos() {
    try {
        const [portos, postos] = await Promise.all([getPortos(), getPostos()]);
        
        const portoSelect = document.getElementById('pedido-porto');
        const postoSelect = document.getElementById('pedido-posto');
        
        portoSelect.innerHTML = portos.map(porto => 
            `<option value="${porto.id}">${porto.nome}</option>`
        ).join('');
        
        postoSelect.innerHTML = postos.map(posto => 
            `<option value="${posto.id}">${posto.nome}</option>`
        ).join('');
    } catch (error) {
        alert('Error loading portos and postos: ' + error.message);
    }
}

async function handleNewPedido(event) {
    event.preventDefault();
    
    const pedidoData = {
        cliente: localStorage.getItem('userId'),
        descricao: document.getElementById('pedido-descricao').value,
        valor_proposto: document.getElementById('pedido-valor').value,
        porto_origem: document.getElementById('pedido-porto').value,
        posto_destino: document.getElementById('pedido-posto').value
    };

    try {
        await createPedido(pedidoData);
        document.getElementById('newPedidoForm').style.display = 'none';
        loadMoradorView();
    } catch (error) {
        alert('Error creating pedido: ' + error.message);
    }
}

// View-specific loading functions
async function loadMoradorView() {
    try {
        const userId = localStorage.getItem('userId');
        const pedidos = await getUserPedidos(userId);
        
        const pedidosList = document.getElementById('pedidosList');
        pedidosList.innerHTML = pedidos.map(pedido => createPedidoCard(pedido, 'MORADOR')).join('');
    } catch (error) {
        console.error('Erro ao carregar pedidos do morador:', error);
    }
}

async function loadEntregadorView() {
    try {
        const pedidos = await getPedidos();
        const userId = parseInt(localStorage.getItem('userId'));

        // Pedidos disponíveis para aceitar
        const availablePedidos = pedidos.filter(p => p.status === 'A_CONFIRMAR');
        
        // Pedidos aceitos pelo entregador atual
        const pedidosAceitos = pedidos.filter(p => 
            p.entregador === userId && p.status === 'ACEITO'
        );

        // Pedidos em transporte pelo entregador atual
        const pedidosEmTransito = pedidos.filter(p => 
            p.entregador === userId && p.status === 'EM_TRANSITO'
        );

        // Pedidos entregues no porto pelo entregador atual
        const pedidosNoPorto = pedidos.filter(p => 
            p.entregador === userId && p.status === 'NO_PORTO'
        );
        
        // Mostrar pedidos disponíveis
        document.getElementById('availablePedidosList').innerHTML = 
            availablePedidos.length > 0 
                ? availablePedidos.map(p => createPedidoCard(p, 'ENTREGADOR', 'DISPONIVEL')).join('')
                : '<p>Não há pedidos disponíveis no momento.</p>';
        
        // Mostrar pedidos em andamento
        const pedidosEmAndamento = [...pedidosAceitos, ...pedidosEmTransito, ...pedidosNoPorto];
        document.getElementById('entregadorPedidosList').innerHTML = 
            pedidosEmAndamento.length > 0
                ? pedidosEmAndamento.map(p => createPedidoCard(p, 'ENTREGADOR', p.status)).join('')
                : '<p>Você não tem pedidos em andamento.</p>';
    } catch (error) {
        console.error('Erro ao carregar pedidos:', error);
    }
}

async function loadBarqueiroView() {
    try {
        const pedidos = await getPedidos();
        const userId = parseInt(localStorage.getItem('userId'));
        
        const portoPedidos = pedidos.filter(p => p.status === 'NO_PORTO');
        const travessiaPedidos = pedidos.filter(p => 
            p.barqueiro === userId &&
            p.status === 'EM_TRAVESSIA'
        );
        const noPostoPedidos = pedidos.filter(p => 
            p.barqueiro === userId &&
            p.status === 'NO_POSTO'
        );
        
        document.getElementById('portoPedidosList').innerHTML = 
            portoPedidos.length > 0
                ? portoPedidos.map(p => createPedidoCard(p, 'BARQUEIRO', 'NO_PORTO')).join('')
                : '<p>Não há pedidos aguardando no porto.</p>';
        
        document.getElementById('travessiaPedidosList').innerHTML = 
            travessiaPedidos.length > 0
                ? travessiaPedidos.map(p => createPedidoCard(p, 'BARQUEIRO', 'EM_TRAVESSIA')).join('')
                : '<p>Não há pedidos em travessia.</p>';
                
        document.getElementById('postoPedidosList').innerHTML = 
            noPostoPedidos.length > 0
                ? noPostoPedidos.map(p => createPedidoCard(p, 'BARQUEIRO', 'NO_POSTO')).join('')
                : '<p>Não há pedidos aguardando entrega no posto.</p>';
    } catch (error) {
        console.error('Erro ao carregar pedidos:', error);
    }
}

// UI Components
function createPedidoCard(pedido, userType, pedidoStatus) {
    const statusColors = {
        'A_CONFIRMAR': '#777',
        'ACEITO': '#007bff',
        'EM_TRANSITO': '#17a2b8',
        'NO_PORTO': '#ffc107',
        'EM_TRAVESSIA': '#6f42c1',
        'NO_POSTO': '#28a745',
        'ENTREGUE': '#20c997',
        'CONCLUIDO': '#28a745'
    };

    let actions = '';
    if (userType === 'ENTREGADOR') {
        if (pedido.status === 'A_CONFIRMAR') {
            actions = `<button onclick="handleAcceptDelivery('${pedido.id}')">Aceitar Entrega</button>`;
        } else if (pedido.status === 'ACEITO') {
            actions = `<button onclick="handleStartTransport('${pedido.id}')">Iniciar Transporte</button>`;
        } else if (pedido.status === 'EM_TRANSITO') {
            actions = `<button onclick="handleDeliverToPort('${pedido.id}')">Entregar no Porto</button>`;
        }
    } else if (userType === 'BARQUEIRO') {
        if (pedido.status === 'NO_PORTO') {
            actions = `<button onclick="handleAcceptWaterTransport('${pedido.id}')">Aceitar Travessia</button>`;
        } else if (pedido.status === 'EM_TRAVESSIA') {
            actions = `<button onclick="handleMarkAsDelivered('${pedido.id}')">Marcar como Entregue</button>`;
        }
    }

    return `
        <div class="pedido-card">
            <h3>Pedido #${pedido.id}</h3>
            <p><strong>Status:</strong> <span class="status-badge" style="background-color: ${statusColors[pedido.status]}">${pedido.status}</span></p>
            <p><strong>Descrição:</strong> ${pedido.descricao}</p>
            <p><strong>Valor Proposto:</strong> R$ ${pedido.valor_proposto}</p>
            <p><strong>Porto:</strong> ${pedido.porto_nome}</p>
            <p><strong>Posto:</strong> ${pedido.posto_nome}</p>
            ${actions}
        </div>
    `;
}

// Event handlers for buttons
async function handleAcceptDelivery(pedidoId) {
    try {
        console.log('Tentando aceitar pedido:', pedidoId);
        const response = await acceptDelivery(pedidoId);
        console.log('Resposta ao aceitar pedido:', response);
        
        alert('Pedido aceito com sucesso!');
        await loadEntregadorView();
    } catch (error) {
        console.error('Erro ao aceitar pedido:', error);
        alert('Erro ao aceitar pedido: ' + error.message);
    }
}

async function handleAcceptWaterTransport(pedidoId) {
    try {
        await acceptWaterTransport(pedidoId);
        loadBarqueiroView();
    } catch (error) {
        alert('Error accepting water transport: ' + error.message);
    }
}

async function handleStartTransport(pedidoId) {
    try {
        console.log('Iniciando transporte do pedido:', pedidoId);
        const response = await fetch(`http://localhost:8000/api/pedidos/${pedidoId}/iniciar_transporte/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': getBasicAuth(
                    localStorage.getItem('username'),
                    localStorage.getItem('password')
                )
            }
        });

        if (!response.ok) {
            throw new Error('Falha ao iniciar transporte');
        }

        alert('Transporte iniciado com sucesso!');
        await loadEntregadorView();
    } catch (error) {
        console.error('Erro ao iniciar transporte:', error);
        alert('Erro ao iniciar transporte: ' + error.message);
    }
}

async function handleDeliverToPort(pedidoId) {
    try {
        console.log('Entregando pedido no porto:', pedidoId);
        const response = await fetch(`http://localhost:8000/api/pedidos/${pedidoId}/entregar_no_porto/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': getBasicAuth(
                    localStorage.getItem('username'),
                    localStorage.getItem('password')
                )
            }
        });

        if (!response.ok) {
            throw new Error('Falha ao entregar no porto');
        }

        alert('Pedido entregue no porto com sucesso!');
        await loadEntregadorView();
    } catch (error) {
        console.error('Erro ao entregar no porto:', error);
        alert('Erro ao entregar no porto: ' + error.message);
    }
}

async function handleMarkAsDelivered(pedidoId) {
    try {
        console.log('Marcando pedido como entregue:', pedidoId);
        await markAsDelivered(pedidoId);
        alert('Pedido marcado como entregue com sucesso!');
        await loadBarqueiroView();
    } catch (error) {
        console.error('Erro ao marcar pedido como entregue:', error);
        alert('Erro ao marcar pedido como entregue: ' + error.message);
    }
}

// Check if user is already logged in on page load
window.onload = function() {
    const credentials = getUserCredentials();
    if (credentials.username && credentials.password) {
        showDashboard();
    } else {
        showLoginForm();
    }
};
