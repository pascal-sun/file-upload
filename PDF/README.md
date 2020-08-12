# PDF

<img src="logo_svg.png" title="" alt="" height="150">

**Facteur de risque** : XSS, XXE, HTML Injection, ,OpenRedirect, SSRF, DoS

**Extensions** : `.svg`, `.svgz`

**Type MIME** : `image/svg+xml`

**Description** : 

Le **Scalable Vector Graphics** ou **SVG**, est un format de données conçu pour décrire des ensembles de graphiques vectoriels et basé sur XML. Exemple :

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

## RCE : ImageTragick CVE-2016–3714

### Pré-requis

### Exploitation

## References

## Todo

- PDF XXE, XXS
