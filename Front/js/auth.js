// Authentication and User Management

function getBasicAuth(username, password) {
    return 'Basic ' + btoa(username + ':' + password);
}

function saveUserCredentials(username, password) {
    localStorage.setItem('username', username);
    localStorage.setItem('password', password);
}

function getUserCredentials() {
    return {
        username: localStorage.getItem('username'),
        password: localStorage.getItem('password')
    };
}

function clearUserCredentials() {
    localStorage.removeItem('username');
    localStorage.removeItem('password');
    localStorage.removeItem('userType');
    localStorage.removeItem('userId');
}

function saveUserInfo(userInfo) {
    localStorage.setItem('userType', userInfo.user_type);
    localStorage.setItem('userId', userInfo.id);
    localStorage.setItem('userFullName', `${userInfo.first_name} ${userInfo.last_name}`);
}

async function handleLogin(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        console.log('Tentando fazer login com:', username);
        const response = await fetch('http://localhost:8000/api/users/', {
            headers: {
                'Authorization': getBasicAuth(username, password)
            }
        });

        if (!response.ok) {
            throw new Error('Login failed');
        }

        const users = await response.json();
        console.log('Usuários retornados:', users);
        
        // Procura o usuário pelo username exato
        const userInfo = users.find(u => u.username === username);
        console.log('Informações do usuário encontrado:', userInfo);
        
        if (!userInfo) {
            throw new Error('User not found');
        }

        // Salva as credenciais do usuário
        saveUserCredentials(username, password);
        
        // Salva as informações do usuário
        localStorage.setItem('userId', userInfo.id);
        localStorage.setItem('userType', userInfo.user_type);
        localStorage.setItem('userFullName', `${userInfo.first_name} ${userInfo.last_name}`);
        
        console.log('Dados salvos no localStorage:', {
            userId: localStorage.getItem('userId'),
            userType: localStorage.getItem('userType'),
            userFullName: localStorage.getItem('userFullName')
        });

        showDashboard();
        return false;
    } catch (error) {
        console.error('Erro no login:', error);
        alert('Login failed: ' + error.message);
        return false;
    }
}

async function handleRegister(event) {
    event.preventDefault();
    
    const userData = {
        username: document.getElementById('reg-username').value,
        password: document.getElementById('reg-password').value,
        email: document.getElementById('reg-email').value,
        first_name: document.getElementById('reg-firstname').value,
        last_name: document.getElementById('reg-lastname').value,
        user_type: document.getElementById('reg-usertype').value,
    };

    try {
        console.log('Enviando dados para registro:', userData);
        const response = await fetch('http://localhost:8000/api/users/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(userData)
        });

        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            const data = await response.json();
            console.log('Resposta do servidor:', data);
            
            if (!response.ok) {
                throw new Error(JSON.stringify(data));
            }
        } else {
            const text = await response.text();
            console.error('Resposta não-JSON do servidor:', text);
            if (!response.ok) {
                throw new Error('Erro no servidor: ' + response.status);
            }
        }

        console.log('Registro bem-sucedido!');
        alert('Registration successful! Please login.');
        showLoginForm();
        return false;
    } catch (error) {
        console.error('Registration error:', error);
        alert('Registration failed: ' + error.message);
        return false;
    }
}

function logout() {
    clearUserCredentials();
    showLoginForm();
}
