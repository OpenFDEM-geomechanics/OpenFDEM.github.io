Downloads
=============================================

Thank you for being interested in OpenFDEM! Please fill out the information requested below. You will be redirected to the download 
page after filling out the form.

.. raw:: html

    <html>
    <head>
        <title>Software Request Form</title>
        <style>
            /* Style for the form */
            form {
                border: 1px solid #ccc;
                padding: 20px;
                width: 500px;
            }
            
            /* Style for labels and inputs */
            label {
                display: inline-block;
                width: 120px; 
                text-align: right; 
                margin-bottom: 10px;
            }
            
            input, select {
                width: 300px; /* Fixed width for input boxes */
                padding: 5px;
                margin-bottom: 10px;
                margin-left: 10px;
            }

            button[type="submit"] {
                position: relative; 
                top: 5px;
                left: 300px;
            }

        </style>
    </head>
    <body>
        <form id="softwareRequestForm" action="http://openFDEM.pythonanywhere.com/submit" method="POST" onsubmit="return validateForm()">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br>

            <label for="country">Country:</label>
            <input type="text" id="country" name="country" required><br>

            <label for="company">Company:</label>
            <input type="text" id="company" name="company" required><br>

            <label for="version">Version:</label>
            <select id="version" name="version" required>
                <option value="">Select Version</option>
                <option value="Windows">Windows</option>
                <option value="Linux">Linux</option>
            </select><br>

            <div class="submit-button">
                <button type="submit" id="requestButton" disabled>Request Software</button>
            </div>
        </form>

        <script>
            function validateForm() {
                // Perform validation here
                var name = document.getElementById('name').value.trim();
                var email = document.getElementById('email').value.trim();
                var country = document.getElementById('country').value.trim();
                var company = document.getElementById('company').value.trim();
                var version = document.getElementById('version').value.trim();

                // Check if all required fields are filled
                if (name !== '' && email !== '' && country !== '' && company !== '' && version !== '') {
                    return true; // Allow form submission
                } else {
                    alert('Please fill out all required fields.');
                    return false; // Prevent form submission
                }
            }

            // Enable the submit button if all required fields are filled
            document.addEventListener('input', function() {
                var name = document.getElementById('name').value.trim();
                var email = document.getElementById('email').value.trim();
                var country = document.getElementById('country').value.trim();
                var company = document.getElementById('company').value.trim();
                var version = document.getElementById('version').value.trim();

                var requestButton = document.getElementById('requestButton');

                if (name !== '' && email !== '' && country !== '' && company !== '' && version !== '') {
                    requestButton.removeAttribute('disabled');
                } else {
                    requestButton.setAttribute('disabled', 'disabled');
                }
            });
        </script>
    </body>
    </html>
