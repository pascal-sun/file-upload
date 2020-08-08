# Apache : .htaccess

<img title="" src="logo.png" alt="" height="150">

**Facteur de risque** : RCE, Information Disclosure, DoS

**Nom du fichier** : `.htaccess`

**Description** : 

Les fichiers **.htaccess** (**h**yper**t**ext **access**) sont des fichiers cachés de configuration des serveurs Apache. 

Contrairement aux autres fichiers de configuration qui sont réunis dans le répertoire de configuration d'Apache, le ficher .htaccess est placé directement dans les **répertoires de données** du site web. 

Les fichiers .htaccess sont utilisés pour configurer les **droits d'accès**, les **redirections d'URL**, des **messages d'erreurs personnalisés**, et des **associations d'extension de nom de fichier à un type de MIME**.

## Sommaire

- Remote code execution (RCE)

- Information Disclosure

## Remote code execution (RCE)

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

- Le serveur tourne avec Apache (avec `AllowOverride` différent de `None` dans la configuration d'Apache)

### Exploitation

De nombreux payloads peuvent être trouvés dans le projet [htshells](https://github.com/wireghoul/htshells), notamment dans le répertoire [shell](https://github.com/wireghoul/htshells/tree/master/shell) pour le code arbitraire à distance.

Les payloads sont nommées de la manière suivante : **module**.**attack**.htaccess.

1. Après avoir choisi le payload, copiez-le dans un nouveau fichier nommé .htaccess.

2. Vérifiez le contenu du fichier pour savoir s'il doit être modifié avant de le téléverser sur un site web.

3. Téléversez le fichier sur le site web.

4. Accédez au fichier, et exécutez des commandes en ajoutant le paramètre `c` dans la requête (sauf si le fichier indique le contraire) :
   
   ```
    http://example.com/.htaccess?c=ls
   ```

**Attention**, écraser le .htaccess original peut conduire à un déni de service.

## Information Disclosure

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

- Le serveur tourne avec Apache (avec `AllowOverride` différent de  `None` dans la configuration d'Apache)

### Exploitation

De nombreux payloads peuvent être trouvés dans le projet [htshells](https://github.com/wireghoul/htshells), notamment dans le répertoire [info](https://github.com/wireghoul/htshells/tree/master/info) et [traversal](https://github.com/wireghoul/htshells/tree/master/traversal) pour la divulgation d'information.

Les payloads sont nommées de la manière suivante : **module**.**attack**.htaccess.

1. Après avoir choisi le payload, copiez-le dans un nouveau fichier nommé .htaccess.

2. Vérifiez le contenu du fichier pour savoir s'il doit être modifié avant de le téléverser sur un site web.

3. Téléversez le fichier sur le site web.

4. Accédez au fichier.

**Attention**, écraser le .htaccess original peut conduire à un déni de service.

## References

- htshells - Just Another Hacker : http://www.justanotherhacker.com/projects/htshells/index.html

- GitHub - wireghoul/htshells: Self contained htaccess shells and attacks : https://github.com/wireghoul/htshells

## Todo

- La ligne suivante permet de rendre une image `.jpg` exécutable, en changeant son type MIME : `AddType application/x-httpd-php .jpg`
  Ensuite, il suffit de téléverser un webshell en PHP par exemple en `.jpg`, qui a beaucoup plus de chance d'être accepté par l'application.

- [l33t-hoster](http://corb3nik.github.io/blog/insomnihack-teaser-2019/l33t-hoster)
