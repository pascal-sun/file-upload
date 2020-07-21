## XXE inside DOCX file

Format of an Open XML file (inject the payload in any .xml file):

    /_rels/.rels
    [Content_Types].xml
    Default Main Document Part
        /word/document.xml
        /ppt/presentation.xml
        /xl/workbook.xml

Then update the file zip -u xxe.docx [Content_Types].xml

Tool : https://github.com/BuffaloWill/oxml_xxe
