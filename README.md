# File Upload

La fonctionnalité de **File Upload** peut représenter un risque pour une application si elle n'est pas implémentée correctement. 

Selon ce que fait l'application du fichier, les conséquences d'un téléversement de fichiers non sûrs sont nombreuses :

- contrôle complète du système,

- déni de service,

- attaque côté client (XSS, XXE, etc) ou serveur (SSRF, etc),

- défiguration du site,

- etc.

Vous trouvez ici une liste de payload de fichier à téléverser, lors d'une test d'intrusion par exemple, et ainsi démontrer l'existence de la faille (*POC*).

## Mind map

![](map.png)

Ce **mind map** permet de résumer les attaques possibles selon le type de fichiers autorisées à être téléverser.

## Présentation

Chaque type de fichier possède un dossier, contenant un **README.md** et un ou plusieurs sous-dossier selon le nombre d'attaques possible.

Le README.md présente les différents attaques et payloads. Des scripts peuvent être présentes pour générer le payload.

## Liste de types de fichiers

Voici la liste de types de fichiers qui peuvent être intéressants à téléverser sur une application.

### Programmation

- PHP : `.php`, `.php3`, `.php4`, `.php5`, `.php7`, `.phar`, `.phps`, `.phpt`, `.pht`, `.phtm`, `.phtml`
- ASP : `.asp`, `.aspx`, `.cer`, `.asa`, `.aspx`, `.cshtml`, `.vbhtml`
- Python : `.py`
- Perl : `.pl`, `.pm`, `.cgi`, `.lib`
- Ruby : `.rb`
- Shell : `.sh`
- Java : `.jsp`, `.jspx`, `.jsw`, `.jsv`, `.jspf`
- Coldfusion : `.cfm`, `.cfml`, `.cfc`, `.dbm`

### Configuration

- Apache : `.htaccess`

- IIS : `web.config`

- `.httpd.conf`

- Python : `__init__.py`

## Archivage

- .zip

- .tar

- .rar

- .7z

## Images

- .jpeg

- .png

- .gif

- .svg

## Langage de balisage

- .html, .htm

- .xml

- xhtml

## Todo

Firstly, it uses a path provided by the user. This path is not 
validated, therefore, it would allow the user to upload the file to any 
path on the hosting server.

Secondly, it does not restrict the type of the file being uploaded, 
therefore, it would allow the user to upload a malicious file to gain 
access to the server.

Finally, it does not restrict the size of the file. This would allow 
to easily exhaust the host resources and consequently produce a DoS.

- [virtualabs.fr - Bulletproof JPEGs](https://virtualabs.fr/Nasty-bulletproof-Jpegs-l.html), pour PHP avec LFI

## Annexes

- Unrestricted File Upload | OWASP : https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload

- Test Upload of Unexpected File Types | WSTG - Latest | OWASP : https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types.html

- Test Upload of Malicious Files | WSTG - Latest | OWASP : https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/09-Test_Upload_of_Malicious_Files.html

- PayloadsAllTheThings: A list of useful payloads and bypass for Web Application Security and Pentest/CTF : https://github.com/swisskyrepo/PayloadsAllTheThings

- https://book.hacktricks.xyz/pentesting-web/file-upload

- [File Upload XSS - Brute XSS](https://brutelogic.com.br/blog/file-upload-xss/)
