<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Recon Tool</title>
</head>
<body>
    <h1>Recon Tool</h1>
    <pre>
 ____  ____  _     ___  ____  _     ____  _     
/  __\/  _ \/ \__/|\  \/  _ \/ \  //  __\/ \  /|
|  \/|| / \|| |\/|||  /| / \|| |\ ||  \/|| |\ || 
|  __/| |-||| |  ||| /_| \_/|| | \||  __/| | \|| 
\_/   \_/ \|\_/  \|\_/\____/\_/  \|\_/   \_/  \| 
    </pre>
    <p>This tool offers various functionalities including:</p>
    <ul>
        <li>My IP Address</li>
        <li>Password Generator</li>
        <li>Wordlist Generator</li>
        <li>Barcode Generator</li>
        <li>QRCode Generator</li>
        <li>Phone Number Info</li>
        <li>Subdomain Scanner</li>
        <li>Port Scanner</li>
        <li>DDOS Attack</li>
    </ul>

<h2>Installation</h2>
    <pre><code>pip install -r requirements.txt</code></pre>

<h2>Usage</h2>
    <pre><code>python recon_tool.py</code></pre>

<h3>Options</h3>
    <p>After running the script, you'll be prompted to select an option:</p>
    <pre>
    1- MY IP ADDRESS
    2- PASSWORD GENERATOR
    3- WORDLIST GENERATOR
    4- BARCODE GENERATOR
    5- QRCODE GENERATOR
    6- PHONE NUMBER INFO
    7- SUBDOMAIN SCANNER
    8- PORT SCANNER
    9- DDOS ATTACK
    </pre>

  <h3>Option 1: My IP Address</h3>
    <p>This option displays your device's hostname and IP address.</p>

<h3>Option 2: Password Generator</h3>
<p>This option generates a random password based on the specified length.</p>

 <h3>Option 3: Wordlist Generator</h3>
    <p>This option generates a wordlist based on provided characters and length range.</p>
    <h3>Option 4: Barcode Generator</h3>
    <p>This option generates a barcode for a provided 12-digit number and saves it as a PNG file.</p>
    <h3>Option 5: QRCode Generator</h3>
    <p>This option generates a QR code for a provided link and saves it as a PNG file.</p>
    <h3>Option 6: Phone Number Info</h3>
    <p>This option provides information about a provided phone number, including the country and carrier.</p>
    <h3>Option 7: Subdomain Scanner</h3>
    <p>This option scans for subdomains of a provided domain using a default wordlist.</p>
    <h3>Option 8: Port Scanner</h3>
    <p>This option scans for open ports on a provided IP address using the specified scanning mode.</p>
    <h3>Option 9: DDOS Attack</h3>
    <p>This option initiates a DDOS attack on a provided IP address and port (use with caution and legality).</p>
    <h2>Requirements</h2>
    <pre><code>
    tqdm
    pyfiglet
    requests
    pyqrcode
    phonenumbers
    tabulate
    barcode
   </code></pre>
    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>
</body>
</html>
