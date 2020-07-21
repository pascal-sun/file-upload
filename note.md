# Téléchargement non restreint de fichier

Unrestricted File Upload

## PHP

> Webshell / Remote Code Execution

## ASP

> Webshell / RCE

## SVG

> Stored XSS / SSRF / XXE?

## GIF

> Stored XSS / SSRF

## CSV

> CSV Injection

## XML

> XXE

## AVI

> LFI / SSRF

## HTML / JS

> HTML injection / XSS / Open redirect

## PNG / JPEG

> Pixel Flood Attack

## ZIP

> RCE via LFI / Dos / Symlink

En un mot, les cybercriminels peuvent créer des archives Zip pour lancer des attaques par traversée de chemin afin d’écraser des fichiers importants sur les systèmes affectés, soit en les détruisant, soit en les remplaçant par d’autres fichiers malveillants.

## PDF / PPTX

> RCE via LFI

## Link

[Unrestricted File Upload | OWASP](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)

[Top 10 - What can you reach in case you uploaded... | Twitter, Salah Hasoneh](https://twitter.com/SalahHasoneh1/status/1281274120395685889?s=20)

https://vulp3cula.gitbook.io/hackers-grimoire/exploitation/web-application/file-upload-bypass

[Media type - Wikipedia](https://en.wikipedia.org/wiki/Media_type#Type_application)

https://book.hacktricks.xyz/pentesting-web/file-upload

http://repository.root-me.org/Exploitation%20-%20Web/EN%20-%20Webshells%20In%20PHP,%20ASP,%20JSP,%20Perl,%20And%20ColdFusion.pdf

```mermaid
graph LR
    %% node
    access[Peut-on accéder au ficher<br/>après l'avoir upload ?]

    type_with_access[Peut-on upload un fichier ...]
    type_with_no_access[Peut-on upload un fichier ...]

    php_with_access[PHP : .php, .php3, .php4,<br/>.php5, .php7, .phar,<br/>.phps, .phpt, .pht,<br/>.phtm, ou .phtml ?]
    asp_with_access[ASP : .asp, .aspx, .cer, .asa ?]
    asp.net_with_access[ASP.NET : .aspx, .cshtml,<br/>.vbhtml ?]
    py_with_access[Python : .py ?]
    pl_with_access[Perl : .pl, .pm, .cgi, .lib ?]
    rb_with_access[Ruby : .rb ?]
    sh_with_access[Shell : .sh ?]
    java_with_access[Java : .jsp, .jspx, .jsw, .jsv, .jspf ?]
    cf_with_access[Coldfusion : .cfm, .cfml, .cfc, .dbm ?]
    svg_with_access[.svg ?]
    gif_with_access[.gif ?]
    cvs_with_access[.csv ?]
    xml_with_access[.xml, .html, .xhtml, config files ?]
    avi_with_access[.avi ?]
    html_js_with_access[.html ou .js ?]
    zip_with_access[.zip ?]
    pdf_pptx_with_access[.pdf ou .pptx ?]
    config_with_access[.htaccess, web.config, httpd.conf, __init__.py ?]


    svg_with_no_access[.svg ?]
    png_jpeg_with_no_access[.png ou .jpeg ?]
    zip_with_no_access[.zip ?]

    img_or_code["Le serveur lit-il l'image<br/>ou le code injecté ?"]

    server[Le serveur<br/>supporte-t-il le langage associé ?]

    %% access
    access -- oui --> type_with_access
    access -. non .-> type_with_no_access

    %% type

    type_with_access --> php_with_access & asp_with_access & asp.net_with_access & py_with_access & pl_with_access & rb_with_access & sh_with_access & java_with_access 
    subgraph RCE
    php_with_access --> server 
    asp_with_access --> server
    asp.net_with_access --> server
    py_with_access --> server
    pl_with_access --> server
    rb_with_access --> server
    sh_with_access --> server
    java_with_access --> server
    server -- oui --> rce[RCE via webshell]
    server -- non --> non01[Non exploitable]
    end

    type_with_access --> gif_with_access --> img_or_code
    img_or_code -- l'image --> no[Non exploitable]:::NoExploit
    img_or_code -- le code PHP --> php[RCE via webshell]:::Exploit
    img_or_code -- le code --> ssrf01[SSRF]:::Exploit
    img_or_code -- le code HTML/JS --> xss01[Stored XSS]:::Exploit

    type_with_access --> svg_with_access --> processed[Le fichier est-il traité<br/>ou juste affiché par le serveur ?]
    processed -- traité --> xxe01[XXE] & ssrf02[SSRF]
    processed -- affiché --> xss02[Stored XSS] & htmlsvg[HTML Injection]
    type_with_access --> cvs_with_access --> csv01[CSV Injection]
    type_with_access --> xml_with_access --> xxe02[XXE]
    type_with_access --> avi_with_access --> lfi02[LFI] & ssrf03[SSRF]
    type_with_access --> html_js_with_access --> html[HTML injection] & xss03[XSS] & open[Open redirect]
    type_with_access --> zip_with_access --> unzip[Le serveur dézippe-t-il le fichier ?]
    unzip -- oui --> fi01["LFI via ZIP Symlink"]:::Exploit
    unzip -- oui --> rcelfi["RCE via LFI"]:::Exploit
    unzip -- non --> non[Non exploitable]:::NoExploit
    type_with_access --> pdf_pptx_with_access
    pdf_pptx_with_access --> ssrf04[SSRF]:::Exploit 
    pdf_pptx_with_access --> pdf_pptx[Blind XXE]:::Exploit



    %% langage du serveur


    subgraph DoS
    type_with_no_access --> svg_with_no_access --> id5[Billion Laugh Attack]:::Exploit
    type_with_no_access --> png_jpeg_with_no_access -->  pixel[Pixel Flood Attack]:::Exploit
    type_with_no_access --> zip_with_no_access --> id6[Bomb]:::Exploit
    end

    classDef Exploit fill:#c6efce,stroke:#006100,color:#006100
    classDef NoExploit fill:#ffc7ce,stroke:#9c0006,color:#9c0006
```
