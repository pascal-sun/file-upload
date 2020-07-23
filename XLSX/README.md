# Office Open XML

<img title="" src="https://www.smallerfaster.com/wp-content/uploads/image-lib/xml-file-optimization/compresssion-optimization-docx-pptx-xlsx-files" alt="" width="400">

**Facteur de risque** : Information Disclosure, LFI, XXE, XSS...

**Extension** : `.docx`, `.docm`, `.xlsx`, `xlsm`, `.pptx` ,`.pptm`

**Type MIME** : `application/vnd.openxmlformats-officedocument.wordprocessingml.document`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, `application/vnd.openxmlformats-officedocument.presentationml.presentation`

**Description** : **Office Open XML** (OOXML) est un fromat de fichier **zippé** et basé sur le **XML**, pour représenter des feuilles de calcul, des graphiques, des présentations et des documents de traitement de texte.

## Sommaire

- .docx

- .xlsx

- .pptx

## Payload 1

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

### Attaque

Blabla

Bla

## XXE dans .xlsx

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

### Attaque

1. Extraire un le fichier Excel `.xlsx` :

```shell
unzip normal.xlsx -d EXPLOIT/
```

## Payload 3

### Pré-requis

- Pré-requis 1

- Pré-requis 2

### Attaque

Blabla

Bla

## References

## Todo



## XXE inside DOCX file

Format of an Open XML file (inject the payload in any .xml file):

```
/_rels/.rels
[Content_Types].xml
Default Main Document Part
    /word/document.xml
    /ppt/presentation.xml
    /xl/workbook.xml
```

Then update the file zip -u xxe.docx [Content_Types].xml

Tool : [GitHub - BuffaloWill/oxml_xxe: A tool for embedding XXE/XML exploits into different filetypes](https://github.com/BuffaloWill/oxml_xxe)
