// API Calls

const API_BASE_URL = 'http://localhost:8000/api';

async function apiCall(endpoint, options = {}) {
    const credentials = getUserCredentials();
    const defaultOptions = {
        headers: {
            'Authorization': getBasicAuth(credentials.username, credentials.password),
            'Content-Type': 'application/json'
        }
    };

    try {
        console.log(`Making API call to: ${API_BASE_URL}${endpoint}`);
        console.log('Credentials:', credentials)
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            ...defaultOptions,
            ...options,
            headers: {
                ...defaultOptions.headers,
                ...options.headers
            }
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error('API Error:', {
                status: response.status,
                statusText: response.statusText,
                error: errorText
            });
            throw new Error(`API call failed: ${response.status} ${response.statusText}\n${errorText}`);
        }

        return response.json();
    } catch (error) {
        console.error('API Call Error:', error);
        throw error;
    }
}

// Pedidos
async function getPedidos() {
    return apiCall('/pedidos/');
}

async function createPedido(pedidoData) {
    const userId = localStorage.getItem('userId');
    const data = {
        ...pedidoData,
        cliente: parseInt(userId)
    };
    return apiCall('/pedidos/', {
        method: 'POST',
        body: JSON.stringify(data)
    });
}

async function acceptDelivery(pedidoId) {
    return apiCall(`/pedidos/${pedidoId}/aceitar_entrega/`, {
        method: 'POST'
    });
}

async function acceptWaterTransport(pedidoId) {
    return apiCall(`/pedidos/${pedidoId}/aceitar_travessia/`, {
        method: 'POST'
    });
}

async function startTransport(pedidoId) {
    return apiCall(`/pedidos/${pedidoId}/iniciar_transporte/`, {
        method: 'POST'
    });
}

async function deliverToPort(pedidoId) {
    return apiCall(`/pedidos/${pedidoId}/entregar_no_porto/`, {
        method: 'POST'
    });
}

async function markAsDelivered(pedidoId) {
    return apiCall(`/pedidos/${pedidoId}/marcar_entregue/`, {
        method: 'POST'
    });
}

async function markAsCompleted(pedidoId) {
    return apiCall(`/pedidos/${pedidoId}/marcar_concluido/`, {
        method: 'POST'
    });
}

// Portos
async function getPortos() {
    return apiCall('/portos/');
}

async function getPortoPedidos(portoId) {
    return apiCall(`/portos/${portoId}/pedidos/`);
}

// Postos
async function getPostos() {
    return apiCall('/postos/');
}

async function getPostoPedidos(postoId) {
    return apiCall(`/postos/${postoId}/pedidos/`);
}

async function getUserPedidos(userId) {
    return apiCall(`/users/${userId}/pedidos/`);
}