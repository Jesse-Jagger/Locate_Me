document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');

    if (loginForm) {
        loginForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            const response = await fetch('/api/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            });

            const data = await response.json();
            if (response.ok) {
                localStorage.setItem('token', data.access_token);
                window.location.href = 'index.html';
            } else {
                alert(data.message);
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const address = document.getElementById('address').value;

            const response = await fetch('/api/auth/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, email, password, address })
            });

            const data = await response.json();
            if (response.ok) {
                alert('Registered successfully!');
                window.location.href = 'login.html';
            } else {
                alert(data.message);
            }
        });
    }
});